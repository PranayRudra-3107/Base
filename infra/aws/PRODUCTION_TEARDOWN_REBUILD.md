# Base Production Teardown And Rebuild Notes

Last updated: 2026-07-13

This file records the AWS production architecture before deletion so the project can be rebuilt later without keeping billable resources alive.

## Current Temporary Rebuild

The architecture was rebuilt for a four-day public demo using the same account and Frankfurt region. Unlike the historical deployment below, both S3 buckets now live in `eu-central-1` to avoid cross-region document traffic.

| Resource | Current value |
|---|---|
| Public URL | `https://d2llye5km5il24.cloudfront.net/` |
| CloudFront | `E2AVPU9QAGIB72` |
| CloudFront OAC | `EQTEMDO3H6TD1` |
| ALB | `base-alb`, DNS `base-alb-1755646895.eu-central-1.elb.amazonaws.com` |
| Target group | `base-api-tg` |
| ECS | cluster `base-cluster`, service `base-api-service`, task family `base-api` |
| RDS | `base`, PostgreSQL `17.9`, `db.t4g.micro`, 20 GB gp3, private |
| S3 | `base-frontend-pranay`, `base-documents-pranay` in `eu-central-1` |
| Budget | `base-four-day-demo`, USD 20, `CUSTOM`, `2026-07-13T00:00:00Z` to `2026-07-16T21:00:00Z` |
| Budget stop SNS | `base-budget-stop`, invokes `base-demo-teardown` at 100% actual spend |
| Teardown Lambda | `base-demo-teardown` |
| Deadline | `2026-07-16T21:00:00Z` / 23:00 Europe/Berlin |

Scheduler jobs `base-demo-teardown-primary`, `base-demo-teardown-finalizer`, and `base-demo-teardown-last-pass` run at `21:00Z`, `21:35Z`, and `22:15Z`. The later runs finish resources whose deletion is asynchronous. The source is `infra/aws/demo_teardown.py`, and `.github/workflows/teardown-aws.yml` is the manual backup.

The expiring AWS Budget monitors this four-day interval. Its 100% actual-spend notification invokes the teardown Lambda through SNS. It is not a hard spend lock and cost reporting can lag, so the fixed scheduler runs remain the authoritative controls for stopping costs.

No final RDS snapshot is retained. The RDS-managed credential secret is also an explicit teardown target. The public UI has no login for the temporary demo, while `/mcp` remains protected with a generated key in `base/mcp-api-key`.

No secret values are stored here. Recreate `OPENAI_API_KEY`, `DATABASE_URL`, and bucket secrets manually in AWS Secrets Manager when rebuilding.

## Account And Regions

```text
AWS account:      626210706801
CLI profile:      base-admin
Backend region:   eu-central-1
Frontend S3:      us-east-1
SSO start URL:    https://d-996748b0aa.awsapps.com/start
```

## Original Production Flow

```text
Browser
  -> CloudFront distribution E1YZJLNPYALOSR
     -> default route: S3 bucket base-frontend-pranay / index.html
     -> /api/* route: Application Load Balancer base-alb
        -> target group base-api-tg
        -> ECS Fargate service base-api-service
           -> task definition base-api:10
           -> ECR image 626210706801.dkr.ecr.eu-central-1.amazonaws.com/base-api:e358e18f07152365da132899a6991b620b6dc783
           -> RDS PostgreSQL instance base
           -> S3 documents bucket base-documents-pranay
           -> Secrets Manager secrets
```

## Resource Names To Recreate

| Layer | Resource |
|---|---|
| Frontend bucket | `base-frontend-pranay` |
| Documents bucket | `base-documents-pranay` |
| CDN | CloudFront distribution `E1YZJLNPYALOSR`, domain `d13xa0pqwvaoqw.cloudfront.net` |
| CloudFront OAC | `base-frontend-oac`, ID `E2NZ0OL8JD3FUJ` |
| API load balancer | `base-alb` |
| API target group | `base-api-tg`, HTTP `8080`, health check `/health` |
| ECS cluster | `base-cluster` |
| ECS service | `base-api-service` |
| ECS task family | `base-api` |
| Container name | `base-api` |
| Container port | `8080` |
| ECR repository | `base-api` |
| Database | RDS PostgreSQL `base`, class `db.t4g.micro`, `20 GB gp2`, encrypted |
| VPC | default VPC `vpc-03ea2e9d4843da40a` |
| Public subnets | `subnet-08772e60815f98ebb`, `subnet-0bd1feed3294f76ce` |
| RDS subnet | `subnet-07b2d84c8a524d1e5` |
| ALB/default security group | `sg-02d8535c0f4290437` |
| ECS task security group | `sg-0c0dcb9be347d599f` / `base-api-service-sg` |
| ECS task role | `base-ecs-task-role` |
| ECS execution role | `ecsTaskExecutionRole` |
| GitHub deploy role | `base-github-deploy-role` |
| RDS monitoring role | `rds-monitoring-role` |
| ECS log group | `/ecs/base-api-task` |
| RDS OS metrics log group | `RDSOSMetrics` |

## Runtime Environment

The ECS container used these environment variables:

```text
ENVIRONMENT=production
PORT=8080
AWS_REGION=eu-central-1
METADATA_BACKEND=postgres
DOCUMENT_STORAGE_BACKEND=s3
VECTOR_BACKEND=pgvector
S3_PREFIX=base
CORS_ORIGINS=https://d13xa0pqwvaoqw.cloudfront.net,http://base-alb-2085702204.eu-central-1.elb.amazonaws.com
```

The ECS task loaded these secrets from Secrets Manager:

```text
base/openai-api-key    JSON key OPENAI_API_KEY
base/database-url      JSON key DATABASE_URL
base/s3-bucket         JSON key DOCUMENTS_BUCKET
```

## Rebuild Order

1. Configure AWS SSO profile `base-admin`.
2. Create or reuse the S3 buckets.
3. Create the RDS PostgreSQL database and enable the application schema/vector setup from the backend.
4. Store fresh secrets in Secrets Manager.
5. Create the ECR repository and push a backend image.
6. Create the ECS task execution role and task role.
7. Register the ECS task definition from `infra/aws/ecs-task-definition.json`, updating secret ARNs and image URI.
8. Create the target group and ALB.
9. Create the ECS service attached to the target group.
10. Upload `frontend/index.html` to the frontend S3 bucket.
11. Create CloudFront with the S3 frontend origin and `/api/*` ALB origin. Keep custom error responses empty because the frontend uses hash routes and API errors must retain their original status and JSON body.
12. Configure GitHub Actions variables/secrets again if CI/CD should redeploy production.

More detailed historical commands are in `infra/aws/AWS_CONTAINER_CREATION_README.md`.

## Teardown Intent

The production environment is being deleted to avoid ongoing AWS charges. The teardown intentionally skips final RDS snapshots because snapshots and retained backups can still incur storage costs.

Data-loss note: uploaded S3 documents, ECR images, CloudWatch logs, Secrets Manager values, and the RDS database contents are not preserved in AWS after teardown. The local project code and this rebuild map are preserved.
