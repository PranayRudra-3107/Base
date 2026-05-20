# GitHub Release Notes - Project Atlas 2018-2026

## REL-2018.06 - Phase 0 Legacy Stabilization
- Release date: 2018-06-21
- Release captain: Jon Bell
- Goal: stabilize legacy checkout, map risks, build team rituals

### Changes
- tax-service: contract test hardening linked to ATLAS-5528 and PR-7905.
- pricing-engine: observability dashboard linked to ATLAS-3238 and PR-9313.
- payment-orchestrator: feature flag rollout linked to ATLAS-5889 and PR-6521.
- checkout-api: support macro update linked to ATLAS-5449 and PR-9159.
- auth-gateway: feature flag rollout linked to ATLAS-5172 and PR-9732.

### Risks and follow-ups
- Risk: payment retry storm. Owner: Dmitri Volkov. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: index bloat. Owner: Theo Martin. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: tax mismatch. Owner: Owen Brooks. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2018.07 - Phase 0 Legacy Stabilization
- Release date: 2018-07-21
- Release captain: Ben Carter
- Goal: stabilize legacy checkout, map risks, build team rituals

### Changes
- auth-gateway: support macro update linked to ATLAS-4428 and PR-10982.
- search-recommendations: database migration guard linked to ATLAS-5984 and PR-6863.
- analytics-pipeline: feature flag rollout linked to ATLAS-4254 and PR-10225.
- search-recommendations: feature flag rollout linked to ATLAS-2415 and PR-9104.
- notification-service: rollback drill linked to ATLAS-3256 and PR-6249.

### Risks and follow-ups
- Risk: latency burn. Owner: Victor Silva. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: queue lag. Owner: Ben Carter. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: tax mismatch. Owner: Anika Sharma. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2018.08 - Phase 0 Legacy Stabilization
- Release date: 2018-08-21
- Release captain: Noah Evans
- Goal: stabilize legacy checkout, map risks, build team rituals

### Changes
- loyalty-service: contract test hardening linked to ATLAS-4213 and PR-7706.
- checkout-api: observability dashboard linked to ATLAS-3604 and PR-6736.
- payment-orchestrator: contract test hardening linked to ATLAS-2921 and PR-6836.
- tax-service: support macro update linked to ATLAS-2312 and PR-5342.
- loyalty-service: contract test hardening linked to ATLAS-4405 and PR-12486.

### Risks and follow-ups
- Risk: support escalation. Owner: Priya Nair. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: payment retry storm. Owner: Kim Tan. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: tax mismatch. Owner: Luca Moretti. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2018.09 - Phase 0 Legacy Stabilization
- Release date: 2018-09-21
- Release captain: Iris Wang
- Goal: stabilize legacy checkout, map risks, build team rituals

### Changes
- cart-service: observability dashboard linked to ATLAS-3239 and PR-9566.
- checkout-api: support macro update linked to ATLAS-4081 and PR-5018.
- order-ledger: database migration guard linked to ATLAS-5965 and PR-6475.
- inventory-reservation: database migration guard linked to ATLAS-4002 and PR-6132.
- auth-gateway: rollback drill linked to ATLAS-2922 and PR-8792.

### Risks and follow-ups
- Risk: queue lag. Owner: Elena Petrova. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: queue lag. Owner: Dmitri Volkov. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: payment retry storm. Owner: Priya Nair. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2018.10 - Phase 0 Legacy Stabilization
- Release date: 2018-10-21
- Release captain: Priya Nair
- Goal: stabilize legacy checkout, map risks, build team rituals

### Changes
- cart-service: observability dashboard linked to ATLAS-1326 and PR-10540.
- loyalty-service: contract test hardening linked to ATLAS-2281 and PR-6492.
- order-ledger: database migration guard linked to ATLAS-5183 and PR-9412.
- notification-service: database migration guard linked to ATLAS-4403 and PR-6154.
- tax-service: rollback drill linked to ATLAS-3101 and PR-10157.

### Risks and follow-ups
- Risk: latency burn. Owner: Mateo Garcia. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: tax mismatch. Owner: Sara Novak. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: payment retry storm. Owner: Victor Silva. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2018.11 - Phase 0 Legacy Stabilization
- Release date: 2018-11-21
- Release captain: Kim Tan
- Goal: stabilize legacy checkout, map risks, build team rituals

### Changes
- pricing-engine: support macro update linked to ATLAS-3979 and PR-10842.
- analytics-pipeline: contract test hardening linked to ATLAS-2115 and PR-9435.
- auth-gateway: rollback drill linked to ATLAS-1868 and PR-7473.
- inventory-reservation: observability dashboard linked to ATLAS-3344 and PR-6236.
- payment-orchestrator: support macro update linked to ATLAS-4441 and PR-8917.

### Risks and follow-ups
- Risk: tax mismatch. Owner: Fatima Noor. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: latency burn. Owner: Fatima Noor. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: latency burn. Owner: Samir Rao. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2018.12 - Phase 0 Legacy Stabilization
- Release date: 2018-12-21
- Release captain: Owen Brooks
- Goal: stabilize legacy checkout, map risks, build team rituals

### Changes
- inventory-reservation: observability dashboard linked to ATLAS-3047 and PR-8335.
- inventory-reservation: rollback drill linked to ATLAS-3637 and PR-7008.
- loyalty-service: observability dashboard linked to ATLAS-2265 and PR-10008.
- analytics-pipeline: support macro update linked to ATLAS-3334 and PR-11503.
- loyalty-service: rollback drill linked to ATLAS-4656 and PR-10006.

### Risks and follow-ups
- Risk: index bloat. Owner: Kim Tan. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: index bloat. Owner: Yara Haddad. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: index bloat. Owner: Anika Sharma. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2019.01 - Phase 1 Service Extraction
- Release date: 2019-01-21
- Release captain: Iris Wang
- Goal: extract cart, pricing, tax, and payment facades

### Changes
- search-recommendations: rollback drill linked to ATLAS-2625 and PR-7258.
- cart-service: support macro update linked to ATLAS-4480 and PR-11267.
- checkout-api: feature flag rollout linked to ATLAS-6073 and PR-6476.
- checkout-api: support macro update linked to ATLAS-4637 and PR-12378.
- pricing-engine: rollback drill linked to ATLAS-2512 and PR-9714.

### Risks and follow-ups
- Risk: queue lag. Owner: Yara Haddad. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: index bloat. Owner: Owen Brooks. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: queue lag. Owner: Samir Rao. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2019.02 - Phase 1 Service Extraction
- Release date: 2019-02-21
- Release captain: Owen Brooks
- Goal: extract cart, pricing, tax, and payment facades

### Changes
- loyalty-service: database migration guard linked to ATLAS-3319 and PR-10759.
- pricing-engine: feature flag rollout linked to ATLAS-4553 and PR-7385.
- checkout-api: contract test hardening linked to ATLAS-6134 and PR-9237.
- order-ledger: support macro update linked to ATLAS-3435 and PR-11101.
- search-recommendations: rollback drill linked to ATLAS-1052 and PR-8468.

### Risks and follow-ups
- Risk: index bloat. Owner: Victor Silva. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: latency burn. Owner: Ravi Patel. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: queue lag. Owner: Priya Nair. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2019.03 - Phase 1 Service Extraction
- Release date: 2019-03-21
- Release captain: Priya Nair
- Goal: extract cart, pricing, tax, and payment facades

### Changes
- checkout-api: contract test hardening linked to ATLAS-2173 and PR-7648.
- analytics-pipeline: feature flag rollout linked to ATLAS-4355 and PR-7708.
- auth-gateway: database migration guard linked to ATLAS-6085 and PR-5006.
- pricing-engine: feature flag rollout linked to ATLAS-2560 and PR-9977.
- notification-service: database migration guard linked to ATLAS-1013 and PR-6275.

### Risks and follow-ups
- Risk: tax mismatch. Owner: Harper Lee. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: support escalation. Owner: Theo Martin. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: queue lag. Owner: Anika Sharma. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2019.04 - Phase 1 Service Extraction
- Release date: 2019-04-21
- Release captain: Ravi Patel
- Goal: extract cart, pricing, tax, and payment facades

### Changes
- payment-orchestrator: rollback drill linked to ATLAS-3796 and PR-8526.
- analytics-pipeline: database migration guard linked to ATLAS-6134 and PR-6641.
- cart-service: observability dashboard linked to ATLAS-3130 and PR-7256.
- notification-service: database migration guard linked to ATLAS-2143 and PR-6280.
- order-ledger: feature flag rollout linked to ATLAS-3399 and PR-6587.

### Risks and follow-ups
- Risk: queue lag. Owner: Ben Carter. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: queue lag. Owner: Sara Novak. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: latency burn. Owner: Victor Silva. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2019.05 - Phase 1 Service Extraction
- Release date: 2019-05-21
- Release captain: Owen Brooks
- Goal: extract cart, pricing, tax, and payment facades

### Changes
- auth-gateway: support macro update linked to ATLAS-2627 and PR-8388.
- order-ledger: rollback drill linked to ATLAS-5960 and PR-6427.
- search-recommendations: database migration guard linked to ATLAS-1175 and PR-6421.
- notification-service: database migration guard linked to ATLAS-2195 and PR-9415.
- analytics-pipeline: database migration guard linked to ATLAS-1966 and PR-7938.

