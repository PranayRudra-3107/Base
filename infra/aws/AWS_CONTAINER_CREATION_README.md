# Base AWS Container Creation And Resource Names

## July 2026 Temporary Deployment

The previous resources documented later in this file were deleted in May and rebuilt on 2026-07-13 with new generated identifiers.

```text
Public URL:       https://d2llye5km5il24.cloudfront.net/
CloudFront ID:    E2AVPU9QAGIB72
CloudFront OAC:   EQTEMDO3H6TD1
ALB DNS:          base-alb-1755646895.eu-central-1.elb.amazonaws.com
ECS cluster:      base-cluster
ECS service:      base-api-service
RDS:              base / PostgreSQL 17.9 / db.t4g.micro / 20 GB gp3
S3 region:        eu-central-1 for both buckets
Budget:           base-four-day-demo / USD 20 / CUSTOM / expires at teardown
Budget stop SNS:  base-budget-stop -> base-demo-teardown at 100% actual spend
Automatic delete: 2026-07-16 23:00 Europe/Berlin / 21:00 UTC
```

AWS Scheduler invokes `base-demo-teardown` at the deadline, with cleanup retries at `21:35Z` and `22:15Z`. The function source is `infra/aws/demo_teardown.py`; `.github/workflows/teardown-aws.yml` is the manual backup. The generated MCP key is stored in Secrets Manager as `base/mcp-api-key` and is not recorded in this file.

The budget period is `2026-07-13T00:00:00Z` through `2026-07-16T21:00:00Z`. At 100% actual spend, SNS topic `base-budget-stop` invokes the teardown Lambda. AWS Budgets still does not enforce a hard payment ceiling and cost data can lag; the fixed teardown schedules stop and remove the billable runtime.

Treat resource IDs in the historical sections below as a command log, not the current live identifiers. The current ECS task definition and the table above are authoritative for this temporary deployment.

Use this file as the naming reference for deploying Base on AWS. When you talk with Codex later, you can say things like:

```text
Use the names from infra/aws/AWS_CONTAINER_CREATION_README.md
```

or:

```text
Help me create the base-api ECS service.
```

## 1. Current Account Values

These are the current values from the live AWS/GitHub setup.

```bash
AWS_ACCOUNT_ID=626210706801
AWS_REGION=eu-central-1
S3_REGION=eu-central-1
IAM_IDENTITY_CENTER_REGION=eu-central-1
IAM_IDENTITY_CENTER_START_URL=https://d-996748b0aa.awsapps.com/start
AWS_CLI_PROFILE=base-admin
PROJECT_SLUG=base
UNIQUE_SUFFIX=pranay
CLOUDFRONT_DOMAIN=d2llye5km5il24.cloudfront.net
ACTIVE_PUBLIC_DOMAIN=d2llye5km5il24.cloudfront.net
```

Important: S3 bucket names must be globally unique across all AWS accounts, so always include a personal/random suffix in bucket names.

Current region split:

```text
Backend AWS resources: eu-central-1
S3 buckets:            us-east-1
IAM Identity Center:   eu-central-1
```

## 1.1. AWS CLI SSO Status

Current intended local CLI profile:

```text
base-admin
```

Current IAM Identity Center values:

```text
Start URL: https://d-996748b0aa.awsapps.com/start
SSO region: eu-central-1
AWS account ID: 626210706801
```

The CLI profile is configured and working:

```text
Profile:      base-admin
Account:      626210706801
Role:         AdministratorAccess
SSO region:   eu-central-1
App region:   eu-central-1
```

Verify:

```bash
aws sts get-caller-identity --profile base-admin
aws s3 ls --profile base-admin
aws ecs list-clusters --profile base-admin --region eu-central-1
```

Last verified by Codex: the CLI returned account `626210706801` with assumed role `AWSReservedSSO_AdministratorAccess_812c9fe8474c7b0b/pranay_rudra`.

## 1.2. Current AWS Resource Inventory

This inventory was discovered from AWS CLI using profile `base-admin`.

| Resource Type | Region | Name / Value | Status |
|---|---:|---|---|
| AWS account | global | `626210706801` | connected |
| CLI profile | local | `base-admin` | configured |
| S3 frontend bucket | us-east-1 | `base-frontend-pranay` | created |
| S3 documents bucket | us-east-1 | `base-documents-pranay` | created |
| ECR backend repo | eu-central-1 | `base-api` | created |
| ECR image tag | eu-central-1 | `base-api:latest` | pushed |
| ECS cluster | eu-central-1 | `base-cluster` | created |
| ECS service | eu-central-1 | `base-api-service` | running, desired count `1` |
| ECS task definition | eu-central-1 | `base-api:6` | active |
| RDS PostgreSQL instance | eu-central-1 | `base` | available |
| RDS endpoint | eu-central-1 | `base.cfqs0omo2oaz.eu-central-1.rds.amazonaws.com` | available |
| Application Load Balancer | eu-central-1 | `base-alb` | created |
| ALB DNS | eu-central-1 | `base-alb-2085702204.eu-central-1.elb.amazonaws.com` | created |
| Target group | eu-central-1 | `base-api-tg` | healthy |
| CloudWatch log group | eu-central-1 | `/ecs/base-api-task` | created |
| ECS execution role | global | `ecsTaskExecutionRole` | exists |
| ECS task role | global | `base-ecs-task-role` | created |
| GitHub deploy role | global | `base-github-deploy-role` | created |
| OpenAI secret | eu-central-1 | `base/openai-api-key` | created |
| Database URL secret | eu-central-1 | `base/database-url` | created, points to RDS |
| S3 bucket secret | eu-central-1 | `base/s3-bucket` | created |
| CloudFront distribution | global | `E1YZJLNPYALOSR` | deployed |
| CloudFront domain | global | `d13xa0pqwvaoqw.cloudfront.net` | created |
| Frontend object | us-east-1 | `s3://base-frontend-pranay/index.html` | uploaded |

## 1.2.1. Official AWS ARNs And Generated IDs

These values were refreshed from AWS CLI after SSO login on `2026-05-24`.

