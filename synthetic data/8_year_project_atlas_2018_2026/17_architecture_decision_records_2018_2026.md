# Architecture Decision Records - Project Atlas 2018-2026

Synthetic ADRs for checkout modernization.

## ADR-001-1: Dual-write migration for order-ledger
- Date: 2018-06-12
- Status: Accepted with Follow-up
- Owner: Yara Haddad
- Related: ATLAS-3450, PR-6771, PD-2771

### Context
order-ledger needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Publish dashboard, alert, runbook, and support macro before declaring release ready.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-001-2: Payment retry policy for order-ledger
- Date: 2018-06-19
- Status: Accepted with Follow-up
- Owner: Sara Novak
- Related: ATLAS-3097, PR-15996, PD-2348

### Context
order-ledger needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Require database migration rehearsal and rollback SQL before production rollout.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-001-3: Feature flag rollout for auth-gateway
- Date: 2018-06-08
- Status: Accepted
- Owner: Harper Lee
- Related: ATLAS-5337, PR-9722, PD-2443

### Context
auth-gateway needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use a progressive traffic flag and require SLO evidence before increasing exposure.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-002-1: Observability standard for notification-service
- Date: 2018-07-07
- Status: Accepted
- Owner: Aisha Khan
- Related: ATLAS-1433, PR-14790, PD-2601

### Context
notification-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Keep reads dual-run until reconciliation errors stay below threshold for two sprints.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-002-2: Rollback strategy for payment-orchestrator
- Date: 2018-07-25
- Status: Under Review
- Owner: Aisha Khan
- Related: ATLAS-2381, PR-12354, PD-2856

### Context
payment-orchestrator needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Require database migration rehearsal and rollback SQL before production rollout.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-002-3: Database partitioning for tax-service
- Date: 2018-07-17
- Status: Accepted with Follow-up
- Owner: Harper Lee
- Related: ATLAS-3749, PR-9997, PD-2021

### Context
tax-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use a progressive traffic flag and require SLO evidence before increasing exposure.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-003-1: Payment retry policy for cart-service
- Date: 2018-08-04
- Status: Accepted
- Owner: Nora Singh
- Related: ATLAS-4934, PR-10550, PD-2013

### Context
cart-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use checkout_id plus attempt_number as the idempotency key for payment mutations.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-003-2: Payment retry policy for cart-service
- Date: 2018-08-08
- Status: Accepted with Follow-up
- Owner: Samir Rao
- Related: ATLAS-4049, PR-12776, PD-2793

### Context
cart-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use checkout_id plus attempt_number as the idempotency key for payment mutations.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-003-3: Dual-write migration for auth-gateway
- Date: 2018-08-11
- Status: Accepted with Follow-up
- Owner: Yara Haddad
- Related: ATLAS-1181, PR-9300, PD-2038

### Context
auth-gateway needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Require database migration rehearsal and rollback SQL before production rollout.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-004-1: Feature flag rollout for analytics-pipeline
- Date: 2018-09-22
- Status: Accepted
- Owner: Iris Wang
- Related: ATLAS-3632, PR-10623, PD-2359

### Context
analytics-pipeline needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Keep reads dual-run until reconciliation errors stay below threshold for two sprints.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-004-2: Payment retry policy for payment-orchestrator
- Date: 2018-09-10
- Status: Superseded
- Owner: Kim Tan
- Related: ATLAS-4187, PR-9052, PD-2241

### Context
payment-orchestrator needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Require database migration rehearsal and rollback SQL before production rollout.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-004-3: Idempotency key design for notification-service
- Date: 2018-09-09
- Status: Accepted
- Owner: Harper Lee
- Related: ATLAS-2513, PR-5329, PD-2270

### Context
notification-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use a progressive traffic flag and require SLO evidence before increasing exposure.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-005-1: Dual-write migration for cart-service
- Date: 2018-10-03
- Status: Superseded
- Owner: Jon Bell
- Related: ATLAS-1844, PR-18758, PD-2421

### Context
cart-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Publish dashboard, alert, runbook, and support macro before declaring release ready.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-005-2: Idempotency key design for tax-service
- Date: 2018-10-13
- Status: Accepted with Follow-up
- Owner: Kim Tan
- Related: ATLAS-2759, PR-12913, PD-2650

### Context
tax-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Publish dashboard, alert, runbook, and support macro before declaring release ready.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-005-3: Payment retry policy for cart-service
- Date: 2018-10-14
- Status: Accepted with Follow-up
- Owner: Owen Brooks
- Related: ATLAS-1192, PR-9546, PD-2035

### Context
cart-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Require database migration rehearsal and rollback SQL before production rollout.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-006-1: Outbox eventing for auth-gateway
- Date: 2018-11-10
- Status: Accepted
- Owner: Kim Tan
- Related: ATLAS-2128, PR-9941, PD-2687

### Context
auth-gateway needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Publish dashboard, alert, runbook, and support macro before declaring release ready.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-006-2: Idempotency key design for order-ledger
- Date: 2018-11-11
- Status: Accepted with Follow-up
- Owner: Noah Evans
- Related: ATLAS-5274, PR-14259, PD-2877

### Context
order-ledger needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Publish dashboard, alert, runbook, and support macro before declaring release ready.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-006-3: Outbox eventing for tax-service
- Date: 2018-11-20
- Status: Accepted
- Owner: Maya Chen
- Related: ATLAS-4640, PR-14398, PD-2499

### Context
tax-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use a progressive traffic flag and require SLO evidence before increasing exposure.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-007-1: Dual-write migration for auth-gateway
- Date: 2018-12-26
- Status: Accepted with Follow-up
- Owner: Dmitri Volkov
- Related: ATLAS-2907, PR-9730, PD-2123

### Context
auth-gateway needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Require database migration rehearsal and rollback SQL before production rollout.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-007-2: Feature flag rollout for search-recommendations
- Date: 2018-12-17
- Status: Under Review
- Owner: Anika Sharma
- Related: ATLAS-4051, PR-6017, PD-2391

### Context
search-recommendations needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Require database migration rehearsal and rollback SQL before production rollout.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-007-3: Database partitioning for payment-orchestrator
- Date: 2018-12-07
- Status: Under Review
- Owner: Grace Kim
- Related: ATLAS-3088, PR-14696, PD-2505

### Context
payment-orchestrator needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Publish dashboard, alert, runbook, and support macro before declaring release ready.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-008-1: Observability standard for checkout-api
- Date: 2019-01-17
- Status: Superseded
- Owner: Noah Evans
- Related: ATLAS-3333, PR-17358, PD-2787

### Context
checkout-api needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use checkout_id plus attempt_number as the idempotency key for payment mutations.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-008-2: Outbox eventing for auth-gateway
- Date: 2019-01-18
- Status: Accepted with Follow-up
- Owner: Sara Novak
- Related: ATLAS-3435, PR-16826, PD-2012

### Context
auth-gateway needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Require database migration rehearsal and rollback SQL before production rollout.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-008-3: Outbox eventing for payment-orchestrator
- Date: 2019-01-19
- Status: Accepted with Follow-up
- Owner: Priya Nair
- Related: ATLAS-2722, PR-13141, PD-2670

### Context
payment-orchestrator needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use checkout_id plus attempt_number as the idempotency key for payment mutations.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-009-1: Database partitioning for auth-gateway
- Date: 2019-02-02
- Status: Accepted
- Owner: Iris Wang
- Related: ATLAS-2176, PR-6927, PD-2346

### Context
auth-gateway needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Publish dashboard, alert, runbook, and support macro before declaring release ready.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-009-2: Database partitioning for loyalty-service
- Date: 2019-02-21
- Status: Accepted with Follow-up
- Owner: Theo Martin
- Related: ATLAS-3348, PR-6518, PD-2017

### Context
loyalty-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Require database migration rehearsal and rollback SQL before production rollout.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-009-3: Outbox eventing for notification-service
- Date: 2019-02-22
- Status: Under Review
- Owner: Maya Chen
- Related: ATLAS-1694, PR-12259, PD-2668

### Context
notification-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use checkout_id plus attempt_number as the idempotency key for payment mutations.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-010-1: Observability standard for search-recommendations
- Date: 2019-03-25
- Status: Superseded
- Owner: Harper Lee
- Related: ATLAS-1452, PR-18723, PD-2798

### Context
search-recommendations needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Publish dashboard, alert, runbook, and support macro before declaring release ready.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-010-2: Rollback strategy for checkout-api
- Date: 2019-03-23
- Status: Superseded
- Owner: Jon Bell
- Related: ATLAS-4943, PR-14869, PD-2733

### Context
checkout-api needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Require database migration rehearsal and rollback SQL before production rollout.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-010-3: Dual-write migration for tax-service
- Date: 2019-03-02
- Status: Accepted with Follow-up
- Owner: Maya Chen
- Related: ATLAS-5543, PR-12700, PD-2618

### Context
tax-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use checkout_id plus attempt_number as the idempotency key for payment mutations.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-011-1: Feature flag rollout for notification-service
- Date: 2019-04-04
- Status: Under Review
- Owner: Fatima Noor
- Related: ATLAS-1287, PR-13583, PD-2489

### Context
notification-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Require database migration rehearsal and rollback SQL before production rollout.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-011-2: Database partitioning for auth-gateway
- Date: 2019-04-26
- Status: Accepted with Follow-up
- Owner: Grace Kim
- Related: ATLAS-3200, PR-8020, PD-2075

### Context
auth-gateway needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Require database migration rehearsal and rollback SQL before production rollout.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-011-3: Rollback strategy for inventory-reservation
- Date: 2019-04-12
- Status: Accepted with Follow-up
- Owner: Priya Nair
- Related: ATLAS-1911, PR-7137, PD-2845

### Context
inventory-reservation needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Keep reads dual-run until reconciliation errors stay below threshold for two sprints.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-012-1: Database partitioning for order-ledger
- Date: 2019-05-16
- Status: Under Review
- Owner: Iris Wang
- Related: ATLAS-3380, PR-15614, PD-2235

### Context
order-ledger needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use checkout_id plus attempt_number as the idempotency key for payment mutations.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-012-2: Rollback strategy for auth-gateway
- Date: 2019-05-06
- Status: Accepted
- Owner: Sara Novak
- Related: ATLAS-2055, PR-13659, PD-2886

### Context
auth-gateway needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use checkout_id plus attempt_number as the idempotency key for payment mutations.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-012-3: Database partitioning for payment-orchestrator
- Date: 2019-05-03
- Status: Under Review
- Owner: Anika Sharma
- Related: ATLAS-5890, PR-13316, PD-2349