### Risks and follow-ups
- Risk: tax mismatch. Owner: Dmitri Volkov. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: latency burn. Owner: Nora Singh. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: support escalation. Owner: Theo Martin. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2019.06 - Phase 1 Service Extraction
- Release date: 2019-06-21
- Release captain: Victor Silva
- Goal: extract cart, pricing, tax, and payment facades

### Changes
- search-recommendations: observability dashboard linked to ATLAS-2260 and PR-9911.
- cart-service: database migration guard linked to ATLAS-4476 and PR-9958.
- tax-service: support macro update linked to ATLAS-1002 and PR-5624.
- payment-orchestrator: observability dashboard linked to ATLAS-2586 and PR-7603.
- loyalty-service: contract test hardening linked to ATLAS-2089 and PR-12593.

### Risks and follow-ups
- Risk: tax mismatch. Owner: Nora Singh. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: tax mismatch. Owner: Victor Silva. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: index bloat. Owner: Kim Tan. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2019.07 - Phase 1 Service Extraction
- Release date: 2019-07-21
- Release captain: Priya Nair
- Goal: extract cart, pricing, tax, and payment facades

### Changes
- tax-service: observability dashboard linked to ATLAS-1249 and PR-7354.
- pricing-engine: contract test hardening linked to ATLAS-1581 and PR-6048.
- checkout-api: contract test hardening linked to ATLAS-1723 and PR-9359.
- notification-service: rollback drill linked to ATLAS-1199 and PR-5697.
- order-ledger: contract test hardening linked to ATLAS-5826 and PR-5513.

### Risks and follow-ups
- Risk: payment retry storm. Owner: Sara Novak. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: payment retry storm. Owner: Noah Evans. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: payment retry storm. Owner: Dmitri Volkov. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2019.08 - Phase 1 Service Extraction
- Release date: 2019-08-21
- Release captain: Harper Lee
- Goal: extract cart, pricing, tax, and payment facades

### Changes
- auth-gateway: observability dashboard linked to ATLAS-2068 and PR-5520.
- notification-service: rollback drill linked to ATLAS-3475 and PR-6425.
- pricing-engine: database migration guard linked to ATLAS-4062 and PR-11973.
- notification-service: database migration guard linked to ATLAS-1988 and PR-7204.
- search-recommendations: support macro update linked to ATLAS-1038 and PR-6569.

### Risks and follow-ups
- Risk: payment retry storm. Owner: Elena Petrova. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: support escalation. Owner: Owen Brooks. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: tax mismatch. Owner: Theo Martin. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2019.09 - Phase 1 Service Extraction
- Release date: 2019-09-21
- Release captain: Harper Lee
- Goal: extract cart, pricing, tax, and payment facades

### Changes
- tax-service: support macro update linked to ATLAS-2818 and PR-11788.
- cart-service: support macro update linked to ATLAS-5685 and PR-10850.
- tax-service: feature flag rollout linked to ATLAS-2216 and PR-8080.
- tax-service: feature flag rollout linked to ATLAS-1714 and PR-9453.
- auth-gateway: contract test hardening linked to ATLAS-4559 and PR-11964.

### Risks and follow-ups
- Risk: latency burn. Owner: Aisha Khan. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: latency burn. Owner: Aisha Khan. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: latency burn. Owner: Grace Kim. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2019.10 - Phase 1 Service Extraction
- Release date: 2019-10-21
- Release captain: Theo Martin
- Goal: extract cart, pricing, tax, and payment facades

### Changes
- search-recommendations: contract test hardening linked to ATLAS-4620 and PR-11996.
- auth-gateway: contract test hardening linked to ATLAS-4866 and PR-7738.
- auth-gateway: support macro update linked to ATLAS-4082 and PR-8227.
- tax-service: observability dashboard linked to ATLAS-5823 and PR-5010.
- loyalty-service: support macro update linked to ATLAS-1777 and PR-6780.

### Risks and follow-ups
- Risk: queue lag. Owner: Mateo Garcia. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: support escalation. Owner: Ben Carter. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: payment retry storm. Owner: Fatima Noor. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2019.11 - Phase 1 Service Extraction
- Release date: 2019-11-21
- Release captain: Iris Wang
- Goal: extract cart, pricing, tax, and payment facades

### Changes
- auth-gateway: feature flag rollout linked to ATLAS-3743 and PR-9279.
- pricing-engine: database migration guard linked to ATLAS-5608 and PR-6972.
- checkout-api: database migration guard linked to ATLAS-3939 and PR-8431.
- order-ledger: observability dashboard linked to ATLAS-6134 and PR-6627.
- loyalty-service: support macro update linked to ATLAS-4070 and PR-10166.

### Risks and follow-ups
- Risk: support escalation. Owner: Samir Rao. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: latency burn. Owner: Sara Novak. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: tax mismatch. Owner: Yara Haddad. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2019.12 - Phase 1 Service Extraction
- Release date: 2019-12-21
- Release captain: Elena Petrova
- Goal: extract cart, pricing, tax, and payment facades

### Changes
- order-ledger: contract test hardening linked to ATLAS-4638 and PR-6707.
- order-ledger: feature flag rollout linked to ATLAS-2012 and PR-11647.
- pricing-engine: feature flag rollout linked to ATLAS-2668 and PR-9701.
- order-ledger: feature flag rollout linked to ATLAS-4427 and PR-5612.
- analytics-pipeline: database migration guard linked to ATLAS-4380 and PR-5069.

### Risks and follow-ups
- Risk: support escalation. Owner: Dmitri Volkov. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: tax mismatch. Owner: Dmitri Volkov. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: support escalation. Owner: Iris Wang. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2020.01 - Phase 2 Cloud Migration
- Release date: 2020-01-21
- Release captain: Elena Petrova
- Goal: move workloads to Kubernetes and managed databases

### Changes
- loyalty-service: rollback drill linked to ATLAS-4133 and PR-7659.
- pricing-engine: observability dashboard linked to ATLAS-2586 and PR-6450.
- cart-service: contract test hardening linked to ATLAS-5407 and PR-5013.
- order-ledger: database migration guard linked to ATLAS-2203 and PR-5163.
- checkout-api: feature flag rollout linked to ATLAS-3588 and PR-6845.

### Risks and follow-ups
- Risk: latency burn. Owner: Theo Martin. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: tax mismatch. Owner: Maya Chen. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: index bloat. Owner: Sara Novak. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2020.02 - Phase 2 Cloud Migration
- Release date: 2020-02-21
- Release captain: Harper Lee
- Goal: move workloads to Kubernetes and managed databases

### Changes
- analytics-pipeline: rollback drill linked to ATLAS-3024 and PR-6005.
- loyalty-service: support macro update linked to ATLAS-1531 and PR-5659.
- notification-service: contract test hardening linked to ATLAS-2872 and PR-6871.
- notification-service: rollback drill linked to ATLAS-2347 and PR-6202.
- analytics-pipeline: support macro update linked to ATLAS-5365 and PR-8869.

### Risks and follow-ups
- Risk: latency burn. Owner: Anika Sharma. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: queue lag. Owner: Owen Brooks. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: support escalation. Owner: Harper Lee. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2020.03 - Phase 2 Cloud Migration
- Release date: 2020-03-21
- Release captain: Aisha Khan
- Goal: move workloads to Kubernetes and managed databases

### Changes
- loyalty-service: rollback drill linked to ATLAS-3139 and PR-7622.
- inventory-reservation: rollback drill linked to ATLAS-1157 and PR-8135.
- inventory-reservation: support macro update linked to ATLAS-2187 and PR-11863.
- notification-service: rollback drill linked to ATLAS-3166 and PR-6354.
- tax-service: contract test hardening linked to ATLAS-2864 and PR-6861.

### Risks and follow-ups
- Risk: payment retry storm. Owner: Aisha Khan. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: index bloat. Owner: Samir Rao. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: latency burn. Owner: Harper Lee. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2020.04 - Phase 2 Cloud Migration
- Release date: 2020-04-21
- Release captain: Dmitri Volkov
- Goal: move workloads to Kubernetes and managed databases

### Changes
- pricing-engine: observability dashboard linked to ATLAS-3329 and PR-12000.
- inventory-reservation: contract test hardening linked to ATLAS-2504 and PR-8575.
- inventory-reservation: contract test hardening linked to ATLAS-2648 and PR-5872.
- search-recommendations: observability dashboard linked to ATLAS-3626 and PR-11051.
- cart-service: feature flag rollout linked to ATLAS-1934 and PR-11807.

### Risks and follow-ups
- Risk: support escalation. Owner: Kim Tan. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: support escalation. Owner: Owen Brooks. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: index bloat. Owner: Sara Novak. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2020.05 - Phase 2 Cloud Migration
- Release date: 2020-05-21
- Release captain: Maya Chen
- Goal: move workloads to Kubernetes and managed databases

### Changes
- cart-service: feature flag rollout linked to ATLAS-2088 and PR-9551.
- pricing-engine: observability dashboard linked to ATLAS-4941 and PR-10966.
- checkout-api: feature flag rollout linked to ATLAS-4357 and PR-6261.
- tax-service: observability dashboard linked to ATLAS-4893 and PR-11804.
- analytics-pipeline: rollback drill linked to ATLAS-5336 and PR-6949.

### Risks and follow-ups
- Risk: tax mismatch. Owner: Samir Rao. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: queue lag. Owner: Ravi Patel. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: payment retry storm. Owner: Aisha Khan. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2020.06 - Phase 2 Cloud Migration
- Release date: 2020-06-21
- Release captain: Anika Sharma
- Goal: move workloads to Kubernetes and managed databases

