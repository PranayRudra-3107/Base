# AWS Deployment Notes

This folder contains the deploy-time scaffolding for running Base on AWS.

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
```

Current live endpoints:

```text
Frontend:        https://d13xa0pqwvaoqw.cloudfront.net/
Backend health:  http://base-alb-2085702204.eu-central-1.elb.amazonaws.com/health
CloudFront API:  https://d13xa0pqwvaoqw.cloudfront.net/api/projects/
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

`ecs-task-definition.json` is a deployable template and has been filled with the current AWS account ID, role ARNs, secret ARNs, region, ECR image URI, and CloudFront/ALB CORS origins.

The GitHub deploy workflow updates only the container image field. Infrastructure should be created first with Terraform, CDK, CloudFormation, or the AWS console.