### Context
payment-orchestrator needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Publish dashboard, alert, runbook, and support macro before declaring release ready.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-013-1: Database partitioning for notification-service
- Date: 2019-06-15
- Status: Accepted with Follow-up
- Owner: Priya Nair
- Related: ATLAS-1277, PR-18423, PD-2416

### Context
notification-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Require database migration rehearsal and rollback SQL before production rollout.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-013-2: Outbox eventing for cart-service
- Date: 2019-06-20
- Status: Superseded
- Owner: Ben Carter
- Related: ATLAS-1826, PR-8103, PD-2155

### Context
cart-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Publish dashboard, alert, runbook, and support macro before declaring release ready.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-013-3: Database partitioning for auth-gateway
- Date: 2019-06-10
- Status: Superseded
- Owner: Anika Sharma
- Related: ATLAS-4540, PR-6274, PD-2346

### Context
auth-gateway needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Require database migration rehearsal and rollback SQL before production rollout.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-014-1: Database partitioning for auth-gateway
- Date: 2019-07-22
- Status: Accepted
- Owner: Anika Sharma
- Related: ATLAS-2850, PR-9108, PD-2149

### Context
auth-gateway needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Require database migration rehearsal and rollback SQL before production rollout.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-014-2: Rollback strategy for notification-service
- Date: 2019-07-24
- Status: Under Review
- Owner: Luca Moretti
- Related: ATLAS-2643, PR-9891, PD-2264

### Context
notification-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Publish dashboard, alert, runbook, and support macro before declaring release ready.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-014-3: Payment retry policy for order-ledger
- Date: 2019-07-23
- Status: Accepted with Follow-up
- Owner: Luca Moretti
- Related: ATLAS-2275, PR-5894, PD-2680

### Context
order-ledger needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use checkout_id plus attempt_number as the idempotency key for payment mutations.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-015-1: Rollback strategy for order-ledger
- Date: 2019-08-10
- Status: Accepted with Follow-up
- Owner: Elena Petrova
- Related: ATLAS-1136, PR-16502, PD-2542

### Context
order-ledger needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Publish dashboard, alert, runbook, and support macro before declaring release ready.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-015-2: Observability standard for payment-orchestrator
- Date: 2019-08-17
- Status: Superseded
- Owner: Theo Martin
- Related: ATLAS-1559, PR-16934, PD-2594

### Context
payment-orchestrator needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use checkout_id plus attempt_number as the idempotency key for payment mutations.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-015-3: Feature flag rollout for inventory-reservation
- Date: 2019-08-18
- Status: Accepted
- Owner: Elena Petrova
- Related: ATLAS-2679, PR-14727, PD-2632

### Context
inventory-reservation needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Keep reads dual-run until reconciliation errors stay below threshold for two sprints.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-016-1: Payment retry policy for payment-orchestrator
- Date: 2019-09-25
- Status: Accepted
- Owner: Owen Brooks
- Related: ATLAS-4486, PR-13753, PD-2423

### Context
payment-orchestrator needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Keep reads dual-run until reconciliation errors stay below threshold for two sprints.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-016-2: Database partitioning for checkout-api
- Date: 2019-09-25
- Status: Accepted
- Owner: Owen Brooks
- Related: ATLAS-2782, PR-16881, PD-2171

### Context
checkout-api needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Keep reads dual-run until reconciliation errors stay below threshold for two sprints.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-016-3: Rollback strategy for analytics-pipeline
- Date: 2019-09-19
- Status: Superseded
- Owner: Jon Bell
- Related: ATLAS-4821, PR-13552, PD-2426

### Context
analytics-pipeline needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use a progressive traffic flag and require SLO evidence before increasing exposure.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-017-1: Idempotency key design for inventory-reservation
- Date: 2019-10-24
- Status: Under Review
- Owner: Fatima Noor
- Related: ATLAS-5063, PR-7182, PD-2005

### Context
inventory-reservation needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Publish dashboard, alert, runbook, and support macro before declaring release ready.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-017-2: Idempotency key design for auth-gateway
- Date: 2019-10-19
- Status: Under Review
- Owner: Owen Brooks
- Related: ATLAS-3718, PR-14966, PD-2233

### Context
auth-gateway needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use checkout_id plus attempt_number as the idempotency key for payment mutations.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-017-3: Outbox eventing for checkout-api
- Date: 2019-10-03
- Status: Superseded
- Owner: Luca Moretti
- Related: ATLAS-2692, PR-10186, PD-2010

### Context
checkout-api needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Require database migration rehearsal and rollback SQL before production rollout.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-018-1: Observability standard for analytics-pipeline
- Date: 2019-11-09
- Status: Accepted
- Owner: Iris Wang
- Related: ATLAS-2534, PR-11169, PD-2126

### Context
analytics-pipeline needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use checkout_id plus attempt_number as the idempotency key for payment mutations.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-018-2: Idempotency key design for search-recommendations
- Date: 2019-11-03
- Status: Accepted
- Owner: Samir Rao
- Related: ATLAS-5174, PR-7865, PD-2607

### Context
search-recommendations needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use a progressive traffic flag and require SLO evidence before increasing exposure.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-018-3: Outbox eventing for loyalty-service
- Date: 2019-11-06
- Status: Accepted
- Owner: Samir Rao
- Related: ATLAS-4593, PR-13837, PD-2652

### Context
loyalty-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use checkout_id plus attempt_number as the idempotency key for payment mutations.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-019-1: Idempotency key design for cart-service
- Date: 2019-12-23
- Status: Accepted with Follow-up
- Owner: Harper Lee
- Related: ATLAS-5451, PR-9634, PD-2731

### Context
cart-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Publish dashboard, alert, runbook, and support macro before declaring release ready.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-019-2: Payment retry policy for notification-service
- Date: 2019-12-15
- Status: Accepted
- Owner: Sara Novak
- Related: ATLAS-2738, PR-8651, PD-2757

### Context
notification-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use checkout_id plus attempt_number as the idempotency key for payment mutations.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-019-3: Database partitioning for notification-service
- Date: 2019-12-21
- Status: Under Review
- Owner: Luca Moretti
- Related: ATLAS-1044, PR-5545, PD-2299

### Context
notification-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Publish dashboard, alert, runbook, and support macro before declaring release ready.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-020-1: Rollback strategy for payment-orchestrator
- Date: 2020-01-17
- Status: Accepted
- Owner: Owen Brooks
- Related: ATLAS-3034, PR-17220, PD-2181

### Context
payment-orchestrator needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use a progressive traffic flag and require SLO evidence before increasing exposure.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-020-2: Payment retry policy for pricing-engine
- Date: 2020-01-02
- Status: Under Review
- Owner: Elena Petrova
- Related: ATLAS-3337, PR-12239, PD-2893

### Context
pricing-engine needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use checkout_id plus attempt_number as the idempotency key for payment mutations.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-020-3: Observability standard for inventory-reservation
- Date: 2020-01-18
- Status: Under Review
- Owner: Iris Wang
- Related: ATLAS-3653, PR-7172, PD-2681

### Context
inventory-reservation needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use checkout_id plus attempt_number as the idempotency key for payment mutations.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-021-1: Rollback strategy for analytics-pipeline
- Date: 2020-02-09
- Status: Accepted
- Owner: Grace Kim
- Related: ATLAS-4762, PR-12913, PD-2135

### Context
analytics-pipeline needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use a progressive traffic flag and require SLO evidence before increasing exposure.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-021-2: Rollback strategy for notification-service
- Date: 2020-02-14
- Status: Accepted
- Owner: Yara Haddad
- Related: ATLAS-5110, PR-14395, PD-2154

### Context
notification-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use checkout_id plus attempt_number as the idempotency key for payment mutations.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-021-3: Database partitioning for cart-service
- Date: 2020-02-22
- Status: Superseded
- Owner: Ravi Patel
- Related: ATLAS-5633, PR-15955, PD-2850

### Context
cart-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use checkout_id plus attempt_number as the idempotency key for payment mutations.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-022-1: Idempotency key design for auth-gateway
- Date: 2020-03-05
- Status: Accepted with Follow-up
- Owner: Grace Kim
- Related: ATLAS-2339, PR-6084, PD-2115

### Context
auth-gateway needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use a progressive traffic flag and require SLO evidence before increasing exposure.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-022-2: Observability standard for checkout-api
- Date: 2020-03-02
- Status: Accepted with Follow-up
- Owner: Yara Haddad
- Related: ATLAS-6137, PR-11400, PD-2070

### Context
checkout-api needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use checkout_id plus attempt_number as the idempotency key for payment mutations.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-022-3: Feature flag rollout for order-ledger
- Date: 2020-03-25
- Status: Superseded
- Owner: Ravi Patel
- Related: ATLAS-1716, PR-9381, PD-2670

### Context
order-ledger needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use a progressive traffic flag and require SLO evidence before increasing exposure.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-023-1: Feature flag rollout for payment-orchestrator
- Date: 2020-04-17
- Status: Accepted
- Owner: Nora Singh
- Related: ATLAS-1482, PR-12845, PD-2042

### Context
payment-orchestrator needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Keep reads dual-run until reconciliation errors stay below threshold for two sprints.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-023-2: Dual-write migration for analytics-pipeline
- Date: 2020-04-19
- Status: Accepted
- Owner: Anika Sharma
- Related: ATLAS-2884, PR-16088, PD-2290

### Context
analytics-pipeline needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Keep reads dual-run until reconciliation errors stay below threshold for two sprints.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-023-3: Rollback strategy for pricing-engine
- Date: 2020-04-23
- Status: Superseded
- Owner: Aisha Khan
- Related: ATLAS-4950, PR-18589, PD-2477

### Context
pricing-engine needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use checkout_id plus attempt_number as the idempotency key for payment mutations.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-024-1: Rollback strategy for pricing-engine
- Date: 2020-05-09
- Status: Superseded
- Owner: Ravi Patel
- Related: ATLAS-5068, PR-17218, PD-2701

### Context
pricing-engine needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Publish dashboard, alert, runbook, and support macro before declaring release ready.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-024-2: Database partitioning for inventory-reservation
- Date: 2020-05-11
- Status: Superseded
- Owner: Samir Rao
- Related: ATLAS-1391, PR-13364, PD-2893

### Context
inventory-reservation needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Require database migration rehearsal and rollback SQL before production rollout.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-024-3: Feature flag rollout for tax-service
- Date: 2020-05-13
- Status: Under Review
- Owner: Grace Kim
- Related: ATLAS-2619, PR-18359, PD-2384