### Changes
- loyalty-service: observability dashboard linked to ATLAS-4628 and PR-12165.
- search-recommendations: support macro update linked to ATLAS-3168 and PR-6588.
- pricing-engine: support macro update linked to ATLAS-3474 and PR-5095.
- payment-orchestrator: database migration guard linked to ATLAS-5411 and PR-9661.
- payment-orchestrator: rollback drill linked to ATLAS-1135 and PR-8608.

### Risks and follow-ups
- Risk: index bloat. Owner: Harper Lee. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: payment retry storm. Owner: Nora Singh. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: support escalation. Owner: Maya Chen. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2020.07 - Phase 2 Cloud Migration
- Release date: 2020-07-21
- Release captain: Ravi Patel
- Goal: move workloads to Kubernetes and managed databases

### Changes
- auth-gateway: feature flag rollout linked to ATLAS-1334 and PR-5252.
- tax-service: rollback drill linked to ATLAS-3329 and PR-11858.
- payment-orchestrator: contract test hardening linked to ATLAS-6032 and PR-5654.
- analytics-pipeline: rollback drill linked to ATLAS-3086 and PR-11574.
- order-ledger: support macro update linked to ATLAS-3786 and PR-8028.

### Risks and follow-ups
- Risk: latency burn. Owner: Fatima Noor. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: latency burn. Owner: Jon Bell. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: queue lag. Owner: Owen Brooks. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2020.08 - Phase 2 Cloud Migration
- Release date: 2020-08-21
- Release captain: Yara Haddad
- Goal: move workloads to Kubernetes and managed databases

### Changes
- checkout-api: database migration guard linked to ATLAS-4796 and PR-8907.
- analytics-pipeline: support macro update linked to ATLAS-3872 and PR-6679.
- cart-service: database migration guard linked to ATLAS-3585 and PR-9015.
- notification-service: support macro update linked to ATLAS-6121 and PR-9759.
- pricing-engine: observability dashboard linked to ATLAS-3716 and PR-7160.

### Risks and follow-ups
- Risk: payment retry storm. Owner: Victor Silva. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: tax mismatch. Owner: Victor Silva. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: queue lag. Owner: Sara Novak. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2020.09 - Phase 2 Cloud Migration
- Release date: 2020-09-21
- Release captain: Grace Kim
- Goal: move workloads to Kubernetes and managed databases

### Changes
- analytics-pipeline: contract test hardening linked to ATLAS-5454 and PR-9729.
- checkout-api: database migration guard linked to ATLAS-3350 and PR-6812.
- search-recommendations: database migration guard linked to ATLAS-2952 and PR-12431.
- inventory-reservation: rollback drill linked to ATLAS-3788 and PR-9063.
- pricing-engine: feature flag rollout linked to ATLAS-4349 and PR-10010.

### Risks and follow-ups
- Risk: tax mismatch. Owner: Jon Bell. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: tax mismatch. Owner: Iris Wang. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: payment retry storm. Owner: Ravi Patel. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2020.10 - Phase 2 Cloud Migration
- Release date: 2020-10-21
- Release captain: Owen Brooks
- Goal: move workloads to Kubernetes and managed databases

### Changes
- tax-service: rollback drill linked to ATLAS-2417 and PR-12169.
- notification-service: observability dashboard linked to ATLAS-1379 and PR-7495.
- analytics-pipeline: rollback drill linked to ATLAS-3030 and PR-5156.
- pricing-engine: database migration guard linked to ATLAS-5623 and PR-7401.
- analytics-pipeline: observability dashboard linked to ATLAS-3206 and PR-6859.

### Risks and follow-ups
- Risk: queue lag. Owner: Harper Lee. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: payment retry storm. Owner: Grace Kim. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: support escalation. Owner: Ravi Patel. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2020.11 - Phase 2 Cloud Migration
- Release date: 2020-11-21
- Release captain: Aisha Khan
- Goal: move workloads to Kubernetes and managed databases

### Changes
- inventory-reservation: contract test hardening linked to ATLAS-2224 and PR-9699.
- inventory-reservation: feature flag rollout linked to ATLAS-5543 and PR-10265.
- loyalty-service: contract test hardening linked to ATLAS-3562 and PR-6453.
- auth-gateway: database migration guard linked to ATLAS-4978 and PR-9164.
- order-ledger: support macro update linked to ATLAS-2084 and PR-11863.

### Risks and follow-ups
- Risk: support escalation. Owner: Anika Sharma. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: support escalation. Owner: Harper Lee. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: index bloat. Owner: Luca Moretti. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2020.12 - Phase 2 Cloud Migration
- Release date: 2020-12-21
- Release captain: Ravi Patel
- Goal: move workloads to Kubernetes and managed databases

### Changes
- tax-service: support macro update linked to ATLAS-5233 and PR-6950.
- payment-orchestrator: contract test hardening linked to ATLAS-2979 and PR-7439.
- cart-service: contract test hardening linked to ATLAS-1127 and PR-7288.
- pricing-engine: rollback drill linked to ATLAS-2973 and PR-5797.
- loyalty-service: database migration guard linked to ATLAS-3002 and PR-5338.

### Risks and follow-ups
- Risk: queue lag. Owner: Priya Nair. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: latency burn. Owner: Dmitri Volkov. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: latency burn. Owner: Luca Moretti. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2021.01 - Phase 3 Global Checkout
- Release date: 2021-01-21
- Release captain: Samir Rao
- Goal: add localization, tax rules, currency, and fraud checks

### Changes
- pricing-engine: feature flag rollout linked to ATLAS-4275 and PR-9093.
- analytics-pipeline: observability dashboard linked to ATLAS-2190 and PR-5381.
- auth-gateway: database migration guard linked to ATLAS-1837 and PR-12588.
- notification-service: contract test hardening linked to ATLAS-2296 and PR-10992.
- cart-service: contract test hardening linked to ATLAS-2466 and PR-8281.

### Risks and follow-ups
- Risk: index bloat. Owner: Noah Evans. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: tax mismatch. Owner: Nora Singh. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: support escalation. Owner: Kim Tan. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2021.02 - Phase 3 Global Checkout
- Release date: 2021-02-21
- Release captain: Anika Sharma
- Goal: add localization, tax rules, currency, and fraud checks

### Changes
- analytics-pipeline: contract test hardening linked to ATLAS-1104 and PR-6118.
- order-ledger: contract test hardening linked to ATLAS-4104 and PR-9445.
- payment-orchestrator: support macro update linked to ATLAS-3483 and PR-6475.
- payment-orchestrator: database migration guard linked to ATLAS-5874 and PR-9083.
- tax-service: feature flag rollout linked to ATLAS-2675 and PR-6392.

### Risks and follow-ups
- Risk: latency burn. Owner: Anika Sharma. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: queue lag. Owner: Priya Nair. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: tax mismatch. Owner: Dmitri Volkov. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2021.03 - Phase 3 Global Checkout
- Release date: 2021-03-21
- Release captain: Victor Silva
- Goal: add localization, tax rules, currency, and fraud checks

### Changes
- payment-orchestrator: contract test hardening linked to ATLAS-6173 and PR-8393.
- search-recommendations: observability dashboard linked to ATLAS-4665 and PR-5199.
- search-recommendations: feature flag rollout linked to ATLAS-5563 and PR-8274.
- order-ledger: observability dashboard linked to ATLAS-1123 and PR-5878.
- notification-service: support macro update linked to ATLAS-5156 and PR-6678.

### Risks and follow-ups
- Risk: index bloat. Owner: Sara Novak. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: payment retry storm. Owner: Nora Singh. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: tax mismatch. Owner: Ravi Patel. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2021.04 - Phase 3 Global Checkout
- Release date: 2021-04-21
- Release captain: Iris Wang
- Goal: add localization, tax rules, currency, and fraud checks

### Changes
- tax-service: observability dashboard linked to ATLAS-4652 and PR-9465.
- analytics-pipeline: database migration guard linked to ATLAS-3443 and PR-9991.
- pricing-engine: support macro update linked to ATLAS-3748 and PR-9143.
- search-recommendations: observability dashboard linked to ATLAS-5273 and PR-5379.
- search-recommendations: observability dashboard linked to ATLAS-5425 and PR-9663.

### Risks and follow-ups
- Risk: tax mismatch. Owner: Mateo Garcia. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: latency burn. Owner: Samir Rao. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: index bloat. Owner: Sara Novak. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2021.05 - Phase 3 Global Checkout
- Release date: 2021-05-21
- Release captain: Fatima Noor
- Goal: add localization, tax rules, currency, and fraud checks

### Changes
- analytics-pipeline: feature flag rollout linked to ATLAS-3327 and PR-10566.
- auth-gateway: observability dashboard linked to ATLAS-3735 and PR-10392.
- auth-gateway: observability dashboard linked to ATLAS-2247 and PR-7608.
- loyalty-service: observability dashboard linked to ATLAS-6112 and PR-5137.
- tax-service: support macro update linked to ATLAS-2375 and PR-7916.

### Risks and follow-ups
- Risk: tax mismatch. Owner: Victor Silva. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: support escalation. Owner: Yara Haddad. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: queue lag. Owner: Sara Novak. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2021.06 - Phase 3 Global Checkout
- Release date: 2021-06-21
- Release captain: Luca Moretti
- Goal: add localization, tax rules, currency, and fraud checks

