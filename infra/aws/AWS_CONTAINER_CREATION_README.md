# Base AWS Container Creation And Resource Names

Use this file as the naming reference for deploying Base on AWS. When you talk with Codex later, you can say things like:

```text
Use the names from infra/aws/AWS_CONTAINER_CREATION_README.md
```

or:

```text
Help me create the base-api ECS service.
```

## 1. Values To Fill Once

Fill these values for your AWS account before creating resources.

```bash
AWS_ACCOUNT_ID=626210706801
AWS_REGION=eu-central-1
S3_REGION=us-east-1
IAM_IDENTITY_CENTER_REGION=eu-central-1
IAM_IDENTITY_CENTER_START_URL=https://d-996748b0aa.awsapps.com/start
AWS_CLI_PROFILE=base-admin
PROJECT_SLUG=base
UNIQUE_SUFFIX=pranay
DOMAIN_NAME=not-configured-yet
```

Example:

```bash
AWS_ACCOUNT_ID=626210706801
AWS_REGION=eu-central-1
S3_REGION=us-east-1
IAM_IDENTITY_CENTER_REGION=eu-central-1
IAM_IDENTITY_CENTER_START_URL=https://d-996748b0aa.awsapps.com/start
AWS_CLI_PROFILE=base-admin
PROJECT_SLUG=base
UNIQUE_SUFFIX=pranay
DOMAIN_NAME=base.example.com
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
| ECS task definition | eu-central-1 | `base-api:3` | active |
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
Task definition:   base-api:3
Target group:      base-api-tg
Target health:     healthy
Container image:   626210706801.dkr.ecr.eu-central-1.amazonaws.com/base-api:latest
```

Important deployment fix that was made:

```text
Initial ECS startup failed because DATABASE_URL was injected as the full JSON secret.
Task definition base-api:3 now uses Secrets Manager JSON key selectors:

OPENAI_API_KEY -> base/openai-api-key:OPENAI_API_KEY
DATABASE_URL   -> base/database-url:DATABASE_URL
S3_BUCKET      -> base/s3-bucket:DOCUMENTS_BUCKET
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

CI/CD remaining handoff:

```text
The GitHub Actions workflow exists at .github/workflows/deploy-aws.yml.
The AWS deploy role exists: arn:aws:iam::626210706801:role/base-github-deploy-role

The GitHub CLI was not installed/authenticated locally, so repository variables
and secrets still need to be added in GitHub.
```

GitHub repository variables to add:

```text
AWS_REGION=eu-central-1
ECR_REPOSITORY=base-api
ECS_CLUSTER=base-cluster
ECS_SERVICE=base-api-service
FRONTEND_BUCKET=base-frontend-pranay
CLOUDFRONT_DISTRIBUTION_ID=E1YZJLNPYALOSR
```

GitHub repository secret to add:

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

Final ECR image URI format:

```text
<AWS_ACCOUNT_ID>.dkr.ecr.<AWS_REGION>.amazonaws.com/base-api:latest
```

Example:

```text
626210706801.dkr.ecr.eu-central-1.amazonaws.com/base-api:latest
```

## 5. ECS Container Names

In ECS, the backend runs like this:

```text
ECS cluster:           base-cluster
ECS service:           base-api-service
Task definition:       base-api:3
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
CORS_ORIGINS=https://yourdomain.com
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
Task family:              base-api:3
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