### Context
tax-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Keep reads dual-run until reconciliation errors stay below threshold for two sprints.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-025-1: Payment retry policy for payment-orchestrator
- Date: 2020-06-25
- Status: Accepted with Follow-up
- Owner: Victor Silva
- Related: ATLAS-4295, PR-5410, PD-2543

### Context
payment-orchestrator needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Publish dashboard, alert, runbook, and support macro before declaring release ready.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-025-2: Payment retry policy for loyalty-service
- Date: 2020-06-15
- Status: Accepted with Follow-up
- Owner: Ravi Patel
- Related: ATLAS-3308, PR-16427, PD-2247

### Context
loyalty-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Publish dashboard, alert, runbook, and support macro before declaring release ready.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-025-3: Dual-write migration for search-recommendations
- Date: 2020-06-05
- Status: Superseded
- Owner: Victor Silva
- Related: ATLAS-5906, PR-9033, PD-2261

### Context
search-recommendations needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Publish dashboard, alert, runbook, and support macro before declaring release ready.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-026-1: Payment retry policy for order-ledger
- Date: 2020-07-03
- Status: Under Review
- Owner: Grace Kim
- Related: ATLAS-3944, PR-7066, PD-2736

### Context
order-ledger needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Require database migration rehearsal and rollback SQL before production rollout.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-026-2: Payment retry policy for payment-orchestrator
- Date: 2020-07-22
- Status: Under Review
- Owner: Aisha Khan
- Related: ATLAS-5036, PR-18574, PD-2309

### Context
payment-orchestrator needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use a progressive traffic flag and require SLO evidence before increasing exposure.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-026-3: Observability standard for loyalty-service
- Date: 2020-07-02
- Status: Accepted
- Owner: Theo Martin
- Related: ATLAS-3281, PR-15898, PD-2458

### Context
loyalty-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Require database migration rehearsal and rollback SQL before production rollout.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-027-1: Feature flag rollout for tax-service
- Date: 2020-08-14
- Status: Accepted
- Owner: Iris Wang
- Related: ATLAS-1580, PR-11210, PD-2779

### Context
tax-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Require database migration rehearsal and rollback SQL before production rollout.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-027-2: Outbox eventing for analytics-pipeline
- Date: 2020-08-25
- Status: Accepted with Follow-up
- Owner: Kim Tan
- Related: ATLAS-5629, PR-10869, PD-2354

### Context
analytics-pipeline needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use checkout_id plus attempt_number as the idempotency key for payment mutations.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-027-3: Dual-write migration for analytics-pipeline
- Date: 2020-08-24
- Status: Accepted with Follow-up
- Owner: Noah Evans
- Related: ATLAS-4569, PR-13070, PD-2635

### Context
analytics-pipeline needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Require database migration rehearsal and rollback SQL before production rollout.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-028-1: Observability standard for search-recommendations
- Date: 2020-09-14
- Status: Under Review
- Owner: Owen Brooks
- Related: ATLAS-4998, PR-11128, PD-2548

### Context
search-recommendations needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use checkout_id plus attempt_number as the idempotency key for payment mutations.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-028-2: Feature flag rollout for auth-gateway
- Date: 2020-09-12
- Status: Superseded
- Owner: Noah Evans
- Related: ATLAS-3689, PR-5356, PD-2165

### Context
auth-gateway needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Publish dashboard, alert, runbook, and support macro before declaring release ready.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-028-3: Observability standard for checkout-api
- Date: 2020-09-20
- Status: Accepted with Follow-up
- Owner: Ravi Patel
- Related: ATLAS-4547, PR-11367, PD-2452

### Context
checkout-api needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use checkout_id plus attempt_number as the idempotency key for payment mutations.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-029-1: Outbox eventing for loyalty-service
- Date: 2020-10-09
- Status: Superseded
- Owner: Samir Rao
- Related: ATLAS-4895, PR-5880, PD-2166

### Context
loyalty-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use checkout_id plus attempt_number as the idempotency key for payment mutations.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-029-2: Outbox eventing for search-recommendations
- Date: 2020-10-21
- Status: Under Review
- Owner: Sara Novak
- Related: ATLAS-4263, PR-18219, PD-2004

### Context
search-recommendations needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use checkout_id plus attempt_number as the idempotency key for payment mutations.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-029-3: Database partitioning for loyalty-service
- Date: 2020-10-09
- Status: Under Review
- Owner: Ravi Patel
- Related: ATLAS-3667, PR-15055, PD-2842

### Context
loyalty-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Keep reads dual-run until reconciliation errors stay below threshold for two sprints.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-030-1: Outbox eventing for pricing-engine
- Date: 2020-11-14
- Status: Under Review
- Owner: Victor Silva
- Related: ATLAS-5344, PR-13614, PD-2691

### Context
pricing-engine needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Require database migration rehearsal and rollback SQL before production rollout.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-030-2: Outbox eventing for search-recommendations
- Date: 2020-11-18
- Status: Under Review
- Owner: Elena Petrova
- Related: ATLAS-2106, PR-15724, PD-2191

### Context
search-recommendations needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Keep reads dual-run until reconciliation errors stay below threshold for two sprints.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-030-3: Database partitioning for tax-service
- Date: 2020-11-08
- Status: Accepted
- Owner: Fatima Noor
- Related: ATLAS-3170, PR-11449, PD-2367

### Context
tax-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Keep reads dual-run until reconciliation errors stay below threshold for two sprints.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-031-1: Observability standard for order-ledger
- Date: 2020-12-26
- Status: Accepted
- Owner: Fatima Noor
- Related: ATLAS-2240, PR-15359, PD-2061

### Context
order-ledger needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Keep reads dual-run until reconciliation errors stay below threshold for two sprints.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-031-2: Payment retry policy for notification-service
- Date: 2020-12-22
- Status: Superseded
- Owner: Dmitri Volkov
- Related: ATLAS-3118, PR-13699, PD-2102

### Context
notification-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Publish dashboard, alert, runbook, and support macro before declaring release ready.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-031-3: Outbox eventing for cart-service
- Date: 2020-12-25
- Status: Accepted with Follow-up
- Owner: Ravi Patel
- Related: ATLAS-1831, PR-13683, PD-2416

### Context
cart-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use checkout_id plus attempt_number as the idempotency key for payment mutations.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-032-1: Rollback strategy for tax-service
- Date: 2021-01-21
- Status: Superseded
- Owner: Victor Silva
- Related: ATLAS-1422, PR-5108, PD-2235

### Context
tax-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Publish dashboard, alert, runbook, and support macro before declaring release ready.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-032-2: Observability standard for tax-service
- Date: 2021-01-10
- Status: Accepted
- Owner: Fatima Noor
- Related: ATLAS-3676, PR-6038, PD-2288

### Context
tax-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use a progressive traffic flag and require SLO evidence before increasing exposure.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-032-3: Feature flag rollout for pricing-engine
- Date: 2021-01-15
- Status: Superseded
- Owner: Dmitri Volkov
- Related: ATLAS-3322, PR-11476, PD-2500

### Context
pricing-engine needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use checkout_id plus attempt_number as the idempotency key for payment mutations.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-033-1: Rollback strategy for auth-gateway
- Date: 2021-02-19
- Status: Accepted
- Owner: Elena Petrova
- Related: ATLAS-2307, PR-6142, PD-2655

### Context
auth-gateway needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use a progressive traffic flag and require SLO evidence before increasing exposure.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-033-2: Rollback strategy for checkout-api
- Date: 2021-02-05
- Status: Accepted
- Owner: Iris Wang
- Related: ATLAS-4670, PR-5503, PD-2180

### Context
checkout-api needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Publish dashboard, alert, runbook, and support macro before declaring release ready.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-033-3: Database partitioning for analytics-pipeline
- Date: 2021-02-17
- Status: Accepted with Follow-up
- Owner: Maya Chen
- Related: ATLAS-1629, PR-5739, PD-2847

### Context
analytics-pipeline needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Require database migration rehearsal and rollback SQL before production rollout.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-034-1: Feature flag rollout for analytics-pipeline
- Date: 2021-03-04
- Status: Accepted
- Owner: Dmitri Volkov
- Related: ATLAS-4161, PR-5770, PD-2195

### Context
analytics-pipeline needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use a progressive traffic flag and require SLO evidence before increasing exposure.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-034-2: Feature flag rollout for search-recommendations
- Date: 2021-03-04
- Status: Under Review
- Owner: Mateo Garcia
- Related: ATLAS-3114, PR-13404, PD-2016

### Context
search-recommendations needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Keep reads dual-run until reconciliation errors stay below threshold for two sprints.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-034-3: Rollback strategy for search-recommendations
- Date: 2021-03-14
- Status: Superseded
- Owner: Ben Carter
- Related: ATLAS-2527, PR-17222, PD-2313

### Context
search-recommendations needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Keep reads dual-run until reconciliation errors stay below threshold for two sprints.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-035-1: Idempotency key design for payment-orchestrator
- Date: 2021-04-17
- Status: Accepted with Follow-up
- Owner: Nora Singh
- Related: ATLAS-2224, PR-12775, PD-2449

### Context
payment-orchestrator needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use a progressive traffic flag and require SLO evidence before increasing exposure.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-035-2: Feature flag rollout for auth-gateway
- Date: 2021-04-08
- Status: Superseded
- Owner: Owen Brooks
- Related: ATLAS-5171, PR-17198, PD-2026

### Context
auth-gateway needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Publish dashboard, alert, runbook, and support macro before declaring release ready.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-035-3: Feature flag rollout for checkout-api
- Date: 2021-04-13
- Status: Accepted with Follow-up
- Owner: Ravi Patel
- Related: ATLAS-1961, PR-7813, PD-2419

### Context
checkout-api needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Require database migration rehearsal and rollback SQL before production rollout.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-036-1: Dual-write migration for auth-gateway
- Date: 2021-05-26
- Status: Accepted
- Owner: Mateo Garcia
- Related: ATLAS-2200, PR-7460, PD-2077

### Context
auth-gateway needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Keep reads dual-run until reconciliation errors stay below threshold for two sprints.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-036-2: Observability standard for analytics-pipeline
- Date: 2021-05-06
- Status: Under Review
- Owner: Luca Moretti
- Related: ATLAS-4798, PR-18068, PD-2765

### Context
analytics-pipeline needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Require database migration rehearsal and rollback SQL before production rollout.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-036-3: Payment retry policy for pricing-engine
- Date: 2021-05-22
- Status: Accepted with Follow-up
- Owner: Victor Silva
- Related: ATLAS-4663, PR-15448, PD-2337