### Changes
- tax-service: contract test hardening linked to ATLAS-2678 and PR-12386.
- checkout-api: observability dashboard linked to ATLAS-4043 and PR-8965.
- pricing-engine: database migration guard linked to ATLAS-2585 and PR-6223.
- inventory-reservation: feature flag rollout linked to ATLAS-5033 and PR-10392.
- loyalty-service: contract test hardening linked to ATLAS-1243 and PR-6875.

### Risks and follow-ups
- Risk: index bloat. Owner: Luca Moretti. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: queue lag. Owner: Jon Bell. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: index bloat. Owner: Priya Nair. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2021.07 - Phase 3 Global Checkout
- Release date: 2021-07-21
- Release captain: Samir Rao
- Goal: add localization, tax rules, currency, and fraud checks

### Changes
- inventory-reservation: feature flag rollout linked to ATLAS-1719 and PR-7647.
- notification-service: feature flag rollout linked to ATLAS-1451 and PR-9229.
- analytics-pipeline: observability dashboard linked to ATLAS-3674 and PR-5107.
- pricing-engine: support macro update linked to ATLAS-4069 and PR-7234.
- analytics-pipeline: rollback drill linked to ATLAS-2106 and PR-10861.

### Risks and follow-ups
- Risk: latency burn. Owner: Jon Bell. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: support escalation. Owner: Jon Bell. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: support escalation. Owner: Mateo Garcia. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2021.08 - Phase 3 Global Checkout
- Release date: 2021-08-21
- Release captain: Kim Tan
- Goal: add localization, tax rules, currency, and fraud checks

### Changes
- auth-gateway: contract test hardening linked to ATLAS-1519 and PR-8141.
- search-recommendations: rollback drill linked to ATLAS-3189 and PR-6973.
- payment-orchestrator: feature flag rollout linked to ATLAS-5177 and PR-5521.
- loyalty-service: rollback drill linked to ATLAS-5351 and PR-7983.
- payment-orchestrator: rollback drill linked to ATLAS-3033 and PR-8731.

### Risks and follow-ups
- Risk: tax mismatch. Owner: Fatima Noor. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: tax mismatch. Owner: Theo Martin. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: tax mismatch. Owner: Yara Haddad. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2021.09 - Phase 3 Global Checkout
- Release date: 2021-09-21
- Release captain: Kim Tan
- Goal: add localization, tax rules, currency, and fraud checks

### Changes
- cart-service: feature flag rollout linked to ATLAS-2480 and PR-8376.
- checkout-api: database migration guard linked to ATLAS-1292 and PR-6097.
- pricing-engine: observability dashboard linked to ATLAS-1816 and PR-7371.
- cart-service: observability dashboard linked to ATLAS-4708 and PR-7803.
- tax-service: contract test hardening linked to ATLAS-1051 and PR-7009.

### Risks and follow-ups
- Risk: support escalation. Owner: Theo Martin. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: tax mismatch. Owner: Harper Lee. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: latency burn. Owner: Fatima Noor. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2021.10 - Phase 3 Global Checkout
- Release date: 2021-10-21
- Release captain: Mateo Garcia
- Goal: add localization, tax rules, currency, and fraud checks

### Changes
- notification-service: feature flag rollout linked to ATLAS-1633 and PR-6467.
- inventory-reservation: support macro update linked to ATLAS-2607 and PR-8235.
- tax-service: database migration guard linked to ATLAS-5875 and PR-5627.
- auth-gateway: database migration guard linked to ATLAS-5082 and PR-9045.
- auth-gateway: feature flag rollout linked to ATLAS-1882 and PR-6781.

### Risks and follow-ups
- Risk: payment retry storm. Owner: Nora Singh. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: tax mismatch. Owner: Fatima Noor. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: payment retry storm. Owner: Maya Chen. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2021.11 - Phase 3 Global Checkout
- Release date: 2021-11-21
- Release captain: Anika Sharma
- Goal: add localization, tax rules, currency, and fraud checks

### Changes
- loyalty-service: database migration guard linked to ATLAS-3715 and PR-9605.
- tax-service: observability dashboard linked to ATLAS-2675 and PR-5078.
- notification-service: support macro update linked to ATLAS-5524 and PR-12407.
- tax-service: observability dashboard linked to ATLAS-1532 and PR-8818.
- pricing-engine: feature flag rollout linked to ATLAS-3664 and PR-7199.

### Risks and follow-ups
- Risk: payment retry storm. Owner: Elena Petrova. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: support escalation. Owner: Ben Carter. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: index bloat. Owner: Dmitri Volkov. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2021.12 - Phase 3 Global Checkout
- Release date: 2021-12-21
- Release captain: Jon Bell
- Goal: add localization, tax rules, currency, and fraud checks

### Changes
- order-ledger: feature flag rollout linked to ATLAS-2161 and PR-9991.
- loyalty-service: rollback drill linked to ATLAS-1636 and PR-5205.
- auth-gateway: support macro update linked to ATLAS-3433 and PR-11525.
- loyalty-service: feature flag rollout linked to ATLAS-5584 and PR-6941.
- pricing-engine: database migration guard linked to ATLAS-3023 and PR-12206.

### Risks and follow-ups
- Risk: index bloat. Owner: Dmitri Volkov. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: queue lag. Owner: Jon Bell. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: queue lag. Owner: Mateo Garcia. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2022.01 - Phase 4 Loyalty and Personalization
- Release date: 2022-01-21
- Release captain: Grace Kim
- Goal: connect loyalty, promotions, and segmentation

### Changes
- inventory-reservation: feature flag rollout linked to ATLAS-5514 and PR-7582.
- payment-orchestrator: observability dashboard linked to ATLAS-2230 and PR-6594.
- notification-service: support macro update linked to ATLAS-2813 and PR-6694.
- loyalty-service: database migration guard linked to ATLAS-5847 and PR-7832.
- checkout-api: observability dashboard linked to ATLAS-4672 and PR-5225.

### Risks and follow-ups
- Risk: tax mismatch. Owner: Kim Tan. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: latency burn. Owner: Iris Wang. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: queue lag. Owner: Fatima Noor. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2022.02 - Phase 4 Loyalty and Personalization
- Release date: 2022-02-21
- Release captain: Anika Sharma
- Goal: connect loyalty, promotions, and segmentation

### Changes
- inventory-reservation: observability dashboard linked to ATLAS-5264 and PR-11668.
- cart-service: rollback drill linked to ATLAS-4901 and PR-10200.
- pricing-engine: feature flag rollout linked to ATLAS-3855 and PR-7129.
- auth-gateway: database migration guard linked to ATLAS-5098 and PR-5366.
- checkout-api: support macro update linked to ATLAS-3073 and PR-8068.

### Risks and follow-ups
- Risk: tax mismatch. Owner: Aisha Khan. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: queue lag. Owner: Dmitri Volkov. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: support escalation. Owner: Kim Tan. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2022.03 - Phase 4 Loyalty and Personalization
- Release date: 2022-03-21
- Release captain: Luca Moretti
- Goal: connect loyalty, promotions, and segmentation

### Changes
- notification-service: rollback drill linked to ATLAS-2196 and PR-10837.
- tax-service: rollback drill linked to ATLAS-5974 and PR-8013.
- order-ledger: database migration guard linked to ATLAS-5148 and PR-7455.
- order-ledger: contract test hardening linked to ATLAS-3603 and PR-8581.
- checkout-api: contract test hardening linked to ATLAS-2077 and PR-7906.

### Risks and follow-ups
- Risk: latency burn. Owner: Ravi Patel. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: tax mismatch. Owner: Yara Haddad. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: payment retry storm. Owner: Theo Martin. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2022.04 - Phase 4 Loyalty and Personalization
- Release date: 2022-04-21
- Release captain: Priya Nair
- Goal: connect loyalty, promotions, and segmentation

### Changes
- auth-gateway: support macro update linked to ATLAS-4507 and PR-9480.
- tax-service: database migration guard linked to ATLAS-4585 and PR-8149.
- tax-service: feature flag rollout linked to ATLAS-5966 and PR-5970.
- analytics-pipeline: support macro update linked to ATLAS-4160 and PR-10028.
- inventory-reservation: feature flag rollout linked to ATLAS-1284 and PR-8500.

### Risks and follow-ups
- Risk: support escalation. Owner: Theo Martin. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: queue lag. Owner: Grace Kim. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: payment retry storm. Owner: Anika Sharma. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2022.05 - Phase 4 Loyalty and Personalization
- Release date: 2022-05-21
- Release captain: Sara Novak
- Goal: connect loyalty, promotions, and segmentation

### Changes
- tax-service: database migration guard linked to ATLAS-5444 and PR-12261.
- order-ledger: support macro update linked to ATLAS-1647 and PR-11111.
- order-ledger: database migration guard linked to ATLAS-5156 and PR-6013.
- analytics-pipeline: feature flag rollout linked to ATLAS-5988 and PR-9730.
- loyalty-service: support macro update linked to ATLAS-2935 and PR-6944.

### Risks and follow-ups
- Risk: queue lag. Owner: Elena Petrova. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: latency burn. Owner: Maya Chen. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: tax mismatch. Owner: Sara Novak. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2022.06 - Phase 4 Loyalty and Personalization
- Release date: 2022-06-21
- Release captain: Ravi Patel
- Goal: connect loyalty, promotions, and segmentation

