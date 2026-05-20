# Confluence Knowledge Base Export - Project Atlas 2018-2026

Synthetic architecture, ADRs, runbooks, onboarding pages, postmortems, and handoff notes.

## CONF-0001: Onboarding - cart-service - 2018-06
- Owner: Luca Moretti
- Updated: 2018-06-24
- Phase: Phase 0 Legacy Stabilization
- Related Jira: ATLAS-2240

### Summary
This page explains how cart-service supports Project Atlas during Phase 0 Legacy Stabilization. The phase goal is to stabilize legacy checkout, map risks, build team rituals. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-4119 and PR-9737.
- Decision: use feature flags for rollout. Evidence links to ATLAS-5652 and PR-9442.
- Decision: dual-write only during migration window. Evidence links to ATLAS-3528 and PR-9847.

### Risks and Runbook Notes
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0002: Data Contract - notification-service - 2018-06
- Owner: Elena Petrova
- Updated: 2018-06-24
- Phase: Phase 0 Legacy Stabilization
- Related Jira: ATLAS-3724

### Summary
This page explains how notification-service supports Project Atlas during Phase 0 Legacy Stabilization. The phase goal is to stabilize legacy checkout, map risks, build team rituals. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-5648 and PR-7221.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-3016 and PR-5080.
- Decision: use feature flags for rollout. Evidence links to ATLAS-2840 and PR-9743.

### Risks and Runbook Notes
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0003: Support Playbook - tax-service - 2018-07
- Owner: Dmitri Volkov
- Updated: 2018-07-10
- Phase: Phase 0 Legacy Stabilization
- Related Jira: ATLAS-2720

### Summary
This page explains how tax-service supports Project Atlas during Phase 0 Legacy Stabilization. The phase goal is to stabilize legacy checkout, map risks, build team rituals. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: dual-write only during migration window. Evidence links to ATLAS-5266 and PR-9336.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-3750 and PR-9073.
- Decision: use feature flags for rollout. Evidence links to ATLAS-3750 and PR-10622.

### Risks and Runbook Notes
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0004: Support Playbook - cart-service - 2018-07
- Owner: Nora Singh
- Updated: 2018-07-06
- Phase: Phase 0 Legacy Stabilization
- Related Jira: ATLAS-1475

### Summary
This page explains how cart-service supports Project Atlas during Phase 0 Legacy Stabilization. The phase goal is to stabilize legacy checkout, map risks, build team rituals. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-4977 and PR-10145.
- Decision: use feature flags for rollout. Evidence links to ATLAS-5320 and PR-5495.
- Decision: support macro must be updated before launch. Evidence links to ATLAS-2046 and PR-9985.

### Risks and Runbook Notes
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0005: Release Checklist - order-ledger - 2018-08
- Owner: Theo Martin
- Updated: 2018-08-24
- Phase: Phase 0 Legacy Stabilization
- Related Jira: ATLAS-1579

### Summary
This page explains how order-ledger supports Project Atlas during Phase 0 Legacy Stabilization. The phase goal is to stabilize legacy checkout, map risks, build team rituals. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: dual-write only during migration window. Evidence links to ATLAS-3884 and PR-11036.
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-3917 and PR-7267.
- Decision: use feature flags for rollout. Evidence links to ATLAS-3777 and PR-8930.

### Risks and Runbook Notes
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0006: Data Contract - tax-service - 2018-08
- Owner: Theo Martin
- Updated: 2018-08-26
- Phase: Phase 0 Legacy Stabilization
- Related Jira: ATLAS-5481

### Summary
This page explains how tax-service supports Project Atlas during Phase 0 Legacy Stabilization. The phase goal is to stabilize legacy checkout, map risks, build team rituals. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: use feature flags for rollout. Evidence links to ATLAS-2147 and PR-12532.
- Decision: dual-write only during migration window. Evidence links to ATLAS-6142 and PR-10323.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-5592 and PR-10640.

### Risks and Runbook Notes
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0007: ADR - payment-orchestrator - 2018-09
- Owner: Sara Novak
- Updated: 2018-09-26
- Phase: Phase 0 Legacy Stabilization
- Related Jira: ATLAS-3526

### Summary
This page explains how payment-orchestrator supports Project Atlas during Phase 0 Legacy Stabilization. The phase goal is to stabilize legacy checkout, map risks, build team rituals. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-5575 and PR-10857.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-2253 and PR-9704.
- Decision: use feature flags for rollout. Evidence links to ATLAS-2541 and PR-9499.

### Risks and Runbook Notes
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0008: Support Playbook - tax-service - 2018-09
- Owner: Harper Lee
- Updated: 2018-09-03
- Phase: Phase 0 Legacy Stabilization
- Related Jira: ATLAS-3817

### Summary
This page explains how tax-service supports Project Atlas during Phase 0 Legacy Stabilization. The phase goal is to stabilize legacy checkout, map risks, build team rituals. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-5758 and PR-8101.
- Decision: dual-write only during migration window. Evidence links to ATLAS-5236 and PR-7410.
- Decision: support macro must be updated before launch. Evidence links to ATLAS-4036 and PR-10108.

### Risks and Runbook Notes
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0009: Data Contract - order-ledger - 2018-10
- Owner: Anika Sharma
- Updated: 2018-10-26
- Phase: Phase 0 Legacy Stabilization
- Related Jira: ATLAS-5975

### Summary
This page explains how order-ledger supports Project Atlas during Phase 0 Legacy Stabilization. The phase goal is to stabilize legacy checkout, map risks, build team rituals. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-3944 and PR-6931.
- Decision: dual-write only during migration window. Evidence links to ATLAS-3606 and PR-6358.
- Decision: dual-write only during migration window. Evidence links to ATLAS-1378 and PR-5316.

### Risks and Runbook Notes
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0010: ADR - payment-orchestrator - 2018-10
- Owner: Grace Kim
- Updated: 2018-10-06
- Phase: Phase 0 Legacy Stabilization
- Related Jira: ATLAS-6138

### Summary
This page explains how payment-orchestrator supports Project Atlas during Phase 0 Legacy Stabilization. The phase goal is to stabilize legacy checkout, map risks, build team rituals. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-1564 and PR-7960.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-1536 and PR-5356.
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-1375 and PR-8363.

### Risks and Runbook Notes
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0011: Data Contract - payment-orchestrator - 2018-11
- Owner: Maya Chen
- Updated: 2018-11-12
- Phase: Phase 0 Legacy Stabilization
- Related Jira: ATLAS-3373

### Summary
This page explains how payment-orchestrator supports Project Atlas during Phase 0 Legacy Stabilization. The phase goal is to stabilize legacy checkout, map risks, build team rituals. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: support macro must be updated before launch. Evidence links to ATLAS-1431 and PR-6167.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-2046 and PR-8327.
- Decision: use feature flags for rollout. Evidence links to ATLAS-1655 and PR-11825.

### Risks and Runbook Notes
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0012: ADR - search-recommendations - 2018-11
- Owner: Fatima Noor
- Updated: 2018-11-05
- Phase: Phase 0 Legacy Stabilization
- Related Jira: ATLAS-1714

### Summary
This page explains how search-recommendations supports Project Atlas during Phase 0 Legacy Stabilization. The phase goal is to stabilize legacy checkout, map risks, build team rituals. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: dual-write only during migration window. Evidence links to ATLAS-4281 and PR-11809.
- Decision: dual-write only during migration window. Evidence links to ATLAS-1827 and PR-7741.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-1874 and PR-10074.

### Risks and Runbook Notes
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0013: Postmortem - checkout-api - 2018-12
- Owner: Owen Brooks
- Updated: 2018-12-24
- Phase: Phase 0 Legacy Stabilization
- Related Jira: ATLAS-1840

### Summary
This page explains how checkout-api supports Project Atlas during Phase 0 Legacy Stabilization. The phase goal is to stabilize legacy checkout, map risks, build team rituals. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: support macro must be updated before launch. Evidence links to ATLAS-4552 and PR-9288.
- Decision: dual-write only during migration window. Evidence links to ATLAS-4755 and PR-5703.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-4095 and PR-7443.

### Risks and Runbook Notes
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0014: ADR - inventory-reservation - 2018-12
- Owner: Fatima Noor
- Updated: 2018-12-21
- Phase: Phase 0 Legacy Stabilization
- Related Jira: ATLAS-3593

### Summary
This page explains how inventory-reservation supports Project Atlas during Phase 0 Legacy Stabilization. The phase goal is to stabilize legacy checkout, map risks, build team rituals. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-1096 and PR-8112.
- Decision: use feature flags for rollout. Evidence links to ATLAS-4039 and PR-9756.
- Decision: dual-write only during migration window. Evidence links to ATLAS-4539 and PR-9775.

### Risks and Runbook Notes
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0015: Release Checklist - payment-orchestrator - 2019-01
- Owner: Luca Moretti
- Updated: 2019-01-17
- Phase: Phase 1 Service Extraction
- Related Jira: ATLAS-4529

### Summary
This page explains how payment-orchestrator supports Project Atlas during Phase 1 Service Extraction. The phase goal is to extract cart, pricing, tax, and payment facades. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-5094 and PR-9058.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-3017 and PR-8104.
- Decision: dual-write only during migration window. Evidence links to ATLAS-3517 and PR-8671.

### Risks and Runbook Notes
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0016: Architecture - loyalty-service - 2019-01
- Owner: Dmitri Volkov
- Updated: 2019-01-19
- Phase: Phase 1 Service Extraction
- Related Jira: ATLAS-3836

### Summary
This page explains how loyalty-service supports Project Atlas during Phase 1 Service Extraction. The phase goal is to extract cart, pricing, tax, and payment facades. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-4759 and PR-6666.
- Decision: support macro must be updated before launch. Evidence links to ATLAS-1634 and PR-6821.
- Decision: support macro must be updated before launch. Evidence links to ATLAS-5584 and PR-5106.

### Risks and Runbook Notes
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0017: Architecture - pricing-engine - 2019-02
- Owner: Kim Tan
- Updated: 2019-02-19
- Phase: Phase 1 Service Extraction
- Related Jira: ATLAS-5902

### Summary
This page explains how pricing-engine supports Project Atlas during Phase 1 Service Extraction. The phase goal is to extract cart, pricing, tax, and payment facades. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: use feature flags for rollout. Evidence links to ATLAS-5548 and PR-5061.
- Decision: dual-write only during migration window. Evidence links to ATLAS-2439 and PR-5808.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-1291 and PR-5336.

### Risks and Runbook Notes
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0018: Support Playbook - payment-orchestrator - 2019-02
- Owner: Owen Brooks
- Updated: 2019-02-11
- Phase: Phase 1 Service Extraction
- Related Jira: ATLAS-2763

### Summary
This page explains how payment-orchestrator supports Project Atlas during Phase 1 Service Extraction. The phase goal is to extract cart, pricing, tax, and payment facades. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: use feature flags for rollout. Evidence links to ATLAS-3640 and PR-5441.
- Decision: dual-write only during migration window. Evidence links to ATLAS-3566 and PR-6617.
- Decision: support macro must be updated before launch. Evidence links to ATLAS-4554 and PR-5434.

### Risks and Runbook Notes
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0019: Runbook - order-ledger - 2019-03
- Owner: Harper Lee
- Updated: 2019-03-23
- Phase: Phase 1 Service Extraction
- Related Jira: ATLAS-4680

### Summary
This page explains how order-ledger supports Project Atlas during Phase 1 Service Extraction. The phase goal is to extract cart, pricing, tax, and payment facades. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: support macro must be updated before launch. Evidence links to ATLAS-5553 and PR-11188.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-4777 and PR-8611.
- Decision: dual-write only during migration window. Evidence links to ATLAS-4360 and PR-11973.

### Risks and Runbook Notes
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0020: Architecture - order-ledger - 2019-03
- Owner: Owen Brooks
- Updated: 2019-03-23
- Phase: Phase 1 Service Extraction
- Related Jira: ATLAS-3167

### Summary
This page explains how order-ledger supports Project Atlas during Phase 1 Service Extraction. The phase goal is to extract cart, pricing, tax, and payment facades. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-5948 and PR-9058.
- Decision: dual-write only during migration window. Evidence links to ATLAS-2143 and PR-8104.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-3082 and PR-9879.

### Risks and Runbook Notes
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0021: ADR - analytics-pipeline - 2019-04
- Owner: Jon Bell
- Updated: 2019-04-07
- Phase: Phase 1 Service Extraction
- Related Jira: ATLAS-5599

### Summary
This page explains how analytics-pipeline supports Project Atlas during Phase 1 Service Extraction. The phase goal is to extract cart, pricing, tax, and payment facades. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-3562 and PR-9365.
- Decision: use feature flags for rollout. Evidence links to ATLAS-4418 and PR-11034.
- Decision: use feature flags for rollout. Evidence links to ATLAS-1426 and PR-12448.

### Risks and Runbook Notes
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0022: Runbook - analytics-pipeline - 2019-04
- Owner: Theo Martin
- Updated: 2019-04-16
- Phase: Phase 1 Service Extraction
- Related Jira: ATLAS-1453

### Summary
This page explains how analytics-pipeline supports Project Atlas during Phase 1 Service Extraction. The phase goal is to extract cart, pricing, tax, and payment facades. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-3881 and PR-8453.
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-5557 and PR-12269.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-4464 and PR-7664.

### Risks and Runbook Notes
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0023: Architecture - cart-service - 2019-05
- Owner: Anika Sharma
- Updated: 2019-05-21
- Phase: Phase 1 Service Extraction
- Related Jira: ATLAS-4209

### Summary
This page explains how cart-service supports Project Atlas during Phase 1 Service Extraction. The phase goal is to extract cart, pricing, tax, and payment facades. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-6159 and PR-6009.
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-1433 and PR-7128.
- Decision: dual-write only during migration window. Evidence links to ATLAS-5620 and PR-5963.

### Risks and Runbook Notes
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0024: Architecture - checkout-api - 2019-05
- Owner: Maya Chen
- Updated: 2019-05-24
- Phase: Phase 1 Service Extraction
- Related Jira: ATLAS-4706

### Summary
This page explains how checkout-api supports Project Atlas during Phase 1 Service Extraction. The phase goal is to extract cart, pricing, tax, and payment facades. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: use feature flags for rollout. Evidence links to ATLAS-4118 and PR-8843.
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-1697 and PR-7009.
- Decision: use feature flags for rollout. Evidence links to ATLAS-2631 and PR-5774.

