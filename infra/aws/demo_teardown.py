"""Idempotent cleanup for the short-lived Base AWS demo deployment."""

import os
from typing import Any, Callable

import boto3
from botocore.exceptions import ClientError, WaiterError


REGION = os.getenv("AWS_REGION", "eu-central-1")
ACCOUNT_ID = os.getenv("AWS_ACCOUNT_ID", "")
ECS_CLUSTER = os.getenv("ECS_CLUSTER", "base-cluster")
ECS_SERVICE = os.getenv("ECS_SERVICE", "base-api-service")
ECS_TASK_FAMILY = os.getenv("ECS_TASK_FAMILY", "base-api")
RDS_INSTANCE = os.getenv("RDS_INSTANCE", "base")
ALB_NAME = os.getenv("ALB_NAME", "base-alb")
TARGET_GROUP_NAME = os.getenv("TARGET_GROUP_NAME", "base-api-tg")
FRONTEND_BUCKET = os.getenv("FRONTEND_BUCKET", "base-frontend-pranay")
DOCUMENTS_BUCKET = os.getenv("DOCUMENTS_BUCKET", "base-documents-pranay")
ECR_REPOSITORY = os.getenv("ECR_REPOSITORY", "base-api")
CLOUDFRONT_DISTRIBUTION_ID = os.getenv("CLOUDFRONT_DISTRIBUTION_ID", "")
CLOUDFRONT_OAC_NAME = os.getenv("CLOUDFRONT_OAC_NAME", "base-frontend-oac")
LOG_GROUP = os.getenv("LOG_GROUP", "/ecs/base-api-task")
BUDGET_NAME = os.getenv("BUDGET_NAME", "base-four-day-demo")
SECRET_PREFIX = os.getenv("SECRET_PREFIX", "base/")
SECURITY_GROUP_NAMES = tuple(
    name.strip()
    for name in os.getenv(
        "SECURITY_GROUP_NAMES",
        "base-alb-sg,base-api-service-sg,base-rds-sg",
    ).split(",")
    if name.strip()
)
DELETE_ROLE_NAMES = tuple(
    name.strip()
    for name in os.getenv(
        "DELETE_ROLE_NAMES",
        "base-github-deploy-role,base-ecs-task-role,ecsTaskExecutionRole",
    ).split(",")
    if name.strip()
)


def _not_found(exc: ClientError) -> bool:
    code = exc.response.get("Error", {}).get("Code", "")
    return code in {
        "AWS.SimpleQueueService.NonExistentQueue",
        "ClusterNotFoundException",
        "DBInstanceNotFound",
        "DBInstanceNotFoundFault",
        "DistributionNotFound",
        "LoadBalancerNotFound",
        "LoadBalancerNotFoundException",
        "NoSuchBucket",
        "NoSuchEntity",
        "RepositoryNotFoundException",
        "ResourceNotFoundException",
        "ServiceNotFoundException",
        "TargetGroupNotFound",
        "TargetGroupNotFoundException",
    }


def _run_step(name: str, operation: Callable[[], Any], results: dict[str, str]) -> None:
    try:
        operation()
        results[name] = "complete"
    except ClientError as exc:
        if _not_found(exc):
            results[name] = "already absent"
        else:
            code = exc.response.get("Error", {}).get("Code", "ClientError")
            message = exc.response.get("Error", {}).get("Message", str(exc))
            results[name] = f"retry required: {code}: {message}"
    except WaiterError as exc:
        results[name] = f"retry required: {exc}"
    except Exception as exc:  # Keep later cleanup steps running.
        results[name] = f"retry required: {type(exc).__name__}: {exc}"