### Changes
- notification-service: rollback drill linked to ATLAS-2779 and PR-5541.
- tax-service: observability dashboard linked to ATLAS-1677 and PR-10584.
- pricing-engine: database migration guard linked to ATLAS-1508 and PR-10520.
- order-ledger: contract test hardening linked to ATLAS-5233 and PR-7897.
- tax-service: rollback drill linked to ATLAS-2441 and PR-6879.

### Risks and follow-ups
- Risk: queue lag. Owner: Anika Sharma. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: latency burn. Owner: Elena Petrova. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: tax mismatch. Owner: Maya Chen. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2022.07 - Phase 4 Loyalty and Personalization
- Release date: 2022-07-21
- Release captain: Priya Nair
- Goal: connect loyalty, promotions, and segmentation

### Changes
- search-recommendations: database migration guard linked to ATLAS-1976 and PR-11106.
- search-recommendations: feature flag rollout linked to ATLAS-2552 and PR-8144.
- loyalty-service: feature flag rollout linked to ATLAS-1878 and PR-6144.
- analytics-pipeline: feature flag rollout linked to ATLAS-1717 and PR-7341.
- cart-service: contract test hardening linked to ATLAS-4919 and PR-10034.

### Risks and follow-ups
- Risk: queue lag. Owner: Fatima Noor. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: queue lag. Owner: Luca Moretti. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: tax mismatch. Owner: Noah Evans. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2022.08 - Phase 4 Loyalty and Personalization
- Release date: 2022-08-21
- Release captain: Aisha Khan
- Goal: connect loyalty, promotions, and segmentation

### Changes
- auth-gateway: support macro update linked to ATLAS-3922 and PR-6610.
- notification-service: database migration guard linked to ATLAS-3738 and PR-7366.
- auth-gateway: observability dashboard linked to ATLAS-1976 and PR-7748.
- search-recommendations: feature flag rollout linked to ATLAS-1162 and PR-5504.
- checkout-api: rollback drill linked to ATLAS-1868 and PR-9483.

### Risks and follow-ups
- Risk: index bloat. Owner: Dmitri Volkov. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: support escalation. Owner: Maya Chen. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: latency burn. Owner: Noah Evans. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2022.09 - Phase 4 Loyalty and Personalization
- Release date: 2022-09-21
- Release captain: Harper Lee
- Goal: connect loyalty, promotions, and segmentation

### Changes
- notification-service: observability dashboard linked to ATLAS-3864 and PR-9616.
- order-ledger: contract test hardening linked to ATLAS-4630 and PR-9266.
- analytics-pipeline: contract test hardening linked to ATLAS-2767 and PR-12314.
- cart-service: feature flag rollout linked to ATLAS-1987 and PR-9888.
- tax-service: database migration guard linked to ATLAS-3042 and PR-8011.

### Risks and follow-ups
- Risk: queue lag. Owner: Luca Moretti. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: support escalation. Owner: Ben Carter. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: support escalation. Owner: Mateo Garcia. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2022.10 - Phase 4 Loyalty and Personalization
- Release date: 2022-10-21
- Release captain: Ravi Patel
- Goal: connect loyalty, promotions, and segmentation

### Changes
- loyalty-service: database migration guard linked to ATLAS-4223 and PR-7927.
- search-recommendations: feature flag rollout linked to ATLAS-3444 and PR-11134.
- pricing-engine: database migration guard linked to ATLAS-5840 and PR-6360.
- inventory-reservation: observability dashboard linked to ATLAS-1392 and PR-6944.
- auth-gateway: contract test hardening linked to ATLAS-4284 and PR-8161.

### Risks and follow-ups
- Risk: index bloat. Owner: Noah Evans. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: support escalation. Owner: Theo Martin. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: index bloat. Owner: Elena Petrova. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2022.11 - Phase 4 Loyalty and Personalization
- Release date: 2022-11-21
- Release captain: Samir Rao
- Goal: connect loyalty, promotions, and segmentation

### Changes
- auth-gateway: database migration guard linked to ATLAS-1186 and PR-7580.
- notification-service: rollback drill linked to ATLAS-5276 and PR-5836.
- notification-service: support macro update linked to ATLAS-5601 and PR-5101.
- checkout-api: database migration guard linked to ATLAS-2636 and PR-9068.
- payment-orchestrator: feature flag rollout linked to ATLAS-1744 and PR-5844.

### Risks and follow-ups
- Risk: latency burn. Owner: Jon Bell. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: latency burn. Owner: Jon Bell. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: payment retry storm. Owner: Priya Nair. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2022.12 - Phase 4 Loyalty and Personalization
- Release date: 2022-12-21
- Release captain: Nora Singh
- Goal: connect loyalty, promotions, and segmentation

### Changes
- payment-orchestrator: support macro update linked to ATLAS-1775 and PR-6750.
- pricing-engine: support macro update linked to ATLAS-6100 and PR-6109.
- search-recommendations: rollback drill linked to ATLAS-1617 and PR-7667.
- loyalty-service: contract test hardening linked to ATLAS-1831 and PR-8874.
- cart-service: observability dashboard linked to ATLAS-1738 and PR-9815.

### Risks and follow-ups
- Risk: payment retry storm. Owner: Grace Kim. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: index bloat. Owner: Ben Carter. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: queue lag. Owner: Aisha Khan. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2023.01 - Phase 5 Resilience and Observability
- Release date: 2023-01-21
- Release captain: Ben Carter
- Goal: burn down incidents, improve SLOs, add tracing

### Changes
- analytics-pipeline: observability dashboard linked to ATLAS-5051 and PR-7850.
- notification-service: contract test hardening linked to ATLAS-2451 and PR-7489.
- inventory-reservation: rollback drill linked to ATLAS-2022 and PR-10022.
- order-ledger: rollback drill linked to ATLAS-1908 and PR-8747.
- notification-service: rollback drill linked to ATLAS-3864 and PR-12505.

### Risks and follow-ups
- Risk: queue lag. Owner: Elena Petrova. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: latency burn. Owner: Nora Singh. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: index bloat. Owner: Nora Singh. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2023.02 - Phase 5 Resilience and Observability
- Release date: 2023-02-21
- Release captain: Aisha Khan
- Goal: burn down incidents, improve SLOs, add tracing

### Changes
- search-recommendations: support macro update linked to ATLAS-3657 and PR-7622.
- auth-gateway: rollback drill linked to ATLAS-4684 and PR-6218.
- inventory-reservation: contract test hardening linked to ATLAS-3807 and PR-9967.
- loyalty-service: database migration guard linked to ATLAS-4177 and PR-6119.
- loyalty-service: feature flag rollout linked to ATLAS-2258 and PR-12213.

### Risks and follow-ups
- Risk: latency burn. Owner: Aisha Khan. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: latency burn. Owner: Sara Novak. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: payment retry storm. Owner: Sara Novak. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2023.03 - Phase 5 Resilience and Observability
- Release date: 2023-03-21
- Release captain: Yara Haddad
- Goal: burn down incidents, improve SLOs, add tracing

### Changes
- checkout-api: feature flag rollout linked to ATLAS-5323 and PR-7054.
- tax-service: database migration guard linked to ATLAS-2218 and PR-5556.
- inventory-reservation: observability dashboard linked to ATLAS-6082 and PR-6396.
- loyalty-service: database migration guard linked to ATLAS-4569 and PR-7409.
- cart-service: support macro update linked to ATLAS-1145 and PR-9190.

### Risks and follow-ups
- Risk: index bloat. Owner: Aisha Khan. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: payment retry storm. Owner: Maya Chen. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: index bloat. Owner: Fatima Noor. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2023.04 - Phase 5 Resilience and Observability
- Release date: 2023-04-21
- Release captain: Ravi Patel
- Goal: burn down incidents, improve SLOs, add tracing

### Changes
- cart-service: feature flag rollout linked to ATLAS-1313 and PR-7600.
- loyalty-service: database migration guard linked to ATLAS-4617 and PR-10186.
- checkout-api: feature flag rollout linked to ATLAS-2587 and PR-8494.
- search-recommendations: database migration guard linked to ATLAS-3086 and PR-8925.
- analytics-pipeline: database migration guard linked to ATLAS-2538 and PR-9882.

### Risks and follow-ups
- Risk: queue lag. Owner: Grace Kim. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: tax mismatch. Owner: Yara Haddad. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: tax mismatch. Owner: Iris Wang. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2023.05 - Phase 5 Resilience and Observability
- Release date: 2023-05-21
- Release captain: Fatima Noor
- Goal: burn down incidents, improve SLOs, add tracing

### Changes
- loyalty-service: database migration guard linked to ATLAS-5181 and PR-7123.
- order-ledger: support macro update linked to ATLAS-2634 and PR-5140.
- analytics-pipeline: support macro update linked to ATLAS-3069 and PR-7506.
- checkout-api: support macro update linked to ATLAS-3180 and PR-8789.
- loyalty-service: observability dashboard linked to ATLAS-2545 and PR-6218.

### Risks and follow-ups
- Risk: latency burn. Owner: Owen Brooks. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: support escalation. Owner: Dmitri Volkov. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: payment retry storm. Owner: Sara Novak. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2023.06 - Phase 5 Resilience and Observability
- Release date: 2023-06-21
- Release captain: Elena Petrova
- Goal: burn down incidents, improve SLOs, add tracing