### Risks and Runbook Notes
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0025: Postmortem - loyalty-service - 2019-06
- Owner: Elena Petrova
- Updated: 2019-06-09
- Phase: Phase 1 Service Extraction
- Related Jira: ATLAS-3510

### Summary
This page explains how loyalty-service supports Project Atlas during Phase 1 Service Extraction. The phase goal is to extract cart, pricing, tax, and payment facades. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-2829 and PR-7126.
- Decision: support macro must be updated before launch. Evidence links to ATLAS-4964 and PR-6556.
- Decision: support macro must be updated before launch. Evidence links to ATLAS-1721 and PR-5402.

### Risks and Runbook Notes
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0026: Support Playbook - auth-gateway - 2019-06
- Owner: Harper Lee
- Updated: 2019-06-23
- Phase: Phase 1 Service Extraction
- Related Jira: ATLAS-1521

### Summary
This page explains how auth-gateway supports Project Atlas during Phase 1 Service Extraction. The phase goal is to extract cart, pricing, tax, and payment facades. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: support macro must be updated before launch. Evidence links to ATLAS-3281 and PR-9107.
- Decision: dual-write only during migration window. Evidence links to ATLAS-2725 and PR-9602.
- Decision: support macro must be updated before launch. Evidence links to ATLAS-5574 and PR-10805.

### Risks and Runbook Notes
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0027: Support Playbook - inventory-reservation - 2019-07
- Owner: Jon Bell
- Updated: 2019-07-21
- Phase: Phase 1 Service Extraction
- Related Jira: ATLAS-4976

### Summary
This page explains how inventory-reservation supports Project Atlas during Phase 1 Service Extraction. The phase goal is to extract cart, pricing, tax, and payment facades. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: dual-write only during migration window. Evidence links to ATLAS-4969 and PR-8890.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-5096 and PR-11417.
- Decision: support macro must be updated before launch. Evidence links to ATLAS-3838 and PR-12102.

### Risks and Runbook Notes
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0028: Data Contract - tax-service - 2019-07
- Owner: Yara Haddad
- Updated: 2019-07-07
- Phase: Phase 1 Service Extraction
- Related Jira: ATLAS-4475

### Summary
This page explains how tax-service supports Project Atlas during Phase 1 Service Extraction. The phase goal is to extract cart, pricing, tax, and payment facades. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-5179 and PR-8450.
- Decision: support macro must be updated before launch. Evidence links to ATLAS-5679 and PR-6616.
- Decision: support macro must be updated before launch. Evidence links to ATLAS-1437 and PR-7289.

### Risks and Runbook Notes
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0029: Data Contract - payment-orchestrator - 2019-08
- Owner: Fatima Noor
- Updated: 2019-08-17
- Phase: Phase 1 Service Extraction
- Related Jira: ATLAS-1693

### Summary
This page explains how payment-orchestrator supports Project Atlas during Phase 1 Service Extraction. The phase goal is to extract cart, pricing, tax, and payment facades. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-4426 and PR-8561.
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-3591 and PR-6804.
- Decision: use feature flags for rollout. Evidence links to ATLAS-1476 and PR-7308.

### Risks and Runbook Notes
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0030: Onboarding - payment-orchestrator - 2019-08
- Owner: Aisha Khan
- Updated: 2019-08-04
- Phase: Phase 1 Service Extraction
- Related Jira: ATLAS-3083

### Summary
This page explains how payment-orchestrator supports Project Atlas during Phase 1 Service Extraction. The phase goal is to extract cart, pricing, tax, and payment facades. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: support macro must be updated before launch. Evidence links to ATLAS-2407 and PR-7862.
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-1174 and PR-7055.
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-2856 and PR-9639.

### Risks and Runbook Notes
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0031: Support Playbook - tax-service - 2019-09
- Owner: Victor Silva
- Updated: 2019-09-08
- Phase: Phase 1 Service Extraction
- Related Jira: ATLAS-5670

### Summary
This page explains how tax-service supports Project Atlas during Phase 1 Service Extraction. The phase goal is to extract cart, pricing, tax, and payment facades. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-1968 and PR-6195.
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-2827 and PR-9261.
- Decision: support macro must be updated before launch. Evidence links to ATLAS-1277 and PR-6472.

### Risks and Runbook Notes
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0032: Runbook - notification-service - 2019-09
- Owner: Anika Sharma
- Updated: 2019-09-21
- Phase: Phase 1 Service Extraction
- Related Jira: ATLAS-2004

### Summary
This page explains how notification-service supports Project Atlas during Phase 1 Service Extraction. The phase goal is to extract cart, pricing, tax, and payment facades. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: use feature flags for rollout. Evidence links to ATLAS-3687 and PR-12240.
- Decision: dual-write only during migration window. Evidence links to ATLAS-5048 and PR-11375.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-2847 and PR-9143.

### Risks and Runbook Notes
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0033: Support Playbook - analytics-pipeline - 2019-10
- Owner: Owen Brooks
- Updated: 2019-10-08
- Phase: Phase 1 Service Extraction
- Related Jira: ATLAS-6196

### Summary
This page explains how analytics-pipeline supports Project Atlas during Phase 1 Service Extraction. The phase goal is to extract cart, pricing, tax, and payment facades. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: use feature flags for rollout. Evidence links to ATLAS-3816 and PR-11053.
- Decision: dual-write only during migration window. Evidence links to ATLAS-3475 and PR-8061.
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-1553 and PR-7483.

### Risks and Runbook Notes
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0034: Onboarding - checkout-api - 2019-10
- Owner: Dmitri Volkov
- Updated: 2019-10-22
- Phase: Phase 1 Service Extraction
- Related Jira: ATLAS-5271

### Summary
This page explains how checkout-api supports Project Atlas during Phase 1 Service Extraction. The phase goal is to extract cart, pricing, tax, and payment facades. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: support macro must be updated before launch. Evidence links to ATLAS-3380 and PR-9591.
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-1061 and PR-9867.
- Decision: dual-write only during migration window. Evidence links to ATLAS-2194 and PR-5511.

### Risks and Runbook Notes
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0035: Onboarding - order-ledger - 2019-11
- Owner: Sara Novak
- Updated: 2019-11-10
- Phase: Phase 1 Service Extraction
- Related Jira: ATLAS-3452

### Summary
This page explains how order-ledger supports Project Atlas during Phase 1 Service Extraction. The phase goal is to extract cart, pricing, tax, and payment facades. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-1318 and PR-7583.
- Decision: dual-write only during migration window. Evidence links to ATLAS-5390 and PR-7256.
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-3052 and PR-5133.

### Risks and Runbook Notes
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0036: Architecture - auth-gateway - 2019-11
- Owner: Samir Rao
- Updated: 2019-11-15
- Phase: Phase 1 Service Extraction
- Related Jira: ATLAS-1913

### Summary
This page explains how auth-gateway supports Project Atlas during Phase 1 Service Extraction. The phase goal is to extract cart, pricing, tax, and payment facades. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-2876 and PR-9165.
- Decision: support macro must be updated before launch. Evidence links to ATLAS-2004 and PR-11666.
- Decision: dual-write only during migration window. Evidence links to ATLAS-3339 and PR-9647.

### Risks and Runbook Notes
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0037: Support Playbook - notification-service - 2019-12
- Owner: Samir Rao
- Updated: 2019-12-04
- Phase: Phase 1 Service Extraction
- Related Jira: ATLAS-1514

### Summary
This page explains how notification-service supports Project Atlas during Phase 1 Service Extraction. The phase goal is to extract cart, pricing, tax, and payment facades. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: use feature flags for rollout. Evidence links to ATLAS-4535 and PR-10711.
- Decision: support macro must be updated before launch. Evidence links to ATLAS-5005 and PR-7878.
- Decision: dual-write only during migration window. Evidence links to ATLAS-2641 and PR-6711.

### Risks and Runbook Notes
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0038: Release Checklist - cart-service - 2019-12
- Owner: Kim Tan
- Updated: 2019-12-24
- Phase: Phase 1 Service Extraction
- Related Jira: ATLAS-3500

### Summary
This page explains how cart-service supports Project Atlas during Phase 1 Service Extraction. The phase goal is to extract cart, pricing, tax, and payment facades. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-4186 and PR-6189.
- Decision: use feature flags for rollout. Evidence links to ATLAS-1100 and PR-5826.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-5737 and PR-5014.

### Risks and Runbook Notes
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0039: Onboarding - pricing-engine - 2020-01
- Owner: Maya Chen
- Updated: 2020-01-22
- Phase: Phase 2 Cloud Migration
- Related Jira: ATLAS-2764

### Summary
This page explains how pricing-engine supports Project Atlas during Phase 2 Cloud Migration. The phase goal is to move workloads to Kubernetes and managed databases. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: use feature flags for rollout. Evidence links to ATLAS-4813 and PR-12099.
- Decision: use feature flags for rollout. Evidence links to ATLAS-2109 and PR-5678.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-1833 and PR-12234.

### Risks and Runbook Notes
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0040: Onboarding - inventory-reservation - 2020-01
- Owner: Anika Sharma
- Updated: 2020-01-19
- Phase: Phase 2 Cloud Migration
- Related Jira: ATLAS-1094

### Summary
This page explains how inventory-reservation supports Project Atlas during Phase 2 Cloud Migration. The phase goal is to move workloads to Kubernetes and managed databases. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: use feature flags for rollout. Evidence links to ATLAS-3164 and PR-9843.
- Decision: use feature flags for rollout. Evidence links to ATLAS-2344 and PR-8439.
- Decision: support macro must be updated before launch. Evidence links to ATLAS-1990 and PR-11072.

### Risks and Runbook Notes
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0041: ADR - pricing-engine - 2020-02
- Owner: Ben Carter
- Updated: 2020-02-13
- Phase: Phase 2 Cloud Migration
- Related Jira: ATLAS-1317

### Summary
This page explains how pricing-engine supports Project Atlas during Phase 2 Cloud Migration. The phase goal is to move workloads to Kubernetes and managed databases. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: support macro must be updated before launch. Evidence links to ATLAS-1073 and PR-7128.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-2877 and PR-7705.
- Decision: use feature flags for rollout. Evidence links to ATLAS-1844 and PR-7396.

### Risks and Runbook Notes
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0042: Postmortem - auth-gateway - 2020-02
- Owner: Kim Tan
- Updated: 2020-02-22
- Phase: Phase 2 Cloud Migration
- Related Jira: ATLAS-4550

### Summary
This page explains how auth-gateway supports Project Atlas during Phase 2 Cloud Migration. The phase goal is to move workloads to Kubernetes and managed databases. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-3705 and PR-8631.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-2941 and PR-8383.
- Decision: support macro must be updated before launch. Evidence links to ATLAS-4057 and PR-8763.

### Risks and Runbook Notes
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0043: Release Checklist - tax-service - 2020-03
- Owner: Harper Lee
- Updated: 2020-03-10
- Phase: Phase 2 Cloud Migration
- Related Jira: ATLAS-4565

### Summary
This page explains how tax-service supports Project Atlas during Phase 2 Cloud Migration. The phase goal is to move workloads to Kubernetes and managed databases. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: support macro must be updated before launch. Evidence links to ATLAS-2235 and PR-12169.
- Decision: dual-write only during migration window. Evidence links to ATLAS-3111 and PR-5469.
- Decision: support macro must be updated before launch. Evidence links to ATLAS-5457 and PR-6244.

### Risks and Runbook Notes
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0044: Architecture - pricing-engine - 2020-03
- Owner: Iris Wang
- Updated: 2020-03-09
- Phase: Phase 2 Cloud Migration
- Related Jira: ATLAS-2977

### Summary
This page explains how pricing-engine supports Project Atlas during Phase 2 Cloud Migration. The phase goal is to move workloads to Kubernetes and managed databases. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: use feature flags for rollout. Evidence links to ATLAS-4793 and PR-6239.
- Decision: use feature flags for rollout. Evidence links to ATLAS-2909 and PR-6513.
- Decision: dual-write only during migration window. Evidence links to ATLAS-3553 and PR-11621.

### Risks and Runbook Notes
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0045: Runbook - tax-service - 2020-04
- Owner: Dmitri Volkov
- Updated: 2020-04-20
- Phase: Phase 2 Cloud Migration
- Related Jira: ATLAS-5864

### Summary
This page explains how tax-service supports Project Atlas during Phase 2 Cloud Migration. The phase goal is to move workloads to Kubernetes and managed databases. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: support macro must be updated before launch. Evidence links to ATLAS-3960 and PR-9807.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-3176 and PR-8673.
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-4703 and PR-12482.

### Risks and Runbook Notes
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0046: Release Checklist - cart-service - 2020-04
- Owner: Theo Martin
- Updated: 2020-04-12
- Phase: Phase 2 Cloud Migration
- Related Jira: ATLAS-5646

### Summary
This page explains how cart-service supports Project Atlas during Phase 2 Cloud Migration. The phase goal is to move workloads to Kubernetes and managed databases. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: use feature flags for rollout. Evidence links to ATLAS-5872 and PR-7276.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-2769 and PR-9170.
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-3651 and PR-5657.

### Risks and Runbook Notes
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0047: Support Playbook - order-ledger - 2020-05
- Owner: Elena Petrova
- Updated: 2020-05-15
- Phase: Phase 2 Cloud Migration
- Related Jira: ATLAS-5687

### Summary
This page explains how order-ledger supports Project Atlas during Phase 2 Cloud Migration. The phase goal is to move workloads to Kubernetes and managed databases. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: use feature flags for rollout. Evidence links to ATLAS-4861 and PR-9841.
- Decision: dual-write only during migration window. Evidence links to ATLAS-4651 and PR-11106.
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-2219 and PR-10144.

### Risks and Runbook Notes
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0048: Data Contract - search-recommendations - 2020-05
- Owner: Noah Evans
- Updated: 2020-05-17
- Phase: Phase 2 Cloud Migration
- Related Jira: ATLAS-1604

### Summary
This page explains how search-recommendations supports Project Atlas during Phase 2 Cloud Migration. The phase goal is to move workloads to Kubernetes and managed databases. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-1767 and PR-7151.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-5701 and PR-7529.
- Decision: use feature flags for rollout. Evidence links to ATLAS-4246 and PR-5517.

### Risks and Runbook Notes
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0049: Data Contract - pricing-engine - 2020-06
- Owner: Ben Carter
- Updated: 2020-06-26
- Phase: Phase 2 Cloud Migration
- Related Jira: ATLAS-6199

