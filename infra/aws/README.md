# AWS Deployment Notes

This folder contains the deploy-time scaffolding for running Base on AWS.

## Current Four-Day Demo

This environment was rebuilt on 2026-07-13 for a public recruiter demo and is scheduled for automatic deletion.

```text
Account:          626210706801
Region:           eu-central-1
Public URL:       https://d2llye5km5il24.cloudfront.net/
CloudFront ID:    E2AVPU9QAGIB72
ALB:              base-alb-1755646895.eu-central-1.elb.amazonaws.com
ECS cluster:      base-cluster
ECS service:      base-api-service
RDS:              base / PostgreSQL 17.9 / db.t4g.micro / 20 GB gp3
Frontend bucket:  base-frontend-pranay
Documents bucket: base-documents-pranay
Budget:           base-four-day-demo / USD 20
Teardown:         2026-07-16T21:00:00Z (23:00 Europe/Berlin)
```

The primary AWS Scheduler job `base-demo-teardown-primary` invokes Lambda `base-demo-teardown`. Two one-time retries run at `21:35Z` and `22:15Z`; all three schedules delete themselves after completion. The Lambda stops ECS first, deletes the ALB and RDS without a final snapshot, disables/deletes CloudFront, empties S3, removes ECR and secrets, and retries dependency cleanup safely.

The public UI has no login for this time-limited demo. `/mcp` is still bearer-key protected. The MCP key and all other secret values are stored only in Secrets Manager.

For the exact resource/container names to create and reuse in future conversations, see:

```text
infra/aws/AWS_CONTAINER_CREATION_README.md
```

## Target Architecture

```text
CloudFront
  |-- S3 frontend origin
  |-- /api/* -> Application Load Balancer -> ECS Fargate backend

ECS Fargate backend
  |-- RDS/Aurora PostgreSQL with pgvector
  |-- S3 uploaded source documents
  |-- Secrets Manager for OPENAI_API_KEY, DATABASE_URL, and S3_BUCKET
  |-- CloudWatch Logs
```

## Required AWS Resources

- ECR repository for the backend image.
- ECS cluster and Fargate service behind an Application Load Balancer.
- S3 bucket for the static frontend.
- S3 bucket for uploaded project source documents. This can be the same bucket with a private prefix, but separate buckets are cleaner.
- RDS PostgreSQL or Aurora PostgreSQL with the `vector` extension available.
- Secrets Manager secrets:
  - `base/openai-api-key` with JSON key `OPENAI_API_KEY`
  - `base/database-url` with JSON key `DATABASE_URL`
  - `base/s3-bucket` with JSON key `DOCUMENTS_BUCKET`
  - `base/mcp-api-key` with JSON key `MCP_API_KEY`
- IAM OIDC role for GitHub Actions deployment.

## Production Environment Variables

```bash
ENVIRONMENT=production
METADATA_BACKEND=postgres
DOCUMENT_STORAGE_BACKEND=s3
VECTOR_BACKEND=pgvector
DATABASE_URL=postgresql://...
S3_BUCKET=your-private-upload-bucket
S3_PREFIX=base
AWS_REGION=eu-central-1
CORS_ORIGINS=https://yourdomain.com
OPENAI_API_KEY=sk-...
MCP_API_KEY=generated-secret
```

Current live endpoints:

```text
Frontend:        https://d2llye5km5il24.cloudfront.net/
Backend API:     https://d2llye5km5il24.cloudfront.net/api/projects/
MCP status:      https://d2llye5km5il24.cloudfront.net/api/mcp/status
MCP transport:   https://d2llye5km5il24.cloudfront.net/mcp
```

## GitHub Actions Variables

Configure these as repository or environment variables:

```text
AWS_REGION
ECR_REPOSITORY
ECS_CLUSTER
ECS_SERVICE
FRONTEND_BUCKET
CLOUDFRONT_DISTRIBUTION_ID
```

Configure this as a repository or environment secret:

```text
AWS_DEPLOY_ROLE_ARN
```

## ECS Task Definition

`ecs-task-definition.json` is a deployable template and has been filled with the current AWS account ID, role ARNs, secret ARNs, region, ECR image URI, and CloudFront CORS origin.

`demo_teardown.py` is deployed as Lambda `base-demo-teardown`. Do not invoke it while the demo should remain online. The manual backup workflow is `.github/workflows/teardown-aws.yml`.

The GitHub deploy workflow updates only the container image field. Infrastructure should be created first with Terraform, CDK, CloudFormation, or the AWS console.