### Changes
- pricing-engine: contract test hardening linked to ATLAS-1038 and PR-11001.
- search-recommendations: rollback drill linked to ATLAS-5476 and PR-10191.
- tax-service: support macro update linked to ATLAS-4005 and PR-8177.
- checkout-api: rollback drill linked to ATLAS-5092 and PR-6303.
- checkout-api: rollback drill linked to ATLAS-3860 and PR-11781.

### Risks and follow-ups
- Risk: queue lag. Owner: Nora Singh. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: support escalation. Owner: Theo Martin. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: payment retry storm. Owner: Sara Novak. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2023.07 - Phase 5 Resilience and Observability
- Release date: 2023-07-21
- Release captain: Noah Evans
- Goal: burn down incidents, improve SLOs, add tracing

### Changes
- tax-service: observability dashboard linked to ATLAS-2689 and PR-7625.
- tax-service: observability dashboard linked to ATLAS-3830 and PR-10134.
- search-recommendations: observability dashboard linked to ATLAS-3202 and PR-5812.
- cart-service: database migration guard linked to ATLAS-1479 and PR-5373.
- payment-orchestrator: feature flag rollout linked to ATLAS-4698 and PR-5219.

### Risks and follow-ups
- Risk: tax mismatch. Owner: Yara Haddad. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: payment retry storm. Owner: Noah Evans. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: latency burn. Owner: Nora Singh. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2023.08 - Phase 5 Resilience and Observability
- Release date: 2023-08-21
- Release captain: Jon Bell
- Goal: burn down incidents, improve SLOs, add tracing

### Changes
- payment-orchestrator: contract test hardening linked to ATLAS-4549 and PR-7523.
- analytics-pipeline: observability dashboard linked to ATLAS-1296 and PR-11717.
- loyalty-service: rollback drill linked to ATLAS-1456 and PR-5535.
- search-recommendations: observability dashboard linked to ATLAS-5268 and PR-8447.
- search-recommendations: support macro update linked to ATLAS-4630 and PR-5720.

### Risks and follow-ups
- Risk: index bloat. Owner: Fatima Noor. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: support escalation. Owner: Ravi Patel. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: index bloat. Owner: Ravi Patel. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2023.09 - Phase 5 Resilience and Observability
- Release date: 2023-09-21
- Release captain: Ravi Patel
- Goal: burn down incidents, improve SLOs, add tracing

### Changes
- analytics-pipeline: rollback drill linked to ATLAS-2479 and PR-5171.
- tax-service: feature flag rollout linked to ATLAS-1441 and PR-6086.
- search-recommendations: support macro update linked to ATLAS-1478 and PR-7281.
- search-recommendations: database migration guard linked to ATLAS-5302 and PR-9680.
- order-ledger: observability dashboard linked to ATLAS-2715 and PR-6167.

### Risks and follow-ups
- Risk: queue lag. Owner: Ravi Patel. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: queue lag. Owner: Priya Nair. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: index bloat. Owner: Iris Wang. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2023.10 - Phase 5 Resilience and Observability
- Release date: 2023-10-21
- Release captain: Samir Rao
- Goal: burn down incidents, improve SLOs, add tracing

### Changes
- auth-gateway: rollback drill linked to ATLAS-5480 and PR-11577.
- cart-service: observability dashboard linked to ATLAS-2352 and PR-12068.
- payment-orchestrator: feature flag rollout linked to ATLAS-2270 and PR-6941.
- loyalty-service: feature flag rollout linked to ATLAS-3745 and PR-11625.
- tax-service: rollback drill linked to ATLAS-1037 and PR-7308.

### Risks and follow-ups
- Risk: queue lag. Owner: Aisha Khan. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: support escalation. Owner: Maya Chen. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: payment retry storm. Owner: Yara Haddad. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2023.11 - Phase 5 Resilience and Observability
- Release date: 2023-11-21
- Release captain: Harper Lee
- Goal: burn down incidents, improve SLOs, add tracing

### Changes
- cart-service: database migration guard linked to ATLAS-1937 and PR-9383.
- order-ledger: feature flag rollout linked to ATLAS-2580 and PR-5622.
- tax-service: database migration guard linked to ATLAS-2344 and PR-8877.
- analytics-pipeline: support macro update linked to ATLAS-2119 and PR-6760.
- loyalty-service: rollback drill linked to ATLAS-2124 and PR-8923.

### Risks and follow-ups
- Risk: payment retry storm. Owner: Luca Moretti. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: queue lag. Owner: Iris Wang. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: support escalation. Owner: Fatima Noor. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2023.12 - Phase 5 Resilience and Observability
- Release date: 2023-12-21
- Release captain: Iris Wang
- Goal: burn down incidents, improve SLOs, add tracing

### Changes
- checkout-api: feature flag rollout linked to ATLAS-5218 and PR-9474.
- analytics-pipeline: rollback drill linked to ATLAS-2096 and PR-7016.
- order-ledger: contract test hardening linked to ATLAS-3011 and PR-5208.
- tax-service: observability dashboard linked to ATLAS-6161 and PR-12590.
- checkout-api: rollback drill linked to ATLAS-5347 and PR-7961.

### Risks and follow-ups
- Risk: latency burn. Owner: Nora Singh. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: queue lag. Owner: Noah Evans. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: latency burn. Owner: Yara Haddad. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2024.01 - Phase 6 Order Orchestration
- Release date: 2024-01-21
- Release captain: Fatima Noor
- Goal: orchestrate inventory reservation and async order ledger

### Changes
- pricing-engine: contract test hardening linked to ATLAS-2082 and PR-12320.
- auth-gateway: feature flag rollout linked to ATLAS-4457 and PR-7786.
- search-recommendations: feature flag rollout linked to ATLAS-5487 and PR-7990.
- inventory-reservation: support macro update linked to ATLAS-5649 and PR-5244.
- tax-service: support macro update linked to ATLAS-1758 and PR-6409.

### Risks and follow-ups
- Risk: support escalation. Owner: Dmitri Volkov. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: latency burn. Owner: Maya Chen. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: queue lag. Owner: Luca Moretti. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2024.02 - Phase 6 Order Orchestration
- Release date: 2024-02-21
- Release captain: Jon Bell
- Goal: orchestrate inventory reservation and async order ledger

### Changes
- tax-service: feature flag rollout linked to ATLAS-6158 and PR-7314.
- order-ledger: observability dashboard linked to ATLAS-3091 and PR-5067.
- pricing-engine: observability dashboard linked to ATLAS-1604 and PR-9664.
- auth-gateway: observability dashboard linked to ATLAS-2334 and PR-5858.
- search-recommendations: feature flag rollout linked to ATLAS-2455 and PR-6704.

### Risks and follow-ups
- Risk: payment retry storm. Owner: Elena Petrova. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: payment retry storm. Owner: Grace Kim. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: queue lag. Owner: Dmitri Volkov. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2024.03 - Phase 6 Order Orchestration
- Release date: 2024-03-21
- Release captain: Harper Lee
- Goal: orchestrate inventory reservation and async order ledger

### Changes
- auth-gateway: database migration guard linked to ATLAS-1788 and PR-6383.
- search-recommendations: observability dashboard linked to ATLAS-2673 and PR-12365.
- payment-orchestrator: rollback drill linked to ATLAS-1522 and PR-7276.
- checkout-api: rollback drill linked to ATLAS-1604 and PR-5500.
- search-recommendations: database migration guard linked to ATLAS-3114 and PR-9455.

### Risks and follow-ups
- Risk: queue lag. Owner: Grace Kim. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: queue lag. Owner: Owen Brooks. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: support escalation. Owner: Grace Kim. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2024.04 - Phase 6 Order Orchestration
- Release date: 2024-04-21
- Release captain: Ravi Patel
- Goal: orchestrate inventory reservation and async order ledger

### Changes
- order-ledger: rollback drill linked to ATLAS-3249 and PR-9224.
- tax-service: support macro update linked to ATLAS-4812 and PR-7736.
- order-ledger: feature flag rollout linked to ATLAS-1931 and PR-8588.
- payment-orchestrator: contract test hardening linked to ATLAS-4786 and PR-5281.
- checkout-api: contract test hardening linked to ATLAS-3588 and PR-8923.

### Risks and follow-ups
- Risk: tax mismatch. Owner: Priya Nair. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: index bloat. Owner: Ben Carter. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: latency burn. Owner: Harper Lee. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2024.05 - Phase 6 Order Orchestration
- Release date: 2024-05-21
- Release captain: Jon Bell
- Goal: orchestrate inventory reservation and async order ledger

### Changes
- cart-service: observability dashboard linked to ATLAS-4138 and PR-7953.
- analytics-pipeline: support macro update linked to ATLAS-2821 and PR-7444.
- cart-service: feature flag rollout linked to ATLAS-4967 and PR-5372.
- inventory-reservation: feature flag rollout linked to ATLAS-2824 and PR-10748.
- checkout-api: observability dashboard linked to ATLAS-3079 and PR-8060.

### Risks and follow-ups
- Risk: payment retry storm. Owner: Yara Haddad. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: latency burn. Owner: Grace Kim. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: payment retry storm. Owner: Fatima Noor. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2024.06 - Phase 6 Order Orchestration
- Release date: 2024-06-21
- Release captain: Aisha Khan
- Goal: orchestrate inventory reservation and async order ledger