### Summary
This page explains how pricing-engine supports Project Atlas during Phase 2 Cloud Migration. The phase goal is to move workloads to Kubernetes and managed databases. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: use feature flags for rollout. Evidence links to ATLAS-3355 and PR-5500.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-1214 and PR-10705.
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-3964 and PR-8362.

### Risks and Runbook Notes
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0050: Data Contract - checkout-api - 2020-06
- Owner: Samir Rao
- Updated: 2020-06-05
- Phase: Phase 2 Cloud Migration
- Related Jira: ATLAS-2512

### Summary
This page explains how checkout-api supports Project Atlas during Phase 2 Cloud Migration. The phase goal is to move workloads to Kubernetes and managed databases. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: support macro must be updated before launch. Evidence links to ATLAS-1514 and PR-6719.
- Decision: dual-write only during migration window. Evidence links to ATLAS-2762 and PR-11634.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-5818 and PR-5103.

### Risks and Runbook Notes
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0051: Architecture - loyalty-service - 2020-07
- Owner: Grace Kim
- Updated: 2020-07-16
- Phase: Phase 2 Cloud Migration
- Related Jira: ATLAS-4439

### Summary
This page explains how loyalty-service supports Project Atlas during Phase 2 Cloud Migration. The phase goal is to move workloads to Kubernetes and managed databases. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: support macro must be updated before launch. Evidence links to ATLAS-2919 and PR-5904.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-1418 and PR-8925.
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-4768 and PR-8134.

### Risks and Runbook Notes
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0052: Release Checklist - tax-service - 2020-07
- Owner: Owen Brooks
- Updated: 2020-07-04
- Phase: Phase 2 Cloud Migration
- Related Jira: ATLAS-3589

### Summary
This page explains how tax-service supports Project Atlas during Phase 2 Cloud Migration. The phase goal is to move workloads to Kubernetes and managed databases. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: support macro must be updated before launch. Evidence links to ATLAS-2296 and PR-6975.
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-4158 and PR-7512.
- Decision: support macro must be updated before launch. Evidence links to ATLAS-2803 and PR-10374.

### Risks and Runbook Notes
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0053: Support Playbook - order-ledger - 2020-08
- Owner: Grace Kim
- Updated: 2020-08-10
- Phase: Phase 2 Cloud Migration
- Related Jira: ATLAS-3904

### Summary
This page explains how order-ledger supports Project Atlas during Phase 2 Cloud Migration. The phase goal is to move workloads to Kubernetes and managed databases. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-5962 and PR-12393.
- Decision: use feature flags for rollout. Evidence links to ATLAS-2476 and PR-9036.
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-1992 and PR-5594.

### Risks and Runbook Notes
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0054: Architecture - search-recommendations - 2020-08
- Owner: Noah Evans
- Updated: 2020-08-09
- Phase: Phase 2 Cloud Migration
- Related Jira: ATLAS-5908

### Summary
This page explains how search-recommendations supports Project Atlas during Phase 2 Cloud Migration. The phase goal is to move workloads to Kubernetes and managed databases. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: dual-write only during migration window. Evidence links to ATLAS-2752 and PR-7153.
- Decision: dual-write only during migration window. Evidence links to ATLAS-1283 and PR-6100.
- Decision: use feature flags for rollout. Evidence links to ATLAS-3860 and PR-8497.

### Risks and Runbook Notes
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0055: Release Checklist - payment-orchestrator - 2020-09
- Owner: Priya Nair
- Updated: 2020-09-09
- Phase: Phase 2 Cloud Migration
- Related Jira: ATLAS-1210

### Summary
This page explains how payment-orchestrator supports Project Atlas during Phase 2 Cloud Migration. The phase goal is to move workloads to Kubernetes and managed databases. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-5087 and PR-5581.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-4237 and PR-9934.
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-1595 and PR-5982.

### Risks and Runbook Notes
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0056: Runbook - tax-service - 2020-09
- Owner: Mateo Garcia
- Updated: 2020-09-21
- Phase: Phase 2 Cloud Migration
- Related Jira: ATLAS-4317

### Summary
This page explains how tax-service supports Project Atlas during Phase 2 Cloud Migration. The phase goal is to move workloads to Kubernetes and managed databases. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-5625 and PR-5197.
- Decision: use feature flags for rollout. Evidence links to ATLAS-5037 and PR-8787.
- Decision: support macro must be updated before launch. Evidence links to ATLAS-5110 and PR-8162.

### Risks and Runbook Notes
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0057: Architecture - loyalty-service - 2020-10
- Owner: Grace Kim
- Updated: 2020-10-06
- Phase: Phase 2 Cloud Migration
- Related Jira: ATLAS-3895

### Summary
This page explains how loyalty-service supports Project Atlas during Phase 2 Cloud Migration. The phase goal is to move workloads to Kubernetes and managed databases. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: support macro must be updated before launch. Evidence links to ATLAS-4290 and PR-7596.
- Decision: support macro must be updated before launch. Evidence links to ATLAS-1651 and PR-7431.
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-2684 and PR-6877.

### Risks and Runbook Notes
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0058: Onboarding - loyalty-service - 2020-10
- Owner: Samir Rao
- Updated: 2020-10-05
- Phase: Phase 2 Cloud Migration
- Related Jira: ATLAS-4732

### Summary
This page explains how loyalty-service supports Project Atlas during Phase 2 Cloud Migration. The phase goal is to move workloads to Kubernetes and managed databases. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-2527 and PR-7013.
- Decision: support macro must be updated before launch. Evidence links to ATLAS-5189 and PR-11241.
- Decision: support macro must be updated before launch. Evidence links to ATLAS-5789 and PR-5639.

### Risks and Runbook Notes
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0059: Release Checklist - cart-service - 2020-11
- Owner: Anika Sharma
- Updated: 2020-11-08
- Phase: Phase 2 Cloud Migration
- Related Jira: ATLAS-3737

### Summary
This page explains how cart-service supports Project Atlas during Phase 2 Cloud Migration. The phase goal is to move workloads to Kubernetes and managed databases. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: support macro must be updated before launch. Evidence links to ATLAS-4421 and PR-8409.
- Decision: use feature flags for rollout. Evidence links to ATLAS-3065 and PR-5064.
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-4054 and PR-5869.

### Risks and Runbook Notes
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0060: Runbook - inventory-reservation - 2020-11
- Owner: Harper Lee
- Updated: 2020-11-19
- Phase: Phase 2 Cloud Migration
- Related Jira: ATLAS-1755

### Summary
This page explains how inventory-reservation supports Project Atlas during Phase 2 Cloud Migration. The phase goal is to move workloads to Kubernetes and managed databases. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: support macro must be updated before launch. Evidence links to ATLAS-3992 and PR-9880.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-4414 and PR-12250.
- Decision: use feature flags for rollout. Evidence links to ATLAS-5169 and PR-8725.

### Risks and Runbook Notes
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0061: Onboarding - loyalty-service - 2020-12
- Owner: Owen Brooks
- Updated: 2020-12-11
- Phase: Phase 2 Cloud Migration
- Related Jira: ATLAS-4898

### Summary
This page explains how loyalty-service supports Project Atlas during Phase 2 Cloud Migration. The phase goal is to move workloads to Kubernetes and managed databases. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-1210 and PR-10934.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-5899 and PR-8769.
- Decision: support macro must be updated before launch. Evidence links to ATLAS-2852 and PR-5078.

### Risks and Runbook Notes
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0062: Release Checklist - auth-gateway - 2020-12
- Owner: Aisha Khan
- Updated: 2020-12-17
- Phase: Phase 2 Cloud Migration
- Related Jira: ATLAS-2621

### Summary
This page explains how auth-gateway supports Project Atlas during Phase 2 Cloud Migration. The phase goal is to move workloads to Kubernetes and managed databases. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-5387 and PR-6068.
- Decision: use feature flags for rollout. Evidence links to ATLAS-5493 and PR-6030.
- Decision: dual-write only during migration window. Evidence links to ATLAS-2262 and PR-6789.

### Risks and Runbook Notes
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0063: Release Checklist - search-recommendations - 2021-01
- Owner: Jon Bell
- Updated: 2021-01-02
- Phase: Phase 3 Global Checkout
- Related Jira: ATLAS-4870

### Summary
This page explains how search-recommendations supports Project Atlas during Phase 3 Global Checkout. The phase goal is to add localization, tax rules, currency, and fraud checks. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: dual-write only during migration window. Evidence links to ATLAS-3735 and PR-8102.
- Decision: use feature flags for rollout. Evidence links to ATLAS-2347 and PR-9961.
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-4009 and PR-7949.

### Risks and Runbook Notes
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0064: Data Contract - payment-orchestrator - 2021-01
- Owner: Aisha Khan
- Updated: 2021-01-18
- Phase: Phase 3 Global Checkout
- Related Jira: ATLAS-5090

### Summary
This page explains how payment-orchestrator supports Project Atlas during Phase 3 Global Checkout. The phase goal is to add localization, tax rules, currency, and fraud checks. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: dual-write only during migration window. Evidence links to ATLAS-1109 and PR-10055.
- Decision: use feature flags for rollout. Evidence links to ATLAS-5059 and PR-8907.
- Decision: support macro must be updated before launch. Evidence links to ATLAS-2394 and PR-9863.

### Risks and Runbook Notes
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0065: Onboarding - inventory-reservation - 2021-02
- Owner: Aisha Khan
- Updated: 2021-02-23
- Phase: Phase 3 Global Checkout
- Related Jira: ATLAS-4436

### Summary
This page explains how inventory-reservation supports Project Atlas during Phase 3 Global Checkout. The phase goal is to add localization, tax rules, currency, and fraud checks. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: support macro must be updated before launch. Evidence links to ATLAS-2101 and PR-10154.
- Decision: use feature flags for rollout. Evidence links to ATLAS-3438 and PR-5644.
- Decision: dual-write only during migration window. Evidence links to ATLAS-1304 and PR-12402.

### Risks and Runbook Notes
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0066: Architecture - order-ledger - 2021-02
- Owner: Anika Sharma
- Updated: 2021-02-26
- Phase: Phase 3 Global Checkout
- Related Jira: ATLAS-1236

### Summary
This page explains how order-ledger supports Project Atlas during Phase 3 Global Checkout. The phase goal is to add localization, tax rules, currency, and fraud checks. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: use feature flags for rollout. Evidence links to ATLAS-2151 and PR-6126.
- Decision: dual-write only during migration window. Evidence links to ATLAS-4250 and PR-9792.
- Decision: dual-write only during migration window. Evidence links to ATLAS-1338 and PR-8979.

### Risks and Runbook Notes
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0067: ADR - tax-service - 2021-03
- Owner: Theo Martin
- Updated: 2021-03-08
- Phase: Phase 3 Global Checkout
- Related Jira: ATLAS-5523

### Summary
This page explains how tax-service supports Project Atlas during Phase 3 Global Checkout. The phase goal is to add localization, tax rules, currency, and fraud checks. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-2643 and PR-8769.
- Decision: support macro must be updated before launch. Evidence links to ATLAS-2376 and PR-8985.
- Decision: dual-write only during migration window. Evidence links to ATLAS-3138 and PR-7037.

### Risks and Runbook Notes
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0068: Architecture - pricing-engine - 2021-03
- Owner: Iris Wang
- Updated: 2021-03-24
- Phase: Phase 3 Global Checkout
- Related Jira: ATLAS-2422

### Summary
This page explains how pricing-engine supports Project Atlas during Phase 3 Global Checkout. The phase goal is to add localization, tax rules, currency, and fraud checks. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: dual-write only during migration window. Evidence links to ATLAS-4501 and PR-5922.
- Decision: support macro must be updated before launch. Evidence links to ATLAS-4958 and PR-5308.
- Decision: dual-write only during migration window. Evidence links to ATLAS-1622 and PR-8531.

### Risks and Runbook Notes
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0069: Runbook - cart-service - 2021-04
- Owner: Nora Singh
- Updated: 2021-04-23
- Phase: Phase 3 Global Checkout
- Related Jira: ATLAS-4889

### Summary
This page explains how cart-service supports Project Atlas during Phase 3 Global Checkout. The phase goal is to add localization, tax rules, currency, and fraud checks. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: dual-write only during migration window. Evidence links to ATLAS-1140 and PR-7891.
- Decision: support macro must be updated before launch. Evidence links to ATLAS-4610 and PR-7440.
- Decision: use feature flags for rollout. Evidence links to ATLAS-2416 and PR-7488.

### Risks and Runbook Notes
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0070: Onboarding - cart-service - 2021-04
- Owner: Yara Haddad
- Updated: 2021-04-13
- Phase: Phase 3 Global Checkout
- Related Jira: ATLAS-1644

### Summary
This page explains how cart-service supports Project Atlas during Phase 3 Global Checkout. The phase goal is to add localization, tax rules, currency, and fraud checks. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-4268 and PR-9334.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-6196 and PR-6254.
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-4851 and PR-11983.

### Risks and Runbook Notes
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0071: Onboarding - inventory-reservation - 2021-05
- Owner: Sara Novak
- Updated: 2021-05-07
- Phase: Phase 3 Global Checkout
- Related Jira: ATLAS-3239

### Summary
This page explains how inventory-reservation supports Project Atlas during Phase 3 Global Checkout. The phase goal is to add localization, tax rules, currency, and fraud checks. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: dual-write only during migration window. Evidence links to ATLAS-1480 and PR-8710.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-6045 and PR-6324.
- Decision: support macro must be updated before launch. Evidence links to ATLAS-4464 and PR-9949.

### Risks and Runbook Notes
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0072: Data Contract - loyalty-service - 2021-05
- Owner: Yara Haddad
- Updated: 2021-05-26
- Phase: Phase 3 Global Checkout
- Related Jira: ATLAS-2281

### Summary
This page explains how loyalty-service supports Project Atlas during Phase 3 Global Checkout. The phase goal is to add localization, tax rules, currency, and fraud checks. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: dual-write only during migration window. Evidence links to ATLAS-5225 and PR-7645.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-3802 and PR-5400.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-5114 and PR-11780.

### Risks and Runbook Notes
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0073: Release Checklist - inventory-reservation - 2021-06
- Owner: Elena Petrova
- Updated: 2021-06-23
- Phase: Phase 3 Global Checkout
- Related Jira: ATLAS-3084

### Summary
This page explains how inventory-reservation supports Project Atlas during Phase 3 Global Checkout. The phase goal is to add localization, tax rules, currency, and fraud checks. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-6180 and PR-10221.
- Decision: dual-write only during migration window. Evidence links to ATLAS-5156 and PR-5557.
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-3665 and PR-8351.