| Purpose | Official Value |
|---|---|
| Current AWS caller | `arn:aws:sts::626210706801:assumed-role/AWSReservedSSO_AdministratorAccess_812c9fe8474c7b0b/pranay_rudra` |
| ECR repository ARN | `arn:aws:ecr:eu-central-1:626210706801:repository/base-api` |
| ECR repository URI | `626210706801.dkr.ecr.eu-central-1.amazonaws.com/base-api` |
| ECS cluster ARN | `arn:aws:ecs:eu-central-1:626210706801:cluster/base-cluster` |
| ECS service ARN | `arn:aws:ecs:eu-central-1:626210706801:service/base-cluster/base-api-service` |
| Current ECS task definition ARN | `arn:aws:ecs:eu-central-1:626210706801:task-definition/base-api:6` |
| Current deployed image | `626210706801.dkr.ecr.eu-central-1.amazonaws.com/base-api:bc1573eef9382df612402e9ed8b36ae8dca8953d` |
| ALB ARN | `arn:aws:elasticloadbalancing:eu-central-1:626210706801:loadbalancer/app/base-alb/17bc7b314892ff68` |
| ALB listener ARN, HTTP 80 | `arn:aws:elasticloadbalancing:eu-central-1:626210706801:listener/app/base-alb/17bc7b314892ff68/5beaccfe2147d088` |
| Target group ARN | `arn:aws:elasticloadbalancing:eu-central-1:626210706801:targetgroup/base-api-tg/3f5af475d1124e71` |
| VPC ID | `vpc-03ea2e9d4843da40a` |
| Public subnet 1 | `subnet-08772e60815f98ebb` |
| Public subnet 2 | `subnet-0bd1feed3294f76ce` |
| ALB/RDS security group | `sg-02d8535c0f4290437` (`default`) |
| ECS task security group | `sg-0c0dcb9be347d599f` (`base-api-service-sg`) |
| RDS instance ARN | `arn:aws:rds:eu-central-1:626210706801:db:base` |
| RDS master secret ARN | `arn:aws:secretsmanager:eu-central-1:626210706801:secret:rds!db-bbfc41d8-91fb-4d5b-87c9-a986608908ba-NrJfXu` |
| CloudWatch log group ARN | `arn:aws:logs:eu-central-1:626210706801:log-group:/ecs/base-api-task:*` |
| ECS execution role ARN | `arn:aws:iam::626210706801:role/ecsTaskExecutionRole` |
| ECS task role ARN | `arn:aws:iam::626210706801:role/base-ecs-task-role` |
| GitHub deploy role ARN | `arn:aws:iam::626210706801:role/base-github-deploy-role` |
| OpenAI secret ARN | `arn:aws:secretsmanager:eu-central-1:626210706801:secret:base/openai-api-key-auaT6u` |
| Database URL secret ARN | `arn:aws:secretsmanager:eu-central-1:626210706801:secret:base/database-url-cHCnfR` |
| S3 bucket secret ARN | `arn:aws:secretsmanager:eu-central-1:626210706801:secret:base/s3-bucket-sDSH6J` |
| CloudFront distribution ARN | `arn:aws:cloudfront::626210706801:distribution/E1YZJLNPYALOSR` |
| CloudFront OAC ID | `E2NZ0OL8JD3FUJ` (`base-frontend-oac`) |
| CloudFront frontend origin | `base-frontend-pranay.s3.us-east-1.amazonaws.com` |
| CloudFront API origin | `base-alb-2085702204.eu-central-1.elb.amazonaws.com` |

## 1.3. Current Deployment Snapshot

Last deployment status saved on `2026-05-23`.

What is live now:

```text
Frontend URL:        https://d13xa0pqwvaoqw.cloudfront.net/
Backend health URL:  http://base-alb-2085702204.eu-central-1.elb.amazonaws.com/health
CloudFront API URL:  https://d13xa0pqwvaoqw.cloudfront.net/api/projects/
```

Verified live responses:

```text
ALB /health:
{"status":"ok","environment":"production","metadata_backend":"postgres","document_storage_backend":"s3","vector_backend":"pgvector"}

CloudFront /api/projects/:
[]
```

Current running backend state:

```text
ECS service:       base-api-service
ECS service state: ACTIVE
Desired tasks:     1
Running tasks:     1
Pending tasks:     0
Task definition:   base-api:6
Target group:      base-api-tg
Target health:     healthy
Container image:   626210706801.dkr.ecr.eu-central-1.amazonaws.com/base-api:bc1573eef9382df612402e9ed8b36ae8dca8953d
```

Important deployment fix that was made:

```text
Initial ECS startup failed because DATABASE_URL was injected as the full JSON secret.
Task definition base-api:3 and later use Secrets Manager JSON key selectors:

OPENAI_API_KEY -> arn:aws:secretsmanager:eu-central-1:626210706801:secret:base/openai-api-key-auaT6u:OPENAI_API_KEY::
DATABASE_URL   -> arn:aws:secretsmanager:eu-central-1:626210706801:secret:base/database-url-cHCnfR:DATABASE_URL::
S3_BUCKET      -> arn:aws:secretsmanager:eu-central-1:626210706801:secret:base/s3-bucket-sDSH6J:DOCUMENTS_BUCKET::
```

The `base/database-url` secret was updated to point to the RDS instance:

```text
RDS instance:  base
RDS endpoint:  base.cfqs0omo2oaz.eu-central-1.rds.amazonaws.com
Database:      postgres
User:          postgres
```

Do not write the real database password or OpenAI key in this file.

Useful verification commands:

```bash
aws ecs describe-services --profile base-admin --region eu-central-1 \
  --cluster base-cluster \
  --services base-api-service \
  --query 'services[0].{Status:status,Desired:desiredCount,Running:runningCount,Pending:pendingCount,TaskDefinition:taskDefinition}' \
  --output json

aws elbv2 describe-target-health --profile base-admin --region eu-central-1 \
  --target-group-arn arn:aws:elasticloadbalancing:eu-central-1:626210706801:targetgroup/base-api-tg/3f5af475d1124e71

curl http://base-alb-2085702204.eu-central-1.elb.amazonaws.com/health

curl https://d13xa0pqwvaoqw.cloudfront.net/api/projects/
```

CI/CD status:

```text
The GitHub Actions workflow exists at .github/workflows/deploy-aws.yml.
The AWS deploy role exists: arn:aws:iam::626210706801:role/base-github-deploy-role

GitHub CLI is installed and authenticated as PranayRudra-3107.
Repository variables and secrets have been configured.
Deploy AWS workflow was triggered successfully and completed.
```

Last successful GitHub Actions deployment:

```text
Workflow:   Deploy AWS
Run ID:     26363680084
Run URL:    https://github.com/PranayRudra-3107/Base/actions/runs/26363680084
Commit:     bc1573e Add live connector hub
Duration:   about 5 minutes 6 seconds
Result:     success
Outputs:    pushed backend image, deployed ECS task definition base-api:6,
            synced frontend to S3, invalidated CloudFront cache
```

Note from the successful workflow run:

```text
GitHub Actions warned that some Node.js 20 actions are deprecated and will move
to Node.js 24 defaults in 2026. The run succeeded, but action versions should be
checked later for Node.js 24 support.
```

GitHub repository variables configured:

```text
AWS_REGION=eu-central-1
ECR_REPOSITORY=base-api
ECS_CLUSTER=base-cluster
ECS_SERVICE=base-api-service
FRONTEND_BUCKET=base-frontend-pranay
CLOUDFRONT_DISTRIBUTION_ID=E1YZJLNPYALOSR
```

GitHub repository secret configured:

```text
AWS_DEPLOY_ROLE_ARN=arn:aws:iam::626210706801:role/base-github-deploy-role
```

## 2. Canonical AWS Resource Names

Use these exact names unless there is a strong reason to change them.

| Purpose | AWS Resource | Recommended Name |
|---|---|---|
| Backend Docker image repo | ECR repository | `base-api` |
| ECS cluster | ECS cluster | `base-cluster` |
| Backend task definition family | ECS task definition | `base-api` |
| Backend container inside task | ECS container name | `base-api` |
| Backend service | ECS service | `base-api-service` |
| Backend load balancer | Application Load Balancer | `base-alb` |
| Backend target group | ALB target group | `base-api-tg` |
| Backend logs | CloudWatch log group | `/ecs/base-api-task` |
| ECS execution role | IAM role | `ecsTaskExecutionRole` |
| ECS app/task role | IAM role | `base-ecs-task-role` |
| GitHub deploy role | IAM role | `base-github-deploy-role` |
| Frontend hosting | S3 bucket | `base-frontend-pranay` |
| Uploaded documents | S3 bucket | `base-documents-pranay` |
| CDN | CloudFront distribution | `E1YZJLNPYALOSR` |
| Database | RDS PostgreSQL instance | `base` |
| Database name | PostgreSQL database | `postgres` |
| Database user | PostgreSQL user | `postgres` |
| OpenAI secret | Secrets Manager secret | `base/openai-api-key` |
| Database URL secret | Secrets Manager secret | `base/database-url` |
| Documents bucket secret | Secrets Manager secret | `base/s3-bucket` |

## 3. Local Docker Container Names

For local testing:

| Purpose | Name |
|---|---|
| Local Docker image | `base-api` |
| Local Docker container | `base-api-local` |
| Local backend port | `8080` |

Local build:

```bash
docker build -t base-api .
```

Local run:

```bash
docker run --rm --name base-api-local \
  -p 8080:8080 \
  --env-file backend/.env \
  base-api
```

Health check:

```bash
curl http://localhost:8080/health
```

## 4. ECR Container Creation

ECR is where AWS stores the backend Docker image.

Set shell variables:

```bash
export AWS_ACCOUNT_ID=626210706801
export AWS_REGION=eu-central-1
export ECR_REPOSITORY=base-api
```

Create the ECR repo:

```bash
aws ecr create-repository \
  --repository-name "$ECR_REPOSITORY" \
  --profile base-admin \
  --region "$AWS_REGION"
```

Login Docker to ECR:

```bash
aws ecr get-login-password --region "$AWS_REGION" \
  --profile base-admin \
  | docker login --username AWS --password-stdin \
    "$AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com"
```

Build the backend image:

```bash
docker build -t base-api .
```

Tag it for ECR:

```bash
docker tag base-api:latest \
  "$AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/base-api:latest"
```

Push it:

```bash
docker push "$AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/base-api:latest"
```

Final ECR image URI:

```text
626210706801.dkr.ecr.eu-central-1.amazonaws.com/base-api:latest
```

Current GitHub Actions deployed image:

```text
626210706801.dkr.ecr.eu-central-1.amazonaws.com/base-api:bc1573eef9382df612402e9ed8b36ae8dca8953d
```

## 5. ECS Container Names

In ECS, the backend runs like this:

```text
ECS cluster:           base-cluster
ECS service:           base-api-service
Task definition:       base-api:6
Container name:        base-api
Container port:        8080
CloudWatch log group:  /ecs/base-api-task
Application LB:        base-alb
ALB DNS:               base-alb-2085702204.eu-central-1.elb.amazonaws.com
Target group:          base-api-tg
```

The container name must match this value in GitHub Actions:

```yaml
ECS_CONTAINER_NAME: base-api
```

It also must match the `containerDefinitions.name` field in:

```text
infra/aws/ecs-task-definition.json
```

Current value:

```json
"name": "base-api"
```

## 6. Secrets Manager Names

Create these secrets in AWS Secrets Manager:

| Secret Name | Value |
|---|---|
| `base/openai-api-key` | JSON with `OPENAI_API_KEY` |
| `base/database-url` | JSON with `DATABASE_URL` |
| `base/s3-bucket` | JSON with `DOCUMENTS_BUCKET` and `FRONTEND_BUCKET` |

The app receives these as environment variables in ECS:

```text
OPENAI_API_KEY
DATABASE_URL
S3_BUCKET
```

Never commit the actual values to GitHub.

## 7. Backend Production Environment

The ECS task should run with:

```bash
ENVIRONMENT=production
PORT=8080
METADATA_BACKEND=postgres
DOCUMENT_STORAGE_BACKEND=s3
VECTOR_BACKEND=pgvector
S3_PREFIX=base
AWS_REGION=eu-central-1
CORS_ORIGINS=https://d13xa0pqwvaoqw.cloudfront.net,http://base-alb-2085702204.eu-central-1.elb.amazonaws.com
```