### Changes
- analytics-pipeline: observability dashboard linked to ATLAS-4607 and PR-11910.
- payment-orchestrator: feature flag rollout linked to ATLAS-2057 and PR-10026.
- pricing-engine: observability dashboard linked to ATLAS-5523 and PR-5411.
- loyalty-service: contract test hardening linked to ATLAS-1489 and PR-8127.
- payment-orchestrator: feature flag rollout linked to ATLAS-4216 and PR-5094.

### Risks and follow-ups
- Risk: latency burn. Owner: Theo Martin. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: tax mismatch. Owner: Luca Moretti. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: support escalation. Owner: Samir Rao. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2024.07 - Phase 6 Order Orchestration
- Release date: 2024-07-21
- Release captain: Jon Bell
- Goal: orchestrate inventory reservation and async order ledger

### Changes
- payment-orchestrator: contract test hardening linked to ATLAS-2957 and PR-6039.
- tax-service: contract test hardening linked to ATLAS-2680 and PR-8773.
- cart-service: observability dashboard linked to ATLAS-5091 and PR-5188.
- notification-service: rollback drill linked to ATLAS-4930 and PR-8275.
- inventory-reservation: feature flag rollout linked to ATLAS-2251 and PR-9934.

### Risks and follow-ups
- Risk: payment retry storm. Owner: Dmitri Volkov. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: index bloat. Owner: Samir Rao. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: support escalation. Owner: Fatima Noor. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2024.08 - Phase 6 Order Orchestration
- Release date: 2024-08-21
- Release captain: Noah Evans
- Goal: orchestrate inventory reservation and async order ledger

### Changes
- cart-service: feature flag rollout linked to ATLAS-5122 and PR-6706.
- order-ledger: contract test hardening linked to ATLAS-2109 and PR-10402.
- inventory-reservation: rollback drill linked to ATLAS-6169 and PR-9274.
- loyalty-service: observability dashboard linked to ATLAS-3184 and PR-12354.
- pricing-engine: observability dashboard linked to ATLAS-4077 and PR-6783.

### Risks and follow-ups
- Risk: tax mismatch. Owner: Dmitri Volkov. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: support escalation. Owner: Jon Bell. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: index bloat. Owner: Aisha Khan. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2024.09 - Phase 6 Order Orchestration
- Release date: 2024-09-21
- Release captain: Mateo Garcia
- Goal: orchestrate inventory reservation and async order ledger

### Changes
- checkout-api: contract test hardening linked to ATLAS-4051 and PR-5576.
- order-ledger: rollback drill linked to ATLAS-4753 and PR-7128.
- inventory-reservation: support macro update linked to ATLAS-1322 and PR-12032.
- analytics-pipeline: rollback drill linked to ATLAS-5269 and PR-7475.
- search-recommendations: support macro update linked to ATLAS-1061 and PR-5376.

### Risks and follow-ups
- Risk: index bloat. Owner: Sara Novak. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: payment retry storm. Owner: Samir Rao. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: support escalation. Owner: Harper Lee. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2024.10 - Phase 6 Order Orchestration
- Release date: 2024-10-21
- Release captain: Ben Carter
- Goal: orchestrate inventory reservation and async order ledger

### Changes
- checkout-api: observability dashboard linked to ATLAS-5193 and PR-11624.
- pricing-engine: rollback drill linked to ATLAS-6163 and PR-7596.
- inventory-reservation: feature flag rollout linked to ATLAS-5373 and PR-6729.
- auth-gateway: observability dashboard linked to ATLAS-6070 and PR-8346.
- search-recommendations: database migration guard linked to ATLAS-4123 and PR-7618.

### Risks and follow-ups
- Risk: tax mismatch. Owner: Dmitri Volkov. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: tax mismatch. Owner: Luca Moretti. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: tax mismatch. Owner: Victor Silva. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2024.11 - Phase 6 Order Orchestration
- Release date: 2024-11-21
- Release captain: Ravi Patel
- Goal: orchestrate inventory reservation and async order ledger

### Changes
- tax-service: rollback drill linked to ATLAS-5410 and PR-9064.
- tax-service: support macro update linked to ATLAS-5660 and PR-7316.
- search-recommendations: observability dashboard linked to ATLAS-5703 and PR-6535.
- auth-gateway: rollback drill linked to ATLAS-4033 and PR-10468.
- loyalty-service: feature flag rollout linked to ATLAS-2580 and PR-5631.

### Risks and follow-ups
- Risk: latency burn. Owner: Dmitri Volkov. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: queue lag. Owner: Luca Moretti. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: queue lag. Owner: Ravi Patel. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2024.12 - Phase 6 Order Orchestration
- Release date: 2024-12-21
- Release captain: Harper Lee
- Goal: orchestrate inventory reservation and async order ledger

### Changes
- tax-service: feature flag rollout linked to ATLAS-1748 and PR-9804.
- notification-service: feature flag rollout linked to ATLAS-5781 and PR-7980.
- checkout-api: observability dashboard linked to ATLAS-3420 and PR-9712.
- checkout-api: contract test hardening linked to ATLAS-3935 and PR-6320.
- search-recommendations: rollback drill linked to ATLAS-5637 and PR-11234.

### Risks and follow-ups
- Risk: queue lag. Owner: Owen Brooks. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: tax mismatch. Owner: Samir Rao. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: index bloat. Owner: Jon Bell. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2025.01 - Phase 7 Checkout Cutover
- Release date: 2025-01-21
- Release captain: Noah Evans
- Goal: route traffic to Atlas and deprecate monolith paths

### Changes
- checkout-api: observability dashboard linked to ATLAS-1158 and PR-11431.
- payment-orchestrator: support macro update linked to ATLAS-3628 and PR-8973.
- inventory-reservation: contract test hardening linked to ATLAS-4162 and PR-8006.
- pricing-engine: support macro update linked to ATLAS-1017 and PR-7906.
- auth-gateway: database migration guard linked to ATLAS-2184 and PR-6604.

### Risks and follow-ups
- Risk: latency burn. Owner: Nora Singh. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: latency burn. Owner: Yara Haddad. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: index bloat. Owner: Owen Brooks. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2025.02 - Phase 7 Checkout Cutover
- Release date: 2025-02-21
- Release captain: Noah Evans
- Goal: route traffic to Atlas and deprecate monolith paths

### Changes
- auth-gateway: database migration guard linked to ATLAS-4445 and PR-9672.
- payment-orchestrator: support macro update linked to ATLAS-5629 and PR-5937.
- cart-service: feature flag rollout linked to ATLAS-3061 and PR-7365.
- tax-service: contract test hardening linked to ATLAS-1147 and PR-7118.
- tax-service: support macro update linked to ATLAS-3915 and PR-10513.

### Risks and follow-ups
- Risk: payment retry storm. Owner: Harper Lee. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: tax mismatch. Owner: Victor Silva. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: latency burn. Owner: Dmitri Volkov. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2025.03 - Phase 7 Checkout Cutover
- Release date: 2025-03-21
- Release captain: Elena Petrova
- Goal: route traffic to Atlas and deprecate monolith paths

### Changes
- cart-service: feature flag rollout linked to ATLAS-4006 and PR-11815.
- analytics-pipeline: support macro update linked to ATLAS-1521 and PR-7585.
- cart-service: feature flag rollout linked to ATLAS-1449 and PR-8951.
- order-ledger: contract test hardening linked to ATLAS-4732 and PR-5069.
- analytics-pipeline: support macro update linked to ATLAS-2405 and PR-9314.

### Risks and follow-ups
- Risk: payment retry storm. Owner: Theo Martin. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: queue lag. Owner: Aisha Khan. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: support escalation. Owner: Theo Martin. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2025.04 - Phase 7 Checkout Cutover
- Release date: 2025-04-21
- Release captain: Ravi Patel
- Goal: route traffic to Atlas and deprecate monolith paths

### Changes
- search-recommendations: feature flag rollout linked to ATLAS-3129 and PR-11297.
- analytics-pipeline: feature flag rollout linked to ATLAS-3631 and PR-5892.
- search-recommendations: database migration guard linked to ATLAS-6027 and PR-9542.
- search-recommendations: feature flag rollout linked to ATLAS-3344 and PR-6463.
- notification-service: support macro update linked to ATLAS-4557 and PR-12308.

### Risks and follow-ups
- Risk: latency burn. Owner: Mateo Garcia. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: support escalation. Owner: Ravi Patel. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: queue lag. Owner: Grace Kim. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2025.05 - Phase 7 Checkout Cutover
- Release date: 2025-05-21
- Release captain: Elena Petrova
- Goal: route traffic to Atlas and deprecate monolith paths

### Changes
- pricing-engine: observability dashboard linked to ATLAS-2033 and PR-5745.
- payment-orchestrator: feature flag rollout linked to ATLAS-2832 and PR-5234.
- notification-service: database migration guard linked to ATLAS-1168 and PR-6452.
- auth-gateway: observability dashboard linked to ATLAS-2883 and PR-5182.
- cart-service: database migration guard linked to ATLAS-6004 and PR-8994.

### Risks and follow-ups
- Risk: latency burn. Owner: Ben Carter. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: support escalation. Owner: Anika Sharma. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: support escalation. Owner: Sara Novak. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2025.06 - Phase 7 Checkout Cutover
- Release date: 2025-06-21
- Release captain: Ben Carter
- Goal: route traffic to Atlas and deprecate monolith paths