def _delete_ecs() -> None:
    ecs = boto3.client("ecs", region_name=REGION)
    services = ecs.describe_services(cluster=ECS_CLUSTER, services=[ECS_SERVICE]).get("services", [])
    if services and services[0].get("status") != "INACTIVE":
        ecs.update_service(cluster=ECS_CLUSTER, service=ECS_SERVICE, desiredCount=0)
        ecs.delete_service(cluster=ECS_CLUSTER, service=ECS_SERVICE, force=True)
    task_arns = ecs.list_tasks(cluster=ECS_CLUSTER).get("taskArns", [])
    for task_arn in task_arns:
        ecs.stop_task(cluster=ECS_CLUSTER, task=task_arn, reason="Base demo deadline reached")

    for task_definition in ecs.list_task_definitions(familyPrefix=ECS_TASK_FAMILY).get("taskDefinitionArns", []):
        try:
            ecs.deregister_task_definition(taskDefinition=task_definition)
        except ClientError:
            pass
    try:
        ecs.delete_cluster(cluster=ECS_CLUSTER)
    except ClientError as exc:
        if exc.response.get("Error", {}).get("Code") != "ClusterContainsServicesException":
            raise


def _delete_load_balancer() -> None:
    elb = boto3.client("elbv2", region_name=REGION)
    load_balancers = elb.describe_load_balancers(Names=[ALB_NAME]).get("LoadBalancers", [])
    for load_balancer in load_balancers:
        elb.delete_load_balancer(LoadBalancerArn=load_balancer["LoadBalancerArn"])

    try:
        target_groups = elb.describe_target_groups(Names=[TARGET_GROUP_NAME]).get("TargetGroups", [])
        for target_group in target_groups:
            elb.delete_target_group(TargetGroupArn=target_group["TargetGroupArn"])
    except ClientError as exc:
        if exc.response.get("Error", {}).get("Code") not in {
            "ResourceInUse",
            "TargetGroupNotFound",
        }:
            raise


def _delete_rds() -> None:
    rds = boto3.client("rds", region_name=REGION)
    try:
        instances = rds.describe_db_instances(DBInstanceIdentifier=RDS_INSTANCE).get("DBInstances", [])
        if instances and instances[0].get("DBInstanceStatus") != "deleting":
            rds.delete_db_instance(
                DBInstanceIdentifier=RDS_INSTANCE,
                SkipFinalSnapshot=True,
                DeleteAutomatedBackups=True,
            )
            return
        if instances:
            return
    except ClientError as exc:
        if not _not_found(exc):
            raise

    try:
        rds.delete_db_subnet_group(DBSubnetGroupName="base-rds-subnet-group")
    except ClientError as exc:
        if not _not_found(exc):
            raise


def _empty_bucket(s3: Any, bucket: str) -> None:
    paginator = s3.get_paginator("list_object_versions")
    for page in paginator.paginate(Bucket=bucket):
        objects = [
            {"Key": item["Key"], "VersionId": item["VersionId"]}
            for item in page.get("Versions", []) + page.get("DeleteMarkers", [])
        ]
        for index in range(0, len(objects), 1000):
            s3.delete_objects(Bucket=bucket, Delete={"Objects": objects[index:index + 1000], "Quiet": True})

    paginator = s3.get_paginator("list_objects_v2")
    for page in paginator.paginate(Bucket=bucket):
        objects = [{"Key": item["Key"]} for item in page.get("Contents", [])]
        for index in range(0, len(objects), 1000):
            s3.delete_objects(Bucket=bucket, Delete={"Objects": objects[index:index + 1000], "Quiet": True})


def _delete_storage() -> None:
    s3 = boto3.client("s3", region_name=REGION)
    for bucket in (FRONTEND_BUCKET, DOCUMENTS_BUCKET):
        try:
            _empty_bucket(s3, bucket)
            s3.delete_bucket(Bucket=bucket)
        except ClientError as exc:
            if not _not_found(exc):
                raise

    ecr = boto3.client("ecr", region_name=REGION)
    try:
        ecr.delete_repository(repositoryName=ECR_REPOSITORY, force=True)
    except ClientError as exc:
        if not _not_found(exc):
            raise