### Risks and Runbook Notes
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0074: Runbook - order-ledger - 2021-06
- Owner: Sara Novak
- Updated: 2021-06-05
- Phase: Phase 3 Global Checkout
- Related Jira: ATLAS-3668

### Summary
This page explains how order-ledger supports Project Atlas during Phase 3 Global Checkout. The phase goal is to add localization, tax rules, currency, and fraud checks. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: support macro must be updated before launch. Evidence links to ATLAS-3093 and PR-9709.
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-5795 and PR-6642.
- Decision: support macro must be updated before launch. Evidence links to ATLAS-5519 and PR-11386.

### Risks and Runbook Notes
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0075: Postmortem - analytics-pipeline - 2021-07
- Owner: Kim Tan
- Updated: 2021-07-26
- Phase: Phase 3 Global Checkout
- Related Jira: ATLAS-3305

### Summary
This page explains how analytics-pipeline supports Project Atlas during Phase 3 Global Checkout. The phase goal is to add localization, tax rules, currency, and fraud checks. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: use feature flags for rollout. Evidence links to ATLAS-2140 and PR-8036.
- Decision: use feature flags for rollout. Evidence links to ATLAS-6068 and PR-10251.
- Decision: use feature flags for rollout. Evidence links to ATLAS-4171 and PR-6772.

### Risks and Runbook Notes
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0076: Support Playbook - payment-orchestrator - 2021-07
- Owner: Samir Rao
- Updated: 2021-07-09
- Phase: Phase 3 Global Checkout
- Related Jira: ATLAS-4831

### Summary
This page explains how payment-orchestrator supports Project Atlas during Phase 3 Global Checkout. The phase goal is to add localization, tax rules, currency, and fraud checks. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: use feature flags for rollout. Evidence links to ATLAS-1012 and PR-11586.
- Decision: dual-write only during migration window. Evidence links to ATLAS-4818 and PR-6945.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-5241 and PR-8466.

### Risks and Runbook Notes
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0077: Release Checklist - cart-service - 2021-08
- Owner: Owen Brooks
- Updated: 2021-08-14
- Phase: Phase 3 Global Checkout
- Related Jira: ATLAS-1757

### Summary
This page explains how cart-service supports Project Atlas during Phase 3 Global Checkout. The phase goal is to add localization, tax rules, currency, and fraud checks. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: dual-write only during migration window. Evidence links to ATLAS-1583 and PR-8022.
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-2205 and PR-5739.
- Decision: use feature flags for rollout. Evidence links to ATLAS-4641 and PR-5157.

### Risks and Runbook Notes
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0078: Data Contract - loyalty-service - 2021-08
- Owner: Elena Petrova
- Updated: 2021-08-16
- Phase: Phase 3 Global Checkout
- Related Jira: ATLAS-1532

### Summary
This page explains how loyalty-service supports Project Atlas during Phase 3 Global Checkout. The phase goal is to add localization, tax rules, currency, and fraud checks. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: dual-write only during migration window. Evidence links to ATLAS-5187 and PR-5579.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-6179 and PR-9125.
- Decision: support macro must be updated before launch. Evidence links to ATLAS-1390 and PR-6215.

### Risks and Runbook Notes
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0079: Runbook - payment-orchestrator - 2021-09
- Owner: Owen Brooks
- Updated: 2021-09-19
- Phase: Phase 3 Global Checkout
- Related Jira: ATLAS-2191

### Summary
This page explains how payment-orchestrator supports Project Atlas during Phase 3 Global Checkout. The phase goal is to add localization, tax rules, currency, and fraud checks. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-5559 and PR-7526.
- Decision: support macro must be updated before launch. Evidence links to ATLAS-4808 and PR-10032.
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-6071 and PR-7850.

### Risks and Runbook Notes
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0080: Release Checklist - pricing-engine - 2021-09
- Owner: Victor Silva
- Updated: 2021-09-10
- Phase: Phase 3 Global Checkout
- Related Jira: ATLAS-3169

### Summary
This page explains how pricing-engine supports Project Atlas during Phase 3 Global Checkout. The phase goal is to add localization, tax rules, currency, and fraud checks. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: dual-write only during migration window. Evidence links to ATLAS-2944 and PR-10055.
- Decision: dual-write only during migration window. Evidence links to ATLAS-1512 and PR-5505.
- Decision: support macro must be updated before launch. Evidence links to ATLAS-5809 and PR-8617.

### Risks and Runbook Notes
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0081: Onboarding - checkout-api - 2021-10
- Owner: Iris Wang
- Updated: 2021-10-15
- Phase: Phase 3 Global Checkout
- Related Jira: ATLAS-4941

### Summary
This page explains how checkout-api supports Project Atlas during Phase 3 Global Checkout. The phase goal is to add localization, tax rules, currency, and fraud checks. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: use feature flags for rollout. Evidence links to ATLAS-3848 and PR-5535.
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-5740 and PR-6130.
- Decision: use feature flags for rollout. Evidence links to ATLAS-5220 and PR-5828.

### Risks and Runbook Notes
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0082: Runbook - loyalty-service - 2021-10
- Owner: Noah Evans
- Updated: 2021-10-16
- Phase: Phase 3 Global Checkout
- Related Jira: ATLAS-4958

### Summary
This page explains how loyalty-service supports Project Atlas during Phase 3 Global Checkout. The phase goal is to add localization, tax rules, currency, and fraud checks. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: dual-write only during migration window. Evidence links to ATLAS-5699 and PR-6791.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-4193 and PR-7612.
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-3747 and PR-9722.

### Risks and Runbook Notes
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0083: Architecture - order-ledger - 2021-11
- Owner: Kim Tan
- Updated: 2021-11-19
- Phase: Phase 3 Global Checkout
- Related Jira: ATLAS-5811

### Summary
This page explains how order-ledger supports Project Atlas during Phase 3 Global Checkout. The phase goal is to add localization, tax rules, currency, and fraud checks. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-1681 and PR-5150.
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-5963 and PR-7389.
- Decision: dual-write only during migration window. Evidence links to ATLAS-4688 and PR-5729.

### Risks and Runbook Notes
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0084: Architecture - auth-gateway - 2021-11
- Owner: Sara Novak
- Updated: 2021-11-24
- Phase: Phase 3 Global Checkout
- Related Jira: ATLAS-3023

### Summary
This page explains how auth-gateway supports Project Atlas during Phase 3 Global Checkout. The phase goal is to add localization, tax rules, currency, and fraud checks. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: support macro must be updated before launch. Evidence links to ATLAS-1537 and PR-9740.
- Decision: use feature flags for rollout. Evidence links to ATLAS-5501 and PR-10930.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-5369 and PR-6538.

### Risks and Runbook Notes
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0085: Data Contract - analytics-pipeline - 2021-12
- Owner: Nora Singh
- Updated: 2021-12-12
- Phase: Phase 3 Global Checkout
- Related Jira: ATLAS-1044

### Summary
This page explains how analytics-pipeline supports Project Atlas during Phase 3 Global Checkout. The phase goal is to add localization, tax rules, currency, and fraud checks. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: support macro must be updated before launch. Evidence links to ATLAS-5801 and PR-7519.
- Decision: dual-write only during migration window. Evidence links to ATLAS-5323 and PR-7360.
- Decision: use feature flags for rollout. Evidence links to ATLAS-1807 and PR-7256.

### Risks and Runbook Notes
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0086: Support Playbook - payment-orchestrator - 2021-12
- Owner: Yara Haddad
- Updated: 2021-12-14
- Phase: Phase 3 Global Checkout
- Related Jira: ATLAS-2207

### Summary
This page explains how payment-orchestrator supports Project Atlas during Phase 3 Global Checkout. The phase goal is to add localization, tax rules, currency, and fraud checks. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-1094 and PR-10883.
- Decision: support macro must be updated before launch. Evidence links to ATLAS-3990 and PR-10926.
- Decision: support macro must be updated before launch. Evidence links to ATLAS-3727 and PR-5698.

### Risks and Runbook Notes
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0087: ADR - search-recommendations - 2022-01
- Owner: Harper Lee
- Updated: 2022-01-16
- Phase: Phase 4 Loyalty and Personalization
- Related Jira: ATLAS-2498

### Summary
This page explains how search-recommendations supports Project Atlas during Phase 4 Loyalty and Personalization. The phase goal is to connect loyalty, promotions, and segmentation. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-6081 and PR-8813.
- Decision: dual-write only during migration window. Evidence links to ATLAS-5229 and PR-12037.
- Decision: use feature flags for rollout. Evidence links to ATLAS-4321 and PR-10346.

### Risks and Runbook Notes
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0088: Onboarding - checkout-api - 2022-01
- Owner: Maya Chen
- Updated: 2022-01-24
- Phase: Phase 4 Loyalty and Personalization
- Related Jira: ATLAS-3355

### Summary
This page explains how checkout-api supports Project Atlas during Phase 4 Loyalty and Personalization. The phase goal is to connect loyalty, promotions, and segmentation. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-1610 and PR-8308.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-3102 and PR-6100.
- Decision: use feature flags for rollout. Evidence links to ATLAS-1336 and PR-10927.

### Risks and Runbook Notes
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0089: ADR - order-ledger - 2022-02
- Owner: Iris Wang
- Updated: 2022-02-10
- Phase: Phase 4 Loyalty and Personalization
- Related Jira: ATLAS-3435

### Summary
This page explains how order-ledger supports Project Atlas during Phase 4 Loyalty and Personalization. The phase goal is to connect loyalty, promotions, and segmentation. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: dual-write only during migration window. Evidence links to ATLAS-1362 and PR-6537.
- Decision: dual-write only during migration window. Evidence links to ATLAS-3197 and PR-6005.
- Decision: dual-write only during migration window. Evidence links to ATLAS-1166 and PR-9141.

### Risks and Runbook Notes
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0090: Runbook - order-ledger - 2022-02
- Owner: Ben Carter
- Updated: 2022-02-14
- Phase: Phase 4 Loyalty and Personalization
- Related Jira: ATLAS-1228

### Summary
This page explains how order-ledger supports Project Atlas during Phase 4 Loyalty and Personalization. The phase goal is to connect loyalty, promotions, and segmentation. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: use feature flags for rollout. Evidence links to ATLAS-6045 and PR-6374.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-2362 and PR-11520.
- Decision: use feature flags for rollout. Evidence links to ATLAS-2699 and PR-5731.

### Risks and Runbook Notes
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0091: Postmortem - search-recommendations - 2022-03
- Owner: Ravi Patel
- Updated: 2022-03-17
- Phase: Phase 4 Loyalty and Personalization
- Related Jira: ATLAS-1402

### Summary
This page explains how search-recommendations supports Project Atlas during Phase 4 Loyalty and Personalization. The phase goal is to connect loyalty, promotions, and segmentation. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: dual-write only during migration window. Evidence links to ATLAS-5540 and PR-7172.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-5045 and PR-8971.
- Decision: dual-write only during migration window. Evidence links to ATLAS-3914 and PR-11173.

### Risks and Runbook Notes
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0092: Runbook - inventory-reservation - 2022-03
- Owner: Kim Tan
- Updated: 2022-03-04
- Phase: Phase 4 Loyalty and Personalization
- Related Jira: ATLAS-4466

### Summary
This page explains how inventory-reservation supports Project Atlas during Phase 4 Loyalty and Personalization. The phase goal is to connect loyalty, promotions, and segmentation. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: dual-write only during migration window. Evidence links to ATLAS-1588 and PR-5916.
- Decision: use feature flags for rollout. Evidence links to ATLAS-5112 and PR-9843.
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-2419 and PR-10598.

### Risks and Runbook Notes
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0093: Release Checklist - checkout-api - 2022-04
- Owner: Dmitri Volkov
- Updated: 2022-04-02
- Phase: Phase 4 Loyalty and Personalization
- Related Jira: ATLAS-2622

### Summary
This page explains how checkout-api supports Project Atlas during Phase 4 Loyalty and Personalization. The phase goal is to connect loyalty, promotions, and segmentation. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-4708 and PR-11739.
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-5457 and PR-5411.
- Decision: dual-write only during migration window. Evidence links to ATLAS-4221 and PR-12061.

### Risks and Runbook Notes
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0094: Onboarding - search-recommendations - 2022-04
- Owner: Jon Bell
- Updated: 2022-04-07
- Phase: Phase 4 Loyalty and Personalization
- Related Jira: ATLAS-5153

### Summary
This page explains how search-recommendations supports Project Atlas during Phase 4 Loyalty and Personalization. The phase goal is to connect loyalty, promotions, and segmentation. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: support macro must be updated before launch. Evidence links to ATLAS-4330 and PR-7775.
- Decision: use feature flags for rollout. Evidence links to ATLAS-3362 and PR-8481.
- Decision: support macro must be updated before launch. Evidence links to ATLAS-2593 and PR-6399.

### Risks and Runbook Notes
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0095: Support Playbook - search-recommendations - 2022-05
- Owner: Fatima Noor
- Updated: 2022-05-21
- Phase: Phase 4 Loyalty and Personalization
- Related Jira: ATLAS-4138

### Summary
This page explains how search-recommendations supports Project Atlas during Phase 4 Loyalty and Personalization. The phase goal is to connect loyalty, promotions, and segmentation. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: use feature flags for rollout. Evidence links to ATLAS-3886 and PR-6081.
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-3221 and PR-7481.
- Decision: use feature flags for rollout. Evidence links to ATLAS-6026 and PR-9807.

### Risks and Runbook Notes
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0096: Release Checklist - cart-service - 2022-05
- Owner: Iris Wang
- Updated: 2022-05-11
- Phase: Phase 4 Loyalty and Personalization
- Related Jira: ATLAS-5601

### Summary
This page explains how cart-service supports Project Atlas during Phase 4 Loyalty and Personalization. The phase goal is to connect loyalty, promotions, and segmentation. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: dual-write only during migration window. Evidence links to ATLAS-3455 and PR-8693.
- Decision: use feature flags for rollout. Evidence links to ATLAS-5626 and PR-11406.
- Decision: dual-write only during migration window. Evidence links to ATLAS-3104 and PR-8457.

### Risks and Runbook Notes
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0097: Onboarding - pricing-engine - 2022-06
- Owner: Luca Moretti
- Updated: 2022-06-12
- Phase: Phase 4 Loyalty and Personalization
- Related Jira: ATLAS-3112