Secrets Manager provides:

```bash
OPENAI_API_KEY
DATABASE_URL
S3_BUCKET
```

Current task definition template:

```text
infra/aws/ecs-task-definition.json
```

This file has been updated with the real account ID, ECR image URI, Secrets Manager ARNs, region, log group, task role, and CloudFront/ALB CORS origins.

## 8. GitHub Actions Names

Add these as GitHub repository or environment variables:

```text
AWS_REGION=eu-central-1
ECR_REPOSITORY=base-api
ECS_CLUSTER=base-cluster
ECS_SERVICE=base-api-service
FRONTEND_BUCKET=base-frontend-pranay
CLOUDFRONT_DISTRIBUTION_ID=E1YZJLNPYALOSR
```

Add this as a GitHub secret:

```text
AWS_DEPLOY_ROLE_ARN=arn:aws:iam::626210706801:role/base-github-deploy-role
```

The deploy workflow that uses these names is:

```text
.github/workflows/deploy-aws.yml
```

## 9. Files In This Repo That Use These Names

| File | What It Controls |
|---|---|
| `Dockerfile` | Builds the backend container image |
| `.dockerignore` | Keeps local data/secrets out of Docker builds |
| `.github/workflows/ci.yml` | Checks and builds the container on push/PR |
| `.github/workflows/deploy-aws.yml` | Pushes image to ECR, deploys ECS, syncs frontend to S3 |
| `infra/aws/ecs-task-definition.json` | ECS task/container template |
| `infra/aws/README.md` | High-level AWS deployment notes |
| `backend/.env.example` | Local and production environment variable reference |

## 10. Creation Order

Create AWS resources in this order:

1. Set account MFA and budget.
2. Pick one backend region: `eu-central-1`.
3. Create S3 buckets:
   - `base-frontend-pranay` - created in `us-east-1`
   - `base-documents-pranay` - created in `us-east-1`
4. Create ECR repository:
   - `base-api` - created in `eu-central-1`
5. Create RDS PostgreSQL:
   - instance: `base` - created in `eu-central-1`
   - database currently used by ECS: `postgres`
   - user currently used by ECS: `postgres`
6. Create Secrets Manager secrets:
   - `base/openai-api-key`
   - `base/database-url`
   - `base/s3-bucket`
7. Create CloudWatch log group:
   - `/ecs/base-api-task` - created in `eu-central-1`
8. Create IAM roles:
   - `ecsTaskExecutionRole` - exists
   - `base-ecs-task-role` - created
   - `base-github-deploy-role` - created
9. Create ECS cluster:
   - `base-cluster` - created in `eu-central-1`
10. Create task definition:
   - family: `base-api`
   - container: `base-api`
11. Create Application Load Balancer:
   - `base-alb` - created in `eu-central-1`
12. Create target group:
   - `base-api-tg` - created in `eu-central-1`
13. Create ECS service:
   - `base-api-service` - created in `eu-central-1` with desired count `1`
14. Create CloudFront distribution:
   - distribution: `E1YZJLNPYALOSR`
   - domain: `d13xa0pqwvaoqw.cloudfront.net`
   - frontend S3 origin: `base-frontend-pranay`
   - `/api/*` route to ALB: `base-alb`
15. Configure GitHub Actions variables/secrets.
16. Run the `Deploy AWS` workflow.
17. Current live checks:
   - ALB health: `http://base-alb-2085702204.eu-central-1.elb.amazonaws.com/health`
   - CloudFront frontend: `https://d13xa0pqwvaoqw.cloudfront.net/`
   - CloudFront API route: `https://d13xa0pqwvaoqw.cloudfront.net/api/projects/`

## 11. How To Refer To This Later

Use these phrases when asking Codex for help:

```text
Use our Base AWS naming doc and help me create the ECR repo.
```

```text
Use our Base AWS naming doc and help me update ecs-task-definition.json with my real ARNs.
```

```text
Use our Base AWS naming doc and debug why base-api-service is failing.
```

```text
Use our Base AWS naming doc and create GitHub Actions variables for deployment.
```

## 12. Quick Name Summary

```text
Project:                  base
Backend region:           eu-central-1
S3 region:                us-east-1
AWS CLI profile:          base-admin
ECR repo:                 base-api
ECR latest image:         pushed
ECS cluster:              base-cluster
ECS service:              base-api-service
ECS desired count:        1
Task family:              base-api:6
Container name:           base-api
Container port:           8080
ALB:                      base-alb
ALB DNS:                  base-alb-2085702204.eu-central-1.elb.amazonaws.com
Target group:             base-api-tg
CloudFront distribution:  E1YZJLNPYALOSR
CloudFront domain:        d13xa0pqwvaoqw.cloudfront.net
CloudWatch logs:          /ecs/base-api-task
Frontend bucket:          base-frontend-pranay
Documents bucket:         base-documents-pranay
RDS instance:             base
Database:                 postgres
Database user:            postgres
GitHub deploy role:       base-github-deploy-role
ECS execution role:       ecsTaskExecutionRole
ECS task role:            base-ecs-task-role
```

## 13. Commands Used For AWS Containers, Resources, And CI/CD

These are the important commands used to create/configure the AWS container deployment and GitHub CI/CD pipeline.

Do not paste real secret values into this file. Commands below use `REDACTED` where a password, OpenAI key, or generated secret value would appear.

### 13.1. Common Shell Variables