### Context
pricing-engine needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use a progressive traffic flag and require SLO evidence before increasing exposure.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-037-1: Database partitioning for cart-service
- Date: 2021-06-23
- Status: Superseded
- Owner: Fatima Noor
- Related: ATLAS-1507, PR-11890, PD-2639

### Context
cart-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use a progressive traffic flag and require SLO evidence before increasing exposure.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-037-2: Dual-write migration for checkout-api
- Date: 2021-06-09
- Status: Superseded
- Owner: Grace Kim
- Related: ATLAS-2880, PR-14501, PD-2403

### Context
checkout-api needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use a progressive traffic flag and require SLO evidence before increasing exposure.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-037-3: Database partitioning for notification-service
- Date: 2021-06-09
- Status: Accepted with Follow-up
- Owner: Priya Nair
- Related: ATLAS-1906, PR-17730, PD-2564

### Context
notification-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use checkout_id plus attempt_number as the idempotency key for payment mutations.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-038-1: Rollback strategy for cart-service
- Date: 2021-07-22
- Status: Superseded
- Owner: Fatima Noor
- Related: ATLAS-1821, PR-17606, PD-2490

### Context
cart-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use a progressive traffic flag and require SLO evidence before increasing exposure.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-038-2: Observability standard for order-ledger
- Date: 2021-07-11
- Status: Superseded
- Owner: Owen Brooks
- Related: ATLAS-4269, PR-15325, PD-2416

### Context
order-ledger needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Publish dashboard, alert, runbook, and support macro before declaring release ready.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-038-3: Feature flag rollout for search-recommendations
- Date: 2021-07-16
- Status: Superseded
- Owner: Victor Silva
- Related: ATLAS-2641, PR-16224, PD-2801

### Context
search-recommendations needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Publish dashboard, alert, runbook, and support macro before declaring release ready.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-039-1: Payment retry policy for order-ledger
- Date: 2021-08-02
- Status: Superseded
- Owner: Priya Nair
- Related: ATLAS-1614, PR-10187, PD-2674

### Context
order-ledger needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Require database migration rehearsal and rollback SQL before production rollout.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-039-2: Observability standard for payment-orchestrator
- Date: 2021-08-12
- Status: Superseded
- Owner: Ravi Patel
- Related: ATLAS-5884, PR-5773, PD-2481

### Context
payment-orchestrator needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Publish dashboard, alert, runbook, and support macro before declaring release ready.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-039-3: Rollback strategy for pricing-engine
- Date: 2021-08-12
- Status: Superseded
- Owner: Jon Bell
- Related: ATLAS-2643, PR-16127, PD-2278

### Context
pricing-engine needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Keep reads dual-run until reconciliation errors stay below threshold for two sprints.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-040-1: Rollback strategy for auth-gateway
- Date: 2021-09-16
- Status: Under Review
- Owner: Elena Petrova
- Related: ATLAS-2145, PR-11809, PD-2816

### Context
auth-gateway needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use a progressive traffic flag and require SLO evidence before increasing exposure.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-040-2: Payment retry policy for auth-gateway
- Date: 2021-09-02
- Status: Superseded
- Owner: Dmitri Volkov
- Related: ATLAS-4815, PR-6344, PD-2606

### Context
auth-gateway needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use a progressive traffic flag and require SLO evidence before increasing exposure.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-040-3: Feature flag rollout for order-ledger
- Date: 2021-09-04
- Status: Superseded
- Owner: Elena Petrova
- Related: ATLAS-4280, PR-13041, PD-2502

### Context
order-ledger needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use a progressive traffic flag and require SLO evidence before increasing exposure.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-041-1: Payment retry policy for loyalty-service
- Date: 2021-10-24
- Status: Accepted with Follow-up
- Owner: Samir Rao
- Related: ATLAS-5965, PR-11487, PD-2870

### Context
loyalty-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Keep reads dual-run until reconciliation errors stay below threshold for two sprints.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-041-2: Outbox eventing for payment-orchestrator
- Date: 2021-10-06
- Status: Under Review
- Owner: Jon Bell
- Related: ATLAS-1318, PR-5417, PD-2200

### Context
payment-orchestrator needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use a progressive traffic flag and require SLO evidence before increasing exposure.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-041-3: Observability standard for analytics-pipeline
- Date: 2021-10-03
- Status: Superseded
- Owner: Priya Nair
- Related: ATLAS-4470, PR-5165, PD-2555

### Context
analytics-pipeline needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Require database migration rehearsal and rollback SQL before production rollout.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-042-1: Observability standard for auth-gateway
- Date: 2021-11-05
- Status: Under Review
- Owner: Nora Singh
- Related: ATLAS-5043, PR-7807, PD-2773

### Context
auth-gateway needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use checkout_id plus attempt_number as the idempotency key for payment mutations.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-042-2: Idempotency key design for loyalty-service
- Date: 2021-11-25
- Status: Accepted with Follow-up
- Owner: Luca Moretti
- Related: ATLAS-5987, PR-12867, PD-2869

### Context
loyalty-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Keep reads dual-run until reconciliation errors stay below threshold for two sprints.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-042-3: Outbox eventing for notification-service
- Date: 2021-11-02
- Status: Superseded
- Owner: Kim Tan
- Related: ATLAS-1413, PR-14886, PD-2275

### Context
notification-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Publish dashboard, alert, runbook, and support macro before declaring release ready.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-043-1: Dual-write migration for notification-service
- Date: 2021-12-16
- Status: Superseded
- Owner: Aisha Khan
- Related: ATLAS-4370, PR-7384, PD-2645

### Context
notification-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use a progressive traffic flag and require SLO evidence before increasing exposure.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-043-2: Outbox eventing for checkout-api
- Date: 2021-12-24
- Status: Accepted with Follow-up
- Owner: Victor Silva
- Related: ATLAS-2333, PR-9460, PD-2154

### Context
checkout-api needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use checkout_id plus attempt_number as the idempotency key for payment mutations.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-043-3: Feature flag rollout for pricing-engine
- Date: 2021-12-26
- Status: Superseded
- Owner: Yara Haddad
- Related: ATLAS-5705, PR-9721, PD-2495

### Context
pricing-engine needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use a progressive traffic flag and require SLO evidence before increasing exposure.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-044-1: Observability standard for tax-service
- Date: 2022-01-18
- Status: Under Review
- Owner: Aisha Khan
- Related: ATLAS-3053, PR-18496, PD-2319

### Context
tax-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Publish dashboard, alert, runbook, and support macro before declaring release ready.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-044-2: Outbox eventing for cart-service
- Date: 2022-01-08
- Status: Superseded
- Owner: Ben Carter
- Related: ATLAS-5200, PR-5580, PD-2058

### Context
cart-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use checkout_id plus attempt_number as the idempotency key for payment mutations.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-044-3: Outbox eventing for order-ledger
- Date: 2022-01-18
- Status: Superseded
- Owner: Luca Moretti
- Related: ATLAS-4123, PR-7755, PD-2492

### Context
order-ledger needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Publish dashboard, alert, runbook, and support macro before declaring release ready.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-045-1: Idempotency key design for analytics-pipeline
- Date: 2022-02-26
- Status: Under Review
- Owner: Harper Lee
- Related: ATLAS-5630, PR-6857, PD-2103

### Context
analytics-pipeline needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Keep reads dual-run until reconciliation errors stay below threshold for two sprints.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-045-2: Idempotency key design for analytics-pipeline
- Date: 2022-02-04
- Status: Accepted
- Owner: Harper Lee
- Related: ATLAS-5876, PR-11342, PD-2373

### Context
analytics-pipeline needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Require database migration rehearsal and rollback SQL before production rollout.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-045-3: Feature flag rollout for order-ledger
- Date: 2022-02-02
- Status: Under Review
- Owner: Elena Petrova
- Related: ATLAS-2471, PR-18621, PD-2259

### Context
order-ledger needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use checkout_id plus attempt_number as the idempotency key for payment mutations.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-046-1: Feature flag rollout for loyalty-service
- Date: 2022-03-05
- Status: Accepted
- Owner: Dmitri Volkov
- Related: ATLAS-2709, PR-10166, PD-2762

### Context
loyalty-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Publish dashboard, alert, runbook, and support macro before declaring release ready.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-046-2: Feature flag rollout for cart-service
- Date: 2022-03-19
- Status: Accepted
- Owner: Sara Novak
- Related: ATLAS-5386, PR-18409, PD-2212

### Context
cart-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Publish dashboard, alert, runbook, and support macro before declaring release ready.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-046-3: Database partitioning for order-ledger
- Date: 2022-03-17
- Status: Accepted
- Owner: Jon Bell
- Related: ATLAS-1808, PR-18777, PD-2605

### Context
order-ledger needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Publish dashboard, alert, runbook, and support macro before declaring release ready.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-047-1: Observability standard for payment-orchestrator
- Date: 2022-04-19
- Status: Superseded
- Owner: Grace Kim
- Related: ATLAS-5586, PR-11336, PD-2393

### Context
payment-orchestrator needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Keep reads dual-run until reconciliation errors stay below threshold for two sprints.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-047-2: Outbox eventing for order-ledger
- Date: 2022-04-20
- Status: Accepted
- Owner: Luca Moretti
- Related: ATLAS-3617, PR-16644, PD-2364

### Context
order-ledger needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Require database migration rehearsal and rollback SQL before production rollout.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-047-3: Dual-write migration for auth-gateway
- Date: 2022-04-14
- Status: Accepted
- Owner: Noah Evans
- Related: ATLAS-1395, PR-7190, PD-2462

### Context
auth-gateway needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Keep reads dual-run until reconciliation errors stay below threshold for two sprints.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-048-1: Feature flag rollout for analytics-pipeline
- Date: 2022-05-12
- Status: Under Review
- Owner: Grace Kim
- Related: ATLAS-4191, PR-18784, PD-2200

### Context
analytics-pipeline needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Keep reads dual-run until reconciliation errors stay below threshold for two sprints.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-048-2: Dual-write migration for auth-gateway
- Date: 2022-05-15
- Status: Under Review
- Owner: Nora Singh
- Related: ATLAS-3206, PR-16370, PD-2499

### Context
auth-gateway needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Require database migration rehearsal and rollback SQL before production rollout.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-048-3: Rollback strategy for order-ledger
- Date: 2022-05-25
- Status: Accepted with Follow-up
- Owner: Fatima Noor
- Related: ATLAS-4262, PR-6745, PD-2531

### Context
order-ledger needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use checkout_id plus attempt_number as the idempotency key for payment mutations.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-049-1: Dual-write migration for checkout-api
- Date: 2022-06-26
- Status: Accepted
- Owner: Dmitri Volkov
- Related: ATLAS-1133, PR-12210, PD-2715