### Summary
This page explains how pricing-engine supports Project Atlas during Phase 4 Loyalty and Personalization. The phase goal is to connect loyalty, promotions, and segmentation. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-2821 and PR-9123.
- Decision: support macro must be updated before launch. Evidence links to ATLAS-3283 and PR-8168.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-3266 and PR-7548.

### Risks and Runbook Notes
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0098: Postmortem - tax-service - 2022-06
- Owner: Aisha Khan
- Updated: 2022-06-12
- Phase: Phase 4 Loyalty and Personalization
- Related Jira: ATLAS-5789

### Summary
This page explains how tax-service supports Project Atlas during Phase 4 Loyalty and Personalization. The phase goal is to connect loyalty, promotions, and segmentation. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-3682 and PR-9556.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-2947 and PR-7511.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-3906 and PR-10169.

### Risks and Runbook Notes
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0099: Release Checklist - inventory-reservation - 2022-07
- Owner: Aisha Khan
- Updated: 2022-07-21
- Phase: Phase 4 Loyalty and Personalization
- Related Jira: ATLAS-2786

### Summary
This page explains how inventory-reservation supports Project Atlas during Phase 4 Loyalty and Personalization. The phase goal is to connect loyalty, promotions, and segmentation. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: dual-write only during migration window. Evidence links to ATLAS-3928 and PR-12433.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-1127 and PR-8623.
- Decision: support macro must be updated before launch. Evidence links to ATLAS-3306 and PR-9662.

### Risks and Runbook Notes
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0100: Runbook - analytics-pipeline - 2022-07
- Owner: Ravi Patel
- Updated: 2022-07-09
- Phase: Phase 4 Loyalty and Personalization
- Related Jira: ATLAS-1138

### Summary
This page explains how analytics-pipeline supports Project Atlas during Phase 4 Loyalty and Personalization. The phase goal is to connect loyalty, promotions, and segmentation. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: support macro must be updated before launch. Evidence links to ATLAS-1073 and PR-7523.
- Decision: use feature flags for rollout. Evidence links to ATLAS-3973 and PR-7869.
- Decision: use feature flags for rollout. Evidence links to ATLAS-5193 and PR-5026.

### Risks and Runbook Notes
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0101: Release Checklist - analytics-pipeline - 2022-08
- Owner: Jon Bell
- Updated: 2022-08-15
- Phase: Phase 4 Loyalty and Personalization
- Related Jira: ATLAS-5394

### Summary
This page explains how analytics-pipeline supports Project Atlas during Phase 4 Loyalty and Personalization. The phase goal is to connect loyalty, promotions, and segmentation. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: dual-write only during migration window. Evidence links to ATLAS-1448 and PR-9940.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-2444 and PR-9748.
- Decision: support macro must be updated before launch. Evidence links to ATLAS-4700 and PR-9825.

### Risks and Runbook Notes
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0102: Support Playbook - analytics-pipeline - 2022-08
- Owner: Fatima Noor
- Updated: 2022-08-13
- Phase: Phase 4 Loyalty and Personalization
- Related Jira: ATLAS-5210

### Summary
This page explains how analytics-pipeline supports Project Atlas during Phase 4 Loyalty and Personalization. The phase goal is to connect loyalty, promotions, and segmentation. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: use feature flags for rollout. Evidence links to ATLAS-2580 and PR-5504.
- Decision: dual-write only during migration window. Evidence links to ATLAS-2594 and PR-8608.
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-3565 and PR-9665.

### Risks and Runbook Notes
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0103: Architecture - notification-service - 2022-09
- Owner: Ben Carter
- Updated: 2022-09-03
- Phase: Phase 4 Loyalty and Personalization
- Related Jira: ATLAS-5379

### Summary
This page explains how notification-service supports Project Atlas during Phase 4 Loyalty and Personalization. The phase goal is to connect loyalty, promotions, and segmentation. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-5681 and PR-7088.
- Decision: dual-write only during migration window. Evidence links to ATLAS-1015 and PR-7078.
- Decision: use feature flags for rollout. Evidence links to ATLAS-5642 and PR-9114.

### Risks and Runbook Notes
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0104: Onboarding - cart-service - 2022-09
- Owner: Mateo Garcia
- Updated: 2022-09-08
- Phase: Phase 4 Loyalty and Personalization
- Related Jira: ATLAS-5795

### Summary
This page explains how cart-service supports Project Atlas during Phase 4 Loyalty and Personalization. The phase goal is to connect loyalty, promotions, and segmentation. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: use feature flags for rollout. Evidence links to ATLAS-1155 and PR-5872.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-2359 and PR-5712.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-5452 and PR-6267.

### Risks and Runbook Notes
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0105: Onboarding - notification-service - 2022-10
- Owner: Aisha Khan
- Updated: 2022-10-24
- Phase: Phase 4 Loyalty and Personalization
- Related Jira: ATLAS-6114

### Summary
This page explains how notification-service supports Project Atlas during Phase 4 Loyalty and Personalization. The phase goal is to connect loyalty, promotions, and segmentation. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: dual-write only during migration window. Evidence links to ATLAS-3065 and PR-5509.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-3870 and PR-5524.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-2265 and PR-7391.

### Risks and Runbook Notes
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0106: Architecture - loyalty-service - 2022-10
- Owner: Dmitri Volkov
- Updated: 2022-10-04
- Phase: Phase 4 Loyalty and Personalization
- Related Jira: ATLAS-6043

### Summary
This page explains how loyalty-service supports Project Atlas during Phase 4 Loyalty and Personalization. The phase goal is to connect loyalty, promotions, and segmentation. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: dual-write only during migration window. Evidence links to ATLAS-1028 and PR-6666.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-6029 and PR-8845.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-1887 and PR-11511.

### Risks and Runbook Notes
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0107: Support Playbook - auth-gateway - 2022-11
- Owner: Elena Petrova
- Updated: 2022-11-19
- Phase: Phase 4 Loyalty and Personalization
- Related Jira: ATLAS-6129

### Summary
This page explains how auth-gateway supports Project Atlas during Phase 4 Loyalty and Personalization. The phase goal is to connect loyalty, promotions, and segmentation. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-3997 and PR-9200.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-4240 and PR-5760.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-3443 and PR-11340.

### Risks and Runbook Notes
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0108: Release Checklist - search-recommendations - 2022-11
- Owner: Fatima Noor
- Updated: 2022-11-19
- Phase: Phase 4 Loyalty and Personalization
- Related Jira: ATLAS-1293

### Summary
This page explains how search-recommendations supports Project Atlas during Phase 4 Loyalty and Personalization. The phase goal is to connect loyalty, promotions, and segmentation. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-1544 and PR-5857.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-4576 and PR-7665.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-5493 and PR-11120.

### Risks and Runbook Notes
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0109: Support Playbook - analytics-pipeline - 2022-12
- Owner: Luca Moretti
- Updated: 2022-12-25
- Phase: Phase 4 Loyalty and Personalization
- Related Jira: ATLAS-2237

### Summary
This page explains how analytics-pipeline supports Project Atlas during Phase 4 Loyalty and Personalization. The phase goal is to connect loyalty, promotions, and segmentation. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-1026 and PR-8218.
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-3464 and PR-10058.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-3483 and PR-6156.

### Risks and Runbook Notes
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0110: Release Checklist - inventory-reservation - 2022-12
- Owner: Luca Moretti
- Updated: 2022-12-11
- Phase: Phase 4 Loyalty and Personalization
- Related Jira: ATLAS-4411

### Summary
This page explains how inventory-reservation supports Project Atlas during Phase 4 Loyalty and Personalization. The phase goal is to connect loyalty, promotions, and segmentation. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: support macro must be updated before launch. Evidence links to ATLAS-2857 and PR-7941.
- Decision: dual-write only during migration window. Evidence links to ATLAS-5181 and PR-8416.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-5325 and PR-8056.

### Risks and Runbook Notes
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0111: Postmortem - payment-orchestrator - 2023-01
- Owner: Kim Tan
- Updated: 2023-01-15
- Phase: Phase 5 Resilience and Observability
- Related Jira: ATLAS-5623

### Summary
This page explains how payment-orchestrator supports Project Atlas during Phase 5 Resilience and Observability. The phase goal is to burn down incidents, improve SLOs, add tracing. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: use feature flags for rollout. Evidence links to ATLAS-4125 and PR-11187.
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-3738 and PR-11117.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-1031 and PR-6698.

### Risks and Runbook Notes
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0112: Release Checklist - order-ledger - 2023-01
- Owner: Yara Haddad
- Updated: 2023-01-25
- Phase: Phase 5 Resilience and Observability
- Related Jira: ATLAS-5390

### Summary
This page explains how order-ledger supports Project Atlas during Phase 5 Resilience and Observability. The phase goal is to burn down incidents, improve SLOs, add tracing. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: dual-write only during migration window. Evidence links to ATLAS-1803 and PR-5193.
- Decision: use feature flags for rollout. Evidence links to ATLAS-3002 and PR-10401.
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-4874 and PR-8088.

### Risks and Runbook Notes
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0113: Release Checklist - notification-service - 2023-02
- Owner: Kim Tan
- Updated: 2023-02-11
- Phase: Phase 5 Resilience and Observability
- Related Jira: ATLAS-1712

### Summary
This page explains how notification-service supports Project Atlas during Phase 5 Resilience and Observability. The phase goal is to burn down incidents, improve SLOs, add tracing. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-5991 and PR-7126.
- Decision: use feature flags for rollout. Evidence links to ATLAS-4069 and PR-8841.
- Decision: support macro must be updated before launch. Evidence links to ATLAS-2039 and PR-6900.

### Risks and Runbook Notes
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0114: Onboarding - notification-service - 2023-02
- Owner: Yara Haddad
- Updated: 2023-02-15
- Phase: Phase 5 Resilience and Observability
- Related Jira: ATLAS-4801

### Summary
This page explains how notification-service supports Project Atlas during Phase 5 Resilience and Observability. The phase goal is to burn down incidents, improve SLOs, add tracing. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-2072 and PR-8115.
- Decision: dual-write only during migration window. Evidence links to ATLAS-1774 and PR-6241.
- Decision: dual-write only during migration window. Evidence links to ATLAS-2198 and PR-8641.

### Risks and Runbook Notes
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0115: Runbook - search-recommendations - 2023-03
- Owner: Ben Carter
- Updated: 2023-03-23
- Phase: Phase 5 Resilience and Observability
- Related Jira: ATLAS-1724

### Summary
This page explains how search-recommendations supports Project Atlas during Phase 5 Resilience and Observability. The phase goal is to burn down incidents, improve SLOs, add tracing. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: support macro must be updated before launch. Evidence links to ATLAS-5151 and PR-8514.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-4354 and PR-5596.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-2779 and PR-6485.

### Risks and Runbook Notes
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0116: Architecture - cart-service - 2023-03
- Owner: Victor Silva
- Updated: 2023-03-08
- Phase: Phase 5 Resilience and Observability
- Related Jira: ATLAS-5001

### Summary
This page explains how cart-service supports Project Atlas during Phase 5 Resilience and Observability. The phase goal is to burn down incidents, improve SLOs, add tracing. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-5732 and PR-9968.
- Decision: support macro must be updated before launch. Evidence links to ATLAS-2164 and PR-7608.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-4239 and PR-7734.

### Risks and Runbook Notes
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0117: Data Contract - pricing-engine - 2023-04
- Owner: Ben Carter
- Updated: 2023-04-09
- Phase: Phase 5 Resilience and Observability
- Related Jira: ATLAS-5265

### Summary
This page explains how pricing-engine supports Project Atlas during Phase 5 Resilience and Observability. The phase goal is to burn down incidents, improve SLOs, add tracing. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: use feature flags for rollout. Evidence links to ATLAS-4793 and PR-5571.
- Decision: use feature flags for rollout. Evidence links to ATLAS-3855 and PR-10143.
- Decision: support macro must be updated before launch. Evidence links to ATLAS-4442 and PR-8798.

### Risks and Runbook Notes
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0118: Architecture - tax-service - 2023-04
- Owner: Anika Sharma
- Updated: 2023-04-19
- Phase: Phase 5 Resilience and Observability
- Related Jira: ATLAS-5107

### Summary
This page explains how tax-service supports Project Atlas during Phase 5 Resilience and Observability. The phase goal is to burn down incidents, improve SLOs, add tracing. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-6085 and PR-10974.
- Decision: use feature flags for rollout. Evidence links to ATLAS-5102 and PR-5507.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-1595 and PR-5329.

### Risks and Runbook Notes
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0119: Support Playbook - analytics-pipeline - 2023-05
- Owner: Jon Bell
- Updated: 2023-05-13
- Phase: Phase 5 Resilience and Observability
- Related Jira: ATLAS-2574

### Summary
This page explains how analytics-pipeline supports Project Atlas during Phase 5 Resilience and Observability. The phase goal is to burn down incidents, improve SLOs, add tracing. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: use feature flags for rollout. Evidence links to ATLAS-4622 and PR-6320.
- Decision: use feature flags for rollout. Evidence links to ATLAS-4502 and PR-9888.
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-4532 and PR-9434.

### Risks and Runbook Notes
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0120: Data Contract - loyalty-service - 2023-05
- Owner: Ravi Patel
- Updated: 2023-05-09
- Phase: Phase 5 Resilience and Observability
- Related Jira: ATLAS-6156

### Summary
This page explains how loyalty-service supports Project Atlas during Phase 5 Resilience and Observability. The phase goal is to burn down incidents, improve SLOs, add tracing. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: dual-write only during migration window. Evidence links to ATLAS-1145 and PR-9473.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-3037 and PR-8784.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-2075 and PR-10130.

### Risks and Runbook Notes
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0121: Support Playbook - search-recommendations - 2023-06
- Owner: Aisha Khan
- Updated: 2023-06-24
- Phase: Phase 5 Resilience and Observability
- Related Jira: ATLAS-4817

### Summary
This page explains how search-recommendations supports Project Atlas during Phase 5 Resilience and Observability. The phase goal is to burn down incidents, improve SLOs, add tracing. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: support macro must be updated before launch. Evidence links to ATLAS-5730 and PR-6330.
- Decision: support macro must be updated before launch. Evidence links to ATLAS-1141 and PR-5815.
- Decision: support macro must be updated before launch. Evidence links to ATLAS-1810 and PR-11330.

### Risks and Runbook Notes
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0122: ADR - search-recommendations - 2023-06
- Owner: Elena Petrova
- Updated: 2023-06-13
- Phase: Phase 5 Resilience and Observability
- Related Jira: ATLAS-3268