```bash
export AWS_PROFILE=base-admin
export AWS_ACCOUNT_ID=626210706801
export AWS_REGION=eu-central-1
export S3_REGION=us-east-1

export PROJECT_SLUG=base
export ECR_REPOSITORY=base-api
export ECS_CLUSTER=base-cluster
export ECS_SERVICE=base-api-service
export ECS_CONTAINER_NAME=base-api
export ECS_TASK_FAMILY=base-api
export ECS_PORT=8080

export FRONTEND_BUCKET=base-frontend-pranay
export DOCUMENTS_BUCKET=base-documents-pranay
export ALB_NAME=base-alb
export ALB_DNS=base-alb-2085702204.eu-central-1.elb.amazonaws.com
export TARGET_GROUP_NAME=base-api-tg
export CLOUDFRONT_DISTRIBUTION_ID=E1YZJLNPYALOSR
export CLOUDFRONT_DOMAIN=d13xa0pqwvaoqw.cloudfront.net

export ECR_REPOSITORY_ARN=arn:aws:ecr:eu-central-1:626210706801:repository/base-api
export ECR_REPOSITORY_URI=626210706801.dkr.ecr.eu-central-1.amazonaws.com/base-api
export ECR_IMAGE_LATEST=626210706801.dkr.ecr.eu-central-1.amazonaws.com/base-api:latest
export ECR_IMAGE_DEPLOYED=626210706801.dkr.ecr.eu-central-1.amazonaws.com/base-api:bc1573eef9382df612402e9ed8b36ae8dca8953d

export ECS_CLUSTER_ARN=arn:aws:ecs:eu-central-1:626210706801:cluster/base-cluster
export ECS_SERVICE_ARN=arn:aws:ecs:eu-central-1:626210706801:service/base-cluster/base-api-service
export ECS_TASK_DEFINITION_ARN=arn:aws:ecs:eu-central-1:626210706801:task-definition/base-api:6

export ALB_ARN=arn:aws:elasticloadbalancing:eu-central-1:626210706801:loadbalancer/app/base-alb/17bc7b314892ff68
export ALB_HTTP_LISTENER_ARN=arn:aws:elasticloadbalancing:eu-central-1:626210706801:listener/app/base-alb/17bc7b314892ff68/5beaccfe2147d088
export TARGET_GROUP_ARN=arn:aws:elasticloadbalancing:eu-central-1:626210706801:targetgroup/base-api-tg/3f5af475d1124e71

export VPC_ID=vpc-03ea2e9d4843da40a
export ALB_SECURITY_GROUP_ID=sg-02d8535c0f4290437
export ECS_SECURITY_GROUP_ID=sg-0c0dcb9be347d599f
export SUBNET_1=subnet-08772e60815f98ebb
export SUBNET_2=subnet-0bd1feed3294f76ce

export CLOUDFRONT_DISTRIBUTION_ARN=arn:aws:cloudfront::626210706801:distribution/E1YZJLNPYALOSR
export CLOUDFRONT_OAC_ID=E2NZ0OL8JD3FUJ
```

### 13.2. AWS CLI Login And Verification

```bash
aws configure sso --profile base-admin
aws sso login --profile base-admin
aws sts get-caller-identity --profile base-admin
aws s3 ls --profile base-admin
aws ecs list-clusters --profile base-admin --region eu-central-1
```

### 13.3. Docker And ECR Container Image Commands

```bash
open -a Docker
docker info

aws ecr create-repository \
  --repository-name "$ECR_REPOSITORY" \
  --profile "$AWS_PROFILE" \
  --region "$AWS_REGION"

aws ecr get-login-password \
  --profile "$AWS_PROFILE" \
  --region "$AWS_REGION" \
  | docker login \
    --username AWS \
    --password-stdin "$AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com"

docker buildx build \
  --platform linux/amd64 \
  -t "$ECR_IMAGE_LATEST" \
  --push .

aws ecr describe-images \
  --profile "$AWS_PROFILE" \
  --region "$AWS_REGION" \
  --repository-name "$ECR_REPOSITORY" \
  --query 'imageDetails[].{Tags:imageTags,Digest:imageDigest,Pushed:imagePushedAt,Size:imageSizeInBytes}' \
  --output json
```

### 13.4. Secrets Manager Commands

The secrets were stored as JSON objects so ECS can inject individual keys.

```bash
aws secretsmanager create-secret \
  --profile "$AWS_PROFILE" \
  --region "$AWS_REGION" \
  --name base/openai-api-key \
  --secret-string '{"OPENAI_API_KEY":"REDACTED"}'

aws secretsmanager create-secret \
  --profile "$AWS_PROFILE" \
  --region "$AWS_REGION" \
  --name base/database-url \
  --secret-string '{"DATABASE_URL":"postgresql://REDACTED"}'

aws secretsmanager create-secret \
  --profile "$AWS_PROFILE" \
  --region "$AWS_REGION" \
  --name base/s3-bucket \
  --secret-string '{"DOCUMENTS_BUCKET":"base-documents-pranay","FRONTEND_BUCKET":"base-frontend-pranay"}'
```

The first database URL was a temporary value. This command rebuilt the real `DATABASE_URL` from the RDS-managed master password secret without printing the password:

```bash
tmp=$(mktemp)

aws secretsmanager get-secret-value \
  --profile "$AWS_PROFILE" \
  --region "$AWS_REGION" \
  --secret-id 'arn:aws:secretsmanager:eu-central-1:626210706801:secret:rds!db-bbfc41d8-91fb-4d5b-87c9-a986608908ba-NrJfXu' \
  --query SecretString \
  --output text \
  | jq -c \
    --arg host 'base.cfqs0omo2oaz.eu-central-1.rds.amazonaws.com' \
    --arg db 'postgres' \
    '{DATABASE_URL: ("postgresql://" + (.username | @uri) + ":" + (.password | @uri) + "@" + $host + ":5432/" + $db)}' \
  > "$tmp"

aws secretsmanager put-secret-value \
  --profile "$AWS_PROFILE" \
  --region "$AWS_REGION" \
  --secret-id base/database-url \
  --secret-string "file://$tmp"

rm -f "$tmp"
```

Secret verification commands used only lengths/keys, not secret values:

```bash
aws secretsmanager get-secret-value \
  --profile "$AWS_PROFILE" \
  --region "$AWS_REGION" \
  --secret-id base/database-url \
  --query 'SecretString' \
  --output text \
  | awk '{print "database_secret_length=" length($0); print ($0 ~ /^\\{/ ? "database_secret_json=yes" : "database_secret_json=no")}'

aws secretsmanager list-secrets \
  --profile "$AWS_PROFILE" \
  --region "$AWS_REGION" \
  --query "SecretList[?starts_with(Name, 'base/')].{Name:Name,ARN:ARN}" \
  --output json
```

### 13.5. IAM Role And Policy Commands

ECS task role trust policy:

```bash
cat > /tmp/base-ecs-task-trust-policy.json <<'JSON'
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "ecs-tasks.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
JSON

aws iam create-role \
  --profile "$AWS_PROFILE" \
  --role-name base-ecs-task-role \
  --assume-role-policy-document file:///tmp/base-ecs-task-trust-policy.json
```

ECS task S3 access policy:

```bash
cat > /tmp/base-task-s3-documents-policy.json <<'JSON'
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:PutObject",
        "s3:DeleteObject"
      ],
      "Resource": "arn:aws:s3:::base-documents-pranay/*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "s3:ListBucket"
      ],
      "Resource": "arn:aws:s3:::base-documents-pranay"
    }
  ]
}
JSON

aws iam put-role-policy \
  --profile "$AWS_PROFILE" \
  --role-name base-ecs-task-role \
  --policy-name base-task-s3-documents \
  --policy-document file:///tmp/base-task-s3-documents-policy.json
```

ECS execution role access to Secrets Manager:

```bash
cat > /tmp/base-execution-secrets-policy.json <<'JSON'
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "secretsmanager:GetSecretValue"
      ],
      "Resource": [
        "arn:aws:secretsmanager:eu-central-1:626210706801:secret:base/openai-api-key-auaT6u",
        "arn:aws:secretsmanager:eu-central-1:626210706801:secret:base/database-url-cHCnfR",
        "arn:aws:secretsmanager:eu-central-1:626210706801:secret:base/s3-bucket-sDSH6J"
      ]
    }
  ]
}
JSON

aws iam put-role-policy \
  --profile "$AWS_PROFILE" \
  --role-name ecsTaskExecutionRole \
  --policy-name base-execution-secrets \
  --policy-document file:///tmp/base-execution-secrets-policy.json
```

GitHub OIDC provider:

```bash
aws iam create-open-id-connect-provider \
  --profile "$AWS_PROFILE" \
  --url https://token.actions.githubusercontent.com \
  --client-id-list sts.amazonaws.com \
  --thumbprint-list 6938fd4d98bab03faadb97b34396831e3780aea1
```

GitHub deploy role trust policy:

```bash
cat > /tmp/base-github-deploy-trust-policy.json <<'JSON'
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Federated": "arn:aws:iam::626210706801:oidc-provider/token.actions.githubusercontent.com"
      },
      "Action": "sts:AssumeRoleWithWebIdentity",
      "Condition": {
        "StringEquals": {
          "token.actions.githubusercontent.com:aud": "sts.amazonaws.com"
        },
        "StringLike": {
          "token.actions.githubusercontent.com:sub": "repo:PranayRudra-3107/Base:*"
        }
      }
    }
  ]
}
JSON

aws iam create-role \
  --profile "$AWS_PROFILE" \
  --role-name base-github-deploy-role \
  --assume-role-policy-document file:///tmp/base-github-deploy-trust-policy.json
```

Split GitHub deploy role policies:

```bash
cat > /tmp/base-github-ecr-auth-policy.json <<'JSON'
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "ecr:GetAuthorizationToken",
      "Resource": "*"
    }
  ]
}
JSON

aws iam put-role-policy \
  --profile "$AWS_PROFILE" \
  --role-name base-github-deploy-role \
  --policy-name base-github-ecr-auth \
  --policy-document file:///tmp/base-github-ecr-auth-policy.json
```

```bash
cat > /tmp/base-github-ecr-repo-policy.json <<'JSON'
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ecr:BatchCheckLayerAvailability",
        "ecr:BatchGetImage",
        "ecr:CompleteLayerUpload",
        "ecr:DescribeImages",
        "ecr:InitiateLayerUpload",
        "ecr:PutImage",
        "ecr:UploadLayerPart"
      ],
      "Resource": "arn:aws:ecr:eu-central-1:626210706801:repository/base-api"
    }
  ]
}
JSON

aws iam put-role-policy \
  --profile "$AWS_PROFILE" \
  --role-name base-github-deploy-role \
  --policy-name base-github-ecr-repo \
  --policy-document file:///tmp/base-github-ecr-repo-policy.json
```

```bash
cat > /tmp/base-github-ecs-policy.json <<'JSON'
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ecs:DescribeServices",
        "ecs:DescribeTaskDefinition",
        "ecs:RegisterTaskDefinition",
        "ecs:UpdateService"
      ],
      "Resource": "*"
    }
  ]
}
JSON

aws iam put-role-policy \
  --profile "$AWS_PROFILE" \
  --role-name base-github-deploy-role \
  --policy-name base-github-ecs \
  --policy-document file:///tmp/base-github-ecs-policy.json
```

```bash
cat > /tmp/base-github-passrole-policy.json <<'JSON'
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "iam:PassRole",
      "Resource": [
        "arn:aws:iam::626210706801:role/ecsTaskExecutionRole",
        "arn:aws:iam::626210706801:role/base-ecs-task-role"
      ]
    }
  ]
}
JSON

aws iam put-role-policy \
  --profile "$AWS_PROFILE" \
  --role-name base-github-deploy-role \
  --policy-name base-github-passrole \
  --policy-document file:///tmp/base-github-passrole-policy.json
```

```bash
cat > /tmp/base-github-s3-policy.json <<'JSON'
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:ListBucket"
      ],
      "Resource": "arn:aws:s3:::base-frontend-pranay"
    },
    {
      "Effect": "Allow",
      "Action": [
        "s3:DeleteObject",
        "s3:GetObject",
        "s3:PutObject"
      ],
      "Resource": "arn:aws:s3:::base-frontend-pranay/*"
    }
  ]
}
JSON

aws iam put-role-policy \
  --profile "$AWS_PROFILE" \
  --role-name base-github-deploy-role \
  --policy-name base-github-s3 \
  --policy-document file:///tmp/base-github-s3-policy.json
```

```bash
cat > /tmp/base-github-cloudfront-policy.json <<'JSON'
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "cloudfront:CreateInvalidation",
      "Resource": "arn:aws:cloudfront::626210706801:distribution/E1YZJLNPYALOSR"
    }
  ]
}
JSON

aws iam put-role-policy \
  --profile "$AWS_PROFILE" \
  --role-name base-github-deploy-role \
  --policy-name base-github-cloudfront \
  --policy-document file:///tmp/base-github-cloudfront-policy.json
```