### Context
checkout-api needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Publish dashboard, alert, runbook, and support macro before declaring release ready.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-049-2: Rollback strategy for cart-service
- Date: 2022-06-19
- Status: Accepted with Follow-up
- Owner: Harper Lee
- Related: ATLAS-1474, PR-16112, PD-2566

### Context
cart-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Require database migration rehearsal and rollback SQL before production rollout.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-049-3: Payment retry policy for search-recommendations
- Date: 2022-06-04
- Status: Accepted with Follow-up
- Owner: Fatima Noor
- Related: ATLAS-2390, PR-14844, PD-2661

### Context
search-recommendations needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Require database migration rehearsal and rollback SQL before production rollout.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-050-1: Database partitioning for tax-service
- Date: 2022-07-23
- Status: Accepted with Follow-up
- Owner: Iris Wang
- Related: ATLAS-4236, PR-10517, PD-2498

### Context
tax-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use a progressive traffic flag and require SLO evidence before increasing exposure.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-050-2: Dual-write migration for analytics-pipeline
- Date: 2022-07-12
- Status: Accepted with Follow-up
- Owner: Yara Haddad
- Related: ATLAS-2228, PR-14472, PD-2784

### Context
analytics-pipeline needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Require database migration rehearsal and rollback SQL before production rollout.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-050-3: Rollback strategy for analytics-pipeline
- Date: 2022-07-12
- Status: Under Review
- Owner: Jon Bell
- Related: ATLAS-1080, PR-6820, PD-2589

### Context
analytics-pipeline needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Require database migration rehearsal and rollback SQL before production rollout.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-051-1: Outbox eventing for loyalty-service
- Date: 2022-08-23
- Status: Accepted with Follow-up
- Owner: Harper Lee
- Related: ATLAS-1163, PR-17653, PD-2158

### Context
loyalty-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use a progressive traffic flag and require SLO evidence before increasing exposure.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-051-2: Feature flag rollout for auth-gateway
- Date: 2022-08-10
- Status: Accepted
- Owner: Ben Carter
- Related: ATLAS-4084, PR-16333, PD-2731

### Context
auth-gateway needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Publish dashboard, alert, runbook, and support macro before declaring release ready.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-051-3: Observability standard for search-recommendations
- Date: 2022-08-16
- Status: Superseded
- Owner: Luca Moretti
- Related: ATLAS-5671, PR-12649, PD-2887

### Context
search-recommendations needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Require database migration rehearsal and rollback SQL before production rollout.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-052-1: Dual-write migration for cart-service
- Date: 2022-09-26
- Status: Under Review
- Owner: Maya Chen
- Related: ATLAS-4420, PR-6362, PD-2201

### Context
cart-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Keep reads dual-run until reconciliation errors stay below threshold for two sprints.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-052-2: Database partitioning for pricing-engine
- Date: 2022-09-12
- Status: Superseded
- Owner: Nora Singh
- Related: ATLAS-5223, PR-6787, PD-2544

### Context
pricing-engine needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use checkout_id plus attempt_number as the idempotency key for payment mutations.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-052-3: Payment retry policy for checkout-api
- Date: 2022-09-24
- Status: Under Review
- Owner: Aisha Khan
- Related: ATLAS-2066, PR-8735, PD-2065

### Context
checkout-api needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Require database migration rehearsal and rollback SQL before production rollout.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-053-1: Dual-write migration for analytics-pipeline
- Date: 2022-10-13
- Status: Accepted with Follow-up
- Owner: Owen Brooks
- Related: ATLAS-5679, PR-10421, PD-2547

### Context
analytics-pipeline needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Require database migration rehearsal and rollback SQL before production rollout.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-053-2: Rollback strategy for order-ledger
- Date: 2022-10-11
- Status: Under Review
- Owner: Harper Lee
- Related: ATLAS-1706, PR-12983, PD-2083

### Context
order-ledger needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Require database migration rehearsal and rollback SQL before production rollout.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-053-3: Rollback strategy for payment-orchestrator
- Date: 2022-10-10
- Status: Superseded
- Owner: Nora Singh
- Related: ATLAS-2282, PR-5573, PD-2168

### Context
payment-orchestrator needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Keep reads dual-run until reconciliation errors stay below threshold for two sprints.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-054-1: Idempotency key design for auth-gateway
- Date: 2022-11-15
- Status: Accepted with Follow-up
- Owner: Fatima Noor
- Related: ATLAS-3404, PR-5378, PD-2298

### Context
auth-gateway needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Publish dashboard, alert, runbook, and support macro before declaring release ready.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-054-2: Database partitioning for checkout-api
- Date: 2022-11-24
- Status: Superseded
- Owner: Maya Chen
- Related: ATLAS-5870, PR-15090, PD-2370

### Context
checkout-api needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use a progressive traffic flag and require SLO evidence before increasing exposure.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-054-3: Payment retry policy for search-recommendations
- Date: 2022-11-05
- Status: Under Review
- Owner: Aisha Khan
- Related: ATLAS-2394, PR-11733, PD-2880

### Context
search-recommendations needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Publish dashboard, alert, runbook, and support macro before declaring release ready.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-055-1: Dual-write migration for tax-service
- Date: 2022-12-08
- Status: Accepted with Follow-up
- Owner: Dmitri Volkov
- Related: ATLAS-1782, PR-16883, PD-2442

### Context
tax-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Keep reads dual-run until reconciliation errors stay below threshold for two sprints.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-055-2: Database partitioning for tax-service
- Date: 2022-12-21
- Status: Under Review
- Owner: Kim Tan
- Related: ATLAS-3380, PR-13625, PD-2774

### Context
tax-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Require database migration rehearsal and rollback SQL before production rollout.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-055-3: Dual-write migration for notification-service
- Date: 2022-12-26
- Status: Under Review
- Owner: Kim Tan
- Related: ATLAS-1355, PR-5296, PD-2295

### Context
notification-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Require database migration rehearsal and rollback SQL before production rollout.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-056-1: Database partitioning for auth-gateway
- Date: 2023-01-20
- Status: Under Review
- Owner: Sara Novak
- Related: ATLAS-2913, PR-17523, PD-2520

### Context
auth-gateway needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Keep reads dual-run until reconciliation errors stay below threshold for two sprints.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-056-2: Idempotency key design for inventory-reservation
- Date: 2023-01-21
- Status: Under Review
- Owner: Noah Evans
- Related: ATLAS-2543, PR-14751, PD-2572

### Context
inventory-reservation needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Require database migration rehearsal and rollback SQL before production rollout.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-056-3: Payment retry policy for order-ledger
- Date: 2023-01-23
- Status: Accepted with Follow-up
- Owner: Samir Rao
- Related: ATLAS-3186, PR-14302, PD-2259

### Context
order-ledger needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Publish dashboard, alert, runbook, and support macro before declaring release ready.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-057-1: Database partitioning for analytics-pipeline
- Date: 2023-02-20
- Status: Accepted with Follow-up
- Owner: Ravi Patel
- Related: ATLAS-2667, PR-17814, PD-2386

### Context
analytics-pipeline needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Require database migration rehearsal and rollback SQL before production rollout.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-057-2: Payment retry policy for auth-gateway
- Date: 2023-02-09
- Status: Superseded
- Owner: Harper Lee
- Related: ATLAS-4236, PR-10779, PD-2776

### Context
auth-gateway needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Publish dashboard, alert, runbook, and support macro before declaring release ready.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-057-3: Feature flag rollout for notification-service
- Date: 2023-02-09
- Status: Accepted
- Owner: Elena Petrova
- Related: ATLAS-5842, PR-18665, PD-2769

### Context
notification-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Keep reads dual-run until reconciliation errors stay below threshold for two sprints.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-058-1: Rollback strategy for order-ledger
- Date: 2023-03-09
- Status: Accepted with Follow-up
- Owner: Iris Wang
- Related: ATLAS-2598, PR-12876, PD-2036

### Context
order-ledger needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Require database migration rehearsal and rollback SQL before production rollout.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-058-2: Feature flag rollout for pricing-engine
- Date: 2023-03-08
- Status: Superseded
- Owner: Victor Silva
- Related: ATLAS-5934, PR-12744, PD-2460

### Context
pricing-engine needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use checkout_id plus attempt_number as the idempotency key for payment mutations.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-058-3: Database partitioning for tax-service
- Date: 2023-03-06
- Status: Accepted with Follow-up
- Owner: Nora Singh
- Related: ATLAS-5110, PR-16147, PD-2274

### Context
tax-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use a progressive traffic flag and require SLO evidence before increasing exposure.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-059-1: Dual-write migration for inventory-reservation
- Date: 2023-04-09
- Status: Under Review
- Owner: Luca Moretti
- Related: ATLAS-4425, PR-5425, PD-2654

### Context
inventory-reservation needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use checkout_id plus attempt_number as the idempotency key for payment mutations.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-059-2: Outbox eventing for payment-orchestrator
- Date: 2023-04-21
- Status: Accepted with Follow-up
- Owner: Harper Lee
- Related: ATLAS-3629, PR-9651, PD-2399

### Context
payment-orchestrator needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Keep reads dual-run until reconciliation errors stay below threshold for two sprints.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-059-3: Outbox eventing for payment-orchestrator
- Date: 2023-04-10
- Status: Accepted with Follow-up
- Owner: Ravi Patel
- Related: ATLAS-5671, PR-13588, PD-2738

### Context
payment-orchestrator needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Publish dashboard, alert, runbook, and support macro before declaring release ready.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-060-1: Payment retry policy for search-recommendations
- Date: 2023-05-06
- Status: Accepted
- Owner: Ben Carter
- Related: ATLAS-6080, PR-8533, PD-2753

### Context
search-recommendations needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Keep reads dual-run until reconciliation errors stay below threshold for two sprints.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-060-2: Observability standard for analytics-pipeline
- Date: 2023-05-08
- Status: Superseded
- Owner: Harper Lee
- Related: ATLAS-5303, PR-16886, PD-2534

### Context
analytics-pipeline needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use a progressive traffic flag and require SLO evidence before increasing exposure.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-060-3: Observability standard for pricing-engine
- Date: 2023-05-22
- Status: Under Review
- Owner: Iris Wang
- Related: ATLAS-4843, PR-16503, PD-2294

### Context
pricing-engine needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Require database migration rehearsal and rollback SQL before production rollout.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-061-1: Payment retry policy for auth-gateway
- Date: 2023-06-15
- Status: Superseded
- Owner: Dmitri Volkov
- Related: ATLAS-1793, PR-14701, PD-2696