### Summary
This page explains how search-recommendations supports Project Atlas during Phase 5 Resilience and Observability. The phase goal is to burn down incidents, improve SLOs, add tracing. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: dual-write only during migration window. Evidence links to ATLAS-5818 and PR-9509.
- Decision: support macro must be updated before launch. Evidence links to ATLAS-1973 and PR-8749.
- Decision: support macro must be updated before launch. Evidence links to ATLAS-3247 and PR-8859.

### Risks and Runbook Notes
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0123: Support Playbook - analytics-pipeline - 2023-07
- Owner: Anika Sharma
- Updated: 2023-07-14
- Phase: Phase 5 Resilience and Observability
- Related Jira: ATLAS-1584

### Summary
This page explains how analytics-pipeline supports Project Atlas during Phase 5 Resilience and Observability. The phase goal is to burn down incidents, improve SLOs, add tracing. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-3270 and PR-5307.
- Decision: support macro must be updated before launch. Evidence links to ATLAS-3431 and PR-8607.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-2323 and PR-10325.

### Risks and Runbook Notes
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0124: Release Checklist - cart-service - 2023-07
- Owner: Noah Evans
- Updated: 2023-07-09
- Phase: Phase 5 Resilience and Observability
- Related Jira: ATLAS-4387

### Summary
This page explains how cart-service supports Project Atlas during Phase 5 Resilience and Observability. The phase goal is to burn down incidents, improve SLOs, add tracing. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-1333 and PR-9977.
- Decision: dual-write only during migration window. Evidence links to ATLAS-3731 and PR-11087.
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-1532 and PR-5314.

### Risks and Runbook Notes
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0125: Architecture - inventory-reservation - 2023-08
- Owner: Anika Sharma
- Updated: 2023-08-24
- Phase: Phase 5 Resilience and Observability
- Related Jira: ATLAS-2619

### Summary
This page explains how inventory-reservation supports Project Atlas during Phase 5 Resilience and Observability. The phase goal is to burn down incidents, improve SLOs, add tracing. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: support macro must be updated before launch. Evidence links to ATLAS-6007 and PR-11964.
- Decision: support macro must be updated before launch. Evidence links to ATLAS-4671 and PR-7846.
- Decision: dual-write only during migration window. Evidence links to ATLAS-1890 and PR-9862.

### Risks and Runbook Notes
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0126: Onboarding - notification-service - 2023-08
- Owner: Dmitri Volkov
- Updated: 2023-08-02
- Phase: Phase 5 Resilience and Observability
- Related Jira: ATLAS-1729

### Summary
This page explains how notification-service supports Project Atlas during Phase 5 Resilience and Observability. The phase goal is to burn down incidents, improve SLOs, add tracing. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-2733 and PR-8319.
- Decision: use feature flags for rollout. Evidence links to ATLAS-2736 and PR-8378.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-5873 and PR-8828.

### Risks and Runbook Notes
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0127: Postmortem - cart-service - 2023-09
- Owner: Elena Petrova
- Updated: 2023-09-15
- Phase: Phase 5 Resilience and Observability
- Related Jira: ATLAS-1998

### Summary
This page explains how cart-service supports Project Atlas during Phase 5 Resilience and Observability. The phase goal is to burn down incidents, improve SLOs, add tracing. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: use feature flags for rollout. Evidence links to ATLAS-4005 and PR-6369.
- Decision: support macro must be updated before launch. Evidence links to ATLAS-2132 and PR-5450.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-2752 and PR-10444.

### Risks and Runbook Notes
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0128: Data Contract - analytics-pipeline - 2023-09
- Owner: Harper Lee
- Updated: 2023-09-12
- Phase: Phase 5 Resilience and Observability
- Related Jira: ATLAS-5788

### Summary
This page explains how analytics-pipeline supports Project Atlas during Phase 5 Resilience and Observability. The phase goal is to burn down incidents, improve SLOs, add tracing. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: support macro must be updated before launch. Evidence links to ATLAS-1034 and PR-6191.
- Decision: support macro must be updated before launch. Evidence links to ATLAS-3911 and PR-6947.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-5845 and PR-5373.

### Risks and Runbook Notes
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0129: Architecture - notification-service - 2023-10
- Owner: Noah Evans
- Updated: 2023-10-22
- Phase: Phase 5 Resilience and Observability
- Related Jira: ATLAS-5334

### Summary
This page explains how notification-service supports Project Atlas during Phase 5 Resilience and Observability. The phase goal is to burn down incidents, improve SLOs, add tracing. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-4761 and PR-5231.
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-4530 and PR-11439.
- Decision: support macro must be updated before launch. Evidence links to ATLAS-1712 and PR-6665.

### Risks and Runbook Notes
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0130: Architecture - notification-service - 2023-10
- Owner: Harper Lee
- Updated: 2023-10-11
- Phase: Phase 5 Resilience and Observability
- Related Jira: ATLAS-5933

### Summary
This page explains how notification-service supports Project Atlas during Phase 5 Resilience and Observability. The phase goal is to burn down incidents, improve SLOs, add tracing. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-5340 and PR-6570.
- Decision: support macro must be updated before launch. Evidence links to ATLAS-3599 and PR-5311.
- Decision: use feature flags for rollout. Evidence links to ATLAS-4075 and PR-7306.

### Risks and Runbook Notes
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0131: Onboarding - pricing-engine - 2023-11
- Owner: Ben Carter
- Updated: 2023-11-14
- Phase: Phase 5 Resilience and Observability
- Related Jira: ATLAS-1191

### Summary
This page explains how pricing-engine supports Project Atlas during Phase 5 Resilience and Observability. The phase goal is to burn down incidents, improve SLOs, add tracing. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-1465 and PR-6717.
- Decision: support macro must be updated before launch. Evidence links to ATLAS-4152 and PR-6734.
- Decision: support macro must be updated before launch. Evidence links to ATLAS-2086 and PR-5020.

### Risks and Runbook Notes
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0132: Postmortem - checkout-api - 2023-11
- Owner: Kim Tan
- Updated: 2023-11-05
- Phase: Phase 5 Resilience and Observability
- Related Jira: ATLAS-2288

### Summary
This page explains how checkout-api supports Project Atlas during Phase 5 Resilience and Observability. The phase goal is to burn down incidents, improve SLOs, add tracing. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: use feature flags for rollout. Evidence links to ATLAS-4459 and PR-8374.
- Decision: dual-write only during migration window. Evidence links to ATLAS-3958 and PR-7282.
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-4397 and PR-9216.

### Risks and Runbook Notes
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0133: Data Contract - auth-gateway - 2023-12
- Owner: Kim Tan
- Updated: 2023-12-18
- Phase: Phase 5 Resilience and Observability
- Related Jira: ATLAS-2031

### Summary
This page explains how auth-gateway supports Project Atlas during Phase 5 Resilience and Observability. The phase goal is to burn down incidents, improve SLOs, add tracing. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: use feature flags for rollout. Evidence links to ATLAS-5236 and PR-5139.
- Decision: support macro must be updated before launch. Evidence links to ATLAS-4031 and PR-9614.
- Decision: use feature flags for rollout. Evidence links to ATLAS-2579 and PR-5373.

### Risks and Runbook Notes
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0134: Data Contract - payment-orchestrator - 2023-12
- Owner: Kim Tan
- Updated: 2023-12-10
- Phase: Phase 5 Resilience and Observability
- Related Jira: ATLAS-2587

### Summary
This page explains how payment-orchestrator supports Project Atlas during Phase 5 Resilience and Observability. The phase goal is to burn down incidents, improve SLOs, add tracing. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-4032 and PR-9951.
- Decision: use feature flags for rollout. Evidence links to ATLAS-4212 and PR-7927.
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-1372 and PR-11904.

### Risks and Runbook Notes
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0135: Release Checklist - notification-service - 2024-01
- Owner: Yara Haddad
- Updated: 2024-01-23
- Phase: Phase 6 Order Orchestration
- Related Jira: ATLAS-5920

### Summary
This page explains how notification-service supports Project Atlas during Phase 6 Order Orchestration. The phase goal is to orchestrate inventory reservation and async order ledger. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-5117 and PR-7307.
- Decision: support macro must be updated before launch. Evidence links to ATLAS-2906 and PR-9851.
- Decision: dual-write only during migration window. Evidence links to ATLAS-4642 and PR-7443.

### Risks and Runbook Notes
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0136: Postmortem - checkout-api - 2024-01
- Owner: Elena Petrova
- Updated: 2024-01-13
- Phase: Phase 6 Order Orchestration
- Related Jira: ATLAS-4774

### Summary
This page explains how checkout-api supports Project Atlas during Phase 6 Order Orchestration. The phase goal is to orchestrate inventory reservation and async order ledger. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-5997 and PR-12326.
- Decision: dual-write only during migration window. Evidence links to ATLAS-5425 and PR-7803.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-1589 and PR-9965.

### Risks and Runbook Notes
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0137: ADR - order-ledger - 2024-02
- Owner: Ben Carter
- Updated: 2024-02-03
- Phase: Phase 6 Order Orchestration
- Related Jira: ATLAS-2866

### Summary
This page explains how order-ledger supports Project Atlas during Phase 6 Order Orchestration. The phase goal is to orchestrate inventory reservation and async order ledger. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-4332 and PR-5067.
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-4029 and PR-6263.
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-5079 and PR-11331.

### Risks and Runbook Notes
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0138: Onboarding - tax-service - 2024-02
- Owner: Theo Martin
- Updated: 2024-02-12
- Phase: Phase 6 Order Orchestration
- Related Jira: ATLAS-6155

### Summary
This page explains how tax-service supports Project Atlas during Phase 6 Order Orchestration. The phase goal is to orchestrate inventory reservation and async order ledger. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-3909 and PR-5403.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-5079 and PR-9664.
- Decision: use feature flags for rollout. Evidence links to ATLAS-4434 and PR-8965.

### Risks and Runbook Notes
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0139: Postmortem - auth-gateway - 2024-03
- Owner: Yara Haddad
- Updated: 2024-03-03
- Phase: Phase 6 Order Orchestration
- Related Jira: ATLAS-1877

### Summary
This page explains how auth-gateway supports Project Atlas during Phase 6 Order Orchestration. The phase goal is to orchestrate inventory reservation and async order ledger. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-3081 and PR-7239.
- Decision: support macro must be updated before launch. Evidence links to ATLAS-4624 and PR-6077.
- Decision: support macro must be updated before launch. Evidence links to ATLAS-5773 and PR-8651.

### Risks and Runbook Notes
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0140: Release Checklist - analytics-pipeline - 2024-03
- Owner: Victor Silva
- Updated: 2024-03-13
- Phase: Phase 6 Order Orchestration
- Related Jira: ATLAS-2680

### Summary
This page explains how analytics-pipeline supports Project Atlas during Phase 6 Order Orchestration. The phase goal is to orchestrate inventory reservation and async order ledger. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: support macro must be updated before launch. Evidence links to ATLAS-3965 and PR-5103.
- Decision: dual-write only during migration window. Evidence links to ATLAS-3623 and PR-11207.
- Decision: support macro must be updated before launch. Evidence links to ATLAS-3738 and PR-12207.

### Risks and Runbook Notes
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0141: ADR - loyalty-service - 2024-04
- Owner: Maya Chen
- Updated: 2024-04-16
- Phase: Phase 6 Order Orchestration
- Related Jira: ATLAS-1693

### Summary
This page explains how loyalty-service supports Project Atlas during Phase 6 Order Orchestration. The phase goal is to orchestrate inventory reservation and async order ledger. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: support macro must be updated before launch. Evidence links to ATLAS-4683 and PR-9251.
- Decision: dual-write only during migration window. Evidence links to ATLAS-4982 and PR-9640.
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-4099 and PR-5880.

### Risks and Runbook Notes
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0142: Release Checklist - pricing-engine - 2024-04
- Owner: Maya Chen
- Updated: 2024-04-14
- Phase: Phase 6 Order Orchestration
- Related Jira: ATLAS-3162

### Summary
This page explains how pricing-engine supports Project Atlas during Phase 6 Order Orchestration. The phase goal is to orchestrate inventory reservation and async order ledger. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-1354 and PR-9558.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-2474 and PR-7648.
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-1861 and PR-5024.

### Risks and Runbook Notes
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0143: Runbook - payment-orchestrator - 2024-05
- Owner: Jon Bell
- Updated: 2024-05-26
- Phase: Phase 6 Order Orchestration
- Related Jira: ATLAS-5443

### Summary
This page explains how payment-orchestrator supports Project Atlas during Phase 6 Order Orchestration. The phase goal is to orchestrate inventory reservation and async order ledger. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-5918 and PR-5428.
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-3037 and PR-9161.
- Decision: support macro must be updated before launch. Evidence links to ATLAS-3577 and PR-7635.

### Risks and Runbook Notes
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0144: Postmortem - cart-service - 2024-05
- Owner: Sara Novak
- Updated: 2024-05-06
- Phase: Phase 6 Order Orchestration
- Related Jira: ATLAS-5520

### Summary
This page explains how cart-service supports Project Atlas during Phase 6 Order Orchestration. The phase goal is to orchestrate inventory reservation and async order ledger. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: use feature flags for rollout. Evidence links to ATLAS-1903 and PR-5717.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-4031 and PR-8515.
- Decision: support macro must be updated before launch. Evidence links to ATLAS-4612 and PR-9976.

### Risks and Runbook Notes
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0145: Data Contract - search-recommendations - 2024-06
- Owner: Fatima Noor
- Updated: 2024-06-11
- Phase: Phase 6 Order Orchestration
- Related Jira: ATLAS-2800

### Summary
This page explains how search-recommendations supports Project Atlas during Phase 6 Order Orchestration. The phase goal is to orchestrate inventory reservation and async order ledger. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: use feature flags for rollout. Evidence links to ATLAS-5626 and PR-5993.
- Decision: support macro must be updated before launch. Evidence links to ATLAS-5511 and PR-12054.
- Decision: support macro must be updated before launch. Evidence links to ATLAS-3954 and PR-8340.

### Risks and Runbook Notes
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0146: Onboarding - checkout-api - 2024-06
- Owner: Iris Wang
- Updated: 2024-06-21
- Phase: Phase 6 Order Orchestration
- Related Jira: ATLAS-3578

### Summary
This page explains how checkout-api supports Project Atlas during Phase 6 Order Orchestration. The phase goal is to orchestrate inventory reservation and async order ledger. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: support macro must be updated before launch. Evidence links to ATLAS-1486 and PR-11862.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-2367 and PR-9558.
- Decision: dual-write only during migration window. Evidence links to ATLAS-3925 and PR-7150.

