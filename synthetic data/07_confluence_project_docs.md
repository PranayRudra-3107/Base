# Confluence Space - Project Atlas Documentation

Space: CONFLUENCE / ATLAS
Pages exported on 2026-04-30

## Page: Project Atlas Overview

Created: 2025-05-03
Owner: Maya Chen

Project Atlas moves checkout traffic from the legacy monolith into the Atlas platform. The core services are:

- atlas-web: customer checkout UI and feature flag controlled route selection.
- atlas-api: checkout orchestration, payment facade, cart total calculation, inventory calls.
- atlas-worker: replay comparison, email receipt retry, finance reconciliation jobs.
- atlas-infra: Grafana dashboards, PagerDuty routing, delivery pipelines, database resources.

Primary workstreams:

- ATLAS-100 Project Atlas checkout modernization kickoff.
- ATLAS-110 Checkout traffic shadowing and validation.
- ATLAS-118 Production cutover and resilience.

Success metrics:

- p95 latency below 450ms during production routing.
- error rate below 0.5 percent for normal traffic.
- uptime at or above 99.95 percent during rollout.
- no double payment captures.
- support case volume below 25 checkout cases per week after 100 percent cutover.

## Page: Architecture Decision Record - Routing And Fallback

Created: 2025-05-14
Updated: 2025-10-03
Owner: Ravi Patel

Decision:

Checkout routing is controlled by feature flags in atlas-web and atlas-api. Supported route percentages are 1, 5, 25, 50, 75, and 100. The monolith fallback stays warm until Atlas has handled 100 percent checkout traffic for 30 healthy days.

Reason:

The team needs rollback without a database restore. Fast rollback is required because incidents such as PD-1002 and PD-1003 can affect customer checkout conversion quickly.

Rollback steps:

1. Open PagerDuty incident if customer impact is active.
2. Announce in Teams channel Atlas Checkout Modernization.
3. Set route percentage to previous healthy value.
4. Check Grafana for p95 latency, error rate, uptime, CPU, memory, and traffic.
5. Verify database connections and slow queries.
6. Ask support to watch Zendesk checkout cases for 60 minutes.

Related work items: ATLAS-119, ATLAS-120, ATLAS-132.

## Page: Payment Idempotency And PCI Notes

Created: 2025-05-28
Updated: 2025-11-21
Owner: Luca Moretti

Decision:

Every payment mutation uses checkout_id plus attempt_number as idempotency key. Atlas services never store card data. Payment tokens expire after 15 minutes.

Audit fields:

- checkout_id
- attempt_number
- payment_decision_code
- retry_safe flag
- source route percentage
- trace_id

Do not log card number, CVV, billing address line 1, or token secret.

Related tickets: ATLAS-103, ATLAS-108, ATLAS-123, ATLAS-136.

## Page: Onboarding Guide For New Backend Engineer

Created: 2025-06-19
Updated: 2026-04-24
Owner: Maya Chen

First week checklist:

1. Read this Confluence page and the routing decision record.
2. Review work items ATLAS-121, ATLAS-126, ATLAS-129, ATLAS-133, and ATLAS-137.
3. Check GitHub repos atlas-api, atlas-worker, atlas-web, and atlas-infra.
4. Read PR-145, PR-156, PR-166, PR-170, and PR-173.
5. Open Grafana checkout traffic dashboard and compare p95 latency before and after 2026-03-03.
6. Review database health checks for storage, slow queries, connection pool, replication lag, and cache hit rate.
7. Join the Teams Atlas Checkout Modernization channel.
8. Read PagerDuty incidents PD-1002, PD-1003, PD-1004, and PD-1005.
9. Run the rollback drill in staging with Nora Singh.

Current owners:

- Engineering lead: Ravi Patel.
- Product manager: Maya Chen.
- SRE: Nora Singh.
- Database: Samir Rao.
- Payments: Luca Moretti.
- Backend: Aisha Khan.
- Frontend: Jon Bell.
- Support: Elena Brooks.

## Page: Release Checklist

Created: 2025-09-18
Updated: 2026-02-27
Owner: Nora Singh

Required before route increase:

- Jira release ticket is approved.
- GitHub release branch is up to date with main.
- Pull requests have two approvals and passing integration tests.
- Grafana p95 latency is below 450ms for seven consecutive days.
- Grafana error rate is below 0.5 percent for seven consecutive days.
- Database connections are below 75 percent.
- Slow queries are below 80 per hour.
- PagerDuty escalation policy is active.
- Teams war room is staffed.
- Support macros are updated.
- Rollback runbook has been tested.

Route increase history:

- 2025-08-08: ATLAS-114 enabled 5 percent shadow traffic.
- 2025-09-12: ATLAS-116 enabled 25 percent shadow traffic.
- 2025-12-05: ATLAS-125 enabled 50 percent production routing.
- 2026-01-24: ATLAS-128 enabled 75 percent production routing.
- 2026-03-03: ATLAS-132 enabled 100 percent production routing.

## Page: Known Risks And Open Questions

Created: 2026-04-24
Owner: Ravi Patel

Open risks:

- ATLAS-134 is blocked by finance reconciliation. Do not archive monolith checkout write path until ATLAS-136 is resolved.
- ATLAS-137 tracks database storage risk. Storage is expected to reach 82 percent by May and 90 percent by June if archive is delayed.
- Refund dashboard currently misses retry reversals for 0.4 percent of April refunds.
- Platform support team needs KT on PagerDuty and database dashboard before full ownership transfer.

Resolved risks:

- ATLAS-115 tax rounding variance resolved before 25 percent traffic.
- ATLAS-121 p95 latency incident resolved by cache warmup and query fix.
- ATLAS-126 database connection incident resolved by pool tuning and read replica.
- ATLAS-129 inventory timeout incident resolved by retry budget and circuit breaker.
- ATLAS-133 mobile Safari p99 latency spike resolved by async address validation.