### 13.6. Network, Target Group, And ECS Service Commands

These commands use the VPC, subnet, and security group IDs discovered during setup.

```bash
export VPC_ID=vpc-03ea2e9d4843da40a
export ALB_SECURITY_GROUP_ID=sg-02d8535c0f4290437
export ECS_SECURITY_GROUP_ID=sg-0c0dcb9be347d599f
export ECS_SECURITY_GROUP_NAME=base-api-service-sg
export SUBNET_1=subnet-08772e60815f98ebb
export SUBNET_2=subnet-0bd1feed3294f76ce
export TARGET_GROUP_ARN=arn:aws:elasticloadbalancing:eu-central-1:626210706801:targetgroup/base-api-tg/3f5af475d1124e71
export ALB_ARN=arn:aws:elasticloadbalancing:eu-central-1:626210706801:loadbalancer/app/base-alb/17bc7b314892ff68
export ALB_HTTP_LISTENER_ARN=arn:aws:elasticloadbalancing:eu-central-1:626210706801:listener/app/base-alb/17bc7b314892ff68/5beaccfe2147d088
```

Security group commands:

```bash
aws ec2 create-security-group \
  --profile "$AWS_PROFILE" \
  --region "$AWS_REGION" \
  --group-name base-api-service-sg \
  --description "Base API ECS service tasks" \
  --vpc-id "$VPC_ID"

aws ec2 authorize-security-group-ingress \
  --profile "$AWS_PROFILE" \
  --region "$AWS_REGION" \
  --group-id "$ECS_SECURITY_GROUP_ID" \
  --protocol tcp \
  --port 8080 \
  --source-group "$ALB_SECURITY_GROUP_ID"

aws ec2 authorize-security-group-ingress \
  --profile "$AWS_PROFILE" \
  --region "$AWS_REGION" \
  --group-id "$ALB_SECURITY_GROUP_ID" \
  --protocol tcp \
  --port 5432 \
  --source-group "$ECS_SECURITY_GROUP_ID"
```

Target group and listener commands:

```bash
aws elbv2 create-target-group \
  --profile "$AWS_PROFILE" \
  --region "$AWS_REGION" \
  --name "$TARGET_GROUP_NAME" \
  --protocol HTTP \
  --port 8080 \
  --target-type ip \
  --vpc-id "$VPC_ID" \
  --health-check-protocol HTTP \
  --health-check-path /health \
  --matcher HttpCode=200

aws elbv2 modify-target-group-attributes \
  --profile "$AWS_PROFILE" \
  --region "$AWS_REGION" \
  --target-group-arn "$TARGET_GROUP_ARN" \
  --attributes Key=deregistration_delay.timeout_seconds,Value=30

aws elbv2 modify-listener \
  --profile "$AWS_PROFILE" \
  --region "$AWS_REGION" \
  --listener-arn "$ALB_HTTP_LISTENER_ARN" \
  --default-actions Type=forward,TargetGroupArn="$TARGET_GROUP_ARN"
```

Task definition and service commands:

```bash
aws logs create-log-group \
  --profile "$AWS_PROFILE" \
  --region "$AWS_REGION" \
  --log-group-name /ecs/base-api-task

aws ecs register-task-definition \
  --profile "$AWS_PROFILE" \
  --region "$AWS_REGION" \
  --cli-input-json file://infra/aws/ecs-task-definition.json

aws ecs create-service \
  --profile "$AWS_PROFILE" \
  --region "$AWS_REGION" \
  --cluster "$ECS_CLUSTER" \
  --service-name "$ECS_SERVICE" \
  --task-definition arn:aws:ecs:eu-central-1:626210706801:task-definition/base-api:2 \
  --desired-count 0 \
  --launch-type FARGATE \
  --network-configuration "awsvpcConfiguration={subnets=[$SUBNET_1,$SUBNET_2],securityGroups=[$ECS_SECURITY_GROUP_ID],assignPublicIp=ENABLED}" \
  --load-balancers "targetGroupArn=$TARGET_GROUP_ARN,containerName=$ECS_CONTAINER_NAME,containerPort=$ECS_PORT"

aws ecs update-service \
  --profile "$AWS_PROFILE" \
  --region "$AWS_REGION" \
  --cluster "$ECS_CLUSTER" \
  --service "$ECS_SERVICE" \
  --task-definition arn:aws:ecs:eu-central-1:626210706801:task-definition/base-api:3 \
  --desired-count 1 \
  --force-new-deployment

aws ecs wait services-stable \
  --profile "$AWS_PROFILE" \
  --region "$AWS_REGION" \
  --cluster "$ECS_CLUSTER" \
  --services "$ECS_SERVICE"
```

After GitHub Actions deployment, ECS registered and deployed `base-api:6`.

### 13.7. CloudFront And Frontend S3 Commands

CloudFront OAC creation:

```bash
cat > /tmp/base-cloudfront-oac.json <<'JSON'
{
  "Name": "base-frontend-oac",
  "Description": "OAC for Base frontend bucket",
  "SigningProtocol": "sigv4",
  "SigningBehavior": "always",
  "OriginAccessControlOriginType": "s3"
}
JSON

aws cloudfront create-origin-access-control \
  --profile "$AWS_PROFILE" \
  --origin-access-control-config file:///tmp/base-cloudfront-oac.json
```

CloudFront distribution creation used a generated distribution config with:

```text
Distribution ID:  E1YZJLNPYALOSR
OAC ID:           E2NZ0OL8JD3FUJ
Default origin:   base-frontend-pranay.s3.us-east-1.amazonaws.com
API origin:       base-alb-2085702204.eu-central-1.elb.amazonaws.com
API behavior:     /api/*
```

Command:

```bash
aws cloudfront create-distribution \
  --profile "$AWS_PROFILE" \
  --distribution-config file:///tmp/base-cloudfront-distribution.json
```

Frontend bucket policy for CloudFront:

```bash
cat > /tmp/base-frontend-cloudfront-policy.json <<'JSON'
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowCloudFrontServicePrincipalReadOnly",
      "Effect": "Allow",
      "Principal": {
        "Service": "cloudfront.amazonaws.com"
      },
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::base-frontend-pranay/*",
      "Condition": {
        "StringEquals": {
          "AWS:SourceArn": "arn:aws:cloudfront::626210706801:distribution/E1YZJLNPYALOSR"
        }
      }
    }
  ]
}
JSON

aws s3api put-bucket-policy \
  --profile "$AWS_PROFILE" \
  --bucket "$FRONTEND_BUCKET" \
  --policy file:///tmp/base-frontend-cloudfront-policy.json
```

Frontend upload and invalidation:

```bash
aws s3 sync frontend/ "s3://$FRONTEND_BUCKET/" \
  --profile "$AWS_PROFILE" \
  --delete \
  --exclude "package.json" \
  --cache-control "public,max-age=300"

aws cloudfront create-invalidation \
  --profile "$AWS_PROFILE" \
  --distribution-id "$CLOUDFRONT_DISTRIBUTION_ID" \
  --paths "/*"
```

### 13.8. Runtime Debug And Verification Commands

```bash
aws ecs describe-services \
  --profile "$AWS_PROFILE" \
  --region "$AWS_REGION" \
  --cluster "$ECS_CLUSTER" \
  --services "$ECS_SERVICE" \
  --query 'services[0].{Status:status,Desired:desiredCount,Running:runningCount,Pending:pendingCount,TaskDefinition:taskDefinition,Events:events[:5]}' \
  --output json

aws ecs list-tasks \
  --profile "$AWS_PROFILE" \
  --region "$AWS_REGION" \
  --cluster "$ECS_CLUSTER" \
  --service-name "$ECS_SERVICE" \
  --desired-status RUNNING

aws logs tail /ecs/base-api-task \
  --profile "$AWS_PROFILE" \
  --region "$AWS_REGION" \
  --since 30m \
  --format short

aws elbv2 describe-target-health \
  --profile "$AWS_PROFILE" \
  --region "$AWS_REGION" \
  --target-group-arn "$TARGET_GROUP_ARN" \
  --query 'TargetHealthDescriptions[].{Target:Target.Id,State:TargetHealth.State,Reason:TargetHealth.Reason,Description:TargetHealth.Description}' \
  --output json

curl http://base-alb-2085702204.eu-central-1.elb.amazonaws.com/health
curl https://d13xa0pqwvaoqw.cloudfront.net/api/projects/
curl -I https://d13xa0pqwvaoqw.cloudfront.net/
```

### 13.9. GitHub CLI And CI/CD Commands

Install and authenticate GitHub CLI:

```bash
brew install gh

gh auth login \
  --hostname github.com \
  --git-protocol https \
  --web \
  --scopes repo,workflow

gh auth status
```

Set GitHub Actions repository variables:

```bash
gh variable set AWS_REGION \
  --repo PranayRudra-3107/Base \
  --body eu-central-1

gh variable set ECR_REPOSITORY \
  --repo PranayRudra-3107/Base \
  --body base-api

gh variable set ECS_CLUSTER \
  --repo PranayRudra-3107/Base \
  --body base-cluster

gh variable set ECS_SERVICE \
  --repo PranayRudra-3107/Base \
  --body base-api-service

gh variable set FRONTEND_BUCKET \
  --repo PranayRudra-3107/Base \
  --body base-frontend-pranay

gh variable set CLOUDFRONT_DISTRIBUTION_ID \
  --repo PranayRudra-3107/Base \
  --body E1YZJLNPYALOSR
```

Set GitHub Actions repository secret:

```bash
gh secret set AWS_DEPLOY_ROLE_ARN \
  --repo PranayRudra-3107/Base \
  --body arn:aws:iam::626210706801:role/base-github-deploy-role
```

Verify GitHub Actions configuration:

```bash
gh variable list --repo PranayRudra-3107/Base
gh secret list --repo PranayRudra-3107/Base
gh workflow list --repo PranayRudra-3107/Base
```

Commit and push the CI/CD files:

```bash
git add \
  Dockerfile \
  README.md \
  backend/.env.example \
  backend/app/api/documents.py \
  backend/app/core/config.py \
  backend/app/main.py \
  backend/app/services/audit_log.py \
  backend/app/services/projects.py \
  backend/app/services/storage.py \
  backend/app/services/vector_store.py \
  backend/app/services/database.py \
  backend/requirements.txt \
  .dockerignore \
  .github \
  infra

git commit -m "Add AWS deployment and CI/CD setup"
git push origin main
```

Trigger and watch the deployment workflow:

```bash
gh workflow run "Deploy AWS" \
  --repo PranayRudra-3107/Base \
  --ref main \
  -f environment=prod

gh run watch 26363680084 \
  --repo PranayRudra-3107/Base \
  --interval 10 \
  --exit-status

gh run view 26363680084 \
  --repo PranayRudra-3107/Base \
  --json status,conclusion,createdAt,updatedAt,url,jobs
```

Commit and push the documentation update after successful deployment:

```bash
git add infra/aws/AWS_CONTAINER_CREATION_README.md
git commit -m "Document successful AWS CI/CD deployment"
git push origin main
```

Watch the automatic CI run from the documentation push:

```bash
gh run list \
  --repo PranayRudra-3107/Base \
  --branch main \
  --limit 5

gh run watch 26337421896 \
  --repo PranayRudra-3107/Base \
  --interval 10 \
  --exit-status
```

### 13.10. Notes About Existing Resources

Some AWS resources were already present when the deployment was completed and were discovered/configured rather than created from scratch:

```text
RDS instance:  base
ALB:           base-alb
S3 buckets:    base-frontend-pranay, base-documents-pranay
ECS cluster:   base-cluster
```

Useful discovery commands:

```bash
aws rds describe-db-instances \
  --profile "$AWS_PROFILE" \
  --region "$AWS_REGION" \
  --db-instance-identifier base

aws elbv2 describe-load-balancers \
  --profile "$AWS_PROFILE" \
  --region "$AWS_REGION" \
  --names base-alb

aws s3api get-bucket-location \
  --profile "$AWS_PROFILE" \
  --bucket "$FRONTEND_BUCKET"

aws ecs describe-clusters \
  --profile "$AWS_PROFILE" \
  --region "$AWS_REGION" \
  --clusters "$ECS_CLUSTER"
```