### Context
auth-gateway needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Keep reads dual-run until reconciliation errors stay below threshold for two sprints.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-061-2: Dual-write migration for auth-gateway
- Date: 2023-06-15
- Status: Accepted
- Owner: Noah Evans
- Related: ATLAS-5159, PR-17620, PD-2739

### Context
auth-gateway needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Require database migration rehearsal and rollback SQL before production rollout.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-061-3: Database partitioning for auth-gateway
- Date: 2023-06-15
- Status: Accepted with Follow-up
- Owner: Anika Sharma
- Related: ATLAS-3501, PR-12882, PD-2241

### Context
auth-gateway needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Publish dashboard, alert, runbook, and support macro before declaring release ready.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-062-1: Feature flag rollout for analytics-pipeline
- Date: 2023-07-19
- Status: Under Review
- Owner: Dmitri Volkov
- Related: ATLAS-4970, PR-11121, PD-2892

### Context
analytics-pipeline needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Publish dashboard, alert, runbook, and support macro before declaring release ready.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-062-2: Idempotency key design for tax-service
- Date: 2023-07-02
- Status: Superseded
- Owner: Priya Nair
- Related: ATLAS-5807, PR-7324, PD-2127

### Context
tax-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Require database migration rehearsal and rollback SQL before production rollout.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-062-3: Observability standard for checkout-api
- Date: 2023-07-26
- Status: Accepted with Follow-up
- Owner: Maya Chen
- Related: ATLAS-2815, PR-15973, PD-2616

### Context
checkout-api needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Require database migration rehearsal and rollback SQL before production rollout.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-063-1: Observability standard for search-recommendations
- Date: 2023-08-17
- Status: Accepted with Follow-up
- Owner: Aisha Khan
- Related: ATLAS-5811, PR-8282, PD-2477

### Context
search-recommendations needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Require database migration rehearsal and rollback SQL before production rollout.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-063-2: Database partitioning for auth-gateway
- Date: 2023-08-06
- Status: Accepted
- Owner: Theo Martin
- Related: ATLAS-2192, PR-16668, PD-2008

### Context
auth-gateway needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use checkout_id plus attempt_number as the idempotency key for payment mutations.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-063-3: Observability standard for loyalty-service
- Date: 2023-08-21
- Status: Under Review
- Owner: Dmitri Volkov
- Related: ATLAS-1872, PR-7050, PD-2865

### Context
loyalty-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use a progressive traffic flag and require SLO evidence before increasing exposure.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-064-1: Payment retry policy for search-recommendations
- Date: 2023-09-03
- Status: Under Review
- Owner: Sara Novak
- Related: ATLAS-3445, PR-15318, PD-2186

### Context
search-recommendations needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use a progressive traffic flag and require SLO evidence before increasing exposure.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-064-2: Feature flag rollout for checkout-api
- Date: 2023-09-21
- Status: Superseded
- Owner: Jon Bell
- Related: ATLAS-3838, PR-13110, PD-2690

### Context
checkout-api needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use checkout_id plus attempt_number as the idempotency key for payment mutations.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-064-3: Database partitioning for search-recommendations
- Date: 2023-09-05
- Status: Accepted with Follow-up
- Owner: Jon Bell
- Related: ATLAS-1148, PR-15361, PD-2538

### Context
search-recommendations needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Require database migration rehearsal and rollback SQL before production rollout.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-065-1: Payment retry policy for loyalty-service
- Date: 2023-10-25
- Status: Under Review
- Owner: Anika Sharma
- Related: ATLAS-1983, PR-12002, PD-2803

### Context
loyalty-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use checkout_id plus attempt_number as the idempotency key for payment mutations.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-065-2: Rollback strategy for search-recommendations
- Date: 2023-10-17
- Status: Superseded
- Owner: Jon Bell
- Related: ATLAS-4622, PR-16472, PD-2190

### Context
search-recommendations needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use a progressive traffic flag and require SLO evidence before increasing exposure.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-065-3: Observability standard for payment-orchestrator
- Date: 2023-10-17
- Status: Accepted with Follow-up
- Owner: Dmitri Volkov
- Related: ATLAS-2719, PR-15262, PD-2632

### Context
payment-orchestrator needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use checkout_id plus attempt_number as the idempotency key for payment mutations.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-066-1: Outbox eventing for analytics-pipeline
- Date: 2023-11-25
- Status: Accepted
- Owner: Mateo Garcia
- Related: ATLAS-1500, PR-14972, PD-2788

### Context
analytics-pipeline needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Require database migration rehearsal and rollback SQL before production rollout.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-066-2: Dual-write migration for tax-service
- Date: 2023-11-17
- Status: Superseded
- Owner: Iris Wang
- Related: ATLAS-2744, PR-9165, PD-2811

### Context
tax-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Require database migration rehearsal and rollback SQL before production rollout.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-066-3: Payment retry policy for inventory-reservation
- Date: 2023-11-06
- Status: Accepted
- Owner: Mateo Garcia
- Related: ATLAS-5331, PR-14680, PD-2786

### Context
inventory-reservation needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use a progressive traffic flag and require SLO evidence before increasing exposure.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-067-1: Rollback strategy for loyalty-service
- Date: 2023-12-12
- Status: Superseded
- Owner: Jon Bell
- Related: ATLAS-2531, PR-18248, PD-2723

### Context
loyalty-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Publish dashboard, alert, runbook, and support macro before declaring release ready.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-067-2: Payment retry policy for analytics-pipeline
- Date: 2023-12-07
- Status: Accepted with Follow-up
- Owner: Jon Bell
- Related: ATLAS-2535, PR-16235, PD-2723

### Context
analytics-pipeline needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Keep reads dual-run until reconciliation errors stay below threshold for two sprints.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-067-3: Database partitioning for notification-service
- Date: 2023-12-19
- Status: Superseded
- Owner: Victor Silva
- Related: ATLAS-2784, PR-14687, PD-2182

### Context
notification-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Publish dashboard, alert, runbook, and support macro before declaring release ready.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-068-1: Observability standard for analytics-pipeline
- Date: 2024-01-15
- Status: Accepted
- Owner: Priya Nair
- Related: ATLAS-5663, PR-13214, PD-2424

### Context
analytics-pipeline needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use checkout_id plus attempt_number as the idempotency key for payment mutations.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-068-2: Rollback strategy for loyalty-service
- Date: 2024-01-02
- Status: Accepted with Follow-up
- Owner: Yara Haddad
- Related: ATLAS-4571, PR-7441, PD-2596

### Context
loyalty-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use a progressive traffic flag and require SLO evidence before increasing exposure.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-068-3: Feature flag rollout for checkout-api
- Date: 2024-01-02
- Status: Under Review
- Owner: Grace Kim
- Related: ATLAS-6079, PR-7985, PD-2454

### Context
checkout-api needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Publish dashboard, alert, runbook, and support macro before declaring release ready.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-069-1: Database partitioning for search-recommendations
- Date: 2024-02-03
- Status: Superseded
- Owner: Ravi Patel
- Related: ATLAS-4604, PR-18624, PD-2571

### Context
search-recommendations needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use checkout_id plus attempt_number as the idempotency key for payment mutations.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-069-2: Observability standard for payment-orchestrator
- Date: 2024-02-02
- Status: Superseded
- Owner: Owen Brooks
- Related: ATLAS-4721, PR-18553, PD-2246

### Context
payment-orchestrator needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use a progressive traffic flag and require SLO evidence before increasing exposure.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-069-3: Payment retry policy for tax-service
- Date: 2024-02-16
- Status: Under Review
- Owner: Maya Chen
- Related: ATLAS-6164, PR-16674, PD-2164

### Context
tax-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Publish dashboard, alert, runbook, and support macro before declaring release ready.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-070-1: Dual-write migration for payment-orchestrator
- Date: 2024-03-18
- Status: Accepted with Follow-up
- Owner: Priya Nair
- Related: ATLAS-2221, PR-18102, PD-2900

### Context
payment-orchestrator needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Keep reads dual-run until reconciliation errors stay below threshold for two sprints.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-070-2: Outbox eventing for pricing-engine
- Date: 2024-03-20
- Status: Under Review
- Owner: Priya Nair
- Related: ATLAS-1233, PR-7961, PD-2660

### Context
pricing-engine needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Require database migration rehearsal and rollback SQL before production rollout.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-070-3: Dual-write migration for checkout-api
- Date: 2024-03-20
- Status: Accepted with Follow-up
- Owner: Anika Sharma
- Related: ATLAS-3482, PR-18258, PD-2896

### Context
checkout-api needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Keep reads dual-run until reconciliation errors stay below threshold for two sprints.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-071-1: Outbox eventing for payment-orchestrator
- Date: 2024-04-09
- Status: Superseded
- Owner: Owen Brooks
- Related: ATLAS-1760, PR-6587, PD-2644

### Context
payment-orchestrator needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Require database migration rehearsal and rollback SQL before production rollout.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-071-2: Dual-write migration for checkout-api
- Date: 2024-04-03
- Status: Under Review
- Owner: Aisha Khan
- Related: ATLAS-1430, PR-5627, PD-2652

### Context
checkout-api needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use a progressive traffic flag and require SLO evidence before increasing exposure.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-071-3: Dual-write migration for loyalty-service
- Date: 2024-04-20
- Status: Accepted with Follow-up
- Owner: Priya Nair
- Related: ATLAS-5297, PR-11057, PD-2784

### Context
loyalty-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Require database migration rehearsal and rollback SQL before production rollout.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-072-1: Dual-write migration for pricing-engine
- Date: 2024-05-16
- Status: Accepted with Follow-up
- Owner: Iris Wang
- Related: ATLAS-5622, PR-11903, PD-2033

### Context
pricing-engine needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use a progressive traffic flag and require SLO evidence before increasing exposure.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-072-2: Feature flag rollout for pricing-engine
- Date: 2024-05-19
- Status: Accepted with Follow-up
- Owner: Yara Haddad
- Related: ATLAS-4179, PR-14581, PD-2204

### Context
pricing-engine needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Keep reads dual-run until reconciliation errors stay below threshold for two sprints.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-072-3: Dual-write migration for analytics-pipeline
- Date: 2024-05-09
- Status: Accepted
- Owner: Priya Nair
- Related: ATLAS-3762, PR-15751, PD-2421

### Context
analytics-pipeline needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Publish dashboard, alert, runbook, and support macro before declaring release ready.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-073-1: Database partitioning for analytics-pipeline
- Date: 2024-06-02
- Status: Superseded
- Owner: Aisha Khan
- Related: ATLAS-6153, PR-9226, PD-2647