### Risks and Runbook Notes
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0147: Postmortem - tax-service - 2024-07
- Owner: Grace Kim
- Updated: 2024-07-08
- Phase: Phase 6 Order Orchestration
- Related Jira: ATLAS-4583

### Summary
This page explains how tax-service supports Project Atlas during Phase 6 Order Orchestration. The phase goal is to orchestrate inventory reservation and async order ledger. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: use feature flags for rollout. Evidence links to ATLAS-2869 and PR-9383.
- Decision: dual-write only during migration window. Evidence links to ATLAS-5494 and PR-10528.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-1186 and PR-7812.

### Risks and Runbook Notes
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0148: Data Contract - search-recommendations - 2024-07
- Owner: Maya Chen
- Updated: 2024-07-21
- Phase: Phase 6 Order Orchestration
- Related Jira: ATLAS-3904

### Summary
This page explains how search-recommendations supports Project Atlas during Phase 6 Order Orchestration. The phase goal is to orchestrate inventory reservation and async order ledger. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-5436 and PR-11055.
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-1489 and PR-8705.
- Decision: dual-write only during migration window. Evidence links to ATLAS-5722 and PR-9320.

### Risks and Runbook Notes
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0149: Postmortem - checkout-api - 2024-08
- Owner: Luca Moretti
- Updated: 2024-08-20
- Phase: Phase 6 Order Orchestration
- Related Jira: ATLAS-3026

### Summary
This page explains how checkout-api supports Project Atlas during Phase 6 Order Orchestration. The phase goal is to orchestrate inventory reservation and async order ledger. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: dual-write only during migration window. Evidence links to ATLAS-5913 and PR-12205.
- Decision: dual-write only during migration window. Evidence links to ATLAS-2762 and PR-5912.
- Decision: use feature flags for rollout. Evidence links to ATLAS-5014 and PR-11428.

### Risks and Runbook Notes
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0150: Onboarding - analytics-pipeline - 2024-08
- Owner: Grace Kim
- Updated: 2024-08-18
- Phase: Phase 6 Order Orchestration
- Related Jira: ATLAS-5183

### Summary
This page explains how analytics-pipeline supports Project Atlas during Phase 6 Order Orchestration. The phase goal is to orchestrate inventory reservation and async order ledger. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-5124 and PR-11907.
- Decision: dual-write only during migration window. Evidence links to ATLAS-2570 and PR-7487.
- Decision: support macro must be updated before launch. Evidence links to ATLAS-1762 and PR-5885.

### Risks and Runbook Notes
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0151: Architecture - analytics-pipeline - 2024-09
- Owner: Nora Singh
- Updated: 2024-09-16
- Phase: Phase 6 Order Orchestration
- Related Jira: ATLAS-5348

### Summary
This page explains how analytics-pipeline supports Project Atlas during Phase 6 Order Orchestration. The phase goal is to orchestrate inventory reservation and async order ledger. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: dual-write only during migration window. Evidence links to ATLAS-1056 and PR-5510.
- Decision: use feature flags for rollout. Evidence links to ATLAS-2054 and PR-9322.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-5977 and PR-7977.

### Risks and Runbook Notes
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0152: Release Checklist - notification-service - 2024-09
- Owner: Nora Singh
- Updated: 2024-09-17
- Phase: Phase 6 Order Orchestration
- Related Jira: ATLAS-4148

### Summary
This page explains how notification-service supports Project Atlas during Phase 6 Order Orchestration. The phase goal is to orchestrate inventory reservation and async order ledger. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: use feature flags for rollout. Evidence links to ATLAS-2661 and PR-9891.
- Decision: use feature flags for rollout. Evidence links to ATLAS-5946 and PR-11872.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-5445 and PR-10341.

### Risks and Runbook Notes
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0153: Data Contract - notification-service - 2024-10
- Owner: Theo Martin
- Updated: 2024-10-21
- Phase: Phase 6 Order Orchestration
- Related Jira: ATLAS-1883

### Summary
This page explains how notification-service supports Project Atlas during Phase 6 Order Orchestration. The phase goal is to orchestrate inventory reservation and async order ledger. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-4307 and PR-7300.
- Decision: support macro must be updated before launch. Evidence links to ATLAS-1563 and PR-8813.
- Decision: support macro must be updated before launch. Evidence links to ATLAS-1998 and PR-6834.

### Risks and Runbook Notes
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0154: Runbook - checkout-api - 2024-10
- Owner: Elena Petrova
- Updated: 2024-10-03
- Phase: Phase 6 Order Orchestration
- Related Jira: ATLAS-2848

### Summary
This page explains how checkout-api supports Project Atlas during Phase 6 Order Orchestration. The phase goal is to orchestrate inventory reservation and async order ledger. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: support macro must be updated before launch. Evidence links to ATLAS-2384 and PR-6470.
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-1078 and PR-6176.
- Decision: use feature flags for rollout. Evidence links to ATLAS-3878 and PR-5964.

### Risks and Runbook Notes
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0155: Runbook - checkout-api - 2024-11
- Owner: Noah Evans
- Updated: 2024-11-16
- Phase: Phase 6 Order Orchestration
- Related Jira: ATLAS-1484

### Summary
This page explains how checkout-api supports Project Atlas during Phase 6 Order Orchestration. The phase goal is to orchestrate inventory reservation and async order ledger. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: support macro must be updated before launch. Evidence links to ATLAS-1632 and PR-8873.
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-5069 and PR-7870.
- Decision: dual-write only during migration window. Evidence links to ATLAS-5840 and PR-7047.

### Risks and Runbook Notes
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0156: Runbook - loyalty-service - 2024-11
- Owner: Fatima Noor
- Updated: 2024-11-05
- Phase: Phase 6 Order Orchestration
- Related Jira: ATLAS-6109

### Summary
This page explains how loyalty-service supports Project Atlas during Phase 6 Order Orchestration. The phase goal is to orchestrate inventory reservation and async order ledger. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: support macro must be updated before launch. Evidence links to ATLAS-1926 and PR-7463.
- Decision: support macro must be updated before launch. Evidence links to ATLAS-2472 and PR-9470.
- Decision: dual-write only during migration window. Evidence links to ATLAS-2188 and PR-7164.

### Risks and Runbook Notes
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0157: Postmortem - cart-service - 2024-12
- Owner: Samir Rao
- Updated: 2024-12-11
- Phase: Phase 6 Order Orchestration
- Related Jira: ATLAS-1722

### Summary
This page explains how cart-service supports Project Atlas during Phase 6 Order Orchestration. The phase goal is to orchestrate inventory reservation and async order ledger. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-3141 and PR-10313.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-1687 and PR-6274.
- Decision: use feature flags for rollout. Evidence links to ATLAS-1905 and PR-11102.

### Risks and Runbook Notes
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0158: Postmortem - analytics-pipeline - 2024-12
- Owner: Ben Carter
- Updated: 2024-12-16
- Phase: Phase 6 Order Orchestration
- Related Jira: ATLAS-3854

### Summary
This page explains how analytics-pipeline supports Project Atlas during Phase 6 Order Orchestration. The phase goal is to orchestrate inventory reservation and async order ledger. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: dual-write only during migration window. Evidence links to ATLAS-2274 and PR-6706.
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-1174 and PR-12512.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-3511 and PR-6355.

### Risks and Runbook Notes
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0159: ADR - search-recommendations - 2025-01
- Owner: Fatima Noor
- Updated: 2025-01-21
- Phase: Phase 7 Checkout Cutover
- Related Jira: ATLAS-3883

### Summary
This page explains how search-recommendations supports Project Atlas during Phase 7 Checkout Cutover. The phase goal is to route traffic to Atlas and deprecate monolith paths. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-3020 and PR-11893.
- Decision: support macro must be updated before launch. Evidence links to ATLAS-1361 and PR-6578.
- Decision: dual-write only during migration window. Evidence links to ATLAS-3511 and PR-5991.

### Risks and Runbook Notes
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0160: ADR - search-recommendations - 2025-01
- Owner: Nora Singh
- Updated: 2025-01-22
- Phase: Phase 7 Checkout Cutover
- Related Jira: ATLAS-5683

### Summary
This page explains how search-recommendations supports Project Atlas during Phase 7 Checkout Cutover. The phase goal is to route traffic to Atlas and deprecate monolith paths. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: dual-write only during migration window. Evidence links to ATLAS-2463 and PR-9176.
- Decision: dual-write only during migration window. Evidence links to ATLAS-4679 and PR-8831.
- Decision: support macro must be updated before launch. Evidence links to ATLAS-2461 and PR-9379.

### Risks and Runbook Notes
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0161: Onboarding - cart-service - 2025-02
- Owner: Theo Martin
- Updated: 2025-02-11
- Phase: Phase 7 Checkout Cutover
- Related Jira: ATLAS-2644

### Summary
This page explains how cart-service supports Project Atlas during Phase 7 Checkout Cutover. The phase goal is to route traffic to Atlas and deprecate monolith paths. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: use feature flags for rollout. Evidence links to ATLAS-3361 and PR-8979.
- Decision: use feature flags for rollout. Evidence links to ATLAS-4188 and PR-10015.
- Decision: use feature flags for rollout. Evidence links to ATLAS-4616 and PR-10840.

### Risks and Runbook Notes
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0162: Release Checklist - tax-service - 2025-02
- Owner: Kim Tan
- Updated: 2025-02-07
- Phase: Phase 7 Checkout Cutover
- Related Jira: ATLAS-3635

### Summary
This page explains how tax-service supports Project Atlas during Phase 7 Checkout Cutover. The phase goal is to route traffic to Atlas and deprecate monolith paths. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: support macro must be updated before launch. Evidence links to ATLAS-5645 and PR-5510.
- Decision: use feature flags for rollout. Evidence links to ATLAS-5815 and PR-9479.
- Decision: dual-write only during migration window. Evidence links to ATLAS-2910 and PR-5032.

### Risks and Runbook Notes
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0163: ADR - payment-orchestrator - 2025-03
- Owner: Iris Wang
- Updated: 2025-03-09
- Phase: Phase 7 Checkout Cutover
- Related Jira: ATLAS-6087

### Summary
This page explains how payment-orchestrator supports Project Atlas during Phase 7 Checkout Cutover. The phase goal is to route traffic to Atlas and deprecate monolith paths. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: use feature flags for rollout. Evidence links to ATLAS-4736 and PR-9114.
- Decision: use feature flags for rollout. Evidence links to ATLAS-4774 and PR-5674.
- Decision: support macro must be updated before launch. Evidence links to ATLAS-3505 and PR-6653.

### Risks and Runbook Notes
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0164: Runbook - notification-service - 2025-03
- Owner: Anika Sharma
- Updated: 2025-03-17
- Phase: Phase 7 Checkout Cutover
- Related Jira: ATLAS-1854

### Summary
This page explains how notification-service supports Project Atlas during Phase 7 Checkout Cutover. The phase goal is to route traffic to Atlas and deprecate monolith paths. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-3215 and PR-9775.
- Decision: support macro must be updated before launch. Evidence links to ATLAS-1745 and PR-11748.
- Decision: use feature flags for rollout. Evidence links to ATLAS-3487 and PR-5604.

### Risks and Runbook Notes
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0165: Data Contract - checkout-api - 2025-04
- Owner: Theo Martin
- Updated: 2025-04-09
- Phase: Phase 7 Checkout Cutover
- Related Jira: ATLAS-4789

### Summary
This page explains how checkout-api supports Project Atlas during Phase 7 Checkout Cutover. The phase goal is to route traffic to Atlas and deprecate monolith paths. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-5489 and PR-7058.
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-5047 and PR-5893.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-1751 and PR-11341.

### Risks and Runbook Notes
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0166: Data Contract - loyalty-service - 2025-04
- Owner: Owen Brooks
- Updated: 2025-04-08
- Phase: Phase 7 Checkout Cutover
- Related Jira: ATLAS-5441

### Summary
This page explains how loyalty-service supports Project Atlas during Phase 7 Checkout Cutover. The phase goal is to route traffic to Atlas and deprecate monolith paths. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: dual-write only during migration window. Evidence links to ATLAS-2354 and PR-7311.
- Decision: use feature flags for rollout. Evidence links to ATLAS-3996 and PR-5462.
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-4727 and PR-8003.

### Risks and Runbook Notes
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0167: Data Contract - auth-gateway - 2025-05
- Owner: Owen Brooks
- Updated: 2025-05-14
- Phase: Phase 7 Checkout Cutover
- Related Jira: ATLAS-1025

### Summary
This page explains how auth-gateway supports Project Atlas during Phase 7 Checkout Cutover. The phase goal is to route traffic to Atlas and deprecate monolith paths. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: use feature flags for rollout. Evidence links to ATLAS-2711 and PR-6116.
- Decision: support macro must be updated before launch. Evidence links to ATLAS-3682 and PR-8915.
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-4086 and PR-7200.

### Risks and Runbook Notes
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0168: Release Checklist - tax-service - 2025-05
- Owner: Noah Evans
- Updated: 2025-05-25
- Phase: Phase 7 Checkout Cutover
- Related Jira: ATLAS-5351

### Summary
This page explains how tax-service supports Project Atlas during Phase 7 Checkout Cutover. The phase goal is to route traffic to Atlas and deprecate monolith paths. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: use feature flags for rollout. Evidence links to ATLAS-5466 and PR-5463.
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-4815 and PR-8552.
- Decision: support macro must be updated before launch. Evidence links to ATLAS-5855 and PR-10974.

### Risks and Runbook Notes
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0169: Data Contract - search-recommendations - 2025-06
- Owner: Aisha Khan
- Updated: 2025-06-02
- Phase: Phase 7 Checkout Cutover
- Related Jira: ATLAS-4229

### Summary
This page explains how search-recommendations supports Project Atlas during Phase 7 Checkout Cutover. The phase goal is to route traffic to Atlas and deprecate monolith paths. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: support macro must be updated before launch. Evidence links to ATLAS-3903 and PR-5974.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-1580 and PR-5962.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-1805 and PR-5307.

### Risks and Runbook Notes
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0170: Postmortem - order-ledger - 2025-06
- Owner: Noah Evans
- Updated: 2025-06-16
- Phase: Phase 7 Checkout Cutover
- Related Jira: ATLAS-5407