def _delete_cloudfront() -> None:
    cloudfront = boto3.client("cloudfront")
    if CLOUDFRONT_DISTRIBUTION_ID:
        try:
            response = cloudfront.get_distribution_config(Id=CLOUDFRONT_DISTRIBUTION_ID)
            config = response["DistributionConfig"]
            if config.get("Enabled"):
                config["Enabled"] = False
                cloudfront.update_distribution(
                    Id=CLOUDFRONT_DISTRIBUTION_ID,
                    IfMatch=response["ETag"],
                    DistributionConfig=config,
                )
                return

            distribution = cloudfront.get_distribution(Id=CLOUDFRONT_DISTRIBUTION_ID)["Distribution"]
            if distribution.get("Status") != "Deployed":
                raise RuntimeError("CloudFront is still propagating its disabled state.")
            response = cloudfront.get_distribution_config(Id=CLOUDFRONT_DISTRIBUTION_ID)
            cloudfront.delete_distribution(Id=CLOUDFRONT_DISTRIBUTION_ID, IfMatch=response["ETag"])
        except ClientError as exc:
            if not _not_found(exc):
                raise

    for item in cloudfront.list_origin_access_controls().get("OriginAccessControlList", {}).get("Items", []):
        if item.get("Name") == CLOUDFRONT_OAC_NAME:
            details = cloudfront.get_origin_access_control(Id=item["Id"])
            cloudfront.delete_origin_access_control(Id=item["Id"], IfMatch=details["ETag"])


def _delete_secrets_and_logs() -> None:
    secrets = boto3.client("secretsmanager", region_name=REGION)
    paginator = secrets.get_paginator("list_secrets")
    for page in paginator.paginate(Filters=[{"Key": "name", "Values": [SECRET_PREFIX]}]):
        for secret in page.get("SecretList", []):
            if secret.get("Name", "").startswith(SECRET_PREFIX):
                secrets.delete_secret(SecretId=secret["ARN"], ForceDeleteWithoutRecovery=True)

    logs = boto3.client("logs", region_name=REGION)
    try:
        logs.delete_log_group(logGroupName=LOG_GROUP)
    except ClientError as exc:
        if not _not_found(exc):
            raise


def _delete_security_groups() -> None:
    ec2 = boto3.client("ec2", region_name=REGION)
    groups = ec2.describe_security_groups(
        Filters=[{"Name": "group-name", "Values": list(SECURITY_GROUP_NAMES)}]
    ).get("SecurityGroups", [])
    for group in groups:
        try:
            ec2.delete_security_group(GroupId=group["GroupId"])
        except ClientError as exc:
            if exc.response.get("Error", {}).get("Code") != "DependencyViolation":
                raise


def _delete_iam() -> None:
    iam = boto3.client("iam")
    for role_name in DELETE_ROLE_NAMES:
        try:
            for policy_name in iam.list_role_policies(RoleName=role_name).get("PolicyNames", []):
                iam.delete_role_policy(RoleName=role_name, PolicyName=policy_name)
            for policy in iam.list_attached_role_policies(RoleName=role_name).get("AttachedPolicies", []):
                iam.detach_role_policy(RoleName=role_name, PolicyArn=policy["PolicyArn"])
            iam.delete_role(RoleName=role_name)
        except ClientError as exc:
            if not _not_found(exc):
                raise

    if ACCOUNT_ID:
        provider_arn = f"arn:aws:iam::{ACCOUNT_ID}:oidc-provider/token.actions.githubusercontent.com"
        try:
            iam.delete_open_id_connect_provider(OpenIDConnectProviderArn=provider_arn)
        except ClientError as exc:
            if not _not_found(exc):
                raise


def _delete_budget() -> None:
    if not ACCOUNT_ID:
        return
    budgets = boto3.client("budgets", region_name="us-east-1")
    budgets.delete_budget(AccountId=ACCOUNT_ID, BudgetName=BUDGET_NAME)


def lambda_handler(event: dict[str, Any], context: Any) -> dict[str, Any]:
    results: dict[str, str] = {}
    steps = (
        ("ecs", _delete_ecs),
        ("load_balancer", _delete_load_balancer),
        ("rds", _delete_rds),
        ("cloudfront", _delete_cloudfront),
        ("storage", _delete_storage),
        ("secrets_and_logs", _delete_secrets_and_logs),
        ("security_groups", _delete_security_groups),
        ("deployment_iam", _delete_iam),
        ("budget", _delete_budget),
    )
    for name, operation in steps:
        _run_step(name, operation, results)
    return {"ok": all("retry required" not in value for value in results.values()), "results": results}


if __name__ == "__main__":
    print(lambda_handler({}, None))