### Context
analytics-pipeline needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Require database migration rehearsal and rollback SQL before production rollout.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-073-2: Feature flag rollout for tax-service
- Date: 2024-06-20
- Status: Under Review
- Owner: Sara Novak
- Related: ATLAS-1214, PR-10869, PD-2687

### Context
tax-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Publish dashboard, alert, runbook, and support macro before declaring release ready.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-073-3: Observability standard for auth-gateway
- Date: 2024-06-04
- Status: Under Review
- Owner: Jon Bell
- Related: ATLAS-1006, PR-6081, PD-2669

### Context
auth-gateway needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use checkout_id plus attempt_number as the idempotency key for payment mutations.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-074-1: Outbox eventing for analytics-pipeline
- Date: 2024-07-13
- Status: Accepted
- Owner: Jon Bell
- Related: ATLAS-2473, PR-7741, PD-2144

### Context
analytics-pipeline needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Keep reads dual-run until reconciliation errors stay below threshold for two sprints.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-074-2: Dual-write migration for inventory-reservation
- Date: 2024-07-25
- Status: Under Review
- Owner: Luca Moretti
- Related: ATLAS-1846, PR-17290, PD-2462

### Context
inventory-reservation needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use a progressive traffic flag and require SLO evidence before increasing exposure.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-074-3: Observability standard for pricing-engine
- Date: 2024-07-13
- Status: Accepted
- Owner: Maya Chen
- Related: ATLAS-3171, PR-9876, PD-2653

### Context
pricing-engine needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use checkout_id plus attempt_number as the idempotency key for payment mutations.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-075-1: Outbox eventing for tax-service
- Date: 2024-08-04
- Status: Under Review
- Owner: Kim Tan
- Related: ATLAS-1437, PR-6861, PD-2224

### Context
tax-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Publish dashboard, alert, runbook, and support macro before declaring release ready.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-075-2: Feature flag rollout for loyalty-service
- Date: 2024-08-09
- Status: Accepted with Follow-up
- Owner: Grace Kim
- Related: ATLAS-2798, PR-6432, PD-2226

### Context
loyalty-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use checkout_id plus attempt_number as the idempotency key for payment mutations.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-075-3: Idempotency key design for order-ledger
- Date: 2024-08-15
- Status: Under Review
- Owner: Samir Rao
- Related: ATLAS-5012, PR-15670, PD-2422

### Context
order-ledger needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use checkout_id plus attempt_number as the idempotency key for payment mutations.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-076-1: Observability standard for order-ledger
- Date: 2024-09-18
- Status: Accepted
- Owner: Elena Petrova
- Related: ATLAS-3219, PR-6423, PD-2003

### Context
order-ledger needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Keep reads dual-run until reconciliation errors stay below threshold for two sprints.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-076-2: Rollback strategy for inventory-reservation
- Date: 2024-09-19
- Status: Accepted with Follow-up
- Owner: Theo Martin
- Related: ATLAS-5003, PR-17570, PD-2165

### Context
inventory-reservation needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Keep reads dual-run until reconciliation errors stay below threshold for two sprints.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-076-3: Rollback strategy for cart-service
- Date: 2024-09-02
- Status: Accepted
- Owner: Dmitri Volkov
- Related: ATLAS-4973, PR-14369, PD-2118

### Context
cart-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Publish dashboard, alert, runbook, and support macro before declaring release ready.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-077-1: Payment retry policy for notification-service
- Date: 2024-10-06
- Status: Accepted with Follow-up
- Owner: Nora Singh
- Related: ATLAS-3630, PR-10615, PD-2655

### Context
notification-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Keep reads dual-run until reconciliation errors stay below threshold for two sprints.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-077-2: Rollback strategy for pricing-engine
- Date: 2024-10-06
- Status: Superseded
- Owner: Theo Martin
- Related: ATLAS-3686, PR-17643, PD-2814

### Context
pricing-engine needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Keep reads dual-run until reconciliation errors stay below threshold for two sprints.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-077-3: Rollback strategy for loyalty-service
- Date: 2024-10-26
- Status: Accepted with Follow-up
- Owner: Elena Petrova
- Related: ATLAS-3387, PR-15184, PD-2358

### Context
loyalty-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Keep reads dual-run until reconciliation errors stay below threshold for two sprints.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-078-1: Observability standard for inventory-reservation
- Date: 2024-11-06
- Status: Accepted with Follow-up
- Owner: Samir Rao
- Related: ATLAS-5680, PR-18458, PD-2439

### Context
inventory-reservation needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Keep reads dual-run until reconciliation errors stay below threshold for two sprints.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-078-2: Feature flag rollout for search-recommendations
- Date: 2024-11-20
- Status: Under Review
- Owner: Priya Nair
- Related: ATLAS-5184, PR-11258, PD-2109

### Context
search-recommendations needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Require database migration rehearsal and rollback SQL before production rollout.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-078-3: Feature flag rollout for auth-gateway
- Date: 2024-11-09
- Status: Superseded
- Owner: Elena Petrova
- Related: ATLAS-5111, PR-7130, PD-2820

### Context
auth-gateway needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Publish dashboard, alert, runbook, and support macro before declaring release ready.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-079-1: Database partitioning for tax-service
- Date: 2024-12-14
- Status: Accepted
- Owner: Nora Singh
- Related: ATLAS-2915, PR-9025, PD-2050

### Context
tax-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use a progressive traffic flag and require SLO evidence before increasing exposure.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-079-2: Observability standard for order-ledger
- Date: 2024-12-05
- Status: Accepted
- Owner: Luca Moretti
- Related: ATLAS-1396, PR-5538, PD-2228

### Context
order-ledger needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Require database migration rehearsal and rollback SQL before production rollout.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-079-3: Outbox eventing for payment-orchestrator
- Date: 2024-12-08
- Status: Accepted
- Owner: Elena Petrova
- Related: ATLAS-4064, PR-15243, PD-2205

### Context
payment-orchestrator needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Keep reads dual-run until reconciliation errors stay below threshold for two sprints.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-080-1: Outbox eventing for pricing-engine
- Date: 2025-01-19
- Status: Accepted with Follow-up
- Owner: Ben Carter
- Related: ATLAS-3731, PR-18646, PD-2704

### Context
pricing-engine needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use a progressive traffic flag and require SLO evidence before increasing exposure.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-080-2: Idempotency key design for pricing-engine
- Date: 2025-01-07
- Status: Accepted
- Owner: Priya Nair
- Related: ATLAS-3835, PR-13729, PD-2679

### Context
pricing-engine needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Keep reads dual-run until reconciliation errors stay below threshold for two sprints.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-080-3: Observability standard for payment-orchestrator
- Date: 2025-01-22
- Status: Superseded
- Owner: Sara Novak
- Related: ATLAS-5990, PR-5092, PD-2141

### Context
payment-orchestrator needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Keep reads dual-run until reconciliation errors stay below threshold for two sprints.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-081-1: Payment retry policy for payment-orchestrator
- Date: 2025-02-06
- Status: Accepted
- Owner: Iris Wang
- Related: ATLAS-3773, PR-16455, PD-2688

### Context
payment-orchestrator needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use a progressive traffic flag and require SLO evidence before increasing exposure.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-081-2: Dual-write migration for tax-service
- Date: 2025-02-10
- Status: Superseded
- Owner: Fatima Noor
- Related: ATLAS-3867, PR-11517, PD-2567

### Context
tax-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Publish dashboard, alert, runbook, and support macro before declaring release ready.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-081-3: Observability standard for loyalty-service
- Date: 2025-02-22
- Status: Under Review
- Owner: Ben Carter
- Related: ATLAS-1837, PR-13581, PD-2701

### Context
loyalty-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use a progressive traffic flag and require SLO evidence before increasing exposure.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-082-1: Dual-write migration for order-ledger
- Date: 2025-03-18
- Status: Accepted with Follow-up
- Owner: Dmitri Volkov
- Related: ATLAS-5993, PR-6379, PD-2099

### Context
order-ledger needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use a progressive traffic flag and require SLO evidence before increasing exposure.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-082-2: Observability standard for analytics-pipeline
- Date: 2025-03-02
- Status: Under Review
- Owner: Dmitri Volkov
- Related: ATLAS-4911, PR-9837, PD-2151

### Context
analytics-pipeline needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Keep reads dual-run until reconciliation errors stay below threshold for two sprints.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-082-3: Idempotency key design for notification-service
- Date: 2025-03-22
- Status: Superseded
- Owner: Fatima Noor
- Related: ATLAS-4100, PR-6730, PD-2079

### Context
notification-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Require database migration rehearsal and rollback SQL before production rollout.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-083-1: Observability standard for inventory-reservation
- Date: 2025-04-24
- Status: Superseded
- Owner: Owen Brooks
- Related: ATLAS-1712, PR-11203, PD-2528

### Context
inventory-reservation needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Keep reads dual-run until reconciliation errors stay below threshold for two sprints.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-083-2: Observability standard for order-ledger
- Date: 2025-04-07
- Status: Superseded
- Owner: Harper Lee
- Related: ATLAS-1564, PR-17012, PD-2562

### Context
order-ledger needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Keep reads dual-run until reconciliation errors stay below threshold for two sprints.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-083-3: Outbox eventing for notification-service
- Date: 2025-04-26
- Status: Accepted with Follow-up
- Owner: Jon Bell
- Related: ATLAS-5282, PR-16328, PD-2126

### Context
notification-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use checkout_id plus attempt_number as the idempotency key for payment mutations.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-084-1: Dual-write migration for search-recommendations
- Date: 2025-05-13
- Status: Superseded
- Owner: Luca Moretti
- Related: ATLAS-2364, PR-10135, PD-2839

### Context
search-recommendations needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use checkout_id plus attempt_number as the idempotency key for payment mutations.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-084-2: Dual-write migration for notification-service
- Date: 2025-05-26
- Status: Accepted with Follow-up
- Owner: Theo Martin
- Related: ATLAS-1036, PR-13785, PD-2630

### Context
notification-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Publish dashboard, alert, runbook, and support macro before declaring release ready.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-084-3: Feature flag rollout for search-recommendations
- Date: 2025-05-17
- Status: Under Review
- Owner: Anika Sharma
- Related: ATLAS-5386, PR-14524, PD-2639

### Context
search-recommendations needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Require database migration rehearsal and rollback SQL before production rollout.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-085-1: Payment retry policy for pricing-engine
- Date: 2025-06-23
- Status: Under Review
- Owner: Noah Evans
- Related: ATLAS-2940, PR-10540, PD-2299