### Changes
- order-ledger: rollback drill linked to ATLAS-3441 and PR-7219.
- cart-service: rollback drill linked to ATLAS-4110 and PR-8496.
- order-ledger: feature flag rollout linked to ATLAS-5204 and PR-5282.
- inventory-reservation: observability dashboard linked to ATLAS-2954 and PR-8143.
- loyalty-service: database migration guard linked to ATLAS-2658 and PR-7706.

### Risks and follow-ups
- Risk: payment retry storm. Owner: Victor Silva. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: tax mismatch. Owner: Jon Bell. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: tax mismatch. Owner: Ravi Patel. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2025.07 - Phase 7 Checkout Cutover
- Release date: 2025-07-21
- Release captain: Noah Evans
- Goal: route traffic to Atlas and deprecate monolith paths

### Changes
- inventory-reservation: observability dashboard linked to ATLAS-1300 and PR-6914.
- pricing-engine: contract test hardening linked to ATLAS-1980 and PR-9488.
- inventory-reservation: support macro update linked to ATLAS-3646 and PR-10745.
- notification-service: support macro update linked to ATLAS-5840 and PR-7390.
- payment-orchestrator: rollback drill linked to ATLAS-2946 and PR-7490.

### Risks and follow-ups
- Risk: support escalation. Owner: Samir Rao. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: latency burn. Owner: Owen Brooks. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: queue lag. Owner: Aisha Khan. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2025.08 - Phase 7 Checkout Cutover
- Release date: 2025-08-21
- Release captain: Kim Tan
- Goal: route traffic to Atlas and deprecate monolith paths

### Changes
- cart-service: database migration guard linked to ATLAS-4615 and PR-10166.
- tax-service: database migration guard linked to ATLAS-3126 and PR-6063.
- pricing-engine: rollback drill linked to ATLAS-2466 and PR-10733.
- tax-service: database migration guard linked to ATLAS-1959 and PR-8612.
- auth-gateway: support macro update linked to ATLAS-1004 and PR-7465.

### Risks and follow-ups
- Risk: queue lag. Owner: Dmitri Volkov. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: index bloat. Owner: Jon Bell. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: support escalation. Owner: Elena Petrova. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2025.09 - Phase 7 Checkout Cutover
- Release date: 2025-09-21
- Release captain: Ben Carter
- Goal: route traffic to Atlas and deprecate monolith paths

### Changes
- tax-service: support macro update linked to ATLAS-2626 and PR-11227.
- tax-service: database migration guard linked to ATLAS-3162 and PR-5855.
- inventory-reservation: support macro update linked to ATLAS-6009 and PR-9282.
- tax-service: feature flag rollout linked to ATLAS-5015 and PR-10460.
- inventory-reservation: rollback drill linked to ATLAS-2359 and PR-6935.

### Risks and follow-ups
- Risk: payment retry storm. Owner: Ravi Patel. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: support escalation. Owner: Dmitri Volkov. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: tax mismatch. Owner: Ben Carter. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2025.10 - Phase 7 Checkout Cutover
- Release date: 2025-10-21
- Release captain: Iris Wang
- Goal: route traffic to Atlas and deprecate monolith paths

### Changes
- analytics-pipeline: rollback drill linked to ATLAS-2701 and PR-6814.
- notification-service: support macro update linked to ATLAS-3589 and PR-8327.
- loyalty-service: rollback drill linked to ATLAS-5016 and PR-7094.
- checkout-api: contract test hardening linked to ATLAS-5502 and PR-7256.
- loyalty-service: feature flag rollout linked to ATLAS-4192 and PR-6334.

### Risks and follow-ups
- Risk: index bloat. Owner: Nora Singh. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: tax mismatch. Owner: Ben Carter. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: payment retry storm. Owner: Victor Silva. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2025.11 - Phase 7 Checkout Cutover
- Release date: 2025-11-21
- Release captain: Victor Silva
- Goal: route traffic to Atlas and deprecate monolith paths

### Changes
- order-ledger: database migration guard linked to ATLAS-3931 and PR-9911.
- checkout-api: feature flag rollout linked to ATLAS-5904 and PR-5235.
- tax-service: contract test hardening linked to ATLAS-1239 and PR-8858.
- order-ledger: rollback drill linked to ATLAS-4568 and PR-5306.
- cart-service: rollback drill linked to ATLAS-2903 and PR-11314.

### Risks and follow-ups
- Risk: tax mismatch. Owner: Sara Novak. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: payment retry storm. Owner: Anika Sharma. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: latency burn. Owner: Priya Nair. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2025.12 - Phase 7 Checkout Cutover
- Release date: 2025-12-21
- Release captain: Nora Singh
- Goal: route traffic to Atlas and deprecate monolith paths

### Changes
- pricing-engine: support macro update linked to ATLAS-3089 and PR-8882.
- loyalty-service: feature flag rollout linked to ATLAS-5384 and PR-7156.
- tax-service: database migration guard linked to ATLAS-5793 and PR-9161.
- tax-service: feature flag rollout linked to ATLAS-1479 and PR-11432.
- checkout-api: feature flag rollout linked to ATLAS-5762 and PR-11266.

### Risks and follow-ups
- Risk: payment retry storm. Owner: Owen Brooks. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: tax mismatch. Owner: Sara Novak. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: queue lag. Owner: Maya Chen. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2026.01 - Phase 8 Scale and Handoff
- Release date: 2026-01-21
- Release captain: Elena Petrova
- Goal: prepare KT, reduce toil, close migration gaps

### Changes
- pricing-engine: support macro update linked to ATLAS-5774 and PR-9680.
- analytics-pipeline: database migration guard linked to ATLAS-1734 and PR-9946.
- tax-service: rollback drill linked to ATLAS-3808 and PR-8981.
- pricing-engine: rollback drill linked to ATLAS-3991 and PR-7014.
- inventory-reservation: contract test hardening linked to ATLAS-5968 and PR-10580.

### Risks and follow-ups
- Risk: support escalation. Owner: Maya Chen. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: payment retry storm. Owner: Grace Kim. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: index bloat. Owner: Priya Nair. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2026.02 - Phase 8 Scale and Handoff
- Release date: 2026-02-21
- Release captain: Kim Tan
- Goal: prepare KT, reduce toil, close migration gaps

### Changes
- search-recommendations: support macro update linked to ATLAS-4454 and PR-10462.
- payment-orchestrator: rollback drill linked to ATLAS-5385 and PR-7306.
- inventory-reservation: database migration guard linked to ATLAS-1616 and PR-9322.
- tax-service: feature flag rollout linked to ATLAS-1174 and PR-6706.
- tax-service: contract test hardening linked to ATLAS-2541 and PR-9591.

### Risks and follow-ups
- Risk: tax mismatch. Owner: Iris Wang. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: tax mismatch. Owner: Yara Haddad. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: support escalation. Owner: Owen Brooks. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2026.03 - Phase 8 Scale and Handoff
- Release date: 2026-03-21
- Release captain: Noah Evans
- Goal: prepare KT, reduce toil, close migration gaps

### Changes
- order-ledger: database migration guard linked to ATLAS-2635 and PR-6258.
- inventory-reservation: observability dashboard linked to ATLAS-2197 and PR-9631.
- checkout-api: rollback drill linked to ATLAS-1624 and PR-8197.
- checkout-api: database migration guard linked to ATLAS-5852 and PR-7884.
- cart-service: rollback drill linked to ATLAS-5472 and PR-6940.

### Risks and follow-ups
- Risk: support escalation. Owner: Sara Novak. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: payment retry storm. Owner: Ravi Patel. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: latency burn. Owner: Iris Wang. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2026.04 - Phase 8 Scale and Handoff
- Release date: 2026-04-21
- Release captain: Victor Silva
- Goal: prepare KT, reduce toil, close migration gaps

### Changes
- inventory-reservation: contract test hardening linked to ATLAS-5584 and PR-7200.
- notification-service: support macro update linked to ATLAS-1663 and PR-5400.
- search-recommendations: support macro update linked to ATLAS-4400 and PR-5495.
- payment-orchestrator: observability dashboard linked to ATLAS-3883 and PR-7410.
- cart-service: feature flag rollout linked to ATLAS-6107 and PR-5663.

### Risks and follow-ups
- Risk: payment retry storm. Owner: Grace Kim. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: payment retry storm. Owner: Theo Martin. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: queue lag. Owner: Anika Sharma. Evidence: Grafana, PagerDuty, Jira, and Confluence.

## REL-2026.05 - Phase 8 Scale and Handoff
- Release date: 2026-05-15
- Release captain: Kim Tan
- Goal: prepare KT, reduce toil, close migration gaps

### Changes
- order-ledger: observability dashboard linked to ATLAS-6060 and PR-9671.
- loyalty-service: feature flag rollout linked to ATLAS-2534 and PR-5427.
- search-recommendations: database migration guard linked to ATLAS-6114 and PR-8063.
- inventory-reservation: support macro update linked to ATLAS-5198 and PR-8818.
- pricing-engine: observability dashboard linked to ATLAS-2230 and PR-10757.

### Risks and follow-ups
- Risk: tax mismatch. Owner: Ben Carter. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: latency burn. Owner: Mateo Garcia. Evidence: Grafana, PagerDuty, Jira, and Confluence.
- Risk: support escalation. Owner: Jon Bell. Evidence: Grafana, PagerDuty, Jira, and Confluence.