### Summary
This page explains how order-ledger supports Project Atlas during Phase 7 Checkout Cutover. The phase goal is to route traffic to Atlas and deprecate monolith paths. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: use feature flags for rollout. Evidence links to ATLAS-1341 and PR-10871.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-4007 and PR-7910.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-5025 and PR-11782.

### Risks and Runbook Notes
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0171: Support Playbook - notification-service - 2025-07
- Owner: Luca Moretti
- Updated: 2025-07-06
- Phase: Phase 7 Checkout Cutover
- Related Jira: ATLAS-4810

### Summary
This page explains how notification-service supports Project Atlas during Phase 7 Checkout Cutover. The phase goal is to route traffic to Atlas and deprecate monolith paths. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: support macro must be updated before launch. Evidence links to ATLAS-5390 and PR-9756.
- Decision: support macro must be updated before launch. Evidence links to ATLAS-4784 and PR-6794.
- Decision: dual-write only during migration window. Evidence links to ATLAS-4215 and PR-6241.

### Risks and Runbook Notes
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0172: Release Checklist - payment-orchestrator - 2025-07
- Owner: Elena Petrova
- Updated: 2025-07-20
- Phase: Phase 7 Checkout Cutover
- Related Jira: ATLAS-4250

### Summary
This page explains how payment-orchestrator supports Project Atlas during Phase 7 Checkout Cutover. The phase goal is to route traffic to Atlas and deprecate monolith paths. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-6145 and PR-5366.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-6041 and PR-11957.
- Decision: use feature flags for rollout. Evidence links to ATLAS-5995 and PR-9530.

### Risks and Runbook Notes
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0173: Runbook - loyalty-service - 2025-08
- Owner: Yara Haddad
- Updated: 2025-08-03
- Phase: Phase 7 Checkout Cutover
- Related Jira: ATLAS-4532

### Summary
This page explains how loyalty-service supports Project Atlas during Phase 7 Checkout Cutover. The phase goal is to route traffic to Atlas and deprecate monolith paths. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-3194 and PR-8494.
- Decision: dual-write only during migration window. Evidence links to ATLAS-1002 and PR-7157.
- Decision: use feature flags for rollout. Evidence links to ATLAS-2028 and PR-10486.

### Risks and Runbook Notes
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0174: Onboarding - tax-service - 2025-08
- Owner: Iris Wang
- Updated: 2025-08-24
- Phase: Phase 7 Checkout Cutover
- Related Jira: ATLAS-3400

### Summary
This page explains how tax-service supports Project Atlas during Phase 7 Checkout Cutover. The phase goal is to route traffic to Atlas and deprecate monolith paths. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: support macro must be updated before launch. Evidence links to ATLAS-4447 and PR-7295.
- Decision: use feature flags for rollout. Evidence links to ATLAS-4419 and PR-12094.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-3916 and PR-5330.

### Risks and Runbook Notes
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0175: Support Playbook - pricing-engine - 2025-09
- Owner: Nora Singh
- Updated: 2025-09-22
- Phase: Phase 7 Checkout Cutover
- Related Jira: ATLAS-1464

### Summary
This page explains how pricing-engine supports Project Atlas during Phase 7 Checkout Cutover. The phase goal is to route traffic to Atlas and deprecate monolith paths. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: use feature flags for rollout. Evidence links to ATLAS-4961 and PR-9634.
- Decision: dual-write only during migration window. Evidence links to ATLAS-5565 and PR-10096.
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-3008 and PR-9216.

### Risks and Runbook Notes
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0176: ADR - pricing-engine - 2025-09
- Owner: Noah Evans
- Updated: 2025-09-11
- Phase: Phase 7 Checkout Cutover
- Related Jira: ATLAS-5899

### Summary
This page explains how pricing-engine supports Project Atlas during Phase 7 Checkout Cutover. The phase goal is to route traffic to Atlas and deprecate monolith paths. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-1535 and PR-6047.
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-4240 and PR-6506.
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-3191 and PR-11757.

### Risks and Runbook Notes
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0177: Release Checklist - analytics-pipeline - 2025-10
- Owner: Maya Chen
- Updated: 2025-10-18
- Phase: Phase 7 Checkout Cutover
- Related Jira: ATLAS-4229

### Summary
This page explains how analytics-pipeline supports Project Atlas during Phase 7 Checkout Cutover. The phase goal is to route traffic to Atlas and deprecate monolith paths. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: use feature flags for rollout. Evidence links to ATLAS-2805 and PR-6609.
- Decision: use feature flags for rollout. Evidence links to ATLAS-4920 and PR-10102.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-1883 and PR-10872.

### Risks and Runbook Notes
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0178: Architecture - checkout-api - 2025-10
- Owner: Nora Singh
- Updated: 2025-10-09
- Phase: Phase 7 Checkout Cutover
- Related Jira: ATLAS-3244

### Summary
This page explains how checkout-api supports Project Atlas during Phase 7 Checkout Cutover. The phase goal is to route traffic to Atlas and deprecate monolith paths. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-5223 and PR-5443.
- Decision: dual-write only during migration window. Evidence links to ATLAS-6190 and PR-6603.
- Decision: support macro must be updated before launch. Evidence links to ATLAS-5024 and PR-10367.

### Risks and Runbook Notes
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0179: Release Checklist - loyalty-service - 2025-11
- Owner: Owen Brooks
- Updated: 2025-11-20
- Phase: Phase 7 Checkout Cutover
- Related Jira: ATLAS-4304

### Summary
This page explains how loyalty-service supports Project Atlas during Phase 7 Checkout Cutover. The phase goal is to route traffic to Atlas and deprecate monolith paths. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-5605 and PR-10171.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-3165 and PR-12182.
- Decision: dual-write only during migration window. Evidence links to ATLAS-2510 and PR-9263.

### Risks and Runbook Notes
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0180: Architecture - auth-gateway - 2025-11
- Owner: Samir Rao
- Updated: 2025-11-20
- Phase: Phase 7 Checkout Cutover
- Related Jira: ATLAS-3962

### Summary
This page explains how auth-gateway supports Project Atlas during Phase 7 Checkout Cutover. The phase goal is to route traffic to Atlas and deprecate monolith paths. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-1054 and PR-5644.
- Decision: dual-write only during migration window. Evidence links to ATLAS-5337 and PR-5760.
- Decision: support macro must be updated before launch. Evidence links to ATLAS-1171 and PR-10623.

### Risks and Runbook Notes
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0181: Architecture - auth-gateway - 2025-12
- Owner: Fatima Noor
- Updated: 2025-12-14
- Phase: Phase 7 Checkout Cutover
- Related Jira: ATLAS-1909

### Summary
This page explains how auth-gateway supports Project Atlas during Phase 7 Checkout Cutover. The phase goal is to route traffic to Atlas and deprecate monolith paths. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: use feature flags for rollout. Evidence links to ATLAS-3028 and PR-7577.
- Decision: support macro must be updated before launch. Evidence links to ATLAS-2961 and PR-10526.
- Decision: use feature flags for rollout. Evidence links to ATLAS-1579 and PR-11395.

### Risks and Runbook Notes
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0182: Support Playbook - notification-service - 2025-12
- Owner: Samir Rao
- Updated: 2025-12-12
- Phase: Phase 7 Checkout Cutover
- Related Jira: ATLAS-5866

### Summary
This page explains how notification-service supports Project Atlas during Phase 7 Checkout Cutover. The phase goal is to route traffic to Atlas and deprecate monolith paths. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: use feature flags for rollout. Evidence links to ATLAS-3208 and PR-5930.
- Decision: use feature flags for rollout. Evidence links to ATLAS-2153 and PR-8738.
- Decision: support macro must be updated before launch. Evidence links to ATLAS-3123 and PR-7560.

### Risks and Runbook Notes
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0183: Onboarding - tax-service - 2026-01
- Owner: Theo Martin
- Updated: 2026-01-26
- Phase: Phase 8 Scale and Handoff
- Related Jira: ATLAS-5509

### Summary
This page explains how tax-service supports Project Atlas during Phase 8 Scale and Handoff. The phase goal is to prepare KT, reduce toil, close migration gaps. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-2745 and PR-6722.
- Decision: use feature flags for rollout. Evidence links to ATLAS-1286 and PR-9955.
- Decision: dual-write only during migration window. Evidence links to ATLAS-2995 and PR-10850.

### Risks and Runbook Notes
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0184: ADR - checkout-api - 2026-01
- Owner: Luca Moretti
- Updated: 2026-01-15
- Phase: Phase 8 Scale and Handoff
- Related Jira: ATLAS-3839

### Summary
This page explains how checkout-api supports Project Atlas during Phase 8 Scale and Handoff. The phase goal is to prepare KT, reduce toil, close migration gaps. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: support macro must be updated before launch. Evidence links to ATLAS-3611 and PR-8308.
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-5066 and PR-5950.
- Decision: use feature flags for rollout. Evidence links to ATLAS-4176 and PR-8008.

### Risks and Runbook Notes
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0185: Postmortem - auth-gateway - 2026-02
- Owner: Luca Moretti
- Updated: 2026-02-05
- Phase: Phase 8 Scale and Handoff
- Related Jira: ATLAS-2702

### Summary
This page explains how auth-gateway supports Project Atlas during Phase 8 Scale and Handoff. The phase goal is to prepare KT, reduce toil, close migration gaps. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: support macro must be updated before launch. Evidence links to ATLAS-2201 and PR-10286.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-4485 and PR-8241.
- Decision: dual-write only during migration window. Evidence links to ATLAS-1705 and PR-6422.

### Risks and Runbook Notes
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0186: Onboarding - tax-service - 2026-02
- Owner: Samir Rao
- Updated: 2026-02-23
- Phase: Phase 8 Scale and Handoff
- Related Jira: ATLAS-5003

### Summary
This page explains how tax-service supports Project Atlas during Phase 8 Scale and Handoff. The phase goal is to prepare KT, reduce toil, close migration gaps. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: support macro must be updated before launch. Evidence links to ATLAS-1650 and PR-7689.
- Decision: use feature flags for rollout. Evidence links to ATLAS-2141 and PR-7475.
- Decision: support macro must be updated before launch. Evidence links to ATLAS-2801 and PR-5030.

### Risks and Runbook Notes
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0187: Runbook - tax-service - 2026-03
- Owner: Maya Chen
- Updated: 2026-03-13
- Phase: Phase 8 Scale and Handoff
- Related Jira: ATLAS-3556

### Summary
This page explains how tax-service supports Project Atlas during Phase 8 Scale and Handoff. The phase goal is to prepare KT, reduce toil, close migration gaps. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: use feature flags for rollout. Evidence links to ATLAS-4959 and PR-7775.
- Decision: support macro must be updated before launch. Evidence links to ATLAS-5265 and PR-5006.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-2304 and PR-8383.

### Risks and Runbook Notes
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0188: Release Checklist - cart-service - 2026-03
- Owner: Samir Rao
- Updated: 2026-03-24
- Phase: Phase 8 Scale and Handoff
- Related Jira: ATLAS-5391

### Summary
This page explains how cart-service supports Project Atlas during Phase 8 Scale and Handoff. The phase goal is to prepare KT, reduce toil, close migration gaps. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-2926 and PR-9394.
- Decision: use feature flags for rollout. Evidence links to ATLAS-1278 and PR-10105.
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-3097 and PR-9817.

### Risks and Runbook Notes
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0189: ADR - checkout-api - 2026-04
- Owner: Jon Bell
- Updated: 2026-04-21
- Phase: Phase 8 Scale and Handoff
- Related Jira: ATLAS-2499

### Summary
This page explains how checkout-api supports Project Atlas during Phase 8 Scale and Handoff. The phase goal is to prepare KT, reduce toil, close migration gaps. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: dual-write only during migration window. Evidence links to ATLAS-5576 and PR-5099.
- Decision: use feature flags for rollout. Evidence links to ATLAS-1892 and PR-7159.
- Decision: dual-write only during migration window. Evidence links to ATLAS-2456 and PR-6794.

### Risks and Runbook Notes
- Risk: mobile session timeout. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0190: Postmortem - auth-gateway - 2026-04
- Owner: Luca Moretti
- Updated: 2026-04-09
- Phase: Phase 8 Scale and Handoff
- Related Jira: ATLAS-4463

### Summary
This page explains how auth-gateway supports Project Atlas during Phase 8 Scale and Handoff. The phase goal is to prepare KT, reduce toil, close migration gaps. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: keep rollback below 15 minutes. Evidence links to ATLAS-4413 and PR-8386.
- Decision: use feature flags for rollout. Evidence links to ATLAS-3734 and PR-11789.
- Decision: support macro must be updated before launch. Evidence links to ATLAS-5029 and PR-7548.

### Risks and Runbook Notes
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0191: Release Checklist - analytics-pipeline - 2026-05
- Owner: Maya Chen
- Updated: 2026-05-15
- Phase: Phase 8 Scale and Handoff
- Related Jira: ATLAS-3797

### Summary
This page explains how analytics-pipeline supports Project Atlas during Phase 8 Scale and Handoff. The phase goal is to prepare KT, reduce toil, close migration gaps. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-2185 and PR-10926.
- Decision: dual-write only during migration window. Evidence links to ATLAS-6190 and PR-6201.
- Decision: support macro must be updated before launch. Evidence links to ATLAS-4741 and PR-6623.

### Risks and Runbook Notes
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: payment retry storm. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: database lag. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: support escalation volume. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.

## CONF-0192: ADR - search-recommendations - 2026-05
- Owner: Fatima Noor
- Updated: 2026-05-15
- Phase: Phase 8 Scale and Handoff
- Related Jira: ATLAS-3336

### Summary
This page explains how search-recommendations supports Project Atlas during Phase 8 Scale and Handoff. The phase goal is to prepare KT, reduce toil, close migration gaps. The page is used for KT, audit review, incident handoff, and release readiness.

### Key Decisions
- Decision: require p95 and error-rate evidence. Evidence links to ATLAS-3378 and PR-8319.
- Decision: use feature flags for rollout. Evidence links to ATLAS-4394 and PR-9369.
- Decision: support macro must be updated before launch. Evidence links to ATLAS-5110 and PR-6380.

### Risks and Runbook Notes
- Risk: inventory mismatch. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: missing owner. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.
- Risk: tax quote drift. Mitigation: check Grafana, PagerDuty, database health, and Jira before declaring green.

### First Responder Checklist
- Check service dashboard and active alerts.
- Read latest Jira comments and linked PRs.
- Confirm rollback owner and feature flag state.
- Post a Teams handoff with incident, metric, and support context.