### Context
pricing-engine needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Keep reads dual-run until reconciliation errors stay below threshold for two sprints.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-085-2: Payment retry policy for payment-orchestrator
- Date: 2025-06-23
- Status: Under Review
- Owner: Priya Nair
- Related: ATLAS-2512, PR-16157, PD-2777

### Context
payment-orchestrator needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Keep reads dual-run until reconciliation errors stay below threshold for two sprints.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-085-3: Payment retry policy for loyalty-service
- Date: 2025-06-12
- Status: Accepted
- Owner: Ravi Patel
- Related: ATLAS-3174, PR-5667, PD-2441

### Context
loyalty-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Keep reads dual-run until reconciliation errors stay below threshold for two sprints.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-086-1: Feature flag rollout for cart-service
- Date: 2025-07-24
- Status: Under Review
- Owner: Theo Martin
- Related: ATLAS-4504, PR-14440, PD-2755

### Context
cart-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use checkout_id plus attempt_number as the idempotency key for payment mutations.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-086-2: Idempotency key design for pricing-engine
- Date: 2025-07-19
- Status: Accepted with Follow-up
- Owner: Harper Lee
- Related: ATLAS-4540, PR-13715, PD-2044

### Context
pricing-engine needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use a progressive traffic flag and require SLO evidence before increasing exposure.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-086-3: Outbox eventing for order-ledger
- Date: 2025-07-08
- Status: Accepted with Follow-up
- Owner: Dmitri Volkov
- Related: ATLAS-4918, PR-18973, PD-2430

### Context
order-ledger needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Keep reads dual-run until reconciliation errors stay below threshold for two sprints.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-087-1: Payment retry policy for checkout-api
- Date: 2025-08-07
- Status: Superseded
- Owner: Aisha Khan
- Related: ATLAS-5181, PR-13667, PD-2618

### Context
checkout-api needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use checkout_id plus attempt_number as the idempotency key for payment mutations.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-087-2: Database partitioning for analytics-pipeline
- Date: 2025-08-03
- Status: Superseded
- Owner: Harper Lee
- Related: ATLAS-5616, PR-13820, PD-2576

### Context
analytics-pipeline needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Keep reads dual-run until reconciliation errors stay below threshold for two sprints.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-087-3: Feature flag rollout for inventory-reservation
- Date: 2025-08-06
- Status: Accepted
- Owner: Noah Evans
- Related: ATLAS-2796, PR-5424, PD-2847

### Context
inventory-reservation needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use a progressive traffic flag and require SLO evidence before increasing exposure.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-088-1: Rollback strategy for tax-service
- Date: 2025-09-16
- Status: Superseded
- Owner: Mateo Garcia
- Related: ATLAS-3850, PR-9965, PD-2109

### Context
tax-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Require database migration rehearsal and rollback SQL before production rollout.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-088-2: Idempotency key design for checkout-api
- Date: 2025-09-09
- Status: Superseded
- Owner: Victor Silva
- Related: ATLAS-5637, PR-14337, PD-2720

### Context
checkout-api needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use checkout_id plus attempt_number as the idempotency key for payment mutations.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-088-3: Dual-write migration for notification-service
- Date: 2025-09-16
- Status: Accepted
- Owner: Sara Novak
- Related: ATLAS-3985, PR-17918, PD-2509

### Context
notification-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Publish dashboard, alert, runbook, and support macro before declaring release ready.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-089-1: Observability standard for tax-service
- Date: 2025-10-21
- Status: Under Review
- Owner: Noah Evans
- Related: ATLAS-1988, PR-12008, PD-2460

### Context
tax-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Publish dashboard, alert, runbook, and support macro before declaring release ready.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-089-2: Rollback strategy for search-recommendations
- Date: 2025-10-22
- Status: Under Review
- Owner: Sara Novak
- Related: ATLAS-1023, PR-13435, PD-2095

### Context
search-recommendations needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Keep reads dual-run until reconciliation errors stay below threshold for two sprints.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-089-3: Idempotency key design for cart-service
- Date: 2025-10-13
- Status: Accepted with Follow-up
- Owner: Jon Bell
- Related: ATLAS-3455, PR-16062, PD-2445

### Context
cart-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Keep reads dual-run until reconciliation errors stay below threshold for two sprints.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-090-1: Rollback strategy for analytics-pipeline
- Date: 2025-11-19
- Status: Superseded
- Owner: Ravi Patel
- Related: ATLAS-4459, PR-16628, PD-2733

### Context
analytics-pipeline needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Publish dashboard, alert, runbook, and support macro before declaring release ready.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-090-2: Rollback strategy for cart-service
- Date: 2025-11-13
- Status: Accepted with Follow-up
- Owner: Mateo Garcia
- Related: ATLAS-4167, PR-11590, PD-2485

### Context
cart-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Keep reads dual-run until reconciliation errors stay below threshold for two sprints.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-090-3: Database partitioning for notification-service
- Date: 2025-11-21
- Status: Accepted
- Owner: Yara Haddad
- Related: ATLAS-5395, PR-14782, PD-2806

### Context
notification-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use a progressive traffic flag and require SLO evidence before increasing exposure.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-091-1: Rollback strategy for pricing-engine
- Date: 2025-12-17
- Status: Under Review
- Owner: Theo Martin
- Related: ATLAS-2171, PR-18057, PD-2536

### Context
pricing-engine needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Require database migration rehearsal and rollback SQL before production rollout.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-091-2: Idempotency key design for analytics-pipeline
- Date: 2025-12-10
- Status: Accepted with Follow-up
- Owner: Fatima Noor
- Related: ATLAS-5042, PR-7526, PD-2229

### Context
analytics-pipeline needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use checkout_id plus attempt_number as the idempotency key for payment mutations.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-091-3: Payment retry policy for notification-service
- Date: 2025-12-06
- Status: Superseded
- Owner: Yara Haddad
- Related: ATLAS-2281, PR-15619, PD-2101

### Context
notification-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use a progressive traffic flag and require SLO evidence before increasing exposure.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-092-1: Database partitioning for cart-service
- Date: 2026-01-10
- Status: Under Review
- Owner: Iris Wang
- Related: ATLAS-3833, PR-13809, PD-2712

### Context
cart-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use checkout_id plus attempt_number as the idempotency key for payment mutations.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-092-2: Database partitioning for cart-service
- Date: 2026-01-11
- Status: Superseded
- Owner: Yara Haddad
- Related: ATLAS-1924, PR-15524, PD-2847

### Context
cart-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Require database migration rehearsal and rollback SQL before production rollout.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-092-3: Rollback strategy for inventory-reservation
- Date: 2026-01-26
- Status: Accepted
- Owner: Grace Kim
- Related: ATLAS-5037, PR-9452, PD-2578

### Context
inventory-reservation needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Keep reads dual-run until reconciliation errors stay below threshold for two sprints.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-093-1: Observability standard for auth-gateway
- Date: 2026-02-17
- Status: Accepted with Follow-up
- Owner: Kim Tan
- Related: ATLAS-4912, PR-16484, PD-2755

### Context
auth-gateway needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Keep reads dual-run until reconciliation errors stay below threshold for two sprints.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-093-2: Outbox eventing for tax-service
- Date: 2026-02-23
- Status: Under Review
- Owner: Aisha Khan
- Related: ATLAS-2563, PR-15262, PD-2169

### Context
tax-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Keep reads dual-run until reconciliation errors stay below threshold for two sprints.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-093-3: Payment retry policy for cart-service
- Date: 2026-02-26
- Status: Accepted with Follow-up
- Owner: Iris Wang
- Related: ATLAS-3591, PR-18735, PD-2087

### Context
cart-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Publish dashboard, alert, runbook, and support macro before declaring release ready.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-094-1: Rollback strategy for payment-orchestrator
- Date: 2026-03-03
- Status: Accepted with Follow-up
- Owner: Noah Evans
- Related: ATLAS-3499, PR-11796, PD-2309

### Context
payment-orchestrator needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Keep reads dual-run until reconciliation errors stay below threshold for two sprints.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-094-2: Feature flag rollout for tax-service
- Date: 2026-03-22
- Status: Accepted with Follow-up
- Owner: Yara Haddad
- Related: ATLAS-3514, PR-11424, PD-2308

### Context
tax-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Publish dashboard, alert, runbook, and support macro before declaring release ready.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-094-3: Dual-write migration for loyalty-service
- Date: 2026-03-15
- Status: Under Review
- Owner: Jon Bell
- Related: ATLAS-4821, PR-17997, PD-2809

### Context
loyalty-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use checkout_id plus attempt_number as the idempotency key for payment mutations.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-095-1: Feature flag rollout for loyalty-service
- Date: 2026-04-10
- Status: Accepted with Follow-up
- Owner: Ravi Patel
- Related: ATLAS-1897, PR-14982, PD-2800

### Context
loyalty-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use a progressive traffic flag and require SLO evidence before increasing exposure.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-095-2: Rollback strategy for inventory-reservation
- Date: 2026-04-10
- Status: Under Review
- Owner: Kim Tan
- Related: ATLAS-1837, PR-6341, PD-2318

### Context
inventory-reservation needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use a progressive traffic flag and require SLO evidence before increasing exposure.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-095-3: Outbox eventing for notification-service
- Date: 2026-04-19
- Status: Accepted
- Owner: Aisha Khan
- Related: ATLAS-2490, PR-18461, PD-2674

### Context
notification-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use a progressive traffic flag and require SLO evidence before increasing exposure.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-096-1: Dual-write migration for loyalty-service
- Date: 2026-05-25
- Status: Under Review
- Owner: Anika Sharma
- Related: ATLAS-3986, PR-18661, PD-2464

### Context
loyalty-service needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Use a progressive traffic flag and require SLO evidence before increasing exposure.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-096-2: Outbox eventing for search-recommendations
- Date: 2026-05-21
- Status: Under Review
- Owner: Priya Nair
- Related: ATLAS-5226, PR-12698, PD-2490

### Context
search-recommendations needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Keep reads dual-run until reconciliation errors stay below threshold for two sprints.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.

## ADR-096-3: Idempotency key design for analytics-pipeline
- Date: 2026-05-09
- Status: Superseded
- Owner: Maya Chen
- Related: ATLAS-2963, PR-13795, PD-2349

### Context
analytics-pipeline needed a durable decision record because the Atlas migration changed traffic routing, rollback behavior, operational ownership, and customer support paths.

### Decision
Publish dashboard, alert, runbook, and support macro before declaring release ready.

### Consequences
- Positive: clearer KT and audit trail.
- Risk: missing owner or stale runbook can slow incident response.
- Follow-up: update Jira, Teams, Confluence, and release checklist evidence.
