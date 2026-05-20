# Email Conversations - Project Atlas

All email content is synthetic and intended for upload testing.

## Thread 1 - Architecture Approval

Date: 2025-05-12
From: Maya Chen <maya.chen@example.test>
To: Ravi Patel, Nora Singh, Samir Rao, Luca Moretti
Subject: Project Atlas architecture decision for checkout modernization

Team,

Please review the proposed architecture for ATLAS-100. The checkout route will move from the legacy monolith to atlas-api. atlas-web will own UI routing and atlas-worker will process replay comparisons. Chroma or RAG is not part of this project data; Base is only used later for KT.

Decision requested:
- Keep monolith fallback until 30 days after 100 percent cutover.
- Use feature flags for 1, 5, 25, 50, 75, and 100 percent traffic routing.
- Store checkout events in checkout_order and publish sanitized audit events.

Known risk:
- Database storage and index bloat may become a blocker unless ATLAS-106 adds health checks.

Maya

Date: 2025-05-13
From: Samir Rao <samir.rao@example.test>
To: Maya Chen, Ravi Patel
Subject: Re: Project Atlas architecture decision for checkout modernization

I approve with one condition. Database health checks must start before shadow traffic. We need storage, slow queries, replication lag, connection pool usage, and cache hit rate in the weekly report.

Action item: Samir owns ATLAS-106.

## Thread 2 - Coupon Timeout Incident Follow Up

Date: 2025-06-05
From: Elena Brooks <elena.brooks@example.test>
To: Project Atlas Core
Subject: Customer support summary for PD-1001 and ATLAS-104

PD-1001 created 18 customer support cases. Customers saw missing cart totals when coupon service timed out. ATLAS-104 is now resolved and PR-109 is deployed.

Support concern:
- The error message said "unexpected issue" and did not tell customers checkout was retry safe.

Decision:
- All checkout failures must include retry-safe guidance unless payment was captured.

## Thread 3 - Shadow Traffic Readiness

Date: 2025-08-08
From: Nora Singh <nora.singh@example.test>
To: Maya Chen, Ravi Patel
Subject: Grafana readiness for ATLAS-114 5 percent shadow traffic

Grafana dashboard is healthy for the 5 percent shadow traffic release.

Metrics:
- traffic average 36 requests per second
- p95 latency 312ms
- p99 latency 612ms
- error rate 0.18 percent
- uptime 99.98 percent
- CPU 42 percent
- memory 58 percent

Risk:
- ATLAS-115 tax rounding variance is still open and should block ATLAS-116 until fixed.

## Thread 4 - 50 Percent Latency Incident

Date: 2025-10-17
From: Ravi Patel <ravi.patel@example.test>
To: Leadership Team
Subject: Incident update PD-1002 - checkout latency at 50 percent routing

Summary:
On 2025-10-15, Project Atlas experienced elevated checkout latency during the 50 percent routing test. p95 latency exceeded 700ms and p99 latency reached 1420ms. Error rate peaked at 1.2 percent. PagerDuty incident PD-1002 was opened and resolved after routing was reduced to 25 percent.

Root cause:
- Redis cache was cold after deploy.
- A checkout price query used a non-covering index.

Actions:
- ATLAS-121 tracks the incident fix.
- ATLAS-122 adds cache warmup before route increases.
- Samir will review slow queries every Monday.

Decision:
No route increase until p95 latency is below 450ms for seven consecutive days.

## Thread 5 - PCI Review Approval

Date: 2025-11-21
From: Priya Nair <security@example.test>
To: Luca Moretti, Maya Chen
Subject: PCI review approval for ATLAS-123 payment facade

Security approves ATLAS-123 for release v2025.11.0.

Conditions:
- Atlas services must not store card data.
- Payment tokens expire after 15 minutes.
- Audit events must include checkout_id, attempt_number, and decision code, but no sensitive card data.

Decision:
Approved for 50 percent checkout routing after support readiness confirmation.

## Thread 6 - Holiday Database Saturation

Date: 2025-12-13
From: Samir Rao <samir.rao@example.test>
To: Project Atlas Core
Subject: PD-1003 database health and read replica action

PD-1003 was caused by database connection pool saturation during promotion traffic. Connections reached 92 percent and slow queries increased to 186 in one hour.

Blocker:
Reporting queries are competing with checkout writes. ATLAS-127 must move reporting to the read replica before ATLAS-128 can enable 75 percent routing.

Action items:
- Samir owns read replica setup.
- Nora owns Grafana alert threshold update.
- Ravi owns release decision.

## Thread 7 - 100 Percent Cutover Approval

Date: 2026-02-27
From: Maya Chen <maya.chen@example.test>
To: Project Atlas Core, Support Leads, Leadership Team
Subject: Launch readiness approval for ATLAS-132

Launch readiness checklist ATLAS-131 is complete.

Status:
- ATLAS-130 circuit breaker passed load test.
- PagerDuty escalation policy is active.
- Grafana dashboards are green.
- Database storage is 76 percent, below the 80 percent warning threshold.
- Monolith fallback is warm and rollback runbook is current.

Decision:
Approved to enable 100 percent checkout routing on 2026-03-03.

## Thread 8 - Handoff and Finance Reconciliation

Date: 2026-04-25
From: Luca Moretti <luca.moretti@example.test>
To: Maya Chen, Ravi Patel, Finance Ops
Subject: ATLAS-136 refund dashboard and monolith archive blocker

ATLAS-136 is still open. The refunds dashboard misses retry reversals for 0.4 percent of April refunds. Finance needs reconciliation before ATLAS-134 archives the monolith checkout write path.

Decision needed:
Do not archive the monolith write path until Finance signs off.

Risk:
Database storage will reach 82 percent in May if archive is delayed. ATLAS-137 tracks the risk and handoff action item.
