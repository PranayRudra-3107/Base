# Project Atlas Meeting Transcripts 2018-2026

Synthetic weekly steering, architecture, release, incident, and KT meeting notes.

## Meeting MTG-0001 - 2018-06-01 - SLO Review
- Facilitator: Nora Singh
- Attendees: Elena Petrova, Owen Brooks, Mateo Garcia, Samir Rao, Iris Wang, Luca Moretti
- Focus service: payment-orchestrator
- Related evidence: ATLAS-3685, PR-18380, PD-2857

### Discussion
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- The team reviewed payment-orchestrator readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Risk: payment-orchestrator ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-3685.
- The team reviewed payment-orchestrator readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- The team reviewed payment-orchestrator readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.

### Decisions and Actions
- Owner Yara Haddad will close the action item before 2018-06-15.
- Update runbook, release checklist, and dashboard annotation for payment-orchestrator.

## Meeting MTG-0002 - 2018-06-08 - Architecture Council
- Facilitator: Sara Novak
- Attendees: Nora Singh, Noah Evans, Priya Nair, Ravi Patel, Theo Martin, Yara Haddad
- Focus service: pricing-engine
- Related evidence: ATLAS-4519, PR-9853, PD-2533

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Risk: pricing-engine ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4519.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- The team reviewed pricing-engine readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.

### Decisions and Actions
- Owner Maya Chen will close the action item before 2018-06-22.
- Update runbook, release checklist, and dashboard annotation for pricing-engine.

## Meeting MTG-0003 - 2018-06-15 - SLO Review
- Facilitator: Fatima Noor
- Attendees: Owen Brooks, Victor Silva, Anika Sharma, Fatima Noor, Theo Martin, Iris Wang
- Focus service: pricing-engine
- Related evidence: ATLAS-3401, PR-16097, PD-2622

### Discussion
- Risk: pricing-engine ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-3401.
- Risk: pricing-engine ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-3401.
- Risk: pricing-engine ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-3401.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Risk: pricing-engine ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-3401.

### Decisions and Actions
- Owner Theo Martin will close the action item before 2018-06-29.
- Update runbook, release checklist, and dashboard annotation for pricing-engine.

## Meeting MTG-0004 - 2018-06-22 - Architecture Council
- Facilitator: Owen Brooks
- Attendees: Priya Nair, Victor Silva, Mateo Garcia, Aisha Khan, Fatima Noor, Owen Brooks
- Focus service: analytics-pipeline
- Related evidence: ATLAS-5531, PR-15891, PD-2600

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- The team reviewed analytics-pipeline readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Blocker: QA needs production-like seed data before approving PR-15891. The workaround is documented but not yet rehearsed by on-call.
- Risk: analytics-pipeline ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5531.
- Risk: analytics-pipeline ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5531.

### Decisions and Actions
- Owner Samir Rao will close the action item before 2018-07-06.
- Update runbook, release checklist, and dashboard annotation for analytics-pipeline.

## Meeting MTG-0005 - 2018-06-29 - Steering Review
- Facilitator: Elena Petrova
- Attendees: Fatima Noor, Mateo Garcia, Luca Moretti, Jon Bell, Iris Wang, Anika Sharma
- Focus service: cart-service
- Related evidence: ATLAS-1377, PR-11951, PD-2425

### Discussion
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Risk: cart-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-1377.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Risk: cart-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-1377.

### Decisions and Actions
- Owner Maya Chen will close the action item before 2018-07-13.
- Update runbook, release checklist, and dashboard annotation for cart-service.

## Meeting MTG-0006 - 2018-07-06 - Incident Review
- Facilitator: Victor Silva
- Attendees: Iris Wang, Elena Petrova, Yara Haddad, Anika Sharma, Ben Carter, Fatima Noor
- Focus service: tax-service
- Related evidence: ATLAS-3244, PR-8846, PD-2337

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Risk: tax-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-3244.
- The team reviewed tax-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- The team reviewed tax-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.

### Decisions and Actions
- Owner Jon Bell will close the action item before 2018-07-20.
- Update runbook, release checklist, and dashboard annotation for tax-service.

## Meeting MTG-0007 - 2018-07-13 - KT Working Session
- Facilitator: Grace Kim
- Attendees: Aisha Khan, Grace Kim, Jon Bell, Theo Martin, Victor Silva, Fatima Noor
- Focus service: payment-orchestrator
- Related evidence: ATLAS-5523, PR-11135, PD-2615

### Discussion
- Blocker: QA needs production-like seed data before approving PR-11135. The workaround is documented but not yet rehearsed by on-call.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- The team reviewed payment-orchestrator readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Blocker: QA needs production-like seed data before approving PR-11135. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Fatima Noor will close the action item before 2018-07-27.
- Update runbook, release checklist, and dashboard annotation for payment-orchestrator.

## Meeting MTG-0008 - 2018-07-20 - KT Working Session
- Facilitator: Victor Silva
- Attendees: Ben Carter, Grace Kim, Aisha Khan, Mateo Garcia, Victor Silva, Iris Wang
- Focus service: payment-orchestrator
- Related evidence: ATLAS-3325, PR-10813, PD-2307

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Risk: payment-orchestrator ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-3325.
- Risk: payment-orchestrator ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-3325.
- Risk: payment-orchestrator ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-3325.

### Decisions and Actions
- Owner Yara Haddad will close the action item before 2018-08-03.
- Update runbook, release checklist, and dashboard annotation for payment-orchestrator.

## Meeting MTG-0009 - 2018-07-27 - Release Readiness
- Facilitator: Luca Moretti
- Attendees: Mateo Garcia, Kim Tan, Dmitri Volkov, Luca Moretti, Elena Petrova, Sara Novak
- Focus service: auth-gateway
- Related evidence: ATLAS-1452, PR-5192, PD-2573

### Discussion
- Blocker: QA needs production-like seed data before approving PR-5192. The workaround is documented but not yet rehearsed by on-call.
- The team reviewed auth-gateway readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- The team reviewed auth-gateway readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Blocker: QA needs production-like seed data before approving PR-5192. The workaround is documented but not yet rehearsed by on-call.
- Blocker: QA needs production-like seed data before approving PR-5192. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Ravi Patel will close the action item before 2018-08-10.
- Update runbook, release checklist, and dashboard annotation for auth-gateway.

## Meeting MTG-0010 - 2018-08-03 - Architecture Council
- Facilitator: Fatima Noor
- Attendees: Owen Brooks, Anika Sharma, Elena Petrova, Victor Silva, Priya Nair, Yara Haddad
- Focus service: notification-service
- Related evidence: ATLAS-5491, PR-10785, PD-2538

### Discussion
- The team reviewed notification-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- The team reviewed notification-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- The team reviewed notification-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Blocker: QA needs production-like seed data before approving PR-10785. The workaround is documented but not yet rehearsed by on-call.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.

### Decisions and Actions
- Owner Nora Singh will close the action item before 2018-08-17.
- Update runbook, release checklist, and dashboard annotation for notification-service.

## Meeting MTG-0011 - 2018-08-10 - KT Working Session
- Facilitator: Noah Evans
- Attendees: Elena Petrova, Mateo Garcia, Noah Evans, Aisha Khan, Fatima Noor, Kim Tan
- Focus service: analytics-pipeline
- Related evidence: ATLAS-4273, PR-8429, PD-2663

### Discussion
- Blocker: QA needs production-like seed data before approving PR-8429. The workaround is documented but not yet rehearsed by on-call.
- Blocker: QA needs production-like seed data before approving PR-8429. The workaround is documented but not yet rehearsed by on-call.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Risk: analytics-pipeline ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4273.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.

### Decisions and Actions
- Owner Priya Nair will close the action item before 2018-08-24.
- Update runbook, release checklist, and dashboard annotation for analytics-pipeline.

## Meeting MTG-0012 - 2018-08-17 - Incident Review
- Facilitator: Maya Chen
- Attendees: Owen Brooks, Aisha Khan, Priya Nair, Maya Chen, Grace Kim, Noah Evans
- Focus service: auth-gateway
- Related evidence: ATLAS-4392, PR-18377, PD-2529

### Discussion
- Risk: auth-gateway ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4392.
- The team reviewed auth-gateway readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Blocker: QA needs production-like seed data before approving PR-18377. The workaround is documented but not yet rehearsed by on-call.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.

### Decisions and Actions
- Owner Kim Tan will close the action item before 2018-08-31.
- Update runbook, release checklist, and dashboard annotation for auth-gateway.

## Meeting MTG-0013 - 2018-08-24 - Steering Review
- Facilitator: Theo Martin
- Attendees: Nora Singh, Anika Sharma, Iris Wang, Theo Martin, Elena Petrova, Priya Nair
- Focus service: auth-gateway
- Related evidence: ATLAS-5721, PR-9850, PD-2120

### Discussion
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Risk: auth-gateway ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5721.
- The team reviewed auth-gateway readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Blocker: QA needs production-like seed data before approving PR-9850. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Harper Lee will close the action item before 2018-09-07.
- Update runbook, release checklist, and dashboard annotation for auth-gateway.

## Meeting MTG-0014 - 2018-08-31 - Incident Review
- Facilitator: Samir Rao
- Attendees: Luca Moretti, Ravi Patel, Elena Petrova, Jon Bell, Theo Martin, Kim Tan
- Focus service: search-recommendations
- Related evidence: ATLAS-2026, PR-11019, PD-2868

### Discussion
- The team reviewed search-recommendations readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- The team reviewed search-recommendations readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- The team reviewed search-recommendations readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Owen Brooks will close the action item before 2018-09-14.
- Update runbook, release checklist, and dashboard annotation for search-recommendations.

## Meeting MTG-0015 - 2018-09-07 - Steering Review
- Facilitator: Theo Martin
- Attendees: Iris Wang, Theo Martin, Maya Chen, Ravi Patel, Noah Evans, Aisha Khan
- Focus service: notification-service
- Related evidence: ATLAS-3729, PR-12170, PD-2351

### Discussion
- Blocker: QA needs production-like seed data before approving PR-12170. The workaround is documented but not yet rehearsed by on-call.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Risk: notification-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-3729.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Blocker: QA needs production-like seed data before approving PR-12170. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Dmitri Volkov will close the action item before 2018-09-21.
- Update runbook, release checklist, and dashboard annotation for notification-service.

## Meeting MTG-0016 - 2018-09-14 - KT Working Session
- Facilitator: Fatima Noor
- Attendees: Fatima Noor, Samir Rao, Sara Novak, Ben Carter, Maya Chen, Victor Silva
- Focus service: pricing-engine
- Related evidence: ATLAS-2385, PR-16751, PD-2341

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Blocker: QA needs production-like seed data before approving PR-16751. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Victor Silva will close the action item before 2018-09-28.
- Update runbook, release checklist, and dashboard annotation for pricing-engine.

## Meeting MTG-0017 - 2018-09-21 - Customer Escalation Review
- Facilitator: Fatima Noor
- Attendees: Luca Moretti, Noah Evans, Ravi Patel, Anika Sharma, Maya Chen, Dmitri Volkov
- Focus service: analytics-pipeline
- Related evidence: ATLAS-3580, PR-16993, PD-2403

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Blocker: QA needs production-like seed data before approving PR-16993. The workaround is documented but not yet rehearsed by on-call.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Risk: analytics-pipeline ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-3580.
- The team reviewed analytics-pipeline readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.

### Decisions and Actions
- Owner Ravi Patel will close the action item before 2018-10-05.
- Update runbook, release checklist, and dashboard annotation for analytics-pipeline.

## Meeting MTG-0018 - 2018-09-28 - Customer Escalation Review
- Facilitator: Priya Nair
- Attendees: Kim Tan, Victor Silva, Anika Sharma, Harper Lee, Theo Martin, Ravi Patel
- Focus service: notification-service
- Related evidence: ATLAS-5475, PR-8981, PD-2723

### Discussion
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- The team reviewed notification-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Risk: notification-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5475.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- The team reviewed notification-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.

### Decisions and Actions
- Owner Nora Singh will close the action item before 2018-10-12.
- Update runbook, release checklist, and dashboard annotation for notification-service.

## Meeting MTG-0019 - 2018-10-05 - Steering Review
- Facilitator: Mateo Garcia
- Attendees: Dmitri Volkov, Ravi Patel, Harper Lee, Victor Silva, Luca Moretti, Fatima Noor
- Focus service: inventory-reservation
- Related evidence: ATLAS-5216, PR-10556, PD-2176

### Discussion
- Blocker: QA needs production-like seed data before approving PR-10556. The workaround is documented but not yet rehearsed by on-call.
- Blocker: QA needs production-like seed data before approving PR-10556. The workaround is documented but not yet rehearsed by on-call.
- The team reviewed inventory-reservation readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- The team reviewed inventory-reservation readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.

### Decisions and Actions
- Owner Owen Brooks will close the action item before 2018-10-19.
- Update runbook, release checklist, and dashboard annotation for inventory-reservation.

## Meeting MTG-0020 - 2018-10-12 - Release Readiness
- Facilitator: Kim Tan
- Attendees: Nora Singh, Ravi Patel, Owen Brooks, Maya Chen, Sara Novak, Theo Martin
- Focus service: pricing-engine
- Related evidence: ATLAS-2008, PR-6079, PD-2535

### Discussion
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Noah Evans will close the action item before 2018-10-26.
- Update runbook, release checklist, and dashboard annotation for pricing-engine.

## Meeting MTG-0021 - 2018-10-19 - Incident Review
- Facilitator: Dmitri Volkov
- Attendees: Victor Silva, Sara Novak, Mateo Garcia, Noah Evans, Elena Petrova, Kim Tan
- Focus service: auth-gateway
- Related evidence: ATLAS-5270, PR-9999, PD-2224

### Discussion
- Risk: auth-gateway ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5270.
- The team reviewed auth-gateway readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Risk: auth-gateway ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5270.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.

### Decisions and Actions
- Owner Nora Singh will close the action item before 2018-11-02.
- Update runbook, release checklist, and dashboard annotation for auth-gateway.

## Meeting MTG-0022 - 2018-10-26 - SLO Review
- Facilitator: Nora Singh
- Attendees: Ravi Patel, Victor Silva, Noah Evans, Elena Petrova, Dmitri Volkov, Iris Wang
- Focus service: payment-orchestrator
- Related evidence: ATLAS-2416, PR-9940, PD-2631

### Discussion
- The team reviewed payment-orchestrator readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- The team reviewed payment-orchestrator readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Blocker: QA needs production-like seed data before approving PR-9940. The workaround is documented but not yet rehearsed by on-call.
- Blocker: QA needs production-like seed data before approving PR-9940. The workaround is documented but not yet rehearsed by on-call.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Iris Wang will close the action item before 2018-11-09.
- Update runbook, release checklist, and dashboard annotation for payment-orchestrator.

## Meeting MTG-0023 - 2018-11-02 - Steering Review
- Facilitator: Harper Lee
- Attendees: Sara Novak, Nora Singh, Samir Rao, Jon Bell, Owen Brooks, Ben Carter
- Focus service: analytics-pipeline
- Related evidence: ATLAS-4790, PR-8690, PD-2257

### Discussion
- Risk: analytics-pipeline ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4790.
- The team reviewed analytics-pipeline readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Risk: analytics-pipeline ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4790.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Aisha Khan will close the action item before 2018-11-16.
- Update runbook, release checklist, and dashboard annotation for analytics-pipeline.

## Meeting MTG-0024 - 2018-11-09 - Release Readiness
- Facilitator: Samir Rao
- Attendees: Elena Petrova, Owen Brooks, Jon Bell, Victor Silva, Aisha Khan, Luca Moretti
- Focus service: loyalty-service
- Related evidence: ATLAS-5289, PR-7485, PD-2479

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Blocker: QA needs production-like seed data before approving PR-7485. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Samir Rao will close the action item before 2018-11-23.
- Update runbook, release checklist, and dashboard annotation for loyalty-service.

## Meeting MTG-0025 - 2018-11-16 - Customer Escalation Review
- Facilitator: Iris Wang
- Attendees: Grace Kim, Kim Tan, Iris Wang, Dmitri Volkov, Samir Rao, Yara Haddad
- Focus service: checkout-api
- Related evidence: ATLAS-3463, PR-11063, PD-2226

### Discussion
- The team reviewed checkout-api readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- The team reviewed checkout-api readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Risk: checkout-api ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-3463.

### Decisions and Actions
- Owner Jon Bell will close the action item before 2018-11-30.
- Update runbook, release checklist, and dashboard annotation for checkout-api.

## Meeting MTG-0026 - 2018-11-23 - Release Readiness
- Facilitator: Theo Martin
- Attendees: Iris Wang, Priya Nair, Anika Sharma, Victor Silva, Nora Singh, Noah Evans
- Focus service: loyalty-service
- Related evidence: ATLAS-3073, PR-13560, PD-2806

### Discussion
- The team reviewed loyalty-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- The team reviewed loyalty-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Blocker: QA needs production-like seed data before approving PR-13560. The workaround is documented but not yet rehearsed by on-call.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Maya Chen will close the action item before 2018-12-07.
- Update runbook, release checklist, and dashboard annotation for loyalty-service.

## Meeting MTG-0027 - 2018-11-30 - Release Readiness
- Facilitator: Maya Chen
- Attendees: Grace Kim, Victor Silva, Anika Sharma, Luca Moretti, Ravi Patel, Sara Novak
- Focus service: order-ledger
- Related evidence: ATLAS-6174, PR-11415, PD-2524

### Discussion
- Risk: order-ledger ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-6174.
- Risk: order-ledger ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-6174.
- Blocker: QA needs production-like seed data before approving PR-11415. The workaround is documented but not yet rehearsed by on-call.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Blocker: QA needs production-like seed data before approving PR-11415. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Ben Carter will close the action item before 2018-12-14.
- Update runbook, release checklist, and dashboard annotation for order-ledger.

## Meeting MTG-0028 - 2018-12-07 - Architecture Council
- Facilitator: Elena Petrova
- Attendees: Victor Silva, Fatima Noor, Harper Lee, Maya Chen, Samir Rao, Dmitri Volkov
- Focus service: checkout-api
- Related evidence: ATLAS-5273, PR-15001, PD-2378

### Discussion
- Risk: checkout-api ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5273.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Risk: checkout-api ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5273.
- The team reviewed checkout-api readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.

### Decisions and Actions
- Owner Nora Singh will close the action item before 2018-12-21.
- Update runbook, release checklist, and dashboard annotation for checkout-api.

## Meeting MTG-0029 - 2018-12-14 - KT Working Session
- Facilitator: Elena Petrova
- Attendees: Elena Petrova, Iris Wang, Luca Moretti, Ben Carter, Aisha Khan, Harper Lee
- Focus service: inventory-reservation
- Related evidence: ATLAS-3258, PR-5612, PD-2697

### Discussion
- Blocker: QA needs production-like seed data before approving PR-5612. The workaround is documented but not yet rehearsed by on-call.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Risk: inventory-reservation ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-3258.
- Risk: inventory-reservation ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-3258.

### Decisions and Actions
- Owner Luca Moretti will close the action item before 2018-12-28.
- Update runbook, release checklist, and dashboard annotation for inventory-reservation.

## Meeting MTG-0030 - 2018-12-21 - KT Working Session
- Facilitator: Sara Novak
- Attendees: Dmitri Volkov, Ravi Patel, Nora Singh, Maya Chen, Jon Bell, Anika Sharma
- Focus service: analytics-pipeline
- Related evidence: ATLAS-5536, PR-16965, PD-2483

### Discussion
- Risk: analytics-pipeline ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5536.
- Blocker: QA needs production-like seed data before approving PR-16965. The workaround is documented but not yet rehearsed by on-call.
- Blocker: QA needs production-like seed data before approving PR-16965. The workaround is documented but not yet rehearsed by on-call.
- Risk: analytics-pipeline ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5536.
- Risk: analytics-pipeline ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5536.

### Decisions and Actions
- Owner Luca Moretti will close the action item before 2019-01-04.
- Update runbook, release checklist, and dashboard annotation for analytics-pipeline.

## Meeting MTG-0031 - 2018-12-28 - SLO Review
- Facilitator: Anika Sharma
- Attendees: Ben Carter, Fatima Noor, Ravi Patel, Nora Singh, Harper Lee, Mateo Garcia
- Focus service: notification-service
- Related evidence: ATLAS-3862, PR-6499, PD-2518

### Discussion
- The team reviewed notification-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- The team reviewed notification-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- The team reviewed notification-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.

### Decisions and Actions
- Owner Noah Evans will close the action item before 2019-01-11.
- Update runbook, release checklist, and dashboard annotation for notification-service.

## Meeting MTG-0032 - 2019-01-04 - Release Readiness
- Facilitator: Jon Bell
- Attendees: Luca Moretti, Jon Bell, Priya Nair, Mateo Garcia, Harper Lee, Fatima Noor
- Focus service: search-recommendations
- Related evidence: ATLAS-4645, PR-5838, PD-2486

### Discussion
- Risk: search-recommendations ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4645.
- Blocker: QA needs production-like seed data before approving PR-5838. The workaround is documented but not yet rehearsed by on-call.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Blocker: QA needs production-like seed data before approving PR-5838. The workaround is documented but not yet rehearsed by on-call.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Mateo Garcia will close the action item before 2019-01-18.
- Update runbook, release checklist, and dashboard annotation for search-recommendations.

## Meeting MTG-0033 - 2019-01-11 - SLO Review
- Facilitator: Elena Petrova
- Attendees: Sara Novak, Samir Rao, Aisha Khan, Owen Brooks, Maya Chen, Priya Nair
- Focus service: order-ledger
- Related evidence: ATLAS-5891, PR-6641, PD-2890

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Blocker: QA needs production-like seed data before approving PR-6641. The workaround is documented but not yet rehearsed by on-call.
- The team reviewed order-ledger readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Blocker: QA needs production-like seed data before approving PR-6641. The workaround is documented but not yet rehearsed by on-call.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Anika Sharma will close the action item before 2019-01-25.
- Update runbook, release checklist, and dashboard annotation for order-ledger.

## Meeting MTG-0034 - 2019-01-18 - Steering Review
- Facilitator: Elena Petrova
- Attendees: Iris Wang, Noah Evans, Yara Haddad, Kim Tan, Ravi Patel, Fatima Noor
- Focus service: auth-gateway
- Related evidence: ATLAS-4966, PR-12942, PD-2769

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- The team reviewed auth-gateway readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- The team reviewed auth-gateway readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Blocker: QA needs production-like seed data before approving PR-12942. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Dmitri Volkov will close the action item before 2019-02-01.
- Update runbook, release checklist, and dashboard annotation for auth-gateway.

## Meeting MTG-0035 - 2019-01-25 - Release Readiness
- Facilitator: Nora Singh
- Attendees: Samir Rao, Harper Lee, Mateo Garcia, Ben Carter, Theo Martin, Elena Petrova
- Focus service: inventory-reservation
- Related evidence: ATLAS-2353, PR-5594, PD-2574

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- The team reviewed inventory-reservation readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- The team reviewed inventory-reservation readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.

### Decisions and Actions
- Owner Yara Haddad will close the action item before 2019-02-08.
- Update runbook, release checklist, and dashboard annotation for inventory-reservation.

## Meeting MTG-0036 - 2019-02-01 - Incident Review
- Facilitator: Kim Tan
- Attendees: Theo Martin, Yara Haddad, Kim Tan, Iris Wang, Samir Rao, Sara Novak
- Focus service: analytics-pipeline
- Related evidence: ATLAS-5523, PR-14228, PD-2327

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Blocker: QA needs production-like seed data before approving PR-14228. The workaround is documented but not yet rehearsed by on-call.
- Risk: analytics-pipeline ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5523.

### Decisions and Actions
- Owner Maya Chen will close the action item before 2019-02-15.
- Update runbook, release checklist, and dashboard annotation for analytics-pipeline.

## Meeting MTG-0037 - 2019-02-08 - Customer Escalation Review
- Facilitator: Samir Rao
- Attendees: Fatima Noor, Aisha Khan, Yara Haddad, Samir Rao, Noah Evans, Priya Nair
- Focus service: analytics-pipeline
- Related evidence: ATLAS-3834, PR-10853, PD-2088

### Discussion
- The team reviewed analytics-pipeline readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- The team reviewed analytics-pipeline readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Blocker: QA needs production-like seed data before approving PR-10853. The workaround is documented but not yet rehearsed by on-call.
- Risk: analytics-pipeline ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-3834.

### Decisions and Actions
- Owner Harper Lee will close the action item before 2019-02-22.
- Update runbook, release checklist, and dashboard annotation for analytics-pipeline.

## Meeting MTG-0038 - 2019-02-15 - Architecture Council
- Facilitator: Anika Sharma
- Attendees: Grace Kim, Yara Haddad, Ben Carter, Mateo Garcia, Victor Silva, Nora Singh
- Focus service: cart-service
- Related evidence: ATLAS-4470, PR-15402, PD-2620

### Discussion
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Blocker: QA needs production-like seed data before approving PR-15402. The workaround is documented but not yet rehearsed by on-call.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Risk: cart-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4470.

### Decisions and Actions
- Owner Maya Chen will close the action item before 2019-03-01.
- Update runbook, release checklist, and dashboard annotation for cart-service.

## Meeting MTG-0039 - 2019-02-22 - SLO Review
- Facilitator: Jon Bell
- Attendees: Fatima Noor, Dmitri Volkov, Priya Nair, Jon Bell, Ben Carter, Luca Moretti
- Focus service: loyalty-service
- Related evidence: ATLAS-1252, PR-16518, PD-2786

### Discussion
- The team reviewed loyalty-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Blocker: QA needs production-like seed data before approving PR-16518. The workaround is documented but not yet rehearsed by on-call.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- The team reviewed loyalty-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- The team reviewed loyalty-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.

### Decisions and Actions
- Owner Nora Singh will close the action item before 2019-03-08.
- Update runbook, release checklist, and dashboard annotation for loyalty-service.

## Meeting MTG-0040 - 2019-03-01 - KT Working Session
- Facilitator: Theo Martin
- Attendees: Grace Kim, Jon Bell, Fatima Noor, Iris Wang, Yara Haddad, Mateo Garcia
- Focus service: order-ledger
- Related evidence: ATLAS-5163, PR-13450, PD-2502

### Discussion
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Risk: order-ledger ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5163.
- The team reviewed order-ledger readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.

### Decisions and Actions
- Owner Samir Rao will close the action item before 2019-03-15.
- Update runbook, release checklist, and dashboard annotation for order-ledger.

## Meeting MTG-0041 - 2019-03-08 - Incident Review
- Facilitator: Theo Martin
- Attendees: Aisha Khan, Owen Brooks, Ravi Patel, Grace Kim, Elena Petrova, Kim Tan
- Focus service: payment-orchestrator
- Related evidence: ATLAS-2382, PR-14275, PD-2841

### Discussion
- Blocker: QA needs production-like seed data before approving PR-14275. The workaround is documented but not yet rehearsed by on-call.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Blocker: QA needs production-like seed data before approving PR-14275. The workaround is documented but not yet rehearsed by on-call.
- Risk: payment-orchestrator ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2382.

### Decisions and Actions
- Owner Mateo Garcia will close the action item before 2019-03-22.
- Update runbook, release checklist, and dashboard annotation for payment-orchestrator.

## Meeting MTG-0042 - 2019-03-15 - KT Working Session
- Facilitator: Dmitri Volkov
- Attendees: Noah Evans, Maya Chen, Luca Moretti, Jon Bell, Samir Rao, Grace Kim
- Focus service: order-ledger
- Related evidence: ATLAS-1501, PR-7987, PD-2288

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Blocker: QA needs production-like seed data before approving PR-7987. The workaround is documented but not yet rehearsed by on-call.
- Blocker: QA needs production-like seed data before approving PR-7987. The workaround is documented but not yet rehearsed by on-call.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Aisha Khan will close the action item before 2019-03-29.
- Update runbook, release checklist, and dashboard annotation for order-ledger.

## Meeting MTG-0043 - 2019-03-22 - Customer Escalation Review
- Facilitator: Dmitri Volkov
- Attendees: Fatima Noor, Kim Tan, Nora Singh, Samir Rao, Anika Sharma, Mateo Garcia
- Focus service: checkout-api
- Related evidence: ATLAS-5945, PR-5245, PD-2111

### Discussion
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Risk: checkout-api ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5945.
- Blocker: QA needs production-like seed data before approving PR-5245. The workaround is documented but not yet rehearsed by on-call.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- The team reviewed checkout-api readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.

### Decisions and Actions
- Owner Harper Lee will close the action item before 2019-04-05.
- Update runbook, release checklist, and dashboard annotation for checkout-api.

## Meeting MTG-0044 - 2019-03-29 - Incident Review
- Facilitator: Anika Sharma
- Attendees: Grace Kim, Kim Tan, Ravi Patel, Luca Moretti, Yara Haddad, Maya Chen
- Focus service: payment-orchestrator
- Related evidence: ATLAS-4383, PR-7006, PD-2836

### Discussion
- The team reviewed payment-orchestrator readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- The team reviewed payment-orchestrator readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Blocker: QA needs production-like seed data before approving PR-7006. The workaround is documented but not yet rehearsed by on-call.
- Blocker: QA needs production-like seed data before approving PR-7006. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Elena Petrova will close the action item before 2019-04-12.
- Update runbook, release checklist, and dashboard annotation for payment-orchestrator.

## Meeting MTG-0045 - 2019-04-05 - Customer Escalation Review
- Facilitator: Iris Wang
- Attendees: Anika Sharma, Samir Rao, Theo Martin, Dmitri Volkov, Grace Kim, Victor Silva
- Focus service: checkout-api
- Related evidence: ATLAS-2893, PR-8947, PD-2388

### Discussion
- Blocker: QA needs production-like seed data before approving PR-8947. The workaround is documented but not yet rehearsed by on-call.
- Blocker: QA needs production-like seed data before approving PR-8947. The workaround is documented but not yet rehearsed by on-call.
- Blocker: QA needs production-like seed data before approving PR-8947. The workaround is documented but not yet rehearsed by on-call.
- Risk: checkout-api ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2893.
- Blocker: QA needs production-like seed data before approving PR-8947. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Ben Carter will close the action item before 2019-04-19.
- Update runbook, release checklist, and dashboard annotation for checkout-api.

## Meeting MTG-0046 - 2019-04-12 - SLO Review
- Facilitator: Dmitri Volkov
- Attendees: Aisha Khan, Nora Singh, Maya Chen, Fatima Noor, Dmitri Volkov, Anika Sharma
- Focus service: order-ledger
- Related evidence: ATLAS-3184, PR-7529, PD-2876

### Discussion
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- The team reviewed order-ledger readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Blocker: QA needs production-like seed data before approving PR-7529. The workaround is documented but not yet rehearsed by on-call.
- The team reviewed order-ledger readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.

### Decisions and Actions
- Owner Nora Singh will close the action item before 2019-04-26.
- Update runbook, release checklist, and dashboard annotation for order-ledger.

## Meeting MTG-0047 - 2019-04-19 - Architecture Council
- Facilitator: Noah Evans
- Attendees: Luca Moretti, Fatima Noor, Jon Bell, Maya Chen, Anika Sharma, Iris Wang
- Focus service: notification-service
- Related evidence: ATLAS-4664, PR-6461, PD-2539

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Blocker: QA needs production-like seed data before approving PR-6461. The workaround is documented but not yet rehearsed by on-call.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Risk: notification-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4664.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Theo Martin will close the action item before 2019-05-03.
- Update runbook, release checklist, and dashboard annotation for notification-service.

## Meeting MTG-0048 - 2019-04-26 - Customer Escalation Review
- Facilitator: Mateo Garcia
- Attendees: Samir Rao, Mateo Garcia, Harper Lee, Ravi Patel, Owen Brooks, Sara Novak
- Focus service: pricing-engine
- Related evidence: ATLAS-5719, PR-6283, PD-2037

### Discussion
- Risk: pricing-engine ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5719.
- Blocker: QA needs production-like seed data before approving PR-6283. The workaround is documented but not yet rehearsed by on-call.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Blocker: QA needs production-like seed data before approving PR-6283. The workaround is documented but not yet rehearsed by on-call.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.

### Decisions and Actions
- Owner Nora Singh will close the action item before 2019-05-10.
- Update runbook, release checklist, and dashboard annotation for pricing-engine.

## Meeting MTG-0049 - 2019-05-03 - Steering Review
- Facilitator: Fatima Noor
- Attendees: Anika Sharma, Fatima Noor, Priya Nair, Nora Singh, Victor Silva, Jon Bell
- Focus service: cart-service
- Related evidence: ATLAS-3338, PR-14693, PD-2264

### Discussion
- The team reviewed cart-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- The team reviewed cart-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Blocker: QA needs production-like seed data before approving PR-14693. The workaround is documented but not yet rehearsed by on-call.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.

### Decisions and Actions
- Owner Luca Moretti will close the action item before 2019-05-17.
- Update runbook, release checklist, and dashboard annotation for cart-service.

## Meeting MTG-0050 - 2019-05-10 - SLO Review
- Facilitator: Luca Moretti
- Attendees: Nora Singh, Maya Chen, Ben Carter, Jon Bell, Yara Haddad, Mateo Garcia
- Focus service: analytics-pipeline
- Related evidence: ATLAS-4986, PR-16630, PD-2774

### Discussion
- Blocker: QA needs production-like seed data before approving PR-16630. The workaround is documented but not yet rehearsed by on-call.
- Blocker: QA needs production-like seed data before approving PR-16630. The workaround is documented but not yet rehearsed by on-call.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- The team reviewed analytics-pipeline readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Blocker: QA needs production-like seed data before approving PR-16630. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Samir Rao will close the action item before 2019-05-24.
- Update runbook, release checklist, and dashboard annotation for analytics-pipeline.

## Meeting MTG-0051 - 2019-05-17 - Incident Review
- Facilitator: Iris Wang
- Attendees: Mateo Garcia, Luca Moretti, Priya Nair, Iris Wang, Sara Novak, Noah Evans
- Focus service: tax-service
- Related evidence: ATLAS-5565, PR-13838, PD-2335

### Discussion
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Risk: tax-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5565.
- The team reviewed tax-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Risk: tax-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5565.

### Decisions and Actions
- Owner Owen Brooks will close the action item before 2019-05-31.
- Update runbook, release checklist, and dashboard annotation for tax-service.

## Meeting MTG-0052 - 2019-05-24 - KT Working Session
- Facilitator: Aisha Khan
- Attendees: Iris Wang, Aisha Khan, Ravi Patel, Maya Chen, Noah Evans, Fatima Noor
- Focus service: cart-service
- Related evidence: ATLAS-2963, PR-11056, PD-2106

### Discussion
- Blocker: QA needs production-like seed data before approving PR-11056. The workaround is documented but not yet rehearsed by on-call.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Blocker: QA needs production-like seed data before approving PR-11056. The workaround is documented but not yet rehearsed by on-call.
- Blocker: QA needs production-like seed data before approving PR-11056. The workaround is documented but not yet rehearsed by on-call.
- Risk: cart-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2963.

### Decisions and Actions
- Owner Elena Petrova will close the action item before 2019-06-07.
- Update runbook, release checklist, and dashboard annotation for cart-service.

## Meeting MTG-0053 - 2019-05-31 - Customer Escalation Review
- Facilitator: Mateo Garcia
- Attendees: Samir Rao, Theo Martin, Mateo Garcia, Anika Sharma, Owen Brooks, Ben Carter
- Focus service: pricing-engine
- Related evidence: ATLAS-4034, PR-6056, PD-2305

### Discussion
- Blocker: QA needs production-like seed data before approving PR-6056. The workaround is documented but not yet rehearsed by on-call.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Risk: pricing-engine ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4034.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.

### Decisions and Actions
- Owner Harper Lee will close the action item before 2019-06-14.
- Update runbook, release checklist, and dashboard annotation for pricing-engine.

## Meeting MTG-0054 - 2019-06-07 - Steering Review
- Facilitator: Iris Wang
- Attendees: Anika Sharma, Sara Novak, Owen Brooks, Priya Nair, Yara Haddad, Maya Chen
- Focus service: notification-service
- Related evidence: ATLAS-1303, PR-17952, PD-2536

### Discussion
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Blocker: QA needs production-like seed data before approving PR-17952. The workaround is documented but not yet rehearsed by on-call.
- Risk: notification-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-1303.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Anika Sharma will close the action item before 2019-06-21.
- Update runbook, release checklist, and dashboard annotation for notification-service.

## Meeting MTG-0055 - 2019-06-14 - Steering Review
- Facilitator: Maya Chen
- Attendees: Maya Chen, Owen Brooks, Elena Petrova, Mateo Garcia, Ravi Patel, Iris Wang
- Focus service: cart-service
- Related evidence: ATLAS-4422, PR-9588, PD-2748

### Discussion
- The team reviewed cart-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- The team reviewed cart-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Blocker: QA needs production-like seed data before approving PR-9588. The workaround is documented but not yet rehearsed by on-call.
- Risk: cart-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4422.

### Decisions and Actions
- Owner Victor Silva will close the action item before 2019-06-28.
- Update runbook, release checklist, and dashboard annotation for cart-service.

## Meeting MTG-0056 - 2019-06-21 - SLO Review
- Facilitator: Aisha Khan
- Attendees: Maya Chen, Theo Martin, Fatima Noor, Yara Haddad, Dmitri Volkov, Noah Evans
- Focus service: notification-service
- Related evidence: ATLAS-1891, PR-6643, PD-2101

### Discussion
- Risk: notification-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-1891.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Risk: notification-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-1891.
- The team reviewed notification-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Maya Chen will close the action item before 2019-07-05.
- Update runbook, release checklist, and dashboard annotation for notification-service.

## Meeting MTG-0057 - 2019-06-28 - SLO Review
- Facilitator: Owen Brooks
- Attendees: Victor Silva, Ben Carter, Kim Tan, Owen Brooks, Samir Rao, Luca Moretti
- Focus service: auth-gateway
- Related evidence: ATLAS-4097, PR-17590, PD-2825

### Discussion
- Blocker: QA needs production-like seed data before approving PR-17590. The workaround is documented but not yet rehearsed by on-call.
- Risk: auth-gateway ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4097.
- Blocker: QA needs production-like seed data before approving PR-17590. The workaround is documented but not yet rehearsed by on-call.
- Risk: auth-gateway ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4097.
- The team reviewed auth-gateway readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.

### Decisions and Actions
- Owner Victor Silva will close the action item before 2019-07-12.
- Update runbook, release checklist, and dashboard annotation for auth-gateway.

## Meeting MTG-0058 - 2019-07-05 - Architecture Council
- Facilitator: Fatima Noor
- Attendees: Luca Moretti, Theo Martin, Sara Novak, Owen Brooks, Samir Rao, Nora Singh
- Focus service: pricing-engine
- Related evidence: ATLAS-2393, PR-7247, PD-2799

### Discussion
- Risk: pricing-engine ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2393.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- The team reviewed pricing-engine readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Blocker: QA needs production-like seed data before approving PR-7247. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Noah Evans will close the action item before 2019-07-19.
- Update runbook, release checklist, and dashboard annotation for pricing-engine.

## Meeting MTG-0059 - 2019-07-12 - Incident Review
- Facilitator: Anika Sharma
- Attendees: Samir Rao, Iris Wang, Fatima Noor, Maya Chen, Aisha Khan, Elena Petrova
- Focus service: payment-orchestrator
- Related evidence: ATLAS-5756, PR-12698, PD-2831

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Risk: payment-orchestrator ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5756.
- Risk: payment-orchestrator ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5756.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.

### Decisions and Actions
- Owner Yara Haddad will close the action item before 2019-07-26.
- Update runbook, release checklist, and dashboard annotation for payment-orchestrator.

## Meeting MTG-0060 - 2019-07-19 - Architecture Council
- Facilitator: Aisha Khan
- Attendees: Anika Sharma, Grace Kim, Kim Tan, Victor Silva, Sara Novak, Maya Chen
- Focus service: pricing-engine
- Related evidence: ATLAS-4448, PR-14227, PD-2319

### Discussion
- Blocker: QA needs production-like seed data before approving PR-14227. The workaround is documented but not yet rehearsed by on-call.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Blocker: QA needs production-like seed data before approving PR-14227. The workaround is documented but not yet rehearsed by on-call.
- Blocker: QA needs production-like seed data before approving PR-14227. The workaround is documented but not yet rehearsed by on-call.
- Risk: pricing-engine ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4448.

### Decisions and Actions
- Owner Yara Haddad will close the action item before 2019-08-02.
- Update runbook, release checklist, and dashboard annotation for pricing-engine.

## Meeting MTG-0061 - 2019-07-26 - Steering Review
- Facilitator: Ravi Patel
- Attendees: Samir Rao, Owen Brooks, Nora Singh, Grace Kim, Elena Petrova, Victor Silva
- Focus service: tax-service
- Related evidence: ATLAS-5952, PR-10212, PD-2405

### Discussion
- Risk: tax-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5952.
- Risk: tax-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5952.
- Blocker: QA needs production-like seed data before approving PR-10212. The workaround is documented but not yet rehearsed by on-call.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- The team reviewed tax-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.

### Decisions and Actions
- Owner Grace Kim will close the action item before 2019-08-09.
- Update runbook, release checklist, and dashboard annotation for tax-service.

## Meeting MTG-0062 - 2019-08-02 - KT Working Session
- Facilitator: Maya Chen
- Attendees: Kim Tan, Fatima Noor, Theo Martin, Ben Carter, Sara Novak, Jon Bell
- Focus service: notification-service
- Related evidence: ATLAS-2658, PR-12467, PD-2576

### Discussion
- The team reviewed notification-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.

### Decisions and Actions
- Owner Ravi Patel will close the action item before 2019-08-16.
- Update runbook, release checklist, and dashboard annotation for notification-service.

## Meeting MTG-0063 - 2019-08-09 - Release Readiness
- Facilitator: Ravi Patel
- Attendees: Priya Nair, Elena Petrova, Nora Singh, Anika Sharma, Mateo Garcia, Sara Novak
- Focus service: loyalty-service
- Related evidence: ATLAS-2879, PR-13812, PD-2040

### Discussion
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Blocker: QA needs production-like seed data before approving PR-13812. The workaround is documented but not yet rehearsed by on-call.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- The team reviewed loyalty-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Nora Singh will close the action item before 2019-08-23.
- Update runbook, release checklist, and dashboard annotation for loyalty-service.

## Meeting MTG-0064 - 2019-08-16 - Steering Review
- Facilitator: Luca Moretti
- Attendees: Noah Evans, Owen Brooks, Elena Petrova, Victor Silva, Grace Kim, Harper Lee
- Focus service: cart-service
- Related evidence: ATLAS-1400, PR-8258, PD-2875

### Discussion
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Risk: cart-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-1400.
- Blocker: QA needs production-like seed data before approving PR-8258. The workaround is documented but not yet rehearsed by on-call.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- The team reviewed cart-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.

### Decisions and Actions
- Owner Grace Kim will close the action item before 2019-08-30.
- Update runbook, release checklist, and dashboard annotation for cart-service.

## Meeting MTG-0065 - 2019-08-23 - KT Working Session
- Facilitator: Dmitri Volkov
- Attendees: Samir Rao, Kim Tan, Victor Silva, Ben Carter, Noah Evans, Jon Bell
- Focus service: notification-service
- Related evidence: ATLAS-6145, PR-17949, PD-2199

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- The team reviewed notification-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.

### Decisions and Actions
- Owner Kim Tan will close the action item before 2019-09-06.
- Update runbook, release checklist, and dashboard annotation for notification-service.

## Meeting MTG-0066 - 2019-08-30 - Steering Review
- Facilitator: Yara Haddad
- Attendees: Elena Petrova, Anika Sharma, Mateo Garcia, Fatima Noor, Grace Kim, Harper Lee
- Focus service: order-ledger
- Related evidence: ATLAS-4146, PR-11436, PD-2668

### Discussion
- Risk: order-ledger ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4146.
- Risk: order-ledger ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4146.
- Risk: order-ledger ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4146.
- The team reviewed order-ledger readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Blocker: QA needs production-like seed data before approving PR-11436. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Luca Moretti will close the action item before 2019-09-13.
- Update runbook, release checklist, and dashboard annotation for order-ledger.

## Meeting MTG-0067 - 2019-09-06 - Architecture Council
- Facilitator: Mateo Garcia
- Attendees: Aisha Khan, Owen Brooks, Nora Singh, Samir Rao, Victor Silva, Fatima Noor
- Focus service: analytics-pipeline
- Related evidence: ATLAS-1637, PR-5132, PD-2677

### Discussion
- Risk: analytics-pipeline ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-1637.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Risk: analytics-pipeline ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-1637.
- The team reviewed analytics-pipeline readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- The team reviewed analytics-pipeline readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.

### Decisions and Actions
- Owner Priya Nair will close the action item before 2019-09-20.
- Update runbook, release checklist, and dashboard annotation for analytics-pipeline.

## Meeting MTG-0068 - 2019-09-13 - Steering Review
- Facilitator: Owen Brooks
- Attendees: Mateo Garcia, Victor Silva, Priya Nair, Iris Wang, Anika Sharma, Theo Martin
- Focus service: tax-service
- Related evidence: ATLAS-3798, PR-12209, PD-2144

### Discussion
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- The team reviewed tax-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.

### Decisions and Actions
- Owner Noah Evans will close the action item before 2019-09-27.
- Update runbook, release checklist, and dashboard annotation for tax-service.

## Meeting MTG-0069 - 2019-09-20 - Steering Review
- Facilitator: Elena Petrova
- Attendees: Grace Kim, Aisha Khan, Yara Haddad, Ben Carter, Theo Martin, Anika Sharma
- Focus service: auth-gateway
- Related evidence: ATLAS-2821, PR-15355, PD-2154

### Discussion
- Blocker: QA needs production-like seed data before approving PR-15355. The workaround is documented but not yet rehearsed by on-call.
- Blocker: QA needs production-like seed data before approving PR-15355. The workaround is documented but not yet rehearsed by on-call.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.

### Decisions and Actions
- Owner Dmitri Volkov will close the action item before 2019-10-04.
- Update runbook, release checklist, and dashboard annotation for auth-gateway.

## Meeting MTG-0070 - 2019-09-27 - Customer Escalation Review
- Facilitator: Ravi Patel
- Attendees: Kim Tan, Samir Rao, Sara Novak, Priya Nair, Jon Bell, Ravi Patel
- Focus service: search-recommendations
- Related evidence: ATLAS-3118, PR-8510, PD-2562

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Blocker: QA needs production-like seed data before approving PR-8510. The workaround is documented but not yet rehearsed by on-call.
- Blocker: QA needs production-like seed data before approving PR-8510. The workaround is documented but not yet rehearsed by on-call.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- The team reviewed search-recommendations readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.

### Decisions and Actions
- Owner Noah Evans will close the action item before 2019-10-11.
- Update runbook, release checklist, and dashboard annotation for search-recommendations.

## Meeting MTG-0071 - 2019-10-04 - Release Readiness
- Facilitator: Elena Petrova
- Attendees: Owen Brooks, Maya Chen, Priya Nair, Ravi Patel, Jon Bell, Grace Kim
- Focus service: payment-orchestrator
- Related evidence: ATLAS-2788, PR-11411, PD-2815

### Discussion
- Risk: payment-orchestrator ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2788.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Blocker: QA needs production-like seed data before approving PR-11411. The workaround is documented but not yet rehearsed by on-call.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.

### Decisions and Actions
- Owner Mateo Garcia will close the action item before 2019-10-18.
- Update runbook, release checklist, and dashboard annotation for payment-orchestrator.

## Meeting MTG-0072 - 2019-10-11 - Incident Review
- Facilitator: Ben Carter
- Attendees: Luca Moretti, Sara Novak, Aisha Khan, Priya Nair, Iris Wang, Kim Tan
- Focus service: analytics-pipeline
- Related evidence: ATLAS-3242, PR-13935, PD-2432

### Discussion
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Blocker: QA needs production-like seed data before approving PR-13935. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Dmitri Volkov will close the action item before 2019-10-25.
- Update runbook, release checklist, and dashboard annotation for analytics-pipeline.

## Meeting MTG-0073 - 2019-10-18 - Release Readiness
- Facilitator: Sara Novak
- Attendees: Harper Lee, Aisha Khan, Dmitri Volkov, Victor Silva, Nora Singh, Owen Brooks
- Focus service: checkout-api
- Related evidence: ATLAS-2229, PR-6556, PD-2058

### Discussion
- The team reviewed checkout-api readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- The team reviewed checkout-api readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- The team reviewed checkout-api readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Risk: checkout-api ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2229.

### Decisions and Actions
- Owner Ravi Patel will close the action item before 2019-11-01.
- Update runbook, release checklist, and dashboard annotation for checkout-api.

## Meeting MTG-0074 - 2019-10-25 - Steering Review
- Facilitator: Dmitri Volkov
- Attendees: Jon Bell, Harper Lee, Ravi Patel, Ben Carter, Mateo Garcia, Kim Tan
- Focus service: loyalty-service
- Related evidence: ATLAS-5309, PR-11576, PD-2604

### Discussion
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Risk: loyalty-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5309.
- Risk: loyalty-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5309.
- The team reviewed loyalty-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- The team reviewed loyalty-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.

### Decisions and Actions
- Owner Jon Bell will close the action item before 2019-11-08.
- Update runbook, release checklist, and dashboard annotation for loyalty-service.

## Meeting MTG-0075 - 2019-11-01 - Architecture Council
- Facilitator: Samir Rao
- Attendees: Elena Petrova, Fatima Noor, Yara Haddad, Victor Silva, Harper Lee, Sara Novak
- Focus service: inventory-reservation
- Related evidence: ATLAS-2139, PR-7507, PD-2856

### Discussion
- The team reviewed inventory-reservation readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Blocker: QA needs production-like seed data before approving PR-7507. The workaround is documented but not yet rehearsed by on-call.
- Risk: inventory-reservation ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2139.
- Risk: inventory-reservation ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2139.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Victor Silva will close the action item before 2019-11-15.
- Update runbook, release checklist, and dashboard annotation for inventory-reservation.

## Meeting MTG-0076 - 2019-11-08 - Customer Escalation Review
- Facilitator: Priya Nair
- Attendees: Owen Brooks, Dmitri Volkov, Priya Nair, Victor Silva, Noah Evans, Maya Chen
- Focus service: payment-orchestrator
- Related evidence: ATLAS-1161, PR-6462, PD-2499

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Blocker: QA needs production-like seed data before approving PR-6462. The workaround is documented but not yet rehearsed by on-call.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- The team reviewed payment-orchestrator readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.

### Decisions and Actions
- Owner Harper Lee will close the action item before 2019-11-22.
- Update runbook, release checklist, and dashboard annotation for payment-orchestrator.

## Meeting MTG-0077 - 2019-11-15 - Steering Review
- Facilitator: Yara Haddad
- Attendees: Noah Evans, Ravi Patel, Samir Rao, Fatima Noor, Owen Brooks, Aisha Khan
- Focus service: search-recommendations
- Related evidence: ATLAS-2581, PR-15213, PD-2112

### Discussion
- Risk: search-recommendations ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2581.
- Risk: search-recommendations ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2581.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Risk: search-recommendations ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2581.

### Decisions and Actions
- Owner Nora Singh will close the action item before 2019-11-29.
- Update runbook, release checklist, and dashboard annotation for search-recommendations.

## Meeting MTG-0078 - 2019-11-22 - Customer Escalation Review
- Facilitator: Ravi Patel
- Attendees: Harper Lee, Aisha Khan, Priya Nair, Maya Chen, Nora Singh, Luca Moretti
- Focus service: inventory-reservation
- Related evidence: ATLAS-4041, PR-9913, PD-2641

### Discussion
- Risk: inventory-reservation ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4041.
- Blocker: QA needs production-like seed data before approving PR-9913. The workaround is documented but not yet rehearsed by on-call.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Risk: inventory-reservation ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4041.
- Risk: inventory-reservation ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4041.

### Decisions and Actions
- Owner Theo Martin will close the action item before 2019-12-06.
- Update runbook, release checklist, and dashboard annotation for inventory-reservation.

## Meeting MTG-0079 - 2019-11-29 - Architecture Council
- Facilitator: Kim Tan
- Attendees: Noah Evans, Kim Tan, Owen Brooks, Yara Haddad, Theo Martin, Samir Rao
- Focus service: inventory-reservation
- Related evidence: ATLAS-5452, PR-8627, PD-2391

### Discussion
- The team reviewed inventory-reservation readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Risk: inventory-reservation ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5452.
- The team reviewed inventory-reservation readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.

### Decisions and Actions
- Owner Maya Chen will close the action item before 2019-12-13.
- Update runbook, release checklist, and dashboard annotation for inventory-reservation.

## Meeting MTG-0080 - 2019-12-06 - Release Readiness
- Facilitator: Harper Lee
- Attendees: Iris Wang, Aisha Khan, Jon Bell, Fatima Noor, Luca Moretti, Theo Martin
- Focus service: notification-service
- Related evidence: ATLAS-3478, PR-17235, PD-2102

### Discussion
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Blocker: QA needs production-like seed data before approving PR-17235. The workaround is documented but not yet rehearsed by on-call.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Aisha Khan will close the action item before 2019-12-20.
- Update runbook, release checklist, and dashboard annotation for notification-service.

## Meeting MTG-0081 - 2019-12-13 - Release Readiness
- Facilitator: Jon Bell
- Attendees: Victor Silva, Ravi Patel, Kim Tan, Owen Brooks, Sara Novak, Fatima Noor
- Focus service: analytics-pipeline
- Related evidence: ATLAS-4736, PR-10783, PD-2526

### Discussion
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Risk: analytics-pipeline ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4736.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- The team reviewed analytics-pipeline readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Risk: analytics-pipeline ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4736.

### Decisions and Actions
- Owner Yara Haddad will close the action item before 2019-12-27.
- Update runbook, release checklist, and dashboard annotation for analytics-pipeline.

## Meeting MTG-0082 - 2019-12-20 - Customer Escalation Review
- Facilitator: Samir Rao
- Attendees: Aisha Khan, Anika Sharma, Ben Carter, Samir Rao, Grace Kim, Mateo Garcia
- Focus service: pricing-engine
- Related evidence: ATLAS-2113, PR-8513, PD-2661

### Discussion
- The team reviewed pricing-engine readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Risk: pricing-engine ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2113.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Risk: pricing-engine ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2113.
- Blocker: QA needs production-like seed data before approving PR-8513. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Mateo Garcia will close the action item before 2020-01-03.
- Update runbook, release checklist, and dashboard annotation for pricing-engine.

## Meeting MTG-0083 - 2019-12-27 - Architecture Council
- Facilitator: Priya Nair
- Attendees: Ravi Patel, Yara Haddad, Iris Wang, Grace Kim, Ben Carter, Priya Nair
- Focus service: tax-service
- Related evidence: ATLAS-3044, PR-7787, PD-2006

### Discussion
- Risk: tax-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-3044.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Blocker: QA needs production-like seed data before approving PR-7787. The workaround is documented but not yet rehearsed by on-call.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Blocker: QA needs production-like seed data before approving PR-7787. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Victor Silva will close the action item before 2020-01-10.
- Update runbook, release checklist, and dashboard annotation for tax-service.

## Meeting MTG-0084 - 2020-01-03 - KT Working Session
- Facilitator: Dmitri Volkov
- Attendees: Anika Sharma, Fatima Noor, Iris Wang, Victor Silva, Noah Evans, Aisha Khan
- Focus service: search-recommendations
- Related evidence: ATLAS-2001, PR-5068, PD-2242

### Discussion
- Blocker: QA needs production-like seed data before approving PR-5068. The workaround is documented but not yet rehearsed by on-call.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- The team reviewed search-recommendations readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Blocker: QA needs production-like seed data before approving PR-5068. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Ravi Patel will close the action item before 2020-01-17.
- Update runbook, release checklist, and dashboard annotation for search-recommendations.

## Meeting MTG-0085 - 2020-01-10 - Release Readiness
- Facilitator: Luca Moretti
- Attendees: Iris Wang, Mateo Garcia, Kim Tan, Sara Novak, Priya Nair, Yara Haddad
- Focus service: search-recommendations
- Related evidence: ATLAS-5551, PR-15662, PD-2099

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Risk: search-recommendations ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5551.
- Blocker: QA needs production-like seed data before approving PR-15662. The workaround is documented but not yet rehearsed by on-call.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- The team reviewed search-recommendations readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.

### Decisions and Actions
- Owner Iris Wang will close the action item before 2020-01-24.
- Update runbook, release checklist, and dashboard annotation for search-recommendations.

## Meeting MTG-0086 - 2020-01-17 - Customer Escalation Review
- Facilitator: Kim Tan
- Attendees: Anika Sharma, Elena Petrova, Ben Carter, Fatima Noor, Kim Tan, Yara Haddad
- Focus service: inventory-reservation
- Related evidence: ATLAS-2428, PR-16032, PD-2010

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Blocker: QA needs production-like seed data before approving PR-16032. The workaround is documented but not yet rehearsed by on-call.
- The team reviewed inventory-reservation readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.

### Decisions and Actions
- Owner Anika Sharma will close the action item before 2020-01-31.
- Update runbook, release checklist, and dashboard annotation for inventory-reservation.

## Meeting MTG-0087 - 2020-01-24 - Steering Review
- Facilitator: Maya Chen
- Attendees: Sara Novak, Ravi Patel, Dmitri Volkov, Nora Singh, Grace Kim, Luca Moretti
- Focus service: notification-service
- Related evidence: ATLAS-5633, PR-7754, PD-2538

### Discussion
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Risk: notification-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5633.
- The team reviewed notification-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- The team reviewed notification-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.

### Decisions and Actions
- Owner Ravi Patel will close the action item before 2020-02-07.
- Update runbook, release checklist, and dashboard annotation for notification-service.

## Meeting MTG-0088 - 2020-01-31 - Steering Review
- Facilitator: Mateo Garcia
- Attendees: Grace Kim, Dmitri Volkov, Noah Evans, Ravi Patel, Kim Tan, Aisha Khan
- Focus service: auth-gateway
- Related evidence: ATLAS-2870, PR-13311, PD-2831

### Discussion
- Risk: auth-gateway ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2870.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Blocker: QA needs production-like seed data before approving PR-13311. The workaround is documented but not yet rehearsed by on-call.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Risk: auth-gateway ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2870.

### Decisions and Actions
- Owner Fatima Noor will close the action item before 2020-02-14.
- Update runbook, release checklist, and dashboard annotation for auth-gateway.

## Meeting MTG-0089 - 2020-02-07 - Incident Review
- Facilitator: Mateo Garcia
- Attendees: Kim Tan, Jon Bell, Ravi Patel, Ben Carter, Sara Novak, Elena Petrova
- Focus service: pricing-engine
- Related evidence: ATLAS-1305, PR-8912, PD-2646

### Discussion
- The team reviewed pricing-engine readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Blocker: QA needs production-like seed data before approving PR-8912. The workaround is documented but not yet rehearsed by on-call.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Risk: pricing-engine ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-1305.

### Decisions and Actions
- Owner Elena Petrova will close the action item before 2020-02-21.
- Update runbook, release checklist, and dashboard annotation for pricing-engine.

## Meeting MTG-0090 - 2020-02-14 - Architecture Council
- Facilitator: Iris Wang
- Attendees: Grace Kim, Mateo Garcia, Ravi Patel, Iris Wang, Dmitri Volkov, Anika Sharma
- Focus service: inventory-reservation
- Related evidence: ATLAS-2218, PR-17437, PD-2022

### Discussion
- Blocker: QA needs production-like seed data before approving PR-17437. The workaround is documented but not yet rehearsed by on-call.
- The team reviewed inventory-reservation readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- The team reviewed inventory-reservation readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Risk: inventory-reservation ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2218.

### Decisions and Actions
- Owner Dmitri Volkov will close the action item before 2020-02-28.
- Update runbook, release checklist, and dashboard annotation for inventory-reservation.

## Meeting MTG-0091 - 2020-02-21 - SLO Review
- Facilitator: Mateo Garcia
- Attendees: Priya Nair, Luca Moretti, Owen Brooks, Ben Carter, Mateo Garcia, Harper Lee
- Focus service: search-recommendations
- Related evidence: ATLAS-5770, PR-17470, PD-2035

### Discussion
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Blocker: QA needs production-like seed data before approving PR-17470. The workaround is documented but not yet rehearsed by on-call.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Blocker: QA needs production-like seed data before approving PR-17470. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Anika Sharma will close the action item before 2020-03-06.
- Update runbook, release checklist, and dashboard annotation for search-recommendations.

## Meeting MTG-0092 - 2020-02-28 - Release Readiness
- Facilitator: Harper Lee
- Attendees: Kim Tan, Fatima Noor, Aisha Khan, Yara Haddad, Grace Kim, Elena Petrova
- Focus service: notification-service
- Related evidence: ATLAS-2450, PR-14545, PD-2760

### Discussion
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Risk: notification-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2450.
- The team reviewed notification-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Blocker: QA needs production-like seed data before approving PR-14545. The workaround is documented but not yet rehearsed by on-call.
- The team reviewed notification-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.

### Decisions and Actions
- Owner Owen Brooks will close the action item before 2020-03-13.
- Update runbook, release checklist, and dashboard annotation for notification-service.

## Meeting MTG-0093 - 2020-03-06 - Steering Review
- Facilitator: Iris Wang
- Attendees: Theo Martin, Sara Novak, Owen Brooks, Samir Rao, Fatima Noor, Aisha Khan
- Focus service: order-ledger
- Related evidence: ATLAS-2821, PR-14087, PD-2067

### Discussion
- Blocker: QA needs production-like seed data before approving PR-14087. The workaround is documented but not yet rehearsed by on-call.
- Blocker: QA needs production-like seed data before approving PR-14087. The workaround is documented but not yet rehearsed by on-call.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Blocker: QA needs production-like seed data before approving PR-14087. The workaround is documented but not yet rehearsed by on-call.
- Risk: order-ledger ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2821.

### Decisions and Actions
- Owner Ben Carter will close the action item before 2020-03-20.
- Update runbook, release checklist, and dashboard annotation for order-ledger.

## Meeting MTG-0094 - 2020-03-13 - SLO Review
- Facilitator: Elena Petrova
- Attendees: Priya Nair, Ben Carter, Anika Sharma, Maya Chen, Victor Silva, Jon Bell
- Focus service: analytics-pipeline
- Related evidence: ATLAS-2405, PR-10543, PD-2480

### Discussion
- The team reviewed analytics-pipeline readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Blocker: QA needs production-like seed data before approving PR-10543. The workaround is documented but not yet rehearsed by on-call.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Risk: analytics-pipeline ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2405.

### Decisions and Actions
- Owner Jon Bell will close the action item before 2020-03-27.
- Update runbook, release checklist, and dashboard annotation for analytics-pipeline.

## Meeting MTG-0095 - 2020-03-20 - Release Readiness
- Facilitator: Yara Haddad
- Attendees: Maya Chen, Harper Lee, Noah Evans, Iris Wang, Nora Singh, Theo Martin
- Focus service: auth-gateway
- Related evidence: ATLAS-2435, PR-10975, PD-2580

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Blocker: QA needs production-like seed data before approving PR-10975. The workaround is documented but not yet rehearsed by on-call.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Nora Singh will close the action item before 2020-04-03.
- Update runbook, release checklist, and dashboard annotation for auth-gateway.

## Meeting MTG-0096 - 2020-03-27 - Incident Review
- Facilitator: Samir Rao
- Attendees: Harper Lee, Anika Sharma, Dmitri Volkov, Fatima Noor, Iris Wang, Victor Silva
- Focus service: order-ledger
- Related evidence: ATLAS-2791, PR-7493, PD-2664

### Discussion
- Risk: order-ledger ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2791.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Risk: order-ledger ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2791.
- Blocker: QA needs production-like seed data before approving PR-7493. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Ben Carter will close the action item before 2020-04-10.
- Update runbook, release checklist, and dashboard annotation for order-ledger.

## Meeting MTG-0097 - 2020-04-03 - Release Readiness
- Facilitator: Aisha Khan
- Attendees: Anika Sharma, Priya Nair, Jon Bell, Luca Moretti, Sara Novak, Elena Petrova
- Focus service: order-ledger
- Related evidence: ATLAS-4407, PR-15146, PD-2640

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Blocker: QA needs production-like seed data before approving PR-15146. The workaround is documented but not yet rehearsed by on-call.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Risk: order-ledger ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4407.
- Blocker: QA needs production-like seed data before approving PR-15146. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Ben Carter will close the action item before 2020-04-17.
- Update runbook, release checklist, and dashboard annotation for order-ledger.

## Meeting MTG-0098 - 2020-04-10 - Customer Escalation Review
- Facilitator: Harper Lee
- Attendees: Aisha Khan, Sara Novak, Kim Tan, Nora Singh, Samir Rao, Victor Silva
- Focus service: auth-gateway
- Related evidence: ATLAS-1782, PR-7733, PD-2385

### Discussion
- The team reviewed auth-gateway readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Mateo Garcia will close the action item before 2020-04-24.
- Update runbook, release checklist, and dashboard annotation for auth-gateway.

## Meeting MTG-0099 - 2020-04-17 - KT Working Session
- Facilitator: Maya Chen
- Attendees: Yara Haddad, Aisha Khan, Elena Petrova, Priya Nair, Sara Novak, Iris Wang
- Focus service: auth-gateway
- Related evidence: ATLAS-3542, PR-18668, PD-2151

### Discussion
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Blocker: QA needs production-like seed data before approving PR-18668. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Elena Petrova will close the action item before 2020-05-01.
- Update runbook, release checklist, and dashboard annotation for auth-gateway.

## Meeting MTG-0100 - 2020-04-24 - SLO Review
- Facilitator: Samir Rao
- Attendees: Fatima Noor, Sara Novak, Priya Nair, Aisha Khan, Nora Singh, Grace Kim
- Focus service: notification-service
- Related evidence: ATLAS-5858, PR-6688, PD-2610

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- The team reviewed notification-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Risk: notification-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5858.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.

### Decisions and Actions
- Owner Aisha Khan will close the action item before 2020-05-08.
- Update runbook, release checklist, and dashboard annotation for notification-service.

## Meeting MTG-0101 - 2020-05-01 - Incident Review
- Facilitator: Dmitri Volkov
- Attendees: Owen Brooks, Anika Sharma, Ben Carter, Sara Novak, Elena Petrova, Luca Moretti
- Focus service: pricing-engine
- Related evidence: ATLAS-3331, PR-13368, PD-2536

### Discussion
- Risk: pricing-engine ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-3331.
- The team reviewed pricing-engine readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.

### Decisions and Actions
- Owner Fatima Noor will close the action item before 2020-05-15.
- Update runbook, release checklist, and dashboard annotation for pricing-engine.

## Meeting MTG-0102 - 2020-05-08 - Steering Review
- Facilitator: Grace Kim
- Attendees: Ben Carter, Theo Martin, Harper Lee, Anika Sharma, Mateo Garcia, Jon Bell
- Focus service: payment-orchestrator
- Related evidence: ATLAS-5925, PR-7163, PD-2254

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- The team reviewed payment-orchestrator readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Risk: payment-orchestrator ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5925.

### Decisions and Actions
- Owner Fatima Noor will close the action item before 2020-05-22.
- Update runbook, release checklist, and dashboard annotation for payment-orchestrator.

## Meeting MTG-0103 - 2020-05-15 - Release Readiness
- Facilitator: Sara Novak
- Attendees: Yara Haddad, Nora Singh, Iris Wang, Owen Brooks, Elena Petrova, Theo Martin
- Focus service: notification-service
- Related evidence: ATLAS-2798, PR-14459, PD-2112

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Risk: notification-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2798.
- Blocker: QA needs production-like seed data before approving PR-14459. The workaround is documented but not yet rehearsed by on-call.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.

### Decisions and Actions
- Owner Kim Tan will close the action item before 2020-05-29.
- Update runbook, release checklist, and dashboard annotation for notification-service.

## Meeting MTG-0104 - 2020-05-22 - Release Readiness
- Facilitator: Grace Kim
- Attendees: Aisha Khan, Dmitri Volkov, Noah Evans, Sara Novak, Fatima Noor, Elena Petrova
- Focus service: cart-service
- Related evidence: ATLAS-2373, PR-13632, PD-2775

### Discussion
- Risk: cart-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2373.
- The team reviewed cart-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Risk: cart-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2373.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Aisha Khan will close the action item before 2020-06-05.
- Update runbook, release checklist, and dashboard annotation for cart-service.

## Meeting MTG-0105 - 2020-05-29 - Steering Review
- Facilitator: Aisha Khan
- Attendees: Nora Singh, Elena Petrova, Luca Moretti, Sara Novak, Yara Haddad, Jon Bell
- Focus service: tax-service
- Related evidence: ATLAS-5433, PR-16461, PD-2126

### Discussion
- The team reviewed tax-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Blocker: QA needs production-like seed data before approving PR-16461. The workaround is documented but not yet rehearsed by on-call.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Risk: tax-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5433.

### Decisions and Actions
- Owner Priya Nair will close the action item before 2020-06-12.
- Update runbook, release checklist, and dashboard annotation for tax-service.

## Meeting MTG-0106 - 2020-06-05 - Steering Review
- Facilitator: Priya Nair
- Attendees: Nora Singh, Mateo Garcia, Elena Petrova, Sara Novak, Iris Wang, Luca Moretti
- Focus service: notification-service
- Related evidence: ATLAS-1313, PR-8042, PD-2747

### Discussion
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Blocker: QA needs production-like seed data before approving PR-8042. The workaround is documented but not yet rehearsed by on-call.
- Blocker: QA needs production-like seed data before approving PR-8042. The workaround is documented but not yet rehearsed by on-call.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Ben Carter will close the action item before 2020-06-19.
- Update runbook, release checklist, and dashboard annotation for notification-service.

## Meeting MTG-0107 - 2020-06-12 - Steering Review
- Facilitator: Nora Singh
- Attendees: Luca Moretti, Aisha Khan, Jon Bell, Nora Singh, Samir Rao, Yara Haddad
- Focus service: cart-service
- Related evidence: ATLAS-5085, PR-17842, PD-2094

### Discussion
- Risk: cart-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5085.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- The team reviewed cart-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Risk: cart-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5085.
- Risk: cart-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5085.

### Decisions and Actions
- Owner Priya Nair will close the action item before 2020-06-26.
- Update runbook, release checklist, and dashboard annotation for cart-service.

## Meeting MTG-0108 - 2020-06-19 - Release Readiness
- Facilitator: Nora Singh
- Attendees: Victor Silva, Mateo Garcia, Owen Brooks, Ravi Patel, Luca Moretti, Kim Tan
- Focus service: payment-orchestrator
- Related evidence: ATLAS-1370, PR-8233, PD-2101

### Discussion
- Risk: payment-orchestrator ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-1370.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Risk: payment-orchestrator ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-1370.
- Risk: payment-orchestrator ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-1370.
- Risk: payment-orchestrator ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-1370.

### Decisions and Actions
- Owner Samir Rao will close the action item before 2020-07-03.
- Update runbook, release checklist, and dashboard annotation for payment-orchestrator.

## Meeting MTG-0109 - 2020-06-26 - SLO Review
- Facilitator: Fatima Noor
- Attendees: Iris Wang, Sara Novak, Maya Chen, Luca Moretti, Noah Evans, Kim Tan
- Focus service: auth-gateway
- Related evidence: ATLAS-4302, PR-6804, PD-2606

### Discussion
- Risk: auth-gateway ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4302.
- Risk: auth-gateway ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4302.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Blocker: QA needs production-like seed data before approving PR-6804. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Iris Wang will close the action item before 2020-07-10.
- Update runbook, release checklist, and dashboard annotation for auth-gateway.

## Meeting MTG-0110 - 2020-07-03 - Steering Review
- Facilitator: Victor Silva
- Attendees: Jon Bell, Yara Haddad, Kim Tan, Maya Chen, Dmitri Volkov, Owen Brooks
- Focus service: search-recommendations
- Related evidence: ATLAS-5179, PR-9577, PD-2769

### Discussion
- Risk: search-recommendations ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5179.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- The team reviewed search-recommendations readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.

### Decisions and Actions
- Owner Grace Kim will close the action item before 2020-07-17.
- Update runbook, release checklist, and dashboard annotation for search-recommendations.

## Meeting MTG-0111 - 2020-07-10 - KT Working Session
- Facilitator: Priya Nair
- Attendees: Elena Petrova, Nora Singh, Grace Kim, Maya Chen, Noah Evans, Ravi Patel
- Focus service: loyalty-service
- Related evidence: ATLAS-1437, PR-18915, PD-2176

### Discussion
- Risk: loyalty-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-1437.
- The team reviewed loyalty-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Risk: loyalty-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-1437.
- Risk: loyalty-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-1437.

### Decisions and Actions
- Owner Yara Haddad will close the action item before 2020-07-24.
- Update runbook, release checklist, and dashboard annotation for loyalty-service.

## Meeting MTG-0112 - 2020-07-17 - Steering Review
- Facilitator: Jon Bell
- Attendees: Victor Silva, Luca Moretti, Grace Kim, Anika Sharma, Theo Martin, Kim Tan
- Focus service: auth-gateway
- Related evidence: ATLAS-2564, PR-7017, PD-2385

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Risk: auth-gateway ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2564.
- Risk: auth-gateway ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2564.
- The team reviewed auth-gateway readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- The team reviewed auth-gateway readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.

### Decisions and Actions
- Owner Priya Nair will close the action item before 2020-07-31.
- Update runbook, release checklist, and dashboard annotation for auth-gateway.

## Meeting MTG-0113 - 2020-07-24 - SLO Review
- Facilitator: Anika Sharma
- Attendees: Mateo Garcia, Fatima Noor, Harper Lee, Nora Singh, Theo Martin, Victor Silva
- Focus service: inventory-reservation
- Related evidence: ATLAS-2516, PR-9904, PD-2144

### Discussion
- Risk: inventory-reservation ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2516.
- Risk: inventory-reservation ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2516.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Nora Singh will close the action item before 2020-08-07.
- Update runbook, release checklist, and dashboard annotation for inventory-reservation.

## Meeting MTG-0114 - 2020-07-31 - Release Readiness
- Facilitator: Anika Sharma
- Attendees: Yara Haddad, Mateo Garcia, Iris Wang, Nora Singh, Anika Sharma, Victor Silva
- Focus service: tax-service
- Related evidence: ATLAS-5310, PR-16054, PD-2372

### Discussion
- Blocker: QA needs production-like seed data before approving PR-16054. The workaround is documented but not yet rehearsed by on-call.
- Blocker: QA needs production-like seed data before approving PR-16054. The workaround is documented but not yet rehearsed by on-call.
- Risk: tax-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5310.
- Risk: tax-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5310.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Grace Kim will close the action item before 2020-08-14.
- Update runbook, release checklist, and dashboard annotation for tax-service.

## Meeting MTG-0115 - 2020-08-07 - Release Readiness
- Facilitator: Priya Nair
- Attendees: Fatima Noor, Jon Bell, Victor Silva, Harper Lee, Owen Brooks, Aisha Khan
- Focus service: auth-gateway
- Related evidence: ATLAS-6189, PR-9894, PD-2274

### Discussion
- Risk: auth-gateway ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-6189.
- Risk: auth-gateway ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-6189.
- Blocker: QA needs production-like seed data before approving PR-9894. The workaround is documented but not yet rehearsed by on-call.
- Blocker: QA needs production-like seed data before approving PR-9894. The workaround is documented but not yet rehearsed by on-call.
- The team reviewed auth-gateway readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.

### Decisions and Actions
- Owner Nora Singh will close the action item before 2020-08-21.
- Update runbook, release checklist, and dashboard annotation for auth-gateway.

## Meeting MTG-0116 - 2020-08-14 - Customer Escalation Review
- Facilitator: Jon Bell
- Attendees: Grace Kim, Dmitri Volkov, Iris Wang, Ravi Patel, Victor Silva, Kim Tan
- Focus service: search-recommendations
- Related evidence: ATLAS-1625, PR-10556, PD-2553

### Discussion
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Risk: search-recommendations ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-1625.
- The team reviewed search-recommendations readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Blocker: QA needs production-like seed data before approving PR-10556. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Priya Nair will close the action item before 2020-08-28.
- Update runbook, release checklist, and dashboard annotation for search-recommendations.

## Meeting MTG-0117 - 2020-08-21 - Release Readiness
- Facilitator: Mateo Garcia
- Attendees: Anika Sharma, Yara Haddad, Sara Novak, Kim Tan, Ben Carter, Dmitri Volkov
- Focus service: tax-service
- Related evidence: ATLAS-6018, PR-6230, PD-2717

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.

### Decisions and Actions
- Owner Dmitri Volkov will close the action item before 2020-09-04.
- Update runbook, release checklist, and dashboard annotation for tax-service.

## Meeting MTG-0118 - 2020-08-28 - Steering Review
- Facilitator: Mateo Garcia
- Attendees: Sara Novak, Ravi Patel, Owen Brooks, Dmitri Volkov, Kim Tan, Aisha Khan
- Focus service: analytics-pipeline
- Related evidence: ATLAS-1453, PR-16850, PD-2863

### Discussion
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- The team reviewed analytics-pipeline readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Risk: analytics-pipeline ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-1453.

### Decisions and Actions
- Owner Owen Brooks will close the action item before 2020-09-11.
- Update runbook, release checklist, and dashboard annotation for analytics-pipeline.

## Meeting MTG-0119 - 2020-09-04 - Customer Escalation Review
- Facilitator: Sara Novak
- Attendees: Owen Brooks, Noah Evans, Dmitri Volkov, Sara Novak, Aisha Khan, Maya Chen
- Focus service: notification-service
- Related evidence: ATLAS-2156, PR-11873, PD-2253

### Discussion
- The team reviewed notification-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Risk: notification-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2156.
- The team reviewed notification-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Blocker: QA needs production-like seed data before approving PR-11873. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Ravi Patel will close the action item before 2020-09-18.
- Update runbook, release checklist, and dashboard annotation for notification-service.

## Meeting MTG-0120 - 2020-09-11 - SLO Review
- Facilitator: Luca Moretti
- Attendees: Harper Lee, Sara Novak, Yara Haddad, Priya Nair, Grace Kim, Victor Silva
- Focus service: tax-service
- Related evidence: ATLAS-3138, PR-10551, PD-2554

### Discussion
- Blocker: QA needs production-like seed data before approving PR-10551. The workaround is documented but not yet rehearsed by on-call.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Risk: tax-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-3138.
- Risk: tax-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-3138.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Aisha Khan will close the action item before 2020-09-25.
- Update runbook, release checklist, and dashboard annotation for tax-service.

## Meeting MTG-0121 - 2020-09-18 - KT Working Session
- Facilitator: Grace Kim
- Attendees: Maya Chen, Fatima Noor, Luca Moretti, Mateo Garcia, Samir Rao, Ben Carter
- Focus service: inventory-reservation
- Related evidence: ATLAS-1437, PR-15363, PD-2308

### Discussion
- Blocker: QA needs production-like seed data before approving PR-15363. The workaround is documented but not yet rehearsed by on-call.
- Blocker: QA needs production-like seed data before approving PR-15363. The workaround is documented but not yet rehearsed by on-call.
- Blocker: QA needs production-like seed data before approving PR-15363. The workaround is documented but not yet rehearsed by on-call.
- Blocker: QA needs production-like seed data before approving PR-15363. The workaround is documented but not yet rehearsed by on-call.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Nora Singh will close the action item before 2020-10-02.
- Update runbook, release checklist, and dashboard annotation for inventory-reservation.

## Meeting MTG-0122 - 2020-09-25 - KT Working Session
- Facilitator: Fatima Noor
- Attendees: Maya Chen, Jon Bell, Nora Singh, Priya Nair, Noah Evans, Theo Martin
- Focus service: analytics-pipeline
- Related evidence: ATLAS-4046, PR-16663, PD-2249

### Discussion
- Risk: analytics-pipeline ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4046.
- Blocker: QA needs production-like seed data before approving PR-16663. The workaround is documented but not yet rehearsed by on-call.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.

### Decisions and Actions
- Owner Ben Carter will close the action item before 2020-10-09.
- Update runbook, release checklist, and dashboard annotation for analytics-pipeline.

## Meeting MTG-0123 - 2020-10-02 - Incident Review
- Facilitator: Samir Rao
- Attendees: Theo Martin, Elena Petrova, Noah Evans, Yara Haddad, Jon Bell, Nora Singh
- Focus service: order-ledger
- Related evidence: ATLAS-5221, PR-17561, PD-2675

### Discussion
- The team reviewed order-ledger readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- The team reviewed order-ledger readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Blocker: QA needs production-like seed data before approving PR-17561. The workaround is documented but not yet rehearsed by on-call.
- Blocker: QA needs production-like seed data before approving PR-17561. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Elena Petrova will close the action item before 2020-10-16.
- Update runbook, release checklist, and dashboard annotation for order-ledger.

## Meeting MTG-0124 - 2020-10-09 - Architecture Council
- Facilitator: Anika Sharma
- Attendees: Nora Singh, Grace Kim, Samir Rao, Kim Tan, Jon Bell, Anika Sharma
- Focus service: loyalty-service
- Related evidence: ATLAS-1081, PR-14550, PD-2617

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Risk: loyalty-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-1081.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- The team reviewed loyalty-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Blocker: QA needs production-like seed data before approving PR-14550. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Ravi Patel will close the action item before 2020-10-23.
- Update runbook, release checklist, and dashboard annotation for loyalty-service.

## Meeting MTG-0125 - 2020-10-16 - Incident Review
- Facilitator: Harper Lee
- Attendees: Yara Haddad, Ben Carter, Maya Chen, Noah Evans, Aisha Khan, Nora Singh
- Focus service: order-ledger
- Related evidence: ATLAS-3975, PR-7932, PD-2435

### Discussion
- Blocker: QA needs production-like seed data before approving PR-7932. The workaround is documented but not yet rehearsed by on-call.
- Risk: order-ledger ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-3975.
- The team reviewed order-ledger readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Risk: order-ledger ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-3975.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Yara Haddad will close the action item before 2020-10-30.
- Update runbook, release checklist, and dashboard annotation for order-ledger.

## Meeting MTG-0126 - 2020-10-23 - Incident Review
- Facilitator: Sara Novak
- Attendees: Dmitri Volkov, Nora Singh, Priya Nair, Jon Bell, Fatima Noor, Noah Evans
- Focus service: inventory-reservation
- Related evidence: ATLAS-4015, PR-16317, PD-2820

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- The team reviewed inventory-reservation readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- The team reviewed inventory-reservation readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Aisha Khan will close the action item before 2020-11-06.
- Update runbook, release checklist, and dashboard annotation for inventory-reservation.

## Meeting MTG-0127 - 2020-10-30 - Architecture Council
- Facilitator: Victor Silva
- Attendees: Samir Rao, Dmitri Volkov, Noah Evans, Kim Tan, Maya Chen, Victor Silva
- Focus service: inventory-reservation
- Related evidence: ATLAS-2945, PR-8586, PD-2145

### Discussion
- Risk: inventory-reservation ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2945.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Blocker: QA needs production-like seed data before approving PR-8586. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Grace Kim will close the action item before 2020-11-13.
- Update runbook, release checklist, and dashboard annotation for inventory-reservation.

## Meeting MTG-0128 - 2020-11-06 - SLO Review
- Facilitator: Elena Petrova
- Attendees: Grace Kim, Fatima Noor, Ravi Patel, Harper Lee, Theo Martin, Aisha Khan
- Focus service: checkout-api
- Related evidence: ATLAS-3230, PR-16833, PD-2667

### Discussion
- Blocker: QA needs production-like seed data before approving PR-16833. The workaround is documented but not yet rehearsed by on-call.
- Blocker: QA needs production-like seed data before approving PR-16833. The workaround is documented but not yet rehearsed by on-call.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Risk: checkout-api ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-3230.
- Risk: checkout-api ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-3230.

### Decisions and Actions
- Owner Owen Brooks will close the action item before 2020-11-20.
- Update runbook, release checklist, and dashboard annotation for checkout-api.

## Meeting MTG-0129 - 2020-11-13 - Release Readiness
- Facilitator: Samir Rao
- Attendees: Priya Nair, Samir Rao, Anika Sharma, Grace Kim, Luca Moretti, Kim Tan
- Focus service: tax-service
- Related evidence: ATLAS-3724, PR-14885, PD-2052

### Discussion
- The team reviewed tax-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- The team reviewed tax-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- The team reviewed tax-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Blocker: QA needs production-like seed data before approving PR-14885. The workaround is documented but not yet rehearsed by on-call.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Victor Silva will close the action item before 2020-11-27.
- Update runbook, release checklist, and dashboard annotation for tax-service.

## Meeting MTG-0130 - 2020-11-20 - Steering Review
- Facilitator: Anika Sharma
- Attendees: Mateo Garcia, Luca Moretti, Noah Evans, Owen Brooks, Kim Tan, Samir Rao
- Focus service: pricing-engine
- Related evidence: ATLAS-5885, PR-8004, PD-2424

### Discussion
- Blocker: QA needs production-like seed data before approving PR-8004. The workaround is documented but not yet rehearsed by on-call.
- Blocker: QA needs production-like seed data before approving PR-8004. The workaround is documented but not yet rehearsed by on-call.
- Blocker: QA needs production-like seed data before approving PR-8004. The workaround is documented but not yet rehearsed by on-call.
- Risk: pricing-engine ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5885.
- Risk: pricing-engine ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5885.

### Decisions and Actions
- Owner Iris Wang will close the action item before 2020-12-04.
- Update runbook, release checklist, and dashboard annotation for pricing-engine.

## Meeting MTG-0131 - 2020-11-27 - Incident Review
- Facilitator: Owen Brooks
- Attendees: Priya Nair, Ravi Patel, Anika Sharma, Aisha Khan, Maya Chen, Samir Rao
- Focus service: notification-service
- Related evidence: ATLAS-2129, PR-5312, PD-2428

### Discussion
- The team reviewed notification-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Blocker: QA needs production-like seed data before approving PR-5312. The workaround is documented but not yet rehearsed by on-call.
- Blocker: QA needs production-like seed data before approving PR-5312. The workaround is documented but not yet rehearsed by on-call.
- The team reviewed notification-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Blocker: QA needs production-like seed data before approving PR-5312. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Elena Petrova will close the action item before 2020-12-11.
- Update runbook, release checklist, and dashboard annotation for notification-service.

## Meeting MTG-0132 - 2020-12-04 - Architecture Council
- Facilitator: Ben Carter
- Attendees: Sara Novak, Grace Kim, Luca Moretti, Owen Brooks, Fatima Noor, Anika Sharma
- Focus service: pricing-engine
- Related evidence: ATLAS-4504, PR-5330, PD-2844

### Discussion
- Risk: pricing-engine ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4504.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Blocker: QA needs production-like seed data before approving PR-5330. The workaround is documented but not yet rehearsed by on-call.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Risk: pricing-engine ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4504.

### Decisions and Actions
- Owner Nora Singh will close the action item before 2020-12-18.
- Update runbook, release checklist, and dashboard annotation for pricing-engine.

## Meeting MTG-0133 - 2020-12-11 - Architecture Council
- Facilitator: Harper Lee
- Attendees: Sara Novak, Iris Wang, Samir Rao, Aisha Khan, Kim Tan, Ben Carter
- Focus service: order-ledger
- Related evidence: ATLAS-3851, PR-5815, PD-2285

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Blocker: QA needs production-like seed data before approving PR-5815. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Yara Haddad will close the action item before 2020-12-25.
- Update runbook, release checklist, and dashboard annotation for order-ledger.

## Meeting MTG-0134 - 2020-12-18 - Steering Review
- Facilitator: Nora Singh
- Attendees: Samir Rao, Dmitri Volkov, Mateo Garcia, Iris Wang, Harper Lee, Ben Carter
- Focus service: notification-service
- Related evidence: ATLAS-1782, PR-15990, PD-2170

### Discussion
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Risk: notification-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-1782.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Risk: notification-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-1782.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.

### Decisions and Actions
- Owner Grace Kim will close the action item before 2021-01-01.
- Update runbook, release checklist, and dashboard annotation for notification-service.

## Meeting MTG-0135 - 2020-12-25 - Incident Review
- Facilitator: Ravi Patel
- Attendees: Priya Nair, Jon Bell, Grace Kim, Harper Lee, Maya Chen, Luca Moretti
- Focus service: pricing-engine
- Related evidence: ATLAS-3413, PR-14343, PD-2572

### Discussion
- The team reviewed pricing-engine readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- The team reviewed pricing-engine readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Blocker: QA needs production-like seed data before approving PR-14343. The workaround is documented but not yet rehearsed by on-call.
- Risk: pricing-engine ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-3413.

### Decisions and Actions
- Owner Luca Moretti will close the action item before 2021-01-08.
- Update runbook, release checklist, and dashboard annotation for pricing-engine.

## Meeting MTG-0136 - 2021-01-01 - Incident Review
- Facilitator: Harper Lee
- Attendees: Aisha Khan, Elena Petrova, Owen Brooks, Grace Kim, Dmitri Volkov, Ben Carter
- Focus service: checkout-api
- Related evidence: ATLAS-2158, PR-9689, PD-2006

### Discussion
- Blocker: QA needs production-like seed data before approving PR-9689. The workaround is documented but not yet rehearsed by on-call.
- The team reviewed checkout-api readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- The team reviewed checkout-api readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Risk: checkout-api ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2158.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Harper Lee will close the action item before 2021-01-15.
- Update runbook, release checklist, and dashboard annotation for checkout-api.

## Meeting MTG-0137 - 2021-01-08 - Release Readiness
- Facilitator: Aisha Khan
- Attendees: Elena Petrova, Grace Kim, Samir Rao, Nora Singh, Sara Novak, Aisha Khan
- Focus service: checkout-api
- Related evidence: ATLAS-4922, PR-15112, PD-2259

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- The team reviewed checkout-api readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- The team reviewed checkout-api readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Risk: checkout-api ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4922.

### Decisions and Actions
- Owner Harper Lee will close the action item before 2021-01-22.
- Update runbook, release checklist, and dashboard annotation for checkout-api.

## Meeting MTG-0138 - 2021-01-15 - Steering Review
- Facilitator: Harper Lee
- Attendees: Noah Evans, Sara Novak, Samir Rao, Elena Petrova, Nora Singh, Iris Wang
- Focus service: cart-service
- Related evidence: ATLAS-3055, PR-5422, PD-2825

### Discussion
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Risk: cart-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-3055.
- Risk: cart-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-3055.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Nora Singh will close the action item before 2021-01-29.
- Update runbook, release checklist, and dashboard annotation for cart-service.

## Meeting MTG-0139 - 2021-01-22 - KT Working Session
- Facilitator: Yara Haddad
- Attendees: Samir Rao, Maya Chen, Noah Evans, Ravi Patel, Grace Kim, Priya Nair
- Focus service: loyalty-service
- Related evidence: ATLAS-5510, PR-16429, PD-2042

### Discussion
- Blocker: QA needs production-like seed data before approving PR-16429. The workaround is documented but not yet rehearsed by on-call.
- The team reviewed loyalty-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- The team reviewed loyalty-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.

### Decisions and Actions
- Owner Theo Martin will close the action item before 2021-02-05.
- Update runbook, release checklist, and dashboard annotation for loyalty-service.

## Meeting MTG-0140 - 2021-01-29 - SLO Review
- Facilitator: Noah Evans
- Attendees: Ben Carter, Yara Haddad, Dmitri Volkov, Iris Wang, Theo Martin, Maya Chen
- Focus service: analytics-pipeline
- Related evidence: ATLAS-6126, PR-15005, PD-2631

### Discussion
- The team reviewed analytics-pipeline readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- The team reviewed analytics-pipeline readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Risk: analytics-pipeline ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-6126.
- The team reviewed analytics-pipeline readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- The team reviewed analytics-pipeline readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.

### Decisions and Actions
- Owner Maya Chen will close the action item before 2021-02-12.
- Update runbook, release checklist, and dashboard annotation for analytics-pipeline.

## Meeting MTG-0141 - 2021-02-05 - SLO Review
- Facilitator: Yara Haddad
- Attendees: Nora Singh, Noah Evans, Samir Rao, Ben Carter, Ravi Patel, Aisha Khan
- Focus service: pricing-engine
- Related evidence: ATLAS-4009, PR-11584, PD-2034

### Discussion
- The team reviewed pricing-engine readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Blocker: QA needs production-like seed data before approving PR-11584. The workaround is documented but not yet rehearsed by on-call.
- Blocker: QA needs production-like seed data before approving PR-11584. The workaround is documented but not yet rehearsed by on-call.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Maya Chen will close the action item before 2021-02-19.
- Update runbook, release checklist, and dashboard annotation for pricing-engine.

## Meeting MTG-0142 - 2021-02-12 - Release Readiness
- Facilitator: Grace Kim
- Attendees: Samir Rao, Dmitri Volkov, Grace Kim, Theo Martin, Noah Evans, Aisha Khan
- Focus service: order-ledger
- Related evidence: ATLAS-2408, PR-9298, PD-2329

### Discussion
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Blocker: QA needs production-like seed data before approving PR-9298. The workaround is documented but not yet rehearsed by on-call.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Risk: order-ledger ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2408.
- The team reviewed order-ledger readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.

### Decisions and Actions
- Owner Jon Bell will close the action item before 2021-02-26.
- Update runbook, release checklist, and dashboard annotation for order-ledger.

## Meeting MTG-0143 - 2021-02-19 - Incident Review
- Facilitator: Kim Tan
- Attendees: Anika Sharma, Luca Moretti, Nora Singh, Kim Tan, Owen Brooks, Ravi Patel
- Focus service: loyalty-service
- Related evidence: ATLAS-5353, PR-17457, PD-2171

### Discussion
- Risk: loyalty-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5353.
- Blocker: QA needs production-like seed data before approving PR-17457. The workaround is documented but not yet rehearsed by on-call.
- Risk: loyalty-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5353.
- The team reviewed loyalty-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Blocker: QA needs production-like seed data before approving PR-17457. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Iris Wang will close the action item before 2021-03-05.
- Update runbook, release checklist, and dashboard annotation for loyalty-service.

## Meeting MTG-0144 - 2021-02-26 - Steering Review
- Facilitator: Elena Petrova
- Attendees: Nora Singh, Aisha Khan, Kim Tan, Jon Bell, Elena Petrova, Priya Nair
- Focus service: payment-orchestrator
- Related evidence: ATLAS-3843, PR-13719, PD-2718

### Discussion
- Risk: payment-orchestrator ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-3843.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Risk: payment-orchestrator ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-3843.

### Decisions and Actions
- Owner Samir Rao will close the action item before 2021-03-12.
- Update runbook, release checklist, and dashboard annotation for payment-orchestrator.

## Meeting MTG-0145 - 2021-03-05 - Release Readiness
- Facilitator: Mateo Garcia
- Attendees: Sara Novak, Priya Nair, Aisha Khan, Yara Haddad, Jon Bell, Samir Rao
- Focus service: analytics-pipeline
- Related evidence: ATLAS-2888, PR-13041, PD-2585

### Discussion
- Blocker: QA needs production-like seed data before approving PR-13041. The workaround is documented but not yet rehearsed by on-call.
- Risk: analytics-pipeline ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2888.
- The team reviewed analytics-pipeline readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Blocker: QA needs production-like seed data before approving PR-13041. The workaround is documented but not yet rehearsed by on-call.
- The team reviewed analytics-pipeline readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.

### Decisions and Actions
- Owner Iris Wang will close the action item before 2021-03-19.
- Update runbook, release checklist, and dashboard annotation for analytics-pipeline.

## Meeting MTG-0146 - 2021-03-12 - Customer Escalation Review
- Facilitator: Maya Chen
- Attendees: Luca Moretti, Fatima Noor, Kim Tan, Iris Wang, Nora Singh, Ravi Patel
- Focus service: analytics-pipeline
- Related evidence: ATLAS-4885, PR-5875, PD-2076

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Risk: analytics-pipeline ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4885.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Risk: analytics-pipeline ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4885.

### Decisions and Actions
- Owner Maya Chen will close the action item before 2021-03-26.
- Update runbook, release checklist, and dashboard annotation for analytics-pipeline.

## Meeting MTG-0147 - 2021-03-19 - Release Readiness
- Facilitator: Iris Wang
- Attendees: Owen Brooks, Jon Bell, Priya Nair, Grace Kim, Samir Rao, Kim Tan
- Focus service: cart-service
- Related evidence: ATLAS-5770, PR-12033, PD-2030

### Discussion
- Risk: cart-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5770.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- The team reviewed cart-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Fatima Noor will close the action item before 2021-04-02.
- Update runbook, release checklist, and dashboard annotation for cart-service.

## Meeting MTG-0148 - 2021-03-26 - Architecture Council
- Facilitator: Mateo Garcia
- Attendees: Sara Novak, Samir Rao, Ben Carter, Theo Martin, Kim Tan, Nora Singh
- Focus service: notification-service
- Related evidence: ATLAS-3063, PR-8849, PD-2242

### Discussion
- Risk: notification-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-3063.
- Blocker: QA needs production-like seed data before approving PR-8849. The workaround is documented but not yet rehearsed by on-call.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- The team reviewed notification-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Risk: notification-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-3063.

### Decisions and Actions
- Owner Iris Wang will close the action item before 2021-04-09.
- Update runbook, release checklist, and dashboard annotation for notification-service.

## Meeting MTG-0149 - 2021-04-02 - Incident Review
- Facilitator: Owen Brooks
- Attendees: Grace Kim, Fatima Noor, Sara Novak, Jon Bell, Noah Evans, Ravi Patel
- Focus service: loyalty-service
- Related evidence: ATLAS-3854, PR-5528, PD-2526

### Discussion
- Risk: loyalty-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-3854.
- Blocker: QA needs production-like seed data before approving PR-5528. The workaround is documented but not yet rehearsed by on-call.
- The team reviewed loyalty-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- The team reviewed loyalty-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Blocker: QA needs production-like seed data before approving PR-5528. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Priya Nair will close the action item before 2021-04-16.
- Update runbook, release checklist, and dashboard annotation for loyalty-service.

## Meeting MTG-0150 - 2021-04-09 - Incident Review
- Facilitator: Dmitri Volkov
- Attendees: Aisha Khan, Priya Nair, Anika Sharma, Harper Lee, Ben Carter, Elena Petrova
- Focus service: search-recommendations
- Related evidence: ATLAS-1141, PR-18921, PD-2895

### Discussion
- Risk: search-recommendations ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-1141.
- Blocker: QA needs production-like seed data before approving PR-18921. The workaround is documented but not yet rehearsed by on-call.
- Blocker: QA needs production-like seed data before approving PR-18921. The workaround is documented but not yet rehearsed by on-call.
- Risk: search-recommendations ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-1141.
- Risk: search-recommendations ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-1141.

### Decisions and Actions
- Owner Sara Novak will close the action item before 2021-04-23.
- Update runbook, release checklist, and dashboard annotation for search-recommendations.

## Meeting MTG-0151 - 2021-04-16 - Steering Review
- Facilitator: Yara Haddad
- Attendees: Aisha Khan, Ben Carter, Samir Rao, Jon Bell, Grace Kim, Owen Brooks
- Focus service: tax-service
- Related evidence: ATLAS-4357, PR-18909, PD-2367

### Discussion
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Blocker: QA needs production-like seed data before approving PR-18909. The workaround is documented but not yet rehearsed by on-call.
- Risk: tax-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4357.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Iris Wang will close the action item before 2021-04-30.
- Update runbook, release checklist, and dashboard annotation for tax-service.

## Meeting MTG-0152 - 2021-04-23 - KT Working Session
- Facilitator: Iris Wang
- Attendees: Ben Carter, Priya Nair, Noah Evans, Kim Tan, Jon Bell, Maya Chen
- Focus service: tax-service
- Related evidence: ATLAS-2235, PR-13057, PD-2779

### Discussion
- Blocker: QA needs production-like seed data before approving PR-13057. The workaround is documented but not yet rehearsed by on-call.
- The team reviewed tax-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- The team reviewed tax-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Blocker: QA needs production-like seed data before approving PR-13057. The workaround is documented but not yet rehearsed by on-call.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Anika Sharma will close the action item before 2021-05-07.
- Update runbook, release checklist, and dashboard annotation for tax-service.

## Meeting MTG-0153 - 2021-04-30 - Architecture Council
- Facilitator: Elena Petrova
- Attendees: Anika Sharma, Elena Petrova, Victor Silva, Dmitri Volkov, Theo Martin, Aisha Khan
- Focus service: analytics-pipeline
- Related evidence: ATLAS-1103, PR-12847, PD-2348

### Discussion
- Blocker: QA needs production-like seed data before approving PR-12847. The workaround is documented but not yet rehearsed by on-call.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Blocker: QA needs production-like seed data before approving PR-12847. The workaround is documented but not yet rehearsed by on-call.
- Blocker: QA needs production-like seed data before approving PR-12847. The workaround is documented but not yet rehearsed by on-call.
- Blocker: QA needs production-like seed data before approving PR-12847. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Luca Moretti will close the action item before 2021-05-14.
- Update runbook, release checklist, and dashboard annotation for analytics-pipeline.

## Meeting MTG-0154 - 2021-05-07 - Incident Review
- Facilitator: Noah Evans
- Attendees: Ben Carter, Kim Tan, Yara Haddad, Victor Silva, Luca Moretti, Samir Rao
- Focus service: order-ledger
- Related evidence: ATLAS-1239, PR-18279, PD-2862

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Risk: order-ledger ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-1239.
- Risk: order-ledger ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-1239.
- The team reviewed order-ledger readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- The team reviewed order-ledger readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.

### Decisions and Actions
- Owner Jon Bell will close the action item before 2021-05-21.
- Update runbook, release checklist, and dashboard annotation for order-ledger.

## Meeting MTG-0155 - 2021-05-14 - Release Readiness
- Facilitator: Samir Rao
- Attendees: Mateo Garcia, Dmitri Volkov, Priya Nair, Harper Lee, Elena Petrova, Aisha Khan
- Focus service: search-recommendations
- Related evidence: ATLAS-5628, PR-11552, PD-2528

### Discussion
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Blocker: QA needs production-like seed data before approving PR-11552. The workaround is documented but not yet rehearsed by on-call.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Owen Brooks will close the action item before 2021-05-28.
- Update runbook, release checklist, and dashboard annotation for search-recommendations.

## Meeting MTG-0156 - 2021-05-21 - Customer Escalation Review
- Facilitator: Maya Chen
- Attendees: Yara Haddad, Dmitri Volkov, Maya Chen, Fatima Noor, Sara Novak, Owen Brooks
- Focus service: inventory-reservation
- Related evidence: ATLAS-3108, PR-11621, PD-2550

### Discussion
- Blocker: QA needs production-like seed data before approving PR-11621. The workaround is documented but not yet rehearsed by on-call.
- Risk: inventory-reservation ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-3108.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Risk: inventory-reservation ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-3108.
- Blocker: QA needs production-like seed data before approving PR-11621. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Aisha Khan will close the action item before 2021-06-04.
- Update runbook, release checklist, and dashboard annotation for inventory-reservation.

## Meeting MTG-0157 - 2021-05-28 - Architecture Council
- Facilitator: Grace Kim
- Attendees: Samir Rao, Kim Tan, Aisha Khan, Priya Nair, Sara Novak, Ben Carter
- Focus service: tax-service
- Related evidence: ATLAS-6161, PR-16575, PD-2716

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Blocker: QA needs production-like seed data before approving PR-16575. The workaround is documented but not yet rehearsed by on-call.
- Blocker: QA needs production-like seed data before approving PR-16575. The workaround is documented but not yet rehearsed by on-call.
- Risk: tax-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-6161.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Elena Petrova will close the action item before 2021-06-11.
- Update runbook, release checklist, and dashboard annotation for tax-service.

## Meeting MTG-0158 - 2021-06-04 - Steering Review
- Facilitator: Owen Brooks
- Attendees: Victor Silva, Owen Brooks, Ben Carter, Aisha Khan, Luca Moretti, Fatima Noor
- Focus service: loyalty-service
- Related evidence: ATLAS-2192, PR-14840, PD-2683

### Discussion
- Blocker: QA needs production-like seed data before approving PR-14840. The workaround is documented but not yet rehearsed by on-call.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Blocker: QA needs production-like seed data before approving PR-14840. The workaround is documented but not yet rehearsed by on-call.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.

### Decisions and Actions
- Owner Anika Sharma will close the action item before 2021-06-18.
- Update runbook, release checklist, and dashboard annotation for loyalty-service.

## Meeting MTG-0159 - 2021-06-11 - KT Working Session
- Facilitator: Samir Rao
- Attendees: Sara Novak, Fatima Noor, Iris Wang, Luca Moretti, Theo Martin, Samir Rao
- Focus service: inventory-reservation
- Related evidence: ATLAS-1313, PR-16405, PD-2898

### Discussion
- Blocker: QA needs production-like seed data before approving PR-16405. The workaround is documented but not yet rehearsed by on-call.
- Risk: inventory-reservation ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-1313.
- Blocker: QA needs production-like seed data before approving PR-16405. The workaround is documented but not yet rehearsed by on-call.
- Blocker: QA needs production-like seed data before approving PR-16405. The workaround is documented but not yet rehearsed by on-call.
- Risk: inventory-reservation ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-1313.

### Decisions and Actions
- Owner Harper Lee will close the action item before 2021-06-25.
- Update runbook, release checklist, and dashboard annotation for inventory-reservation.

## Meeting MTG-0160 - 2021-06-18 - Release Readiness
- Facilitator: Anika Sharma
- Attendees: Yara Haddad, Ravi Patel, Luca Moretti, Priya Nair, Elena Petrova, Ben Carter
- Focus service: search-recommendations
- Related evidence: ATLAS-1465, PR-5498, PD-2448

### Discussion
- Blocker: QA needs production-like seed data before approving PR-5498. The workaround is documented but not yet rehearsed by on-call.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- The team reviewed search-recommendations readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.

### Decisions and Actions
- Owner Jon Bell will close the action item before 2021-07-02.
- Update runbook, release checklist, and dashboard annotation for search-recommendations.

## Meeting MTG-0161 - 2021-06-25 - KT Working Session
- Facilitator: Grace Kim
- Attendees: Harper Lee, Jon Bell, Luca Moretti, Yara Haddad, Elena Petrova, Ben Carter
- Focus service: search-recommendations
- Related evidence: ATLAS-4837, PR-7153, PD-2448

### Discussion
- Blocker: QA needs production-like seed data before approving PR-7153. The workaround is documented but not yet rehearsed by on-call.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- The team reviewed search-recommendations readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- The team reviewed search-recommendations readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- The team reviewed search-recommendations readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.

### Decisions and Actions
- Owner Noah Evans will close the action item before 2021-07-09.
- Update runbook, release checklist, and dashboard annotation for search-recommendations.

## Meeting MTG-0162 - 2021-07-02 - Customer Escalation Review
- Facilitator: Owen Brooks
- Attendees: Nora Singh, Fatima Noor, Noah Evans, Elena Petrova, Kim Tan, Victor Silva
- Focus service: cart-service
- Related evidence: ATLAS-2168, PR-11376, PD-2656

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Blocker: QA needs production-like seed data before approving PR-11376. The workaround is documented but not yet rehearsed by on-call.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Blocker: QA needs production-like seed data before approving PR-11376. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Samir Rao will close the action item before 2021-07-16.
- Update runbook, release checklist, and dashboard annotation for cart-service.

## Meeting MTG-0163 - 2021-07-09 - Steering Review
- Facilitator: Luca Moretti
- Attendees: Ben Carter, Grace Kim, Mateo Garcia, Jon Bell, Kim Tan, Noah Evans
- Focus service: cart-service
- Related evidence: ATLAS-4277, PR-9660, PD-2181

### Discussion
- Risk: cart-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4277.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- The team reviewed cart-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Risk: cart-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4277.

### Decisions and Actions
- Owner Ben Carter will close the action item before 2021-07-23.
- Update runbook, release checklist, and dashboard annotation for cart-service.

## Meeting MTG-0164 - 2021-07-16 - Release Readiness
- Facilitator: Noah Evans
- Attendees: Mateo Garcia, Jon Bell, Nora Singh, Iris Wang, Grace Kim, Kim Tan
- Focus service: cart-service
- Related evidence: ATLAS-2196, PR-14394, PD-2259

### Discussion
- Risk: cart-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2196.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- The team reviewed cart-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- The team reviewed cart-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- The team reviewed cart-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.

### Decisions and Actions
- Owner Iris Wang will close the action item before 2021-07-30.
- Update runbook, release checklist, and dashboard annotation for cart-service.

## Meeting MTG-0165 - 2021-07-23 - Architecture Council
- Facilitator: Dmitri Volkov
- Attendees: Ravi Patel, Kim Tan, Theo Martin, Noah Evans, Iris Wang, Grace Kim
- Focus service: pricing-engine
- Related evidence: ATLAS-4592, PR-13474, PD-2010

### Discussion
- The team reviewed pricing-engine readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Risk: pricing-engine ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4592.
- Blocker: QA needs production-like seed data before approving PR-13474. The workaround is documented but not yet rehearsed by on-call.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.

### Decisions and Actions
- Owner Yara Haddad will close the action item before 2021-08-06.
- Update runbook, release checklist, and dashboard annotation for pricing-engine.

## Meeting MTG-0166 - 2021-07-30 - Architecture Council
- Facilitator: Kim Tan
- Attendees: Samir Rao, Ben Carter, Victor Silva, Sara Novak, Owen Brooks, Theo Martin
- Focus service: auth-gateway
- Related evidence: ATLAS-2218, PR-9873, PD-2211

### Discussion
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Blocker: QA needs production-like seed data before approving PR-9873. The workaround is documented but not yet rehearsed by on-call.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Blocker: QA needs production-like seed data before approving PR-9873. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Dmitri Volkov will close the action item before 2021-08-13.
- Update runbook, release checklist, and dashboard annotation for auth-gateway.

## Meeting MTG-0167 - 2021-08-06 - Incident Review
- Facilitator: Dmitri Volkov
- Attendees: Maya Chen, Anika Sharma, Victor Silva, Samir Rao, Kim Tan, Theo Martin
- Focus service: order-ledger
- Related evidence: ATLAS-3952, PR-6148, PD-2838

### Discussion
- The team reviewed order-ledger readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Risk: order-ledger ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-3952.
- The team reviewed order-ledger readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Blocker: QA needs production-like seed data before approving PR-6148. The workaround is documented but not yet rehearsed by on-call.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.

### Decisions and Actions
- Owner Sara Novak will close the action item before 2021-08-20.
- Update runbook, release checklist, and dashboard annotation for order-ledger.

## Meeting MTG-0168 - 2021-08-13 - KT Working Session
- Facilitator: Yara Haddad
- Attendees: Dmitri Volkov, Anika Sharma, Ben Carter, Fatima Noor, Elena Petrova, Theo Martin
- Focus service: pricing-engine
- Related evidence: ATLAS-4765, PR-16533, PD-2885

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- The team reviewed pricing-engine readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Blocker: QA needs production-like seed data before approving PR-16533. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Sara Novak will close the action item before 2021-08-27.
- Update runbook, release checklist, and dashboard annotation for pricing-engine.

## Meeting MTG-0169 - 2021-08-20 - Incident Review
- Facilitator: Dmitri Volkov
- Attendees: Harper Lee, Mateo Garcia, Maya Chen, Dmitri Volkov, Fatima Noor, Priya Nair
- Focus service: loyalty-service
- Related evidence: ATLAS-4159, PR-9288, PD-2113

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Blocker: QA needs production-like seed data before approving PR-9288. The workaround is documented but not yet rehearsed by on-call.
- Blocker: QA needs production-like seed data before approving PR-9288. The workaround is documented but not yet rehearsed by on-call.
- Risk: loyalty-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4159.
- Blocker: QA needs production-like seed data before approving PR-9288. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Priya Nair will close the action item before 2021-09-03.
- Update runbook, release checklist, and dashboard annotation for loyalty-service.

## Meeting MTG-0170 - 2021-08-27 - Incident Review
- Facilitator: Yara Haddad
- Attendees: Priya Nair, Aisha Khan, Fatima Noor, Mateo Garcia, Dmitri Volkov, Owen Brooks
- Focus service: tax-service
- Related evidence: ATLAS-5343, PR-17292, PD-2499

### Discussion
- The team reviewed tax-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- The team reviewed tax-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Risk: tax-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5343.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.

### Decisions and Actions
- Owner Luca Moretti will close the action item before 2021-09-10.
- Update runbook, release checklist, and dashboard annotation for tax-service.

## Meeting MTG-0171 - 2021-09-03 - Incident Review
- Facilitator: Theo Martin
- Attendees: Noah Evans, Samir Rao, Luca Moretti, Grace Kim, Priya Nair, Elena Petrova
- Focus service: notification-service
- Related evidence: ATLAS-2826, PR-10943, PD-2822

### Discussion
- Blocker: QA needs production-like seed data before approving PR-10943. The workaround is documented but not yet rehearsed by on-call.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Blocker: QA needs production-like seed data before approving PR-10943. The workaround is documented but not yet rehearsed by on-call.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Risk: notification-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2826.

### Decisions and Actions
- Owner Nora Singh will close the action item before 2021-09-17.
- Update runbook, release checklist, and dashboard annotation for notification-service.

## Meeting MTG-0172 - 2021-09-10 - SLO Review
- Facilitator: Grace Kim
- Attendees: Ben Carter, Mateo Garcia, Elena Petrova, Grace Kim, Anika Sharma, Nora Singh
- Focus service: analytics-pipeline
- Related evidence: ATLAS-5388, PR-9386, PD-2498

### Discussion
- The team reviewed analytics-pipeline readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Risk: analytics-pipeline ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5388.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Risk: analytics-pipeline ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5388.
- Risk: analytics-pipeline ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5388.

### Decisions and Actions
- Owner Kim Tan will close the action item before 2021-09-24.
- Update runbook, release checklist, and dashboard annotation for analytics-pipeline.

## Meeting MTG-0173 - 2021-09-17 - Release Readiness
- Facilitator: Ravi Patel
- Attendees: Priya Nair, Elena Petrova, Kim Tan, Anika Sharma, Sara Novak, Luca Moretti
- Focus service: checkout-api
- Related evidence: ATLAS-3404, PR-5338, PD-2087

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Samir Rao will close the action item before 2021-10-01.
- Update runbook, release checklist, and dashboard annotation for checkout-api.

## Meeting MTG-0174 - 2021-09-24 - KT Working Session
- Facilitator: Priya Nair
- Attendees: Fatima Noor, Nora Singh, Sara Novak, Samir Rao, Yara Haddad, Victor Silva
- Focus service: order-ledger
- Related evidence: ATLAS-5999, PR-5261, PD-2398

### Discussion
- Risk: order-ledger ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5999.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Blocker: QA needs production-like seed data before approving PR-5261. The workaround is documented but not yet rehearsed by on-call.
- Risk: order-ledger ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5999.
- Risk: order-ledger ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5999.

### Decisions and Actions
- Owner Anika Sharma will close the action item before 2021-10-08.
- Update runbook, release checklist, and dashboard annotation for order-ledger.

## Meeting MTG-0175 - 2021-10-01 - Release Readiness
- Facilitator: Luca Moretti
- Attendees: Ravi Patel, Harper Lee, Nora Singh, Anika Sharma, Grace Kim, Noah Evans
- Focus service: payment-orchestrator
- Related evidence: ATLAS-4070, PR-8712, PD-2388

### Discussion
- Risk: payment-orchestrator ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4070.
- Risk: payment-orchestrator ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4070.
- The team reviewed payment-orchestrator readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Risk: payment-orchestrator ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4070.

### Decisions and Actions
- Owner Ravi Patel will close the action item before 2021-10-15.
- Update runbook, release checklist, and dashboard annotation for payment-orchestrator.

## Meeting MTG-0176 - 2021-10-08 - SLO Review
- Facilitator: Owen Brooks
- Attendees: Fatima Noor, Sara Novak, Dmitri Volkov, Noah Evans, Kim Tan, Maya Chen
- Focus service: order-ledger
- Related evidence: ATLAS-2505, PR-13027, PD-2489

### Discussion
- Risk: order-ledger ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2505.
- Blocker: QA needs production-like seed data before approving PR-13027. The workaround is documented but not yet rehearsed by on-call.
- Risk: order-ledger ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2505.
- Blocker: QA needs production-like seed data before approving PR-13027. The workaround is documented but not yet rehearsed by on-call.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.

### Decisions and Actions
- Owner Dmitri Volkov will close the action item before 2021-10-22.
- Update runbook, release checklist, and dashboard annotation for order-ledger.

## Meeting MTG-0177 - 2021-10-15 - SLO Review
- Facilitator: Dmitri Volkov
- Attendees: Grace Kim, Ben Carter, Nora Singh, Priya Nair, Iris Wang, Elena Petrova
- Focus service: notification-service
- Related evidence: ATLAS-1481, PR-15260, PD-2068

### Discussion
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- The team reviewed notification-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- The team reviewed notification-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Risk: notification-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-1481.
- Blocker: QA needs production-like seed data before approving PR-15260. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Grace Kim will close the action item before 2021-10-29.
- Update runbook, release checklist, and dashboard annotation for notification-service.

## Meeting MTG-0178 - 2021-10-22 - Release Readiness
- Facilitator: Samir Rao
- Attendees: Grace Kim, Ravi Patel, Priya Nair, Anika Sharma, Fatima Noor, Noah Evans
- Focus service: tax-service
- Related evidence: ATLAS-2412, PR-17177, PD-2541

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Blocker: QA needs production-like seed data before approving PR-17177. The workaround is documented but not yet rehearsed by on-call.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- The team reviewed tax-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.

### Decisions and Actions
- Owner Maya Chen will close the action item before 2021-11-05.
- Update runbook, release checklist, and dashboard annotation for tax-service.

## Meeting MTG-0179 - 2021-10-29 - Release Readiness
- Facilitator: Nora Singh
- Attendees: Theo Martin, Victor Silva, Priya Nair, Owen Brooks, Jon Bell, Nora Singh
- Focus service: tax-service
- Related evidence: ATLAS-5634, PR-16414, PD-2228

### Discussion
- The team reviewed tax-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Blocker: QA needs production-like seed data before approving PR-16414. The workaround is documented but not yet rehearsed by on-call.
- The team reviewed tax-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- The team reviewed tax-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Blocker: QA needs production-like seed data before approving PR-16414. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Aisha Khan will close the action item before 2021-11-12.
- Update runbook, release checklist, and dashboard annotation for tax-service.

## Meeting MTG-0180 - 2021-11-05 - KT Working Session
- Facilitator: Ravi Patel
- Attendees: Anika Sharma, Priya Nair, Ben Carter, Theo Martin, Kim Tan, Noah Evans
- Focus service: inventory-reservation
- Related evidence: ATLAS-4871, PR-11583, PD-2643

### Discussion
- The team reviewed inventory-reservation readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Blocker: QA needs production-like seed data before approving PR-11583. The workaround is documented but not yet rehearsed by on-call.
- The team reviewed inventory-reservation readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Risk: inventory-reservation ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4871.

### Decisions and Actions
- Owner Maya Chen will close the action item before 2021-11-19.
- Update runbook, release checklist, and dashboard annotation for inventory-reservation.

## Meeting MTG-0181 - 2021-11-12 - Incident Review
- Facilitator: Jon Bell
- Attendees: Nora Singh, Ravi Patel, Priya Nair, Noah Evans, Maya Chen, Ben Carter
- Focus service: search-recommendations
- Related evidence: ATLAS-5972, PR-14922, PD-2250

### Discussion
- Blocker: QA needs production-like seed data before approving PR-14922. The workaround is documented but not yet rehearsed by on-call.
- The team reviewed search-recommendations readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Risk: search-recommendations ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5972.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Risk: search-recommendations ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5972.

### Decisions and Actions
- Owner Yara Haddad will close the action item before 2021-11-26.
- Update runbook, release checklist, and dashboard annotation for search-recommendations.

## Meeting MTG-0182 - 2021-11-19 - Release Readiness
- Facilitator: Jon Bell
- Attendees: Yara Haddad, Samir Rao, Noah Evans, Fatima Noor, Ravi Patel, Grace Kim
- Focus service: auth-gateway
- Related evidence: ATLAS-5264, PR-10544, PD-2057

### Discussion
- Risk: auth-gateway ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5264.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Blocker: QA needs production-like seed data before approving PR-10544. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Anika Sharma will close the action item before 2021-12-03.
- Update runbook, release checklist, and dashboard annotation for auth-gateway.

## Meeting MTG-0183 - 2021-11-26 - Incident Review
- Facilitator: Sara Novak
- Attendees: Sara Novak, Theo Martin, Mateo Garcia, Ravi Patel, Owen Brooks, Victor Silva
- Focus service: tax-service
- Related evidence: ATLAS-4828, PR-14327, PD-2491

### Discussion
- Risk: tax-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4828.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Blocker: QA needs production-like seed data before approving PR-14327. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Grace Kim will close the action item before 2021-12-10.
- Update runbook, release checklist, and dashboard annotation for tax-service.

## Meeting MTG-0184 - 2021-12-03 - SLO Review
- Facilitator: Jon Bell
- Attendees: Priya Nair, Noah Evans, Victor Silva, Harper Lee, Ravi Patel, Fatima Noor
- Focus service: tax-service
- Related evidence: ATLAS-5540, PR-15847, PD-2273

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Blocker: QA needs production-like seed data before approving PR-15847. The workaround is documented but not yet rehearsed by on-call.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Risk: tax-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5540.

### Decisions and Actions
- Owner Mateo Garcia will close the action item before 2021-12-17.
- Update runbook, release checklist, and dashboard annotation for tax-service.

## Meeting MTG-0185 - 2021-12-10 - KT Working Session
- Facilitator: Mateo Garcia
- Attendees: Dmitri Volkov, Grace Kim, Priya Nair, Samir Rao, Fatima Noor, Elena Petrova
- Focus service: notification-service
- Related evidence: ATLAS-4997, PR-17961, PD-2542

### Discussion
- The team reviewed notification-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Blocker: QA needs production-like seed data before approving PR-17961. The workaround is documented but not yet rehearsed by on-call.
- Blocker: QA needs production-like seed data before approving PR-17961. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Aisha Khan will close the action item before 2021-12-24.
- Update runbook, release checklist, and dashboard annotation for notification-service.

## Meeting MTG-0186 - 2021-12-17 - SLO Review
- Facilitator: Sara Novak
- Attendees: Nora Singh, Grace Kim, Dmitri Volkov, Aisha Khan, Iris Wang, Samir Rao
- Focus service: order-ledger
- Related evidence: ATLAS-4072, PR-8166, PD-2548

### Discussion
- The team reviewed order-ledger readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- The team reviewed order-ledger readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Risk: order-ledger ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4072.

### Decisions and Actions
- Owner Yara Haddad will close the action item before 2021-12-31.
- Update runbook, release checklist, and dashboard annotation for order-ledger.

## Meeting MTG-0187 - 2021-12-24 - Customer Escalation Review
- Facilitator: Priya Nair
- Attendees: Sara Novak, Ravi Patel, Iris Wang, Owen Brooks, Luca Moretti, Maya Chen
- Focus service: order-ledger
- Related evidence: ATLAS-1368, PR-9145, PD-2825

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Blocker: QA needs production-like seed data before approving PR-9145. The workaround is documented but not yet rehearsed by on-call.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Risk: order-ledger ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-1368.
- The team reviewed order-ledger readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.

### Decisions and Actions
- Owner Kim Tan will close the action item before 2022-01-07.
- Update runbook, release checklist, and dashboard annotation for order-ledger.

## Meeting MTG-0188 - 2021-12-31 - SLO Review
- Facilitator: Maya Chen
- Attendees: Yara Haddad, Iris Wang, Victor Silva, Luca Moretti, Theo Martin, Aisha Khan
- Focus service: loyalty-service
- Related evidence: ATLAS-4642, PR-7786, PD-2357

### Discussion
- The team reviewed loyalty-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Risk: loyalty-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4642.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- The team reviewed loyalty-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.

### Decisions and Actions
- Owner Theo Martin will close the action item before 2022-01-14.
- Update runbook, release checklist, and dashboard annotation for loyalty-service.

## Meeting MTG-0189 - 2022-01-07 - Customer Escalation Review
- Facilitator: Kim Tan
- Attendees: Yara Haddad, Kim Tan, Luca Moretti, Mateo Garcia, Ravi Patel, Harper Lee
- Focus service: search-recommendations
- Related evidence: ATLAS-6081, PR-14043, PD-2056

### Discussion
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Blocker: QA needs production-like seed data before approving PR-14043. The workaround is documented but not yet rehearsed by on-call.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Risk: search-recommendations ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-6081.
- Risk: search-recommendations ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-6081.

### Decisions and Actions
- Owner Owen Brooks will close the action item before 2022-01-21.
- Update runbook, release checklist, and dashboard annotation for search-recommendations.

## Meeting MTG-0190 - 2022-01-14 - KT Working Session
- Facilitator: Samir Rao
- Attendees: Priya Nair, Jon Bell, Ravi Patel, Mateo Garcia, Fatima Noor, Nora Singh
- Focus service: tax-service
- Related evidence: ATLAS-2172, PR-18377, PD-2498

### Discussion
- The team reviewed tax-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- The team reviewed tax-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Risk: tax-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2172.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Noah Evans will close the action item before 2022-01-28.
- Update runbook, release checklist, and dashboard annotation for tax-service.

## Meeting MTG-0191 - 2022-01-21 - Release Readiness
- Facilitator: Noah Evans
- Attendees: Yara Haddad, Elena Petrova, Victor Silva, Maya Chen, Harper Lee, Samir Rao
- Focus service: analytics-pipeline
- Related evidence: ATLAS-4427, PR-9226, PD-2282

### Discussion
- Risk: analytics-pipeline ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4427.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- The team reviewed analytics-pipeline readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Blocker: QA needs production-like seed data before approving PR-9226. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Nora Singh will close the action item before 2022-02-04.
- Update runbook, release checklist, and dashboard annotation for analytics-pipeline.

## Meeting MTG-0192 - 2022-01-28 - Steering Review
- Facilitator: Iris Wang
- Attendees: Mateo Garcia, Samir Rao, Victor Silva, Noah Evans, Ben Carter, Elena Petrova
- Focus service: search-recommendations
- Related evidence: ATLAS-1928, PR-14399, PD-2263

### Discussion
- The team reviewed search-recommendations readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- The team reviewed search-recommendations readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Risk: search-recommendations ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-1928.

### Decisions and Actions
- Owner Victor Silva will close the action item before 2022-02-11.
- Update runbook, release checklist, and dashboard annotation for search-recommendations.

## Meeting MTG-0193 - 2022-02-04 - KT Working Session
- Facilitator: Theo Martin
- Attendees: Priya Nair, Nora Singh, Grace Kim, Aisha Khan, Mateo Garcia, Luca Moretti
- Focus service: search-recommendations
- Related evidence: ATLAS-2028, PR-11751, PD-2844

### Discussion
- Blocker: QA needs production-like seed data before approving PR-11751. The workaround is documented but not yet rehearsed by on-call.
- Blocker: QA needs production-like seed data before approving PR-11751. The workaround is documented but not yet rehearsed by on-call.
- The team reviewed search-recommendations readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- The team reviewed search-recommendations readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Risk: search-recommendations ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2028.

### Decisions and Actions
- Owner Samir Rao will close the action item before 2022-02-18.
- Update runbook, release checklist, and dashboard annotation for search-recommendations.

## Meeting MTG-0194 - 2022-02-11 - KT Working Session
- Facilitator: Harper Lee
- Attendees: Samir Rao, Theo Martin, Maya Chen, Aisha Khan, Noah Evans, Yara Haddad
- Focus service: payment-orchestrator
- Related evidence: ATLAS-2893, PR-17104, PD-2031

### Discussion
- The team reviewed payment-orchestrator readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- The team reviewed payment-orchestrator readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Risk: payment-orchestrator ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2893.
- The team reviewed payment-orchestrator readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.

### Decisions and Actions
- Owner Dmitri Volkov will close the action item before 2022-02-25.
- Update runbook, release checklist, and dashboard annotation for payment-orchestrator.

## Meeting MTG-0195 - 2022-02-18 - Customer Escalation Review
- Facilitator: Fatima Noor
- Attendees: Victor Silva, Harper Lee, Ravi Patel, Iris Wang, Grace Kim, Luca Moretti
- Focus service: auth-gateway
- Related evidence: ATLAS-3360, PR-10887, PD-2459

### Discussion
- Risk: auth-gateway ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-3360.
- The team reviewed auth-gateway readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Risk: auth-gateway ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-3360.
- The team reviewed auth-gateway readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Risk: auth-gateway ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-3360.

### Decisions and Actions
- Owner Kim Tan will close the action item before 2022-03-04.
- Update runbook, release checklist, and dashboard annotation for auth-gateway.

## Meeting MTG-0196 - 2022-02-25 - KT Working Session
- Facilitator: Sara Novak
- Attendees: Harper Lee, Ben Carter, Elena Petrova, Iris Wang, Priya Nair, Victor Silva
- Focus service: analytics-pipeline
- Related evidence: ATLAS-1646, PR-16108, PD-2494

### Discussion
- The team reviewed analytics-pipeline readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- The team reviewed analytics-pipeline readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Risk: analytics-pipeline ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-1646.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.

### Decisions and Actions
- Owner Iris Wang will close the action item before 2022-03-11.
- Update runbook, release checklist, and dashboard annotation for analytics-pipeline.

## Meeting MTG-0197 - 2022-03-04 - KT Working Session
- Facilitator: Anika Sharma
- Attendees: Ben Carter, Anika Sharma, Yara Haddad, Nora Singh, Samir Rao, Iris Wang
- Focus service: auth-gateway
- Related evidence: ATLAS-3977, PR-5413, PD-2497

### Discussion
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Blocker: QA needs production-like seed data before approving PR-5413. The workaround is documented but not yet rehearsed by on-call.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.

### Decisions and Actions
- Owner Nora Singh will close the action item before 2022-03-18.
- Update runbook, release checklist, and dashboard annotation for auth-gateway.

## Meeting MTG-0198 - 2022-03-11 - Steering Review
- Facilitator: Priya Nair
- Attendees: Mateo Garcia, Luca Moretti, Jon Bell, Grace Kim, Ben Carter, Dmitri Volkov
- Focus service: payment-orchestrator
- Related evidence: ATLAS-1166, PR-16182, PD-2388

### Discussion
- Risk: payment-orchestrator ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-1166.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- The team reviewed payment-orchestrator readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- The team reviewed payment-orchestrator readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Blocker: QA needs production-like seed data before approving PR-16182. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Noah Evans will close the action item before 2022-03-25.
- Update runbook, release checklist, and dashboard annotation for payment-orchestrator.

## Meeting MTG-0199 - 2022-03-18 - Incident Review
- Facilitator: Jon Bell
- Attendees: Iris Wang, Sara Novak, Victor Silva, Priya Nair, Maya Chen, Dmitri Volkov
- Focus service: order-ledger
- Related evidence: ATLAS-1195, PR-7732, PD-2192

### Discussion
- Blocker: QA needs production-like seed data before approving PR-7732. The workaround is documented but not yet rehearsed by on-call.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- The team reviewed order-ledger readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Risk: order-ledger ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-1195.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Yara Haddad will close the action item before 2022-04-01.
- Update runbook, release checklist, and dashboard annotation for order-ledger.

## Meeting MTG-0200 - 2022-03-25 - KT Working Session
- Facilitator: Noah Evans
- Attendees: Nora Singh, Anika Sharma, Elena Petrova, Iris Wang, Ben Carter, Sara Novak
- Focus service: analytics-pipeline
- Related evidence: ATLAS-4173, PR-14780, PD-2593

### Discussion
- The team reviewed analytics-pipeline readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Blocker: QA needs production-like seed data before approving PR-14780. The workaround is documented but not yet rehearsed by on-call.
- Risk: analytics-pipeline ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4173.
- Blocker: QA needs production-like seed data before approving PR-14780. The workaround is documented but not yet rehearsed by on-call.
- Blocker: QA needs production-like seed data before approving PR-14780. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Jon Bell will close the action item before 2022-04-08.
- Update runbook, release checklist, and dashboard annotation for analytics-pipeline.

## Meeting MTG-0201 - 2022-04-01 - Architecture Council
- Facilitator: Sara Novak
- Attendees: Noah Evans, Aisha Khan, Owen Brooks, Maya Chen, Dmitri Volkov, Sara Novak
- Focus service: auth-gateway
- Related evidence: ATLAS-2636, PR-6388, PD-2076

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Risk: auth-gateway ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2636.
- Blocker: QA needs production-like seed data before approving PR-6388. The workaround is documented but not yet rehearsed by on-call.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Anika Sharma will close the action item before 2022-04-15.
- Update runbook, release checklist, and dashboard annotation for auth-gateway.

## Meeting MTG-0202 - 2022-04-08 - Steering Review
- Facilitator: Jon Bell
- Attendees: Kim Tan, Samir Rao, Iris Wang, Dmitri Volkov, Mateo Garcia, Theo Martin
- Focus service: pricing-engine
- Related evidence: ATLAS-3975, PR-8634, PD-2699

### Discussion
- The team reviewed pricing-engine readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Risk: pricing-engine ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-3975.
- Blocker: QA needs production-like seed data before approving PR-8634. The workaround is documented but not yet rehearsed by on-call.
- Blocker: QA needs production-like seed data before approving PR-8634. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Yara Haddad will close the action item before 2022-04-22.
- Update runbook, release checklist, and dashboard annotation for pricing-engine.

## Meeting MTG-0203 - 2022-04-15 - Architecture Council
- Facilitator: Nora Singh
- Attendees: Victor Silva, Fatima Noor, Theo Martin, Noah Evans, Samir Rao, Nora Singh
- Focus service: analytics-pipeline
- Related evidence: ATLAS-4119, PR-14479, PD-2169

### Discussion
- Risk: analytics-pipeline ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4119.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Risk: analytics-pipeline ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4119.
- The team reviewed analytics-pipeline readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- The team reviewed analytics-pipeline readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.

### Decisions and Actions
- Owner Ben Carter will close the action item before 2022-04-29.
- Update runbook, release checklist, and dashboard annotation for analytics-pipeline.

## Meeting MTG-0204 - 2022-04-22 - Steering Review
- Facilitator: Mateo Garcia
- Attendees: Harper Lee, Sara Novak, Maya Chen, Owen Brooks, Priya Nair, Nora Singh
- Focus service: tax-service
- Related evidence: ATLAS-5339, PR-12911, PD-2129

### Discussion
- Risk: tax-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5339.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Risk: tax-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5339.

### Decisions and Actions
- Owner Iris Wang will close the action item before 2022-05-06.
- Update runbook, release checklist, and dashboard annotation for tax-service.

## Meeting MTG-0205 - 2022-04-29 - Customer Escalation Review
- Facilitator: Victor Silva
- Attendees: Noah Evans, Anika Sharma, Fatima Noor, Sara Novak, Mateo Garcia, Ben Carter
- Focus service: cart-service
- Related evidence: ATLAS-3417, PR-14148, PD-2183

### Discussion
- Risk: cart-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-3417.
- The team reviewed cart-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Blocker: QA needs production-like seed data before approving PR-14148. The workaround is documented but not yet rehearsed by on-call.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Maya Chen will close the action item before 2022-05-13.
- Update runbook, release checklist, and dashboard annotation for cart-service.

## Meeting MTG-0206 - 2022-05-06 - Incident Review
- Facilitator: Harper Lee
- Attendees: Elena Petrova, Mateo Garcia, Aisha Khan, Anika Sharma, Yara Haddad, Victor Silva
- Focus service: notification-service
- Related evidence: ATLAS-5637, PR-9219, PD-2898

### Discussion
- The team reviewed notification-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- The team reviewed notification-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Blocker: QA needs production-like seed data before approving PR-9219. The workaround is documented but not yet rehearsed by on-call.
- Blocker: QA needs production-like seed data before approving PR-9219. The workaround is documented but not yet rehearsed by on-call.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Samir Rao will close the action item before 2022-05-20.
- Update runbook, release checklist, and dashboard annotation for notification-service.

## Meeting MTG-0207 - 2022-05-13 - Incident Review
- Facilitator: Fatima Noor
- Attendees: Dmitri Volkov, Priya Nair, Ben Carter, Anika Sharma, Mateo Garcia, Victor Silva
- Focus service: cart-service
- Related evidence: ATLAS-1438, PR-7900, PD-2382

### Discussion
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Risk: cart-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-1438.

### Decisions and Actions
- Owner Harper Lee will close the action item before 2022-05-27.
- Update runbook, release checklist, and dashboard annotation for cart-service.

## Meeting MTG-0208 - 2022-05-20 - Release Readiness
- Facilitator: Nora Singh
- Attendees: Anika Sharma, Elena Petrova, Fatima Noor, Kim Tan, Noah Evans, Grace Kim
- Focus service: analytics-pipeline
- Related evidence: ATLAS-3251, PR-12416, PD-2687

### Discussion
- The team reviewed analytics-pipeline readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Risk: analytics-pipeline ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-3251.
- Blocker: QA needs production-like seed data before approving PR-12416. The workaround is documented but not yet rehearsed by on-call.
- Risk: analytics-pipeline ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-3251.
- The team reviewed analytics-pipeline readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.

### Decisions and Actions
- Owner Aisha Khan will close the action item before 2022-06-03.
- Update runbook, release checklist, and dashboard annotation for analytics-pipeline.

## Meeting MTG-0209 - 2022-05-27 - Architecture Council
- Facilitator: Luca Moretti
- Attendees: Iris Wang, Theo Martin, Anika Sharma, Jon Bell, Grace Kim, Owen Brooks
- Focus service: cart-service
- Related evidence: ATLAS-2633, PR-16053, PD-2416

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Nora Singh will close the action item before 2022-06-10.
- Update runbook, release checklist, and dashboard annotation for cart-service.

## Meeting MTG-0210 - 2022-06-03 - Incident Review
- Facilitator: Maya Chen
- Attendees: Ben Carter, Harper Lee, Sara Novak, Samir Rao, Grace Kim, Ravi Patel
- Focus service: tax-service
- Related evidence: ATLAS-4711, PR-10572, PD-2131

### Discussion
- Blocker: QA needs production-like seed data before approving PR-10572. The workaround is documented but not yet rehearsed by on-call.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Risk: tax-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4711.

### Decisions and Actions
- Owner Dmitri Volkov will close the action item before 2022-06-17.
- Update runbook, release checklist, and dashboard annotation for tax-service.

## Meeting MTG-0211 - 2022-06-10 - Customer Escalation Review
- Facilitator: Ben Carter
- Attendees: Elena Petrova, Iris Wang, Jon Bell, Ben Carter, Nora Singh, Theo Martin
- Focus service: order-ledger
- Related evidence: ATLAS-5894, PR-8128, PD-2285

### Discussion
- The team reviewed order-ledger readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Risk: order-ledger ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5894.
- The team reviewed order-ledger readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- The team reviewed order-ledger readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.

### Decisions and Actions
- Owner Nora Singh will close the action item before 2022-06-24.
- Update runbook, release checklist, and dashboard annotation for order-ledger.

## Meeting MTG-0212 - 2022-06-17 - SLO Review
- Facilitator: Mateo Garcia
- Attendees: Ravi Patel, Harper Lee, Nora Singh, Iris Wang, Noah Evans, Kim Tan
- Focus service: search-recommendations
- Related evidence: ATLAS-2566, PR-14094, PD-2524

### Discussion
- Blocker: QA needs production-like seed data before approving PR-14094. The workaround is documented but not yet rehearsed by on-call.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Blocker: QA needs production-like seed data before approving PR-14094. The workaround is documented but not yet rehearsed by on-call.
- The team reviewed search-recommendations readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.

### Decisions and Actions
- Owner Mateo Garcia will close the action item before 2022-07-01.
- Update runbook, release checklist, and dashboard annotation for search-recommendations.

## Meeting MTG-0213 - 2022-06-24 - Architecture Council
- Facilitator: Fatima Noor
- Attendees: Grace Kim, Dmitri Volkov, Fatima Noor, Nora Singh, Priya Nair, Samir Rao
- Focus service: payment-orchestrator
- Related evidence: ATLAS-2342, PR-8089, PD-2698

### Discussion
- The team reviewed payment-orchestrator readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Risk: payment-orchestrator ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2342.
- Blocker: QA needs production-like seed data before approving PR-8089. The workaround is documented but not yet rehearsed by on-call.
- The team reviewed payment-orchestrator readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.

### Decisions and Actions
- Owner Samir Rao will close the action item before 2022-07-08.
- Update runbook, release checklist, and dashboard annotation for payment-orchestrator.

## Meeting MTG-0214 - 2022-07-01 - Incident Review
- Facilitator: Elena Petrova
- Attendees: Theo Martin, Ben Carter, Mateo Garcia, Anika Sharma, Aisha Khan, Sara Novak
- Focus service: notification-service
- Related evidence: ATLAS-3316, PR-15517, PD-2167

### Discussion
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Blocker: QA needs production-like seed data before approving PR-15517. The workaround is documented but not yet rehearsed by on-call.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- The team reviewed notification-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.

### Decisions and Actions
- Owner Yara Haddad will close the action item before 2022-07-15.
- Update runbook, release checklist, and dashboard annotation for notification-service.

## Meeting MTG-0215 - 2022-07-08 - Customer Escalation Review
- Facilitator: Fatima Noor
- Attendees: Anika Sharma, Nora Singh, Sara Novak, Mateo Garcia, Kim Tan, Jon Bell
- Focus service: inventory-reservation
- Related evidence: ATLAS-2131, PR-14696, PD-2123

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Blocker: QA needs production-like seed data before approving PR-14696. The workaround is documented but not yet rehearsed by on-call.
- Blocker: QA needs production-like seed data before approving PR-14696. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Aisha Khan will close the action item before 2022-07-22.
- Update runbook, release checklist, and dashboard annotation for inventory-reservation.

## Meeting MTG-0216 - 2022-07-15 - Customer Escalation Review
- Facilitator: Dmitri Volkov
- Attendees: Samir Rao, Owen Brooks, Noah Evans, Maya Chen, Kim Tan, Nora Singh
- Focus service: search-recommendations
- Related evidence: ATLAS-4158, PR-17409, PD-2896

### Discussion
- Risk: search-recommendations ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4158.
- The team reviewed search-recommendations readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Blocker: QA needs production-like seed data before approving PR-17409. The workaround is documented but not yet rehearsed by on-call.
- Risk: search-recommendations ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4158.
- Risk: search-recommendations ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4158.

### Decisions and Actions
- Owner Kim Tan will close the action item before 2022-07-29.
- Update runbook, release checklist, and dashboard annotation for search-recommendations.

## Meeting MTG-0217 - 2022-07-22 - Architecture Council
- Facilitator: Harper Lee
- Attendees: Ravi Patel, Victor Silva, Elena Petrova, Jon Bell, Ben Carter, Harper Lee
- Focus service: notification-service
- Related evidence: ATLAS-3890, PR-9420, PD-2446

### Discussion
- The team reviewed notification-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Risk: notification-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-3890.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- The team reviewed notification-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Blocker: QA needs production-like seed data before approving PR-9420. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Owen Brooks will close the action item before 2022-08-05.
- Update runbook, release checklist, and dashboard annotation for notification-service.

## Meeting MTG-0218 - 2022-07-29 - Release Readiness
- Facilitator: Aisha Khan
- Attendees: Mateo Garcia, Iris Wang, Elena Petrova, Nora Singh, Samir Rao, Priya Nair
- Focus service: order-ledger
- Related evidence: ATLAS-5332, PR-13332, PD-2797

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Blocker: QA needs production-like seed data before approving PR-13332. The workaround is documented but not yet rehearsed by on-call.
- The team reviewed order-ledger readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.

### Decisions and Actions
- Owner Victor Silva will close the action item before 2022-08-12.
- Update runbook, release checklist, and dashboard annotation for order-ledger.

## Meeting MTG-0219 - 2022-08-05 - Release Readiness
- Facilitator: Noah Evans
- Attendees: Iris Wang, Harper Lee, Noah Evans, Theo Martin, Mateo Garcia, Owen Brooks
- Focus service: order-ledger
- Related evidence: ATLAS-6121, PR-15833, PD-2884

### Discussion
- The team reviewed order-ledger readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Risk: order-ledger ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-6121.
- The team reviewed order-ledger readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Risk: order-ledger ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-6121.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.

### Decisions and Actions
- Owner Theo Martin will close the action item before 2022-08-19.
- Update runbook, release checklist, and dashboard annotation for order-ledger.

## Meeting MTG-0220 - 2022-08-12 - Customer Escalation Review
- Facilitator: Yara Haddad
- Attendees: Iris Wang, Yara Haddad, Jon Bell, Kim Tan, Maya Chen, Owen Brooks
- Focus service: checkout-api
- Related evidence: ATLAS-2269, PR-14317, PD-2696

### Discussion
- The team reviewed checkout-api readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Blocker: QA needs production-like seed data before approving PR-14317. The workaround is documented but not yet rehearsed by on-call.
- Blocker: QA needs production-like seed data before approving PR-14317. The workaround is documented but not yet rehearsed by on-call.
- Blocker: QA needs production-like seed data before approving PR-14317. The workaround is documented but not yet rehearsed by on-call.
- Blocker: QA needs production-like seed data before approving PR-14317. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Maya Chen will close the action item before 2022-08-26.
- Update runbook, release checklist, and dashboard annotation for checkout-api.

## Meeting MTG-0221 - 2022-08-19 - Architecture Council
- Facilitator: Priya Nair
- Attendees: Jon Bell, Elena Petrova, Theo Martin, Ben Carter, Nora Singh, Ravi Patel
- Focus service: payment-orchestrator
- Related evidence: ATLAS-5273, PR-18452, PD-2107

### Discussion
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- The team reviewed payment-orchestrator readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Risk: payment-orchestrator ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5273.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Mateo Garcia will close the action item before 2022-09-02.
- Update runbook, release checklist, and dashboard annotation for payment-orchestrator.

## Meeting MTG-0222 - 2022-08-26 - Architecture Council
- Facilitator: Fatima Noor
- Attendees: Aisha Khan, Noah Evans, Maya Chen, Victor Silva, Theo Martin, Luca Moretti
- Focus service: inventory-reservation
- Related evidence: ATLAS-3642, PR-7851, PD-2503

### Discussion
- The team reviewed inventory-reservation readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- The team reviewed inventory-reservation readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- The team reviewed inventory-reservation readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Nora Singh will close the action item before 2022-09-09.
- Update runbook, release checklist, and dashboard annotation for inventory-reservation.

## Meeting MTG-0223 - 2022-09-02 - SLO Review
- Facilitator: Iris Wang
- Attendees: Samir Rao, Priya Nair, Harper Lee, Luca Moretti, Ravi Patel, Dmitri Volkov
- Focus service: auth-gateway
- Related evidence: ATLAS-1986, PR-18914, PD-2513

### Discussion
- The team reviewed auth-gateway readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Risk: auth-gateway ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-1986.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.

### Decisions and Actions
- Owner Aisha Khan will close the action item before 2022-09-16.
- Update runbook, release checklist, and dashboard annotation for auth-gateway.

## Meeting MTG-0224 - 2022-09-09 - Architecture Council
- Facilitator: Jon Bell
- Attendees: Dmitri Volkov, Luca Moretti, Aisha Khan, Harper Lee, Grace Kim, Mateo Garcia
- Focus service: inventory-reservation
- Related evidence: ATLAS-4451, PR-17216, PD-2276

### Discussion
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- The team reviewed inventory-reservation readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- The team reviewed inventory-reservation readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Risk: inventory-reservation ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4451.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Aisha Khan will close the action item before 2022-09-23.
- Update runbook, release checklist, and dashboard annotation for inventory-reservation.

## Meeting MTG-0225 - 2022-09-16 - Release Readiness
- Facilitator: Iris Wang
- Attendees: Victor Silva, Priya Nair, Elena Petrova, Fatima Noor, Luca Moretti, Ben Carter
- Focus service: order-ledger
- Related evidence: ATLAS-4711, PR-13147, PD-2063

### Discussion
- Risk: order-ledger ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4711.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Blocker: QA needs production-like seed data before approving PR-13147. The workaround is documented but not yet rehearsed by on-call.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Mateo Garcia will close the action item before 2022-09-30.
- Update runbook, release checklist, and dashboard annotation for order-ledger.

## Meeting MTG-0226 - 2022-09-23 - SLO Review
- Facilitator: Aisha Khan
- Attendees: Noah Evans, Ravi Patel, Kim Tan, Fatima Noor, Harper Lee, Iris Wang
- Focus service: checkout-api
- Related evidence: ATLAS-5073, PR-9687, PD-2517

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- The team reviewed checkout-api readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Mateo Garcia will close the action item before 2022-10-07.
- Update runbook, release checklist, and dashboard annotation for checkout-api.

## Meeting MTG-0227 - 2022-09-30 - Customer Escalation Review
- Facilitator: Jon Bell
- Attendees: Fatima Noor, Sara Novak, Aisha Khan, Samir Rao, Mateo Garcia, Nora Singh
- Focus service: tax-service
- Related evidence: ATLAS-1535, PR-6574, PD-2497

### Discussion
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Blocker: QA needs production-like seed data before approving PR-6574. The workaround is documented but not yet rehearsed by on-call.
- The team reviewed tax-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- The team reviewed tax-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Risk: tax-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-1535.

### Decisions and Actions
- Owner Maya Chen will close the action item before 2022-10-14.
- Update runbook, release checklist, and dashboard annotation for tax-service.

## Meeting MTG-0228 - 2022-10-07 - Architecture Council
- Facilitator: Owen Brooks
- Attendees: Victor Silva, Kim Tan, Noah Evans, Maya Chen, Samir Rao, Fatima Noor
- Focus service: analytics-pipeline
- Related evidence: ATLAS-2262, PR-7502, PD-2248

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Blocker: QA needs production-like seed data before approving PR-7502. The workaround is documented but not yet rehearsed by on-call.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- The team reviewed analytics-pipeline readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Blocker: QA needs production-like seed data before approving PR-7502. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Maya Chen will close the action item before 2022-10-21.
- Update runbook, release checklist, and dashboard annotation for analytics-pipeline.

## Meeting MTG-0229 - 2022-10-14 - SLO Review
- Facilitator: Kim Tan
- Attendees: Luca Moretti, Ravi Patel, Sara Novak, Fatima Noor, Mateo Garcia, Victor Silva
- Focus service: cart-service
- Related evidence: ATLAS-3338, PR-5480, PD-2251

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Risk: cart-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-3338.
- Risk: cart-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-3338.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Theo Martin will close the action item before 2022-10-28.
- Update runbook, release checklist, and dashboard annotation for cart-service.

## Meeting MTG-0230 - 2022-10-21 - Incident Review
- Facilitator: Harper Lee
- Attendees: Ben Carter, Owen Brooks, Dmitri Volkov, Maya Chen, Aisha Khan, Priya Nair
- Focus service: checkout-api
- Related evidence: ATLAS-2311, PR-7312, PD-2507

### Discussion
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- The team reviewed checkout-api readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Blocker: QA needs production-like seed data before approving PR-7312. The workaround is documented but not yet rehearsed by on-call.
- Risk: checkout-api ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2311.

### Decisions and Actions
- Owner Jon Bell will close the action item before 2022-11-04.
- Update runbook, release checklist, and dashboard annotation for checkout-api.

## Meeting MTG-0231 - 2022-10-28 - KT Working Session
- Facilitator: Nora Singh
- Attendees: Anika Sharma, Kim Tan, Theo Martin, Yara Haddad, Ravi Patel, Mateo Garcia
- Focus service: notification-service
- Related evidence: ATLAS-2964, PR-7391, PD-2429

### Discussion
- Blocker: QA needs production-like seed data before approving PR-7391. The workaround is documented but not yet rehearsed by on-call.
- Blocker: QA needs production-like seed data before approving PR-7391. The workaround is documented but not yet rehearsed by on-call.
- The team reviewed notification-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Blocker: QA needs production-like seed data before approving PR-7391. The workaround is documented but not yet rehearsed by on-call.
- Risk: notification-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2964.

### Decisions and Actions
- Owner Anika Sharma will close the action item before 2022-11-11.
- Update runbook, release checklist, and dashboard annotation for notification-service.

## Meeting MTG-0232 - 2022-11-04 - Incident Review
- Facilitator: Dmitri Volkov
- Attendees: Nora Singh, Sara Novak, Dmitri Volkov, Kim Tan, Elena Petrova, Iris Wang
- Focus service: inventory-reservation
- Related evidence: ATLAS-2238, PR-8818, PD-2762

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- The team reviewed inventory-reservation readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Blocker: QA needs production-like seed data before approving PR-8818. The workaround is documented but not yet rehearsed by on-call.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Blocker: QA needs production-like seed data before approving PR-8818. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Nora Singh will close the action item before 2022-11-18.
- Update runbook, release checklist, and dashboard annotation for inventory-reservation.

## Meeting MTG-0233 - 2022-11-11 - Customer Escalation Review
- Facilitator: Maya Chen
- Attendees: Mateo Garcia, Luca Moretti, Anika Sharma, Jon Bell, Noah Evans, Theo Martin
- Focus service: payment-orchestrator
- Related evidence: ATLAS-5825, PR-7375, PD-2780

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Blocker: QA needs production-like seed data before approving PR-7375. The workaround is documented but not yet rehearsed by on-call.
- The team reviewed payment-orchestrator readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Blocker: QA needs production-like seed data before approving PR-7375. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Harper Lee will close the action item before 2022-11-25.
- Update runbook, release checklist, and dashboard annotation for payment-orchestrator.

## Meeting MTG-0234 - 2022-11-18 - Architecture Council
- Facilitator: Aisha Khan
- Attendees: Sara Novak, Ravi Patel, Fatima Noor, Samir Rao, Noah Evans, Grace Kim
- Focus service: payment-orchestrator
- Related evidence: ATLAS-4113, PR-7994, PD-2482

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- The team reviewed payment-orchestrator readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Maya Chen will close the action item before 2022-12-02.
- Update runbook, release checklist, and dashboard annotation for payment-orchestrator.

## Meeting MTG-0235 - 2022-11-25 - Incident Review
- Facilitator: Ben Carter
- Attendees: Elena Petrova, Jon Bell, Harper Lee, Samir Rao, Fatima Noor, Iris Wang
- Focus service: loyalty-service
- Related evidence: ATLAS-4163, PR-6882, PD-2657

### Discussion
- Risk: loyalty-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4163.
- Blocker: QA needs production-like seed data before approving PR-6882. The workaround is documented but not yet rehearsed by on-call.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- The team reviewed loyalty-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Nora Singh will close the action item before 2022-12-09.
- Update runbook, release checklist, and dashboard annotation for loyalty-service.

## Meeting MTG-0236 - 2022-12-02 - Steering Review
- Facilitator: Sara Novak
- Attendees: Anika Sharma, Theo Martin, Yara Haddad, Victor Silva, Owen Brooks, Sara Novak
- Focus service: checkout-api
- Related evidence: ATLAS-1702, PR-7328, PD-2353

### Discussion
- The team reviewed checkout-api readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Risk: checkout-api ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-1702.
- Risk: checkout-api ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-1702.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Risk: checkout-api ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-1702.

### Decisions and Actions
- Owner Dmitri Volkov will close the action item before 2022-12-16.
- Update runbook, release checklist, and dashboard annotation for checkout-api.

## Meeting MTG-0237 - 2022-12-09 - SLO Review
- Facilitator: Fatima Noor
- Attendees: Mateo Garcia, Sara Novak, Theo Martin, Owen Brooks, Ben Carter, Yara Haddad
- Focus service: cart-service
- Related evidence: ATLAS-2568, PR-18293, PD-2104

### Discussion
- Blocker: QA needs production-like seed data before approving PR-18293. The workaround is documented but not yet rehearsed by on-call.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Risk: cart-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2568.
- Risk: cart-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2568.
- Risk: cart-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2568.

### Decisions and Actions
- Owner Sara Novak will close the action item before 2022-12-23.
- Update runbook, release checklist, and dashboard annotation for cart-service.

## Meeting MTG-0238 - 2022-12-16 - Customer Escalation Review
- Facilitator: Kim Tan
- Attendees: Noah Evans, Sara Novak, Harper Lee, Owen Brooks, Victor Silva, Dmitri Volkov
- Focus service: payment-orchestrator
- Related evidence: ATLAS-4343, PR-12985, PD-2814

### Discussion
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- The team reviewed payment-orchestrator readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Risk: payment-orchestrator ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4343.
- Blocker: QA needs production-like seed data before approving PR-12985. The workaround is documented but not yet rehearsed by on-call.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Luca Moretti will close the action item before 2022-12-30.
- Update runbook, release checklist, and dashboard annotation for payment-orchestrator.

## Meeting MTG-0239 - 2022-12-23 - Customer Escalation Review
- Facilitator: Maya Chen
- Attendees: Ravi Patel, Iris Wang, Samir Rao, Theo Martin, Harper Lee, Kim Tan
- Focus service: loyalty-service
- Related evidence: ATLAS-1635, PR-13436, PD-2684

### Discussion
- The team reviewed loyalty-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Risk: loyalty-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-1635.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- The team reviewed loyalty-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.

### Decisions and Actions
- Owner Jon Bell will close the action item before 2023-01-06.
- Update runbook, release checklist, and dashboard annotation for loyalty-service.

## Meeting MTG-0240 - 2022-12-30 - Architecture Council
- Facilitator: Luca Moretti
- Attendees: Victor Silva, Nora Singh, Iris Wang, Jon Bell, Yara Haddad, Ravi Patel
- Focus service: checkout-api
- Related evidence: ATLAS-2164, PR-16783, PD-2418

### Discussion
- Risk: checkout-api ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2164.
- Blocker: QA needs production-like seed data before approving PR-16783. The workaround is documented but not yet rehearsed by on-call.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Risk: checkout-api ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2164.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.

### Decisions and Actions
- Owner Jon Bell will close the action item before 2023-01-13.
- Update runbook, release checklist, and dashboard annotation for checkout-api.

## Meeting MTG-0241 - 2023-01-06 - Architecture Council
- Facilitator: Ravi Patel
- Attendees: Sara Novak, Priya Nair, Iris Wang, Fatima Noor, Harper Lee, Kim Tan
- Focus service: pricing-engine
- Related evidence: ATLAS-6119, PR-15062, PD-2560

### Discussion
- Risk: pricing-engine ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-6119.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Risk: pricing-engine ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-6119.
- Risk: pricing-engine ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-6119.
- Risk: pricing-engine ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-6119.

### Decisions and Actions
- Owner Maya Chen will close the action item before 2023-01-20.
- Update runbook, release checklist, and dashboard annotation for pricing-engine.

## Meeting MTG-0242 - 2023-01-13 - KT Working Session
- Facilitator: Anika Sharma
- Attendees: Grace Kim, Anika Sharma, Elena Petrova, Samir Rao, Fatima Noor, Iris Wang
- Focus service: tax-service
- Related evidence: ATLAS-2771, PR-8076, PD-2521

### Discussion
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Blocker: QA needs production-like seed data before approving PR-8076. The workaround is documented but not yet rehearsed by on-call.
- Blocker: QA needs production-like seed data before approving PR-8076. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Noah Evans will close the action item before 2023-01-27.
- Update runbook, release checklist, and dashboard annotation for tax-service.

## Meeting MTG-0243 - 2023-01-20 - Customer Escalation Review
- Facilitator: Noah Evans
- Attendees: Ben Carter, Fatima Noor, Victor Silva, Iris Wang, Luca Moretti, Anika Sharma
- Focus service: payment-orchestrator
- Related evidence: ATLAS-3428, PR-14865, PD-2493

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Blocker: QA needs production-like seed data before approving PR-14865. The workaround is documented but not yet rehearsed by on-call.
- The team reviewed payment-orchestrator readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Risk: payment-orchestrator ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-3428.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Luca Moretti will close the action item before 2023-02-03.
- Update runbook, release checklist, and dashboard annotation for payment-orchestrator.

## Meeting MTG-0244 - 2023-01-27 - Customer Escalation Review
- Facilitator: Grace Kim
- Attendees: Dmitri Volkov, Ravi Patel, Kim Tan, Nora Singh, Samir Rao, Ben Carter
- Focus service: loyalty-service
- Related evidence: ATLAS-2787, PR-14051, PD-2775

### Discussion
- The team reviewed loyalty-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Harper Lee will close the action item before 2023-02-10.
- Update runbook, release checklist, and dashboard annotation for loyalty-service.

## Meeting MTG-0245 - 2023-02-03 - Architecture Council
- Facilitator: Samir Rao
- Attendees: Jon Bell, Maya Chen, Anika Sharma, Sara Novak, Fatima Noor, Samir Rao
- Focus service: auth-gateway
- Related evidence: ATLAS-5505, PR-14880, PD-2218

### Discussion
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Risk: auth-gateway ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5505.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Risk: auth-gateway ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5505.
- Risk: auth-gateway ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5505.

### Decisions and Actions
- Owner Nora Singh will close the action item before 2023-02-17.
- Update runbook, release checklist, and dashboard annotation for auth-gateway.

## Meeting MTG-0246 - 2023-02-10 - Incident Review
- Facilitator: Iris Wang
- Attendees: Elena Petrova, Luca Moretti, Harper Lee, Owen Brooks, Dmitri Volkov, Noah Evans
- Focus service: tax-service
- Related evidence: ATLAS-5603, PR-16892, PD-2304

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Risk: tax-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5603.
- Blocker: QA needs production-like seed data before approving PR-16892. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Anika Sharma will close the action item before 2023-02-24.
- Update runbook, release checklist, and dashboard annotation for tax-service.

## Meeting MTG-0247 - 2023-02-17 - SLO Review
- Facilitator: Kim Tan
- Attendees: Yara Haddad, Ben Carter, Harper Lee, Victor Silva, Elena Petrova, Sara Novak
- Focus service: inventory-reservation
- Related evidence: ATLAS-4366, PR-12249, PD-2588

### Discussion
- Blocker: QA needs production-like seed data before approving PR-12249. The workaround is documented but not yet rehearsed by on-call.
- The team reviewed inventory-reservation readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Risk: inventory-reservation ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4366.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.

### Decisions and Actions
- Owner Harper Lee will close the action item before 2023-03-03.
- Update runbook, release checklist, and dashboard annotation for inventory-reservation.

## Meeting MTG-0248 - 2023-02-24 - Release Readiness
- Facilitator: Luca Moretti
- Attendees: Jon Bell, Nora Singh, Aisha Khan, Luca Moretti, Kim Tan, Owen Brooks
- Focus service: notification-service
- Related evidence: ATLAS-1850, PR-16529, PD-2216

### Discussion
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- The team reviewed notification-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- The team reviewed notification-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- The team reviewed notification-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.

### Decisions and Actions
- Owner Priya Nair will close the action item before 2023-03-10.
- Update runbook, release checklist, and dashboard annotation for notification-service.

## Meeting MTG-0249 - 2023-03-03 - KT Working Session
- Facilitator: Iris Wang
- Attendees: Harper Lee, Jon Bell, Elena Petrova, Sara Novak, Nora Singh, Owen Brooks
- Focus service: inventory-reservation
- Related evidence: ATLAS-5902, PR-6228, PD-2800

### Discussion
- Risk: inventory-reservation ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5902.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- The team reviewed inventory-reservation readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Blocker: QA needs production-like seed data before approving PR-6228. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Elena Petrova will close the action item before 2023-03-17.
- Update runbook, release checklist, and dashboard annotation for inventory-reservation.

## Meeting MTG-0250 - 2023-03-10 - SLO Review
- Facilitator: Nora Singh
- Attendees: Elena Petrova, Sara Novak, Mateo Garcia, Yara Haddad, Ben Carter, Theo Martin
- Focus service: search-recommendations
- Related evidence: ATLAS-3593, PR-6050, PD-2785

### Discussion
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Blocker: QA needs production-like seed data before approving PR-6050. The workaround is documented but not yet rehearsed by on-call.
- Risk: search-recommendations ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-3593.
- Risk: search-recommendations ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-3593.
- Risk: search-recommendations ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-3593.

### Decisions and Actions
- Owner Grace Kim will close the action item before 2023-03-24.
- Update runbook, release checklist, and dashboard annotation for search-recommendations.

## Meeting MTG-0251 - 2023-03-17 - Incident Review
- Facilitator: Ben Carter
- Attendees: Iris Wang, Nora Singh, Grace Kim, Luca Moretti, Ben Carter, Aisha Khan
- Focus service: analytics-pipeline
- Related evidence: ATLAS-4856, PR-16036, PD-2008

### Discussion
- Risk: analytics-pipeline ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4856.
- Blocker: QA needs production-like seed data before approving PR-16036. The workaround is documented but not yet rehearsed by on-call.
- Risk: analytics-pipeline ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4856.
- The team reviewed analytics-pipeline readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Risk: analytics-pipeline ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4856.

### Decisions and Actions
- Owner Priya Nair will close the action item before 2023-03-31.
- Update runbook, release checklist, and dashboard annotation for analytics-pipeline.

## Meeting MTG-0252 - 2023-03-24 - KT Working Session
- Facilitator: Kim Tan
- Attendees: Luca Moretti, Kim Tan, Sara Novak, Jon Bell, Dmitri Volkov, Priya Nair
- Focus service: inventory-reservation
- Related evidence: ATLAS-2336, PR-11640, PD-2511

### Discussion
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- The team reviewed inventory-reservation readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Blocker: QA needs production-like seed data before approving PR-11640. The workaround is documented but not yet rehearsed by on-call.
- The team reviewed inventory-reservation readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.

### Decisions and Actions
- Owner Priya Nair will close the action item before 2023-04-07.
- Update runbook, release checklist, and dashboard annotation for inventory-reservation.

## Meeting MTG-0253 - 2023-03-31 - Incident Review
- Facilitator: Kim Tan
- Attendees: Victor Silva, Grace Kim, Noah Evans, Dmitri Volkov, Yara Haddad, Elena Petrova
- Focus service: auth-gateway
- Related evidence: ATLAS-4268, PR-6797, PD-2458

### Discussion
- Blocker: QA needs production-like seed data before approving PR-6797. The workaround is documented but not yet rehearsed by on-call.
- The team reviewed auth-gateway readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Blocker: QA needs production-like seed data before approving PR-6797. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Theo Martin will close the action item before 2023-04-14.
- Update runbook, release checklist, and dashboard annotation for auth-gateway.

## Meeting MTG-0254 - 2023-04-07 - Architecture Council
- Facilitator: Sara Novak
- Attendees: Aisha Khan, Nora Singh, Kim Tan, Owen Brooks, Maya Chen, Sara Novak
- Focus service: loyalty-service
- Related evidence: ATLAS-2953, PR-11869, PD-2627

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Risk: loyalty-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2953.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- The team reviewed loyalty-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- The team reviewed loyalty-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.

### Decisions and Actions
- Owner Theo Martin will close the action item before 2023-04-21.
- Update runbook, release checklist, and dashboard annotation for loyalty-service.

## Meeting MTG-0255 - 2023-04-14 - Incident Review
- Facilitator: Theo Martin
- Attendees: Anika Sharma, Aisha Khan, Kim Tan, Harper Lee, Ben Carter, Sara Novak
- Focus service: notification-service
- Related evidence: ATLAS-3292, PR-11114, PD-2605

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- The team reviewed notification-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Blocker: QA needs production-like seed data before approving PR-11114. The workaround is documented but not yet rehearsed by on-call.
- Risk: notification-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-3292.
- Risk: notification-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-3292.

### Decisions and Actions
- Owner Fatima Noor will close the action item before 2023-04-28.
- Update runbook, release checklist, and dashboard annotation for notification-service.

## Meeting MTG-0256 - 2023-04-21 - Architecture Council
- Facilitator: Fatima Noor
- Attendees: Owen Brooks, Jon Bell, Maya Chen, Ravi Patel, Victor Silva, Noah Evans
- Focus service: inventory-reservation
- Related evidence: ATLAS-1161, PR-7120, PD-2014

### Discussion
- The team reviewed inventory-reservation readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Blocker: QA needs production-like seed data before approving PR-7120. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Priya Nair will close the action item before 2023-05-05.
- Update runbook, release checklist, and dashboard annotation for inventory-reservation.

## Meeting MTG-0257 - 2023-04-28 - Customer Escalation Review
- Facilitator: Harper Lee
- Attendees: Noah Evans, Nora Singh, Maya Chen, Owen Brooks, Luca Moretti, Victor Silva
- Focus service: inventory-reservation
- Related evidence: ATLAS-2999, PR-10470, PD-2782

### Discussion
- Risk: inventory-reservation ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2999.
- The team reviewed inventory-reservation readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Fatima Noor will close the action item before 2023-05-12.
- Update runbook, release checklist, and dashboard annotation for inventory-reservation.

## Meeting MTG-0258 - 2023-05-05 - Architecture Council
- Facilitator: Mateo Garcia
- Attendees: Ben Carter, Samir Rao, Elena Petrova, Luca Moretti, Maya Chen, Theo Martin
- Focus service: notification-service
- Related evidence: ATLAS-2746, PR-9664, PD-2379

### Discussion
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Risk: notification-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2746.
- The team reviewed notification-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- The team reviewed notification-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.

### Decisions and Actions
- Owner Fatima Noor will close the action item before 2023-05-19.
- Update runbook, release checklist, and dashboard annotation for notification-service.

## Meeting MTG-0259 - 2023-05-12 - Steering Review
- Facilitator: Luca Moretti
- Attendees: Anika Sharma, Dmitri Volkov, Maya Chen, Yara Haddad, Grace Kim, Aisha Khan
- Focus service: loyalty-service
- Related evidence: ATLAS-5176, PR-7817, PD-2003

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Risk: loyalty-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5176.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Owen Brooks will close the action item before 2023-05-26.
- Update runbook, release checklist, and dashboard annotation for loyalty-service.

## Meeting MTG-0260 - 2023-05-19 - Architecture Council
- Facilitator: Fatima Noor
- Attendees: Victor Silva, Priya Nair, Ravi Patel, Grace Kim, Jon Bell, Samir Rao
- Focus service: payment-orchestrator
- Related evidence: ATLAS-4660, PR-15345, PD-2815

### Discussion
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Risk: payment-orchestrator ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4660.
- Risk: payment-orchestrator ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4660.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.

### Decisions and Actions
- Owner Yara Haddad will close the action item before 2023-06-02.
- Update runbook, release checklist, and dashboard annotation for payment-orchestrator.

## Meeting MTG-0261 - 2023-05-26 - Incident Review
- Facilitator: Noah Evans
- Attendees: Grace Kim, Luca Moretti, Sara Novak, Kim Tan, Theo Martin, Harper Lee
- Focus service: inventory-reservation
- Related evidence: ATLAS-5685, PR-7540, PD-2374

### Discussion
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Blocker: QA needs production-like seed data before approving PR-7540. The workaround is documented but not yet rehearsed by on-call.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- The team reviewed inventory-reservation readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.

### Decisions and Actions
- Owner Samir Rao will close the action item before 2023-06-09.
- Update runbook, release checklist, and dashboard annotation for inventory-reservation.

## Meeting MTG-0262 - 2023-06-02 - Customer Escalation Review
- Facilitator: Kim Tan
- Attendees: Anika Sharma, Samir Rao, Nora Singh, Luca Moretti, Iris Wang, Mateo Garcia
- Focus service: payment-orchestrator
- Related evidence: ATLAS-3707, PR-12641, PD-2454

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Blocker: QA needs production-like seed data before approving PR-12641. The workaround is documented but not yet rehearsed by on-call.
- Risk: payment-orchestrator ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-3707.
- Risk: payment-orchestrator ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-3707.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Jon Bell will close the action item before 2023-06-16.
- Update runbook, release checklist, and dashboard annotation for payment-orchestrator.

## Meeting MTG-0263 - 2023-06-09 - SLO Review
- Facilitator: Jon Bell
- Attendees: Kim Tan, Yara Haddad, Ravi Patel, Mateo Garcia, Ben Carter, Maya Chen
- Focus service: loyalty-service
- Related evidence: ATLAS-3068, PR-15293, PD-2443

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- The team reviewed loyalty-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- The team reviewed loyalty-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- The team reviewed loyalty-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.

### Decisions and Actions
- Owner Iris Wang will close the action item before 2023-06-23.
- Update runbook, release checklist, and dashboard annotation for loyalty-service.

## Meeting MTG-0264 - 2023-06-16 - Architecture Council
- Facilitator: Mateo Garcia
- Attendees: Sara Novak, Theo Martin, Ben Carter, Fatima Noor, Maya Chen, Noah Evans
- Focus service: analytics-pipeline
- Related evidence: ATLAS-5636, PR-16503, PD-2719

### Discussion
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- The team reviewed analytics-pipeline readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Blocker: QA needs production-like seed data before approving PR-16503. The workaround is documented but not yet rehearsed by on-call.
- The team reviewed analytics-pipeline readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.

### Decisions and Actions
- Owner Noah Evans will close the action item before 2023-06-30.
- Update runbook, release checklist, and dashboard annotation for analytics-pipeline.

## Meeting MTG-0265 - 2023-06-23 - Release Readiness
- Facilitator: Priya Nair
- Attendees: Nora Singh, Maya Chen, Grace Kim, Anika Sharma, Harper Lee, Aisha Khan
- Focus service: loyalty-service
- Related evidence: ATLAS-3871, PR-18007, PD-2017

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- The team reviewed loyalty-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Risk: loyalty-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-3871.

### Decisions and Actions
- Owner Nora Singh will close the action item before 2023-07-07.
- Update runbook, release checklist, and dashboard annotation for loyalty-service.

## Meeting MTG-0266 - 2023-06-30 - Architecture Council
- Facilitator: Grace Kim
- Attendees: Victor Silva, Harper Lee, Kim Tan, Mateo Garcia, Jon Bell, Luca Moretti
- Focus service: analytics-pipeline
- Related evidence: ATLAS-2111, PR-13206, PD-2643

### Discussion
- The team reviewed analytics-pipeline readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- The team reviewed analytics-pipeline readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Risk: analytics-pipeline ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2111.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Priya Nair will close the action item before 2023-07-14.
- Update runbook, release checklist, and dashboard annotation for analytics-pipeline.

## Meeting MTG-0267 - 2023-07-07 - Steering Review
- Facilitator: Anika Sharma
- Attendees: Fatima Noor, Yara Haddad, Mateo Garcia, Nora Singh, Owen Brooks, Ben Carter
- Focus service: tax-service
- Related evidence: ATLAS-4095, PR-12677, PD-2348

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- The team reviewed tax-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- The team reviewed tax-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Risk: tax-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4095.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.

### Decisions and Actions
- Owner Ben Carter will close the action item before 2023-07-21.
- Update runbook, release checklist, and dashboard annotation for tax-service.

## Meeting MTG-0268 - 2023-07-14 - Architecture Council
- Facilitator: Samir Rao
- Attendees: Fatima Noor, Luca Moretti, Ravi Patel, Maya Chen, Jon Bell, Anika Sharma
- Focus service: loyalty-service
- Related evidence: ATLAS-1737, PR-7667, PD-2392

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- The team reviewed loyalty-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Blocker: QA needs production-like seed data before approving PR-7667. The workaround is documented but not yet rehearsed by on-call.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Kim Tan will close the action item before 2023-07-28.
- Update runbook, release checklist, and dashboard annotation for loyalty-service.

## Meeting MTG-0269 - 2023-07-21 - Steering Review
- Facilitator: Jon Bell
- Attendees: Elena Petrova, Priya Nair, Sara Novak, Samir Rao, Fatima Noor, Victor Silva
- Focus service: checkout-api
- Related evidence: ATLAS-5653, PR-5186, PD-2273

### Discussion
- Blocker: QA needs production-like seed data before approving PR-5186. The workaround is documented but not yet rehearsed by on-call.
- Blocker: QA needs production-like seed data before approving PR-5186. The workaround is documented but not yet rehearsed by on-call.
- The team reviewed checkout-api readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- The team reviewed checkout-api readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- The team reviewed checkout-api readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.

### Decisions and Actions
- Owner Anika Sharma will close the action item before 2023-08-04.
- Update runbook, release checklist, and dashboard annotation for checkout-api.

## Meeting MTG-0270 - 2023-07-28 - KT Working Session
- Facilitator: Luca Moretti
- Attendees: Mateo Garcia, Elena Petrova, Ravi Patel, Luca Moretti, Ben Carter, Owen Brooks
- Focus service: inventory-reservation
- Related evidence: ATLAS-3097, PR-17924, PD-2513

### Discussion
- The team reviewed inventory-reservation readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- The team reviewed inventory-reservation readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Blocker: QA needs production-like seed data before approving PR-17924. The workaround is documented but not yet rehearsed by on-call.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.

### Decisions and Actions
- Owner Grace Kim will close the action item before 2023-08-11.
- Update runbook, release checklist, and dashboard annotation for inventory-reservation.

## Meeting MTG-0271 - 2023-08-04 - Customer Escalation Review
- Facilitator: Iris Wang
- Attendees: Ben Carter, Kim Tan, Grace Kim, Theo Martin, Victor Silva, Maya Chen
- Focus service: search-recommendations
- Related evidence: ATLAS-1406, PR-16777, PD-2498

### Discussion
- The team reviewed search-recommendations readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- The team reviewed search-recommendations readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Risk: search-recommendations ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-1406.
- Risk: search-recommendations ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-1406.
- Risk: search-recommendations ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-1406.

### Decisions and Actions
- Owner Aisha Khan will close the action item before 2023-08-18.
- Update runbook, release checklist, and dashboard annotation for search-recommendations.

## Meeting MTG-0272 - 2023-08-11 - Release Readiness
- Facilitator: Elena Petrova
- Attendees: Victor Silva, Kim Tan, Fatima Noor, Ravi Patel, Noah Evans, Sara Novak
- Focus service: inventory-reservation
- Related evidence: ATLAS-5646, PR-16490, PD-2122

### Discussion
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- The team reviewed inventory-reservation readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Blocker: QA needs production-like seed data before approving PR-16490. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Owen Brooks will close the action item before 2023-08-25.
- Update runbook, release checklist, and dashboard annotation for inventory-reservation.

## Meeting MTG-0273 - 2023-08-18 - Incident Review
- Facilitator: Iris Wang
- Attendees: Yara Haddad, Aisha Khan, Anika Sharma, Samir Rao, Priya Nair, Owen Brooks
- Focus service: search-recommendations
- Related evidence: ATLAS-1429, PR-14688, PD-2016

### Discussion
- Risk: search-recommendations ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-1429.
- The team reviewed search-recommendations readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- The team reviewed search-recommendations readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- The team reviewed search-recommendations readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.

### Decisions and Actions
- Owner Maya Chen will close the action item before 2023-09-01.
- Update runbook, release checklist, and dashboard annotation for search-recommendations.

## Meeting MTG-0274 - 2023-08-25 - Steering Review
- Facilitator: Jon Bell
- Attendees: Maya Chen, Sara Novak, Ben Carter, Owen Brooks, Anika Sharma, Iris Wang
- Focus service: notification-service
- Related evidence: ATLAS-6183, PR-12649, PD-2073

### Discussion
- Risk: notification-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-6183.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Blocker: QA needs production-like seed data before approving PR-12649. The workaround is documented but not yet rehearsed by on-call.
- Risk: notification-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-6183.
- The team reviewed notification-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.

### Decisions and Actions
- Owner Elena Petrova will close the action item before 2023-09-08.
- Update runbook, release checklist, and dashboard annotation for notification-service.

## Meeting MTG-0275 - 2023-09-01 - SLO Review
- Facilitator: Samir Rao
- Attendees: Priya Nair, Dmitri Volkov, Iris Wang, Anika Sharma, Aisha Khan, Samir Rao
- Focus service: payment-orchestrator
- Related evidence: ATLAS-3831, PR-9013, PD-2063

### Discussion
- Blocker: QA needs production-like seed data before approving PR-9013. The workaround is documented but not yet rehearsed by on-call.
- The team reviewed payment-orchestrator readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Risk: payment-orchestrator ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-3831.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Luca Moretti will close the action item before 2023-09-15.
- Update runbook, release checklist, and dashboard annotation for payment-orchestrator.

## Meeting MTG-0276 - 2023-09-08 - Architecture Council
- Facilitator: Priya Nair
- Attendees: Elena Petrova, Fatima Noor, Ravi Patel, Jon Bell, Maya Chen, Aisha Khan
- Focus service: analytics-pipeline
- Related evidence: ATLAS-4117, PR-11793, PD-2625

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Blocker: QA needs production-like seed data before approving PR-11793. The workaround is documented but not yet rehearsed by on-call.
- Risk: analytics-pipeline ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4117.

### Decisions and Actions
- Owner Ravi Patel will close the action item before 2023-09-22.
- Update runbook, release checklist, and dashboard annotation for analytics-pipeline.

## Meeting MTG-0277 - 2023-09-15 - Architecture Council
- Facilitator: Ben Carter
- Attendees: Luca Moretti, Mateo Garcia, Samir Rao, Theo Martin, Ben Carter, Maya Chen
- Focus service: inventory-reservation
- Related evidence: ATLAS-1453, PR-12061, PD-2063

### Discussion
- Blocker: QA needs production-like seed data before approving PR-12061. The workaround is documented but not yet rehearsed by on-call.
- The team reviewed inventory-reservation readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Risk: inventory-reservation ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-1453.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.

### Decisions and Actions
- Owner Fatima Noor will close the action item before 2023-09-29.
- Update runbook, release checklist, and dashboard annotation for inventory-reservation.

## Meeting MTG-0278 - 2023-09-22 - Customer Escalation Review
- Facilitator: Victor Silva
- Attendees: Samir Rao, Noah Evans, Priya Nair, Fatima Noor, Iris Wang, Dmitri Volkov
- Focus service: tax-service
- Related evidence: ATLAS-3084, PR-14409, PD-2236

### Discussion
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Blocker: QA needs production-like seed data before approving PR-14409. The workaround is documented but not yet rehearsed by on-call.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Risk: tax-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-3084.

### Decisions and Actions
- Owner Aisha Khan will close the action item before 2023-10-06.
- Update runbook, release checklist, and dashboard annotation for tax-service.

## Meeting MTG-0279 - 2023-09-29 - Architecture Council
- Facilitator: Mateo Garcia
- Attendees: Yara Haddad, Harper Lee, Sara Novak, Anika Sharma, Theo Martin, Grace Kim
- Focus service: inventory-reservation
- Related evidence: ATLAS-1163, PR-8355, PD-2812

### Discussion
- Blocker: QA needs production-like seed data before approving PR-8355. The workaround is documented but not yet rehearsed by on-call.
- Risk: inventory-reservation ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-1163.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Blocker: QA needs production-like seed data before approving PR-8355. The workaround is documented but not yet rehearsed by on-call.
- Risk: inventory-reservation ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-1163.

### Decisions and Actions
- Owner Anika Sharma will close the action item before 2023-10-13.
- Update runbook, release checklist, and dashboard annotation for inventory-reservation.

## Meeting MTG-0280 - 2023-10-06 - Incident Review
- Facilitator: Jon Bell
- Attendees: Noah Evans, Harper Lee, Theo Martin, Priya Nair, Anika Sharma, Maya Chen
- Focus service: cart-service
- Related evidence: ATLAS-6181, PR-16491, PD-2429

### Discussion
- Risk: cart-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-6181.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Risk: cart-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-6181.
- The team reviewed cart-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Mateo Garcia will close the action item before 2023-10-20.
- Update runbook, release checklist, and dashboard annotation for cart-service.

## Meeting MTG-0281 - 2023-10-13 - Incident Review
- Facilitator: Ravi Patel
- Attendees: Grace Kim, Sara Novak, Ravi Patel, Dmitri Volkov, Anika Sharma, Priya Nair
- Focus service: payment-orchestrator
- Related evidence: ATLAS-5017, PR-8803, PD-2634

### Discussion
- The team reviewed payment-orchestrator readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Risk: payment-orchestrator ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5017.

### Decisions and Actions
- Owner Aisha Khan will close the action item before 2023-10-27.
- Update runbook, release checklist, and dashboard annotation for payment-orchestrator.

## Meeting MTG-0282 - 2023-10-20 - Release Readiness
- Facilitator: Aisha Khan
- Attendees: Fatima Noor, Noah Evans, Owen Brooks, Luca Moretti, Harper Lee, Iris Wang
- Focus service: checkout-api
- Related evidence: ATLAS-2640, PR-10702, PD-2206

### Discussion
- Blocker: QA needs production-like seed data before approving PR-10702. The workaround is documented but not yet rehearsed by on-call.
- Blocker: QA needs production-like seed data before approving PR-10702. The workaround is documented but not yet rehearsed by on-call.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- The team reviewed checkout-api readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.

### Decisions and Actions
- Owner Luca Moretti will close the action item before 2023-11-03.
- Update runbook, release checklist, and dashboard annotation for checkout-api.

## Meeting MTG-0283 - 2023-10-27 - Steering Review
- Facilitator: Kim Tan
- Attendees: Aisha Khan, Anika Sharma, Kim Tan, Fatima Noor, Mateo Garcia, Ravi Patel
- Focus service: cart-service
- Related evidence: ATLAS-3957, PR-16561, PD-2362

### Discussion
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Blocker: QA needs production-like seed data before approving PR-16561. The workaround is documented but not yet rehearsed by on-call.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- The team reviewed cart-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Risk: cart-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-3957.

### Decisions and Actions
- Owner Elena Petrova will close the action item before 2023-11-10.
- Update runbook, release checklist, and dashboard annotation for cart-service.

## Meeting MTG-0284 - 2023-11-03 - Release Readiness
- Facilitator: Priya Nair
- Attendees: Mateo Garcia, Jon Bell, Samir Rao, Grace Kim, Elena Petrova, Ben Carter
- Focus service: search-recommendations
- Related evidence: ATLAS-3503, PR-9362, PD-2520

### Discussion
- Risk: search-recommendations ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-3503.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Risk: search-recommendations ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-3503.
- The team reviewed search-recommendations readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- The team reviewed search-recommendations readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.

### Decisions and Actions
- Owner Fatima Noor will close the action item before 2023-11-17.
- Update runbook, release checklist, and dashboard annotation for search-recommendations.

## Meeting MTG-0285 - 2023-11-10 - SLO Review
- Facilitator: Victor Silva
- Attendees: Iris Wang, Jon Bell, Samir Rao, Luca Moretti, Mateo Garcia, Owen Brooks
- Focus service: inventory-reservation
- Related evidence: ATLAS-1652, PR-18164, PD-2460

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- The team reviewed inventory-reservation readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Risk: inventory-reservation ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-1652.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.

### Decisions and Actions
- Owner Jon Bell will close the action item before 2023-11-24.
- Update runbook, release checklist, and dashboard annotation for inventory-reservation.

## Meeting MTG-0286 - 2023-11-17 - Release Readiness
- Facilitator: Mateo Garcia
- Attendees: Luca Moretti, Yara Haddad, Nora Singh, Maya Chen, Theo Martin, Priya Nair
- Focus service: checkout-api
- Related evidence: ATLAS-5353, PR-19000, PD-2016

### Discussion
- The team reviewed checkout-api readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Risk: checkout-api ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5353.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Jon Bell will close the action item before 2023-12-01.
- Update runbook, release checklist, and dashboard annotation for checkout-api.

## Meeting MTG-0287 - 2023-11-24 - Steering Review
- Facilitator: Harper Lee
- Attendees: Elena Petrova, Luca Moretti, Dmitri Volkov, Aisha Khan, Nora Singh, Ben Carter
- Focus service: loyalty-service
- Related evidence: ATLAS-4596, PR-9023, PD-2533

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- The team reviewed loyalty-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Blocker: QA needs production-like seed data before approving PR-9023. The workaround is documented but not yet rehearsed by on-call.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.

### Decisions and Actions
- Owner Samir Rao will close the action item before 2023-12-08.
- Update runbook, release checklist, and dashboard annotation for loyalty-service.

## Meeting MTG-0288 - 2023-12-01 - Steering Review
- Facilitator: Ravi Patel
- Attendees: Mateo Garcia, Anika Sharma, Ravi Patel, Fatima Noor, Kim Tan, Priya Nair
- Focus service: auth-gateway
- Related evidence: ATLAS-3876, PR-11424, PD-2402

### Discussion
- The team reviewed auth-gateway readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- The team reviewed auth-gateway readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Risk: auth-gateway ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-3876.
- Blocker: QA needs production-like seed data before approving PR-11424. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Fatima Noor will close the action item before 2023-12-15.
- Update runbook, release checklist, and dashboard annotation for auth-gateway.

## Meeting MTG-0289 - 2023-12-08 - Architecture Council
- Facilitator: Jon Bell
- Attendees: Elena Petrova, Dmitri Volkov, Kim Tan, Iris Wang, Yara Haddad, Jon Bell
- Focus service: tax-service
- Related evidence: ATLAS-3496, PR-5743, PD-2482

### Discussion
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Blocker: QA needs production-like seed data before approving PR-5743. The workaround is documented but not yet rehearsed by on-call.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- The team reviewed tax-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.

### Decisions and Actions
- Owner Jon Bell will close the action item before 2023-12-22.
- Update runbook, release checklist, and dashboard annotation for tax-service.

## Meeting MTG-0290 - 2023-12-15 - KT Working Session
- Facilitator: Victor Silva
- Attendees: Fatima Noor, Dmitri Volkov, Priya Nair, Iris Wang, Ben Carter, Nora Singh
- Focus service: loyalty-service
- Related evidence: ATLAS-2341, PR-11617, PD-2067

### Discussion
- Risk: loyalty-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2341.
- The team reviewed loyalty-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Risk: loyalty-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2341.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Kim Tan will close the action item before 2023-12-29.
- Update runbook, release checklist, and dashboard annotation for loyalty-service.

## Meeting MTG-0291 - 2023-12-22 - Architecture Council
- Facilitator: Elena Petrova
- Attendees: Harper Lee, Elena Petrova, Victor Silva, Grace Kim, Noah Evans, Sara Novak
- Focus service: pricing-engine
- Related evidence: ATLAS-2942, PR-15473, PD-2672

### Discussion
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Risk: pricing-engine ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2942.
- Risk: pricing-engine ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2942.
- Blocker: QA needs production-like seed data before approving PR-15473. The workaround is documented but not yet rehearsed by on-call.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.

### Decisions and Actions
- Owner Ravi Patel will close the action item before 2024-01-05.
- Update runbook, release checklist, and dashboard annotation for pricing-engine.

## Meeting MTG-0292 - 2023-12-29 - Incident Review
- Facilitator: Noah Evans
- Attendees: Ben Carter, Fatima Noor, Victor Silva, Maya Chen, Luca Moretti, Grace Kim
- Focus service: cart-service
- Related evidence: ATLAS-3384, PR-12532, PD-2322

### Discussion
- The team reviewed cart-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- The team reviewed cart-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Risk: cart-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-3384.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.

### Decisions and Actions
- Owner Kim Tan will close the action item before 2024-01-12.
- Update runbook, release checklist, and dashboard annotation for cart-service.

## Meeting MTG-0293 - 2024-01-05 - KT Working Session
- Facilitator: Kim Tan
- Attendees: Ben Carter, Theo Martin, Yara Haddad, Aisha Khan, Grace Kim, Anika Sharma
- Focus service: pricing-engine
- Related evidence: ATLAS-1331, PR-16471, PD-2226

### Discussion
- The team reviewed pricing-engine readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Risk: pricing-engine ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-1331.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- The team reviewed pricing-engine readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.

### Decisions and Actions
- Owner Mateo Garcia will close the action item before 2024-01-19.
- Update runbook, release checklist, and dashboard annotation for pricing-engine.

## Meeting MTG-0294 - 2024-01-12 - Release Readiness
- Facilitator: Ben Carter
- Attendees: Owen Brooks, Ben Carter, Dmitri Volkov, Fatima Noor, Luca Moretti, Victor Silva
- Focus service: tax-service
- Related evidence: ATLAS-1981, PR-15803, PD-2338

### Discussion
- Blocker: QA needs production-like seed data before approving PR-15803. The workaround is documented but not yet rehearsed by on-call.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Blocker: QA needs production-like seed data before approving PR-15803. The workaround is documented but not yet rehearsed by on-call.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Jon Bell will close the action item before 2024-01-26.
- Update runbook, release checklist, and dashboard annotation for tax-service.

## Meeting MTG-0295 - 2024-01-19 - Release Readiness
- Facilitator: Ravi Patel
- Attendees: Victor Silva, Grace Kim, Fatima Noor, Priya Nair, Owen Brooks, Samir Rao
- Focus service: auth-gateway
- Related evidence: ATLAS-5893, PR-9199, PD-2170

### Discussion
- Risk: auth-gateway ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5893.
- The team reviewed auth-gateway readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Blocker: QA needs production-like seed data before approving PR-9199. The workaround is documented but not yet rehearsed by on-call.
- The team reviewed auth-gateway readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.

### Decisions and Actions
- Owner Luca Moretti will close the action item before 2024-02-02.
- Update runbook, release checklist, and dashboard annotation for auth-gateway.

## Meeting MTG-0296 - 2024-01-26 - SLO Review
- Facilitator: Dmitri Volkov
- Attendees: Yara Haddad, Harper Lee, Mateo Garcia, Grace Kim, Fatima Noor, Kim Tan
- Focus service: search-recommendations
- Related evidence: ATLAS-1487, PR-10781, PD-2891

### Discussion
- Risk: search-recommendations ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-1487.
- Risk: search-recommendations ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-1487.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Blocker: QA needs production-like seed data before approving PR-10781. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Elena Petrova will close the action item before 2024-02-09.
- Update runbook, release checklist, and dashboard annotation for search-recommendations.

## Meeting MTG-0297 - 2024-02-02 - KT Working Session
- Facilitator: Theo Martin
- Attendees: Theo Martin, Dmitri Volkov, Samir Rao, Mateo Garcia, Kim Tan, Ben Carter
- Focus service: notification-service
- Related evidence: ATLAS-3570, PR-10142, PD-2678

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Blocker: QA needs production-like seed data before approving PR-10142. The workaround is documented but not yet rehearsed by on-call.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.

### Decisions and Actions
- Owner Dmitri Volkov will close the action item before 2024-02-16.
- Update runbook, release checklist, and dashboard annotation for notification-service.

## Meeting MTG-0298 - 2024-02-09 - Incident Review
- Facilitator: Nora Singh
- Attendees: Yara Haddad, Aisha Khan, Grace Kim, Owen Brooks, Jon Bell, Nora Singh
- Focus service: tax-service
- Related evidence: ATLAS-3080, PR-17660, PD-2060

### Discussion
- Blocker: QA needs production-like seed data before approving PR-17660. The workaround is documented but not yet rehearsed by on-call.
- The team reviewed tax-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Blocker: QA needs production-like seed data before approving PR-17660. The workaround is documented but not yet rehearsed by on-call.
- Risk: tax-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-3080.
- Risk: tax-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-3080.

### Decisions and Actions
- Owner Nora Singh will close the action item before 2024-02-23.
- Update runbook, release checklist, and dashboard annotation for tax-service.

## Meeting MTG-0299 - 2024-02-16 - KT Working Session
- Facilitator: Grace Kim
- Attendees: Dmitri Volkov, Iris Wang, Sara Novak, Theo Martin, Luca Moretti, Mateo Garcia
- Focus service: payment-orchestrator
- Related evidence: ATLAS-3502, PR-7722, PD-2556

### Discussion
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Risk: payment-orchestrator ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-3502.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- The team reviewed payment-orchestrator readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Risk: payment-orchestrator ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-3502.

### Decisions and Actions
- Owner Victor Silva will close the action item before 2024-03-01.
- Update runbook, release checklist, and dashboard annotation for payment-orchestrator.

## Meeting MTG-0300 - 2024-02-23 - Architecture Council
- Facilitator: Aisha Khan
- Attendees: Samir Rao, Yara Haddad, Elena Petrova, Ravi Patel, Aisha Khan, Victor Silva
- Focus service: analytics-pipeline
- Related evidence: ATLAS-3262, PR-6096, PD-2832

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Blocker: QA needs production-like seed data before approving PR-6096. The workaround is documented but not yet rehearsed by on-call.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.

### Decisions and Actions
- Owner Ben Carter will close the action item before 2024-03-08.
- Update runbook, release checklist, and dashboard annotation for analytics-pipeline.

## Meeting MTG-0301 - 2024-03-01 - Steering Review
- Facilitator: Fatima Noor
- Attendees: Ben Carter, Aisha Khan, Mateo Garcia, Maya Chen, Elena Petrova, Anika Sharma
- Focus service: payment-orchestrator
- Related evidence: ATLAS-5294, PR-14946, PD-2001

### Discussion
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- The team reviewed payment-orchestrator readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- The team reviewed payment-orchestrator readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- The team reviewed payment-orchestrator readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.

### Decisions and Actions
- Owner Fatima Noor will close the action item before 2024-03-15.
- Update runbook, release checklist, and dashboard annotation for payment-orchestrator.

## Meeting MTG-0302 - 2024-03-08 - Incident Review
- Facilitator: Ben Carter
- Attendees: Harper Lee, Grace Kim, Ravi Patel, Luca Moretti, Owen Brooks, Kim Tan
- Focus service: order-ledger
- Related evidence: ATLAS-3403, PR-11357, PD-2855

### Discussion
- The team reviewed order-ledger readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Risk: order-ledger ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-3403.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.

### Decisions and Actions
- Owner Maya Chen will close the action item before 2024-03-22.
- Update runbook, release checklist, and dashboard annotation for order-ledger.

## Meeting MTG-0303 - 2024-03-15 - Architecture Council
- Facilitator: Priya Nair
- Attendees: Owen Brooks, Elena Petrova, Iris Wang, Priya Nair, Mateo Garcia, Samir Rao
- Focus service: tax-service
- Related evidence: ATLAS-3190, PR-16991, PD-2244

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- The team reviewed tax-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Victor Silva will close the action item before 2024-03-29.
- Update runbook, release checklist, and dashboard annotation for tax-service.

## Meeting MTG-0304 - 2024-03-22 - Architecture Council
- Facilitator: Elena Petrova
- Attendees: Priya Nair, Aisha Khan, Luca Moretti, Samir Rao, Jon Bell, Ravi Patel
- Focus service: checkout-api
- Related evidence: ATLAS-3556, PR-14999, PD-2677

### Discussion
- The team reviewed checkout-api readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Blocker: QA needs production-like seed data before approving PR-14999. The workaround is documented but not yet rehearsed by on-call.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Kim Tan will close the action item before 2024-04-05.
- Update runbook, release checklist, and dashboard annotation for checkout-api.

## Meeting MTG-0305 - 2024-03-29 - Customer Escalation Review
- Facilitator: Theo Martin
- Attendees: Priya Nair, Sara Novak, Theo Martin, Yara Haddad, Fatima Noor, Ben Carter
- Focus service: pricing-engine
- Related evidence: ATLAS-3521, PR-16610, PD-2061

### Discussion
- Risk: pricing-engine ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-3521.
- The team reviewed pricing-engine readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Risk: pricing-engine ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-3521.
- The team reviewed pricing-engine readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Risk: pricing-engine ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-3521.

### Decisions and Actions
- Owner Anika Sharma will close the action item before 2024-04-12.
- Update runbook, release checklist, and dashboard annotation for pricing-engine.

## Meeting MTG-0306 - 2024-04-05 - KT Working Session
- Facilitator: Yara Haddad
- Attendees: Grace Kim, Kim Tan, Nora Singh, Fatima Noor, Samir Rao, Mateo Garcia
- Focus service: auth-gateway
- Related evidence: ATLAS-5602, PR-14022, PD-2210

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- The team reviewed auth-gateway readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Risk: auth-gateway ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5602.

### Decisions and Actions
- Owner Noah Evans will close the action item before 2024-04-19.
- Update runbook, release checklist, and dashboard annotation for auth-gateway.

## Meeting MTG-0307 - 2024-04-12 - Architecture Council
- Facilitator: Harper Lee
- Attendees: Theo Martin, Harper Lee, Victor Silva, Yara Haddad, Noah Evans, Mateo Garcia
- Focus service: notification-service
- Related evidence: ATLAS-5482, PR-13961, PD-2814

### Discussion
- Risk: notification-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5482.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Blocker: QA needs production-like seed data before approving PR-13961. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Luca Moretti will close the action item before 2024-04-26.
- Update runbook, release checklist, and dashboard annotation for notification-service.

## Meeting MTG-0308 - 2024-04-19 - Incident Review
- Facilitator: Noah Evans
- Attendees: Dmitri Volkov, Ravi Patel, Kim Tan, Victor Silva, Aisha Khan, Noah Evans
- Focus service: order-ledger
- Related evidence: ATLAS-1887, PR-9427, PD-2771

### Discussion
- Blocker: QA needs production-like seed data before approving PR-9427. The workaround is documented but not yet rehearsed by on-call.
- Blocker: QA needs production-like seed data before approving PR-9427. The workaround is documented but not yet rehearsed by on-call.
- Risk: order-ledger ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-1887.
- Blocker: QA needs production-like seed data before approving PR-9427. The workaround is documented but not yet rehearsed by on-call.
- The team reviewed order-ledger readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.

### Decisions and Actions
- Owner Grace Kim will close the action item before 2024-05-03.
- Update runbook, release checklist, and dashboard annotation for order-ledger.

## Meeting MTG-0309 - 2024-04-26 - Architecture Council
- Facilitator: Aisha Khan
- Attendees: Maya Chen, Noah Evans, Luca Moretti, Nora Singh, Yara Haddad, Anika Sharma
- Focus service: analytics-pipeline
- Related evidence: ATLAS-5812, PR-8660, PD-2186

### Discussion
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Risk: analytics-pipeline ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5812.
- Risk: analytics-pipeline ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5812.
- Risk: analytics-pipeline ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5812.
- Risk: analytics-pipeline ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5812.

### Decisions and Actions
- Owner Luca Moretti will close the action item before 2024-05-10.
- Update runbook, release checklist, and dashboard annotation for analytics-pipeline.

## Meeting MTG-0310 - 2024-05-03 - KT Working Session
- Facilitator: Nora Singh
- Attendees: Priya Nair, Iris Wang, Ravi Patel, Maya Chen, Nora Singh, Yara Haddad
- Focus service: checkout-api
- Related evidence: ATLAS-4688, PR-15936, PD-2318

### Discussion
- Blocker: QA needs production-like seed data before approving PR-15936. The workaround is documented but not yet rehearsed by on-call.
- Risk: checkout-api ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4688.
- The team reviewed checkout-api readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.

### Decisions and Actions
- Owner Samir Rao will close the action item before 2024-05-17.
- Update runbook, release checklist, and dashboard annotation for checkout-api.

## Meeting MTG-0311 - 2024-05-10 - KT Working Session
- Facilitator: Anika Sharma
- Attendees: Elena Petrova, Grace Kim, Theo Martin, Fatima Noor, Anika Sharma, Maya Chen
- Focus service: order-ledger
- Related evidence: ATLAS-4053, PR-18138, PD-2496

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Risk: order-ledger ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4053.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- The team reviewed order-ledger readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- The team reviewed order-ledger readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.

### Decisions and Actions
- Owner Maya Chen will close the action item before 2024-05-24.
- Update runbook, release checklist, and dashboard annotation for order-ledger.

## Meeting MTG-0312 - 2024-05-17 - KT Working Session
- Facilitator: Ben Carter
- Attendees: Grace Kim, Elena Petrova, Luca Moretti, Maya Chen, Harper Lee, Samir Rao
- Focus service: pricing-engine
- Related evidence: ATLAS-4213, PR-16141, PD-2474

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- The team reviewed pricing-engine readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Blocker: QA needs production-like seed data before approving PR-16141. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Mateo Garcia will close the action item before 2024-05-31.
- Update runbook, release checklist, and dashboard annotation for pricing-engine.

## Meeting MTG-0313 - 2024-05-24 - Architecture Council
- Facilitator: Owen Brooks
- Attendees: Owen Brooks, Yara Haddad, Luca Moretti, Elena Petrova, Noah Evans, Dmitri Volkov
- Focus service: notification-service
- Related evidence: ATLAS-4561, PR-9137, PD-2301

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Risk: notification-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4561.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Risk: notification-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4561.
- Blocker: QA needs production-like seed data before approving PR-9137. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Ben Carter will close the action item before 2024-06-07.
- Update runbook, release checklist, and dashboard annotation for notification-service.

## Meeting MTG-0314 - 2024-05-31 - SLO Review
- Facilitator: Kim Tan
- Attendees: Anika Sharma, Owen Brooks, Fatima Noor, Theo Martin, Kim Tan, Victor Silva
- Focus service: analytics-pipeline
- Related evidence: ATLAS-1275, PR-8260, PD-2153

### Discussion
- The team reviewed analytics-pipeline readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Luca Moretti will close the action item before 2024-06-14.
- Update runbook, release checklist, and dashboard annotation for analytics-pipeline.

## Meeting MTG-0315 - 2024-06-07 - Architecture Council
- Facilitator: Yara Haddad
- Attendees: Noah Evans, Victor Silva, Elena Petrova, Aisha Khan, Ravi Patel, Mateo Garcia
- Focus service: inventory-reservation
- Related evidence: ATLAS-1979, PR-13278, PD-2616

### Discussion
- Blocker: QA needs production-like seed data before approving PR-13278. The workaround is documented but not yet rehearsed by on-call.
- Blocker: QA needs production-like seed data before approving PR-13278. The workaround is documented but not yet rehearsed by on-call.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Risk: inventory-reservation ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-1979.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.

### Decisions and Actions
- Owner Harper Lee will close the action item before 2024-06-21.
- Update runbook, release checklist, and dashboard annotation for inventory-reservation.

## Meeting MTG-0316 - 2024-06-14 - Release Readiness
- Facilitator: Victor Silva
- Attendees: Mateo Garcia, Jon Bell, Samir Rao, Anika Sharma, Owen Brooks, Maya Chen
- Focus service: auth-gateway
- Related evidence: ATLAS-3751, PR-16444, PD-2452

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Risk: auth-gateway ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-3751.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- The team reviewed auth-gateway readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.

### Decisions and Actions
- Owner Samir Rao will close the action item before 2024-06-28.
- Update runbook, release checklist, and dashboard annotation for auth-gateway.

## Meeting MTG-0317 - 2024-06-21 - Architecture Council
- Facilitator: Noah Evans
- Attendees: Sara Novak, Dmitri Volkov, Kim Tan, Luca Moretti, Fatima Noor, Maya Chen
- Focus service: order-ledger
- Related evidence: ATLAS-4992, PR-10174, PD-2720

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Blocker: QA needs production-like seed data before approving PR-10174. The workaround is documented but not yet rehearsed by on-call.
- Risk: order-ledger ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4992.
- Risk: order-ledger ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4992.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Aisha Khan will close the action item before 2024-07-05.
- Update runbook, release checklist, and dashboard annotation for order-ledger.

## Meeting MTG-0318 - 2024-06-28 - Customer Escalation Review
- Facilitator: Nora Singh
- Attendees: Ben Carter, Noah Evans, Dmitri Volkov, Priya Nair, Owen Brooks, Jon Bell
- Focus service: loyalty-service
- Related evidence: ATLAS-5194, PR-7988, PD-2119

### Discussion
- Risk: loyalty-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5194.
- Blocker: QA needs production-like seed data before approving PR-7988. The workaround is documented but not yet rehearsed by on-call.
- The team reviewed loyalty-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Risk: loyalty-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5194.
- Blocker: QA needs production-like seed data before approving PR-7988. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Dmitri Volkov will close the action item before 2024-07-12.
- Update runbook, release checklist, and dashboard annotation for loyalty-service.

## Meeting MTG-0319 - 2024-07-05 - Steering Review
- Facilitator: Fatima Noor
- Attendees: Yara Haddad, Ravi Patel, Anika Sharma, Noah Evans, Kim Tan, Ben Carter
- Focus service: notification-service
- Related evidence: ATLAS-4735, PR-10011, PD-2722

### Discussion
- Risk: notification-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4735.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- The team reviewed notification-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Blocker: QA needs production-like seed data before approving PR-10011. The workaround is documented but not yet rehearsed by on-call.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.

### Decisions and Actions
- Owner Yara Haddad will close the action item before 2024-07-19.
- Update runbook, release checklist, and dashboard annotation for notification-service.

## Meeting MTG-0320 - 2024-07-12 - Architecture Council
- Facilitator: Aisha Khan
- Attendees: Jon Bell, Dmitri Volkov, Fatima Noor, Yara Haddad, Mateo Garcia, Ravi Patel
- Focus service: tax-service
- Related evidence: ATLAS-2485, PR-8841, PD-2078

### Discussion
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Blocker: QA needs production-like seed data before approving PR-8841. The workaround is documented but not yet rehearsed by on-call.
- The team reviewed tax-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Blocker: QA needs production-like seed data before approving PR-8841. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Kim Tan will close the action item before 2024-07-26.
- Update runbook, release checklist, and dashboard annotation for tax-service.

## Meeting MTG-0321 - 2024-07-19 - Steering Review
- Facilitator: Grace Kim
- Attendees: Ben Carter, Victor Silva, Aisha Khan, Owen Brooks, Samir Rao, Nora Singh
- Focus service: notification-service
- Related evidence: ATLAS-5365, PR-17926, PD-2321

### Discussion
- The team reviewed notification-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Risk: notification-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5365.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Anika Sharma will close the action item before 2024-08-02.
- Update runbook, release checklist, and dashboard annotation for notification-service.

## Meeting MTG-0322 - 2024-07-26 - SLO Review
- Facilitator: Yara Haddad
- Attendees: Fatima Noor, Anika Sharma, Nora Singh, Aisha Khan, Iris Wang, Victor Silva
- Focus service: pricing-engine
- Related evidence: ATLAS-6099, PR-8879, PD-2019

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Risk: pricing-engine ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-6099.
- Risk: pricing-engine ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-6099.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Elena Petrova will close the action item before 2024-08-09.
- Update runbook, release checklist, and dashboard annotation for pricing-engine.

## Meeting MTG-0323 - 2024-08-02 - Architecture Council
- Facilitator: Dmitri Volkov
- Attendees: Noah Evans, Iris Wang, Harper Lee, Priya Nair, Anika Sharma, Maya Chen
- Focus service: analytics-pipeline
- Related evidence: ATLAS-2777, PR-7700, PD-2167

### Discussion
- Risk: analytics-pipeline ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2777.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Risk: analytics-pipeline ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2777.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Risk: analytics-pipeline ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2777.

### Decisions and Actions
- Owner Jon Bell will close the action item before 2024-08-16.
- Update runbook, release checklist, and dashboard annotation for analytics-pipeline.

## Meeting MTG-0324 - 2024-08-09 - Release Readiness
- Facilitator: Victor Silva
- Attendees: Grace Kim, Elena Petrova, Aisha Khan, Iris Wang, Samir Rao, Nora Singh
- Focus service: loyalty-service
- Related evidence: ATLAS-4565, PR-10719, PD-2621

### Discussion
- Risk: loyalty-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4565.
- Blocker: QA needs production-like seed data before approving PR-10719. The workaround is documented but not yet rehearsed by on-call.
- Risk: loyalty-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4565.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.

### Decisions and Actions
- Owner Owen Brooks will close the action item before 2024-08-23.
- Update runbook, release checklist, and dashboard annotation for loyalty-service.

## Meeting MTG-0325 - 2024-08-16 - Customer Escalation Review
- Facilitator: Harper Lee
- Attendees: Elena Petrova, Iris Wang, Nora Singh, Anika Sharma, Samir Rao, Harper Lee
- Focus service: loyalty-service
- Related evidence: ATLAS-5515, PR-5164, PD-2222

### Discussion
- Risk: loyalty-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5515.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Risk: loyalty-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5515.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- The team reviewed loyalty-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.

### Decisions and Actions
- Owner Kim Tan will close the action item before 2024-08-30.
- Update runbook, release checklist, and dashboard annotation for loyalty-service.

## Meeting MTG-0326 - 2024-08-23 - Customer Escalation Review
- Facilitator: Noah Evans
- Attendees: Maya Chen, Yara Haddad, Owen Brooks, Grace Kim, Samir Rao, Victor Silva
- Focus service: search-recommendations
- Related evidence: ATLAS-2583, PR-13038, PD-2062

### Discussion
- The team reviewed search-recommendations readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Risk: search-recommendations ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2583.
- The team reviewed search-recommendations readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Risk: search-recommendations ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2583.

### Decisions and Actions
- Owner Yara Haddad will close the action item before 2024-09-06.
- Update runbook, release checklist, and dashboard annotation for search-recommendations.

## Meeting MTG-0327 - 2024-08-30 - Architecture Council
- Facilitator: Sara Novak
- Attendees: Samir Rao, Dmitri Volkov, Yara Haddad, Luca Moretti, Aisha Khan, Jon Bell
- Focus service: cart-service
- Related evidence: ATLAS-4016, PR-14138, PD-2364

### Discussion
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- The team reviewed cart-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Blocker: QA needs production-like seed data before approving PR-14138. The workaround is documented but not yet rehearsed by on-call.
- Risk: cart-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4016.

### Decisions and Actions
- Owner Grace Kim will close the action item before 2024-09-13.
- Update runbook, release checklist, and dashboard annotation for cart-service.

## Meeting MTG-0328 - 2024-09-06 - Release Readiness
- Facilitator: Grace Kim
- Attendees: Mateo Garcia, Dmitri Volkov, Owen Brooks, Ravi Patel, Elena Petrova, Priya Nair
- Focus service: loyalty-service
- Related evidence: ATLAS-5645, PR-9725, PD-2551

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- The team reviewed loyalty-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Risk: loyalty-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5645.

### Decisions and Actions
- Owner Owen Brooks will close the action item before 2024-09-20.
- Update runbook, release checklist, and dashboard annotation for loyalty-service.

## Meeting MTG-0329 - 2024-09-13 - SLO Review
- Facilitator: Theo Martin
- Attendees: Noah Evans, Kim Tan, Ravi Patel, Jon Bell, Maya Chen, Grace Kim
- Focus service: analytics-pipeline
- Related evidence: ATLAS-1293, PR-14696, PD-2478

### Discussion
- The team reviewed analytics-pipeline readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- The team reviewed analytics-pipeline readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- The team reviewed analytics-pipeline readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Blocker: QA needs production-like seed data before approving PR-14696. The workaround is documented but not yet rehearsed by on-call.
- Risk: analytics-pipeline ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-1293.

### Decisions and Actions
- Owner Theo Martin will close the action item before 2024-09-27.
- Update runbook, release checklist, and dashboard annotation for analytics-pipeline.

## Meeting MTG-0330 - 2024-09-20 - Architecture Council
- Facilitator: Yara Haddad
- Attendees: Luca Moretti, Aisha Khan, Iris Wang, Sara Novak, Grace Kim, Owen Brooks
- Focus service: order-ledger
- Related evidence: ATLAS-1278, PR-9240, PD-2144

### Discussion
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- The team reviewed order-ledger readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- The team reviewed order-ledger readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.

### Decisions and Actions
- Owner Victor Silva will close the action item before 2024-10-04.
- Update runbook, release checklist, and dashboard annotation for order-ledger.

## Meeting MTG-0331 - 2024-09-27 - Customer Escalation Review
- Facilitator: Jon Bell
- Attendees: Victor Silva, Nora Singh, Noah Evans, Elena Petrova, Owen Brooks, Yara Haddad
- Focus service: tax-service
- Related evidence: ATLAS-1249, PR-17492, PD-2391

### Discussion
- The team reviewed tax-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Risk: tax-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-1249.
- The team reviewed tax-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Blocker: QA needs production-like seed data before approving PR-17492. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Anika Sharma will close the action item before 2024-10-11.
- Update runbook, release checklist, and dashboard annotation for tax-service.

## Meeting MTG-0332 - 2024-10-04 - SLO Review
- Facilitator: Samir Rao
- Attendees: Ravi Patel, Mateo Garcia, Luca Moretti, Ben Carter, Nora Singh, Iris Wang
- Focus service: order-ledger
- Related evidence: ATLAS-4056, PR-6900, PD-2156

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- The team reviewed order-ledger readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- The team reviewed order-ledger readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Risk: order-ledger ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4056.

### Decisions and Actions
- Owner Theo Martin will close the action item before 2024-10-18.
- Update runbook, release checklist, and dashboard annotation for order-ledger.

## Meeting MTG-0333 - 2024-10-11 - Architecture Council
- Facilitator: Jon Bell
- Attendees: Iris Wang, Harper Lee, Samir Rao, Jon Bell, Fatima Noor, Grace Kim
- Focus service: payment-orchestrator
- Related evidence: ATLAS-1151, PR-6015, PD-2041

### Discussion
- Risk: payment-orchestrator ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-1151.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Blocker: QA needs production-like seed data before approving PR-6015. The workaround is documented but not yet rehearsed by on-call.
- Risk: payment-orchestrator ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-1151.

### Decisions and Actions
- Owner Ravi Patel will close the action item before 2024-10-25.
- Update runbook, release checklist, and dashboard annotation for payment-orchestrator.

## Meeting MTG-0334 - 2024-10-18 - Release Readiness
- Facilitator: Dmitri Volkov
- Attendees: Dmitri Volkov, Anika Sharma, Theo Martin, Aisha Khan, Luca Moretti, Iris Wang
- Focus service: analytics-pipeline
- Related evidence: ATLAS-2288, PR-11237, PD-2649

### Discussion
- Blocker: QA needs production-like seed data before approving PR-11237. The workaround is documented but not yet rehearsed by on-call.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Blocker: QA needs production-like seed data before approving PR-11237. The workaround is documented but not yet rehearsed by on-call.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Blocker: QA needs production-like seed data before approving PR-11237. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Sara Novak will close the action item before 2024-11-01.
- Update runbook, release checklist, and dashboard annotation for analytics-pipeline.

## Meeting MTG-0335 - 2024-10-25 - Release Readiness
- Facilitator: Priya Nair
- Attendees: Mateo Garcia, Sara Novak, Yara Haddad, Samir Rao, Ravi Patel, Owen Brooks
- Focus service: notification-service
- Related evidence: ATLAS-1184, PR-11912, PD-2053

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.

### Decisions and Actions
- Owner Kim Tan will close the action item before 2024-11-08.
- Update runbook, release checklist, and dashboard annotation for notification-service.

## Meeting MTG-0336 - 2024-11-01 - Steering Review
- Facilitator: Noah Evans
- Attendees: Yara Haddad, Grace Kim, Harper Lee, Priya Nair, Owen Brooks, Noah Evans
- Focus service: loyalty-service
- Related evidence: ATLAS-5457, PR-8893, PD-2117

### Discussion
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Risk: loyalty-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5457.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Blocker: QA needs production-like seed data before approving PR-8893. The workaround is documented but not yet rehearsed by on-call.
- Blocker: QA needs production-like seed data before approving PR-8893. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Elena Petrova will close the action item before 2024-11-15.
- Update runbook, release checklist, and dashboard annotation for loyalty-service.

## Meeting MTG-0337 - 2024-11-08 - Incident Review
- Facilitator: Ben Carter
- Attendees: Jon Bell, Ravi Patel, Elena Petrova, Fatima Noor, Maya Chen, Nora Singh
- Focus service: search-recommendations
- Related evidence: ATLAS-1878, PR-11544, PD-2142

### Discussion
- The team reviewed search-recommendations readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Blocker: QA needs production-like seed data before approving PR-11544. The workaround is documented but not yet rehearsed by on-call.
- The team reviewed search-recommendations readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Blocker: QA needs production-like seed data before approving PR-11544. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Harper Lee will close the action item before 2024-11-22.
- Update runbook, release checklist, and dashboard annotation for search-recommendations.

## Meeting MTG-0338 - 2024-11-15 - KT Working Session
- Facilitator: Owen Brooks
- Attendees: Maya Chen, Ben Carter, Anika Sharma, Elena Petrova, Kim Tan, Mateo Garcia
- Focus service: payment-orchestrator
- Related evidence: ATLAS-4596, PR-6568, PD-2408

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Blocker: QA needs production-like seed data before approving PR-6568. The workaround is documented but not yet rehearsed by on-call.
- Risk: payment-orchestrator ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4596.
- Blocker: QA needs production-like seed data before approving PR-6568. The workaround is documented but not yet rehearsed by on-call.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.

### Decisions and Actions
- Owner Dmitri Volkov will close the action item before 2024-11-29.
- Update runbook, release checklist, and dashboard annotation for payment-orchestrator.

## Meeting MTG-0339 - 2024-11-22 - Steering Review
- Facilitator: Aisha Khan
- Attendees: Elena Petrova, Luca Moretti, Ben Carter, Kim Tan, Ravi Patel, Sara Novak
- Focus service: order-ledger
- Related evidence: ATLAS-4768, PR-7495, PD-2862

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- The team reviewed order-ledger readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Nora Singh will close the action item before 2024-12-06.
- Update runbook, release checklist, and dashboard annotation for order-ledger.

## Meeting MTG-0340 - 2024-11-29 - SLO Review
- Facilitator: Aisha Khan
- Attendees: Grace Kim, Priya Nair, Sara Novak, Anika Sharma, Samir Rao, Luca Moretti
- Focus service: cart-service
- Related evidence: ATLAS-2321, PR-12277, PD-2525

### Discussion
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Risk: cart-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2321.
- Risk: cart-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2321.
- Risk: cart-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2321.

### Decisions and Actions
- Owner Anika Sharma will close the action item before 2024-12-13.
- Update runbook, release checklist, and dashboard annotation for cart-service.

## Meeting MTG-0341 - 2024-12-06 - KT Working Session
- Facilitator: Owen Brooks
- Attendees: Anika Sharma, Iris Wang, Elena Petrova, Ben Carter, Yara Haddad, Luca Moretti
- Focus service: analytics-pipeline
- Related evidence: ATLAS-2746, PR-7620, PD-2823

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- The team reviewed analytics-pipeline readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Risk: analytics-pipeline ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2746.
- Risk: analytics-pipeline ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2746.
- The team reviewed analytics-pipeline readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.

### Decisions and Actions
- Owner Priya Nair will close the action item before 2024-12-20.
- Update runbook, release checklist, and dashboard annotation for analytics-pipeline.

## Meeting MTG-0342 - 2024-12-13 - Customer Escalation Review
- Facilitator: Theo Martin
- Attendees: Dmitri Volkov, Luca Moretti, Owen Brooks, Kim Tan, Sara Novak, Aisha Khan
- Focus service: order-ledger
- Related evidence: ATLAS-1574, PR-10291, PD-2327

### Discussion
- The team reviewed order-ledger readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Risk: order-ledger ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-1574.
- Risk: order-ledger ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-1574.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Blocker: QA needs production-like seed data before approving PR-10291. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Theo Martin will close the action item before 2024-12-27.
- Update runbook, release checklist, and dashboard annotation for order-ledger.

## Meeting MTG-0343 - 2024-12-20 - Architecture Council
- Facilitator: Dmitri Volkov
- Attendees: Samir Rao, Yara Haddad, Theo Martin, Grace Kim, Harper Lee, Sara Novak
- Focus service: search-recommendations
- Related evidence: ATLAS-1066, PR-16075, PD-2634

### Discussion
- Risk: search-recommendations ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-1066.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- The team reviewed search-recommendations readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.

### Decisions and Actions
- Owner Theo Martin will close the action item before 2025-01-03.
- Update runbook, release checklist, and dashboard annotation for search-recommendations.

## Meeting MTG-0344 - 2024-12-27 - Release Readiness
- Facilitator: Ben Carter
- Attendees: Yara Haddad, Aisha Khan, Grace Kim, Dmitri Volkov, Noah Evans, Ravi Patel
- Focus service: notification-service
- Related evidence: ATLAS-2919, PR-7733, PD-2394

### Discussion
- Risk: notification-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2919.
- Risk: notification-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2919.
- Blocker: QA needs production-like seed data before approving PR-7733. The workaround is documented but not yet rehearsed by on-call.
- The team reviewed notification-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- The team reviewed notification-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.

### Decisions and Actions
- Owner Victor Silva will close the action item before 2025-01-10.
- Update runbook, release checklist, and dashboard annotation for notification-service.

## Meeting MTG-0345 - 2025-01-03 - Incident Review
- Facilitator: Luca Moretti
- Attendees: Maya Chen, Mateo Garcia, Victor Silva, Harper Lee, Ravi Patel, Elena Petrova
- Focus service: loyalty-service
- Related evidence: ATLAS-2512, PR-8752, PD-2360

### Discussion
- The team reviewed loyalty-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Blocker: QA needs production-like seed data before approving PR-8752. The workaround is documented but not yet rehearsed by on-call.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Risk: loyalty-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2512.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.

### Decisions and Actions
- Owner Dmitri Volkov will close the action item before 2025-01-17.
- Update runbook, release checklist, and dashboard annotation for loyalty-service.

## Meeting MTG-0346 - 2025-01-10 - Release Readiness
- Facilitator: Luca Moretti
- Attendees: Theo Martin, Victor Silva, Harper Lee, Priya Nair, Nora Singh, Elena Petrova
- Focus service: pricing-engine
- Related evidence: ATLAS-4362, PR-18114, PD-2652

### Discussion
- Blocker: QA needs production-like seed data before approving PR-18114. The workaround is documented but not yet rehearsed by on-call.
- The team reviewed pricing-engine readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Blocker: QA needs production-like seed data before approving PR-18114. The workaround is documented but not yet rehearsed by on-call.
- Blocker: QA needs production-like seed data before approving PR-18114. The workaround is documented but not yet rehearsed by on-call.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.

### Decisions and Actions
- Owner Harper Lee will close the action item before 2025-01-24.
- Update runbook, release checklist, and dashboard annotation for pricing-engine.

## Meeting MTG-0347 - 2025-01-17 - Incident Review
- Facilitator: Ravi Patel
- Attendees: Jon Bell, Ravi Patel, Fatima Noor, Kim Tan, Iris Wang, Dmitri Volkov
- Focus service: loyalty-service
- Related evidence: ATLAS-5735, PR-15261, PD-2473

### Discussion
- Risk: loyalty-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5735.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Blocker: QA needs production-like seed data before approving PR-15261. The workaround is documented but not yet rehearsed by on-call.
- Risk: loyalty-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5735.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Harper Lee will close the action item before 2025-01-31.
- Update runbook, release checklist, and dashboard annotation for loyalty-service.

## Meeting MTG-0348 - 2025-01-24 - SLO Review
- Facilitator: Aisha Khan
- Attendees: Kim Tan, Mateo Garcia, Owen Brooks, Dmitri Volkov, Nora Singh, Elena Petrova
- Focus service: inventory-reservation
- Related evidence: ATLAS-5894, PR-17205, PD-2308

### Discussion
- Risk: inventory-reservation ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5894.
- Blocker: QA needs production-like seed data before approving PR-17205. The workaround is documented but not yet rehearsed by on-call.
- Blocker: QA needs production-like seed data before approving PR-17205. The workaround is documented but not yet rehearsed by on-call.
- The team reviewed inventory-reservation readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Risk: inventory-reservation ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5894.

### Decisions and Actions
- Owner Yara Haddad will close the action item before 2025-02-07.
- Update runbook, release checklist, and dashboard annotation for inventory-reservation.

## Meeting MTG-0349 - 2025-01-31 - Customer Escalation Review
- Facilitator: Harper Lee
- Attendees: Mateo Garcia, Dmitri Volkov, Owen Brooks, Theo Martin, Maya Chen, Sara Novak
- Focus service: analytics-pipeline
- Related evidence: ATLAS-5975, PR-10130, PD-2332

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Risk: analytics-pipeline ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5975.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- The team reviewed analytics-pipeline readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.

### Decisions and Actions
- Owner Ravi Patel will close the action item before 2025-02-14.
- Update runbook, release checklist, and dashboard annotation for analytics-pipeline.

## Meeting MTG-0350 - 2025-02-07 - Release Readiness
- Facilitator: Iris Wang
- Attendees: Theo Martin, Jon Bell, Yara Haddad, Ravi Patel, Dmitri Volkov, Harper Lee
- Focus service: payment-orchestrator
- Related evidence: ATLAS-4556, PR-5786, PD-2107

### Discussion
- Risk: payment-orchestrator ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4556.
- Blocker: QA needs production-like seed data before approving PR-5786. The workaround is documented but not yet rehearsed by on-call.
- Blocker: QA needs production-like seed data before approving PR-5786. The workaround is documented but not yet rehearsed by on-call.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.

### Decisions and Actions
- Owner Sara Novak will close the action item before 2025-02-21.
- Update runbook, release checklist, and dashboard annotation for payment-orchestrator.

## Meeting MTG-0351 - 2025-02-14 - Architecture Council
- Facilitator: Iris Wang
- Attendees: Theo Martin, Yara Haddad, Elena Petrova, Priya Nair, Ben Carter, Noah Evans
- Focus service: analytics-pipeline
- Related evidence: ATLAS-5556, PR-12680, PD-2512

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- The team reviewed analytics-pipeline readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Risk: analytics-pipeline ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5556.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.

### Decisions and Actions
- Owner Priya Nair will close the action item before 2025-02-28.
- Update runbook, release checklist, and dashboard annotation for analytics-pipeline.

## Meeting MTG-0352 - 2025-02-21 - KT Working Session
- Facilitator: Jon Bell
- Attendees: Grace Kim, Mateo Garcia, Jon Bell, Fatima Noor, Anika Sharma, Ben Carter
- Focus service: analytics-pipeline
- Related evidence: ATLAS-2432, PR-14769, PD-2011

### Discussion
- Blocker: QA needs production-like seed data before approving PR-14769. The workaround is documented but not yet rehearsed by on-call.
- The team reviewed analytics-pipeline readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Blocker: QA needs production-like seed data before approving PR-14769. The workaround is documented but not yet rehearsed by on-call.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Risk: analytics-pipeline ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2432.

### Decisions and Actions
- Owner Yara Haddad will close the action item before 2025-03-07.
- Update runbook, release checklist, and dashboard annotation for analytics-pipeline.

## Meeting MTG-0353 - 2025-02-28 - Incident Review
- Facilitator: Maya Chen
- Attendees: Owen Brooks, Fatima Noor, Samir Rao, Maya Chen, Theo Martin, Mateo Garcia
- Focus service: analytics-pipeline
- Related evidence: ATLAS-1922, PR-10970, PD-2429

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Blocker: QA needs production-like seed data before approving PR-10970. The workaround is documented but not yet rehearsed by on-call.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.

### Decisions and Actions
- Owner Nora Singh will close the action item before 2025-03-14.
- Update runbook, release checklist, and dashboard annotation for analytics-pipeline.

## Meeting MTG-0354 - 2025-03-07 - Steering Review
- Facilitator: Jon Bell
- Attendees: Jon Bell, Dmitri Volkov, Noah Evans, Ravi Patel, Fatima Noor, Ben Carter
- Focus service: search-recommendations
- Related evidence: ATLAS-3283, PR-11128, PD-2532

### Discussion
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- The team reviewed search-recommendations readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Theo Martin will close the action item before 2025-03-21.
- Update runbook, release checklist, and dashboard annotation for search-recommendations.

## Meeting MTG-0355 - 2025-03-14 - KT Working Session
- Facilitator: Harper Lee
- Attendees: Samir Rao, Noah Evans, Nora Singh, Jon Bell, Victor Silva, Harper Lee
- Focus service: cart-service
- Related evidence: ATLAS-2621, PR-7625, PD-2560

### Discussion
- The team reviewed cart-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- The team reviewed cart-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Blocker: QA needs production-like seed data before approving PR-7625. The workaround is documented but not yet rehearsed by on-call.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Victor Silva will close the action item before 2025-03-28.
- Update runbook, release checklist, and dashboard annotation for cart-service.

## Meeting MTG-0356 - 2025-03-21 - Customer Escalation Review
- Facilitator: Anika Sharma
- Attendees: Priya Nair, Samir Rao, Anika Sharma, Harper Lee, Dmitri Volkov, Noah Evans
- Focus service: loyalty-service
- Related evidence: ATLAS-5013, PR-15022, PD-2403

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Risk: loyalty-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5013.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Jon Bell will close the action item before 2025-04-04.
- Update runbook, release checklist, and dashboard annotation for loyalty-service.

## Meeting MTG-0357 - 2025-03-28 - Architecture Council
- Facilitator: Theo Martin
- Attendees: Iris Wang, Samir Rao, Fatima Noor, Jon Bell, Aisha Khan, Owen Brooks
- Focus service: pricing-engine
- Related evidence: ATLAS-5068, PR-13539, PD-2133

### Discussion
- Blocker: QA needs production-like seed data before approving PR-13539. The workaround is documented but not yet rehearsed by on-call.
- The team reviewed pricing-engine readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Owen Brooks will close the action item before 2025-04-11.
- Update runbook, release checklist, and dashboard annotation for pricing-engine.

## Meeting MTG-0358 - 2025-04-04 - Release Readiness
- Facilitator: Harper Lee
- Attendees: Anika Sharma, Mateo Garcia, Yara Haddad, Ben Carter, Samir Rao, Theo Martin
- Focus service: cart-service
- Related evidence: ATLAS-2405, PR-16531, PD-2293

### Discussion
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- The team reviewed cart-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Risk: cart-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2405.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Grace Kim will close the action item before 2025-04-18.
- Update runbook, release checklist, and dashboard annotation for cart-service.

## Meeting MTG-0359 - 2025-04-11 - SLO Review
- Facilitator: Yara Haddad
- Attendees: Fatima Noor, Kim Tan, Anika Sharma, Maya Chen, Harper Lee, Sara Novak
- Focus service: analytics-pipeline
- Related evidence: ATLAS-4376, PR-5956, PD-2840

### Discussion
- Blocker: QA needs production-like seed data before approving PR-5956. The workaround is documented but not yet rehearsed by on-call.
- Blocker: QA needs production-like seed data before approving PR-5956. The workaround is documented but not yet rehearsed by on-call.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.

### Decisions and Actions
- Owner Grace Kim will close the action item before 2025-04-25.
- Update runbook, release checklist, and dashboard annotation for analytics-pipeline.

## Meeting MTG-0360 - 2025-04-18 - Customer Escalation Review
- Facilitator: Maya Chen
- Attendees: Iris Wang, Grace Kim, Maya Chen, Ravi Patel, Mateo Garcia, Yara Haddad
- Focus service: search-recommendations
- Related evidence: ATLAS-6175, PR-16098, PD-2698

### Discussion
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- The team reviewed search-recommendations readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.

### Decisions and Actions
- Owner Anika Sharma will close the action item before 2025-05-02.
- Update runbook, release checklist, and dashboard annotation for search-recommendations.

## Meeting MTG-0361 - 2025-04-25 - Architecture Council
- Facilitator: Kim Tan
- Attendees: Ben Carter, Yara Haddad, Maya Chen, Dmitri Volkov, Priya Nair, Luca Moretti
- Focus service: analytics-pipeline
- Related evidence: ATLAS-5086, PR-14581, PD-2674

### Discussion
- The team reviewed analytics-pipeline readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Blocker: QA needs production-like seed data before approving PR-14581. The workaround is documented but not yet rehearsed by on-call.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Blocker: QA needs production-like seed data before approving PR-14581. The workaround is documented but not yet rehearsed by on-call.
- Risk: analytics-pipeline ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5086.

### Decisions and Actions
- Owner Nora Singh will close the action item before 2025-05-09.
- Update runbook, release checklist, and dashboard annotation for analytics-pipeline.

## Meeting MTG-0362 - 2025-05-02 - Release Readiness
- Facilitator: Maya Chen
- Attendees: Noah Evans, Dmitri Volkov, Ravi Patel, Anika Sharma, Priya Nair, Victor Silva
- Focus service: inventory-reservation
- Related evidence: ATLAS-1522, PR-14880, PD-2365

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.

### Decisions and Actions
- Owner Nora Singh will close the action item before 2025-05-16.
- Update runbook, release checklist, and dashboard annotation for inventory-reservation.

## Meeting MTG-0363 - 2025-05-09 - SLO Review
- Facilitator: Sara Novak
- Attendees: Fatima Noor, Noah Evans, Anika Sharma, Grace Kim, Mateo Garcia, Jon Bell
- Focus service: tax-service
- Related evidence: ATLAS-5925, PR-10003, PD-2318

### Discussion
- Risk: tax-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5925.
- Blocker: QA needs production-like seed data before approving PR-10003. The workaround is documented but not yet rehearsed by on-call.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Blocker: QA needs production-like seed data before approving PR-10003. The workaround is documented but not yet rehearsed by on-call.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.

### Decisions and Actions
- Owner Sara Novak will close the action item before 2025-05-23.
- Update runbook, release checklist, and dashboard annotation for tax-service.

## Meeting MTG-0364 - 2025-05-16 - Customer Escalation Review
- Facilitator: Elena Petrova
- Attendees: Dmitri Volkov, Nora Singh, Yara Haddad, Priya Nair, Theo Martin, Sara Novak
- Focus service: search-recommendations
- Related evidence: ATLAS-1043, PR-18466, PD-2688

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- The team reviewed search-recommendations readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Risk: search-recommendations ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-1043.
- The team reviewed search-recommendations readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Victor Silva will close the action item before 2025-05-30.
- Update runbook, release checklist, and dashboard annotation for search-recommendations.

## Meeting MTG-0365 - 2025-05-23 - Steering Review
- Facilitator: Ben Carter
- Attendees: Grace Kim, Theo Martin, Mateo Garcia, Jon Bell, Harper Lee, Aisha Khan
- Focus service: pricing-engine
- Related evidence: ATLAS-3336, PR-6444, PD-2592

### Discussion
- Blocker: QA needs production-like seed data before approving PR-6444. The workaround is documented but not yet rehearsed by on-call.
- Risk: pricing-engine ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-3336.
- The team reviewed pricing-engine readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Anika Sharma will close the action item before 2025-06-06.
- Update runbook, release checklist, and dashboard annotation for pricing-engine.

## Meeting MTG-0366 - 2025-05-30 - Customer Escalation Review
- Facilitator: Nora Singh
- Attendees: Victor Silva, Maya Chen, Aisha Khan, Priya Nair, Mateo Garcia, Fatima Noor
- Focus service: pricing-engine
- Related evidence: ATLAS-4401, PR-14990, PD-2443

### Discussion
- Blocker: QA needs production-like seed data before approving PR-14990. The workaround is documented but not yet rehearsed by on-call.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Risk: pricing-engine ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4401.
- Risk: pricing-engine ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4401.

### Decisions and Actions
- Owner Owen Brooks will close the action item before 2025-06-13.
- Update runbook, release checklist, and dashboard annotation for pricing-engine.

## Meeting MTG-0367 - 2025-06-06 - Customer Escalation Review
- Facilitator: Iris Wang
- Attendees: Mateo Garcia, Ben Carter, Priya Nair, Anika Sharma, Aisha Khan, Yara Haddad
- Focus service: tax-service
- Related evidence: ATLAS-2161, PR-5528, PD-2380

### Discussion
- Blocker: QA needs production-like seed data before approving PR-5528. The workaround is documented but not yet rehearsed by on-call.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Blocker: QA needs production-like seed data before approving PR-5528. The workaround is documented but not yet rehearsed by on-call.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Risk: tax-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2161.

### Decisions and Actions
- Owner Aisha Khan will close the action item before 2025-06-20.
- Update runbook, release checklist, and dashboard annotation for tax-service.

## Meeting MTG-0368 - 2025-06-13 - KT Working Session
- Facilitator: Grace Kim
- Attendees: Ravi Patel, Sara Novak, Harper Lee, Kim Tan, Samir Rao, Jon Bell
- Focus service: analytics-pipeline
- Related evidence: ATLAS-1155, PR-13926, PD-2738

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Risk: analytics-pipeline ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-1155.
- The team reviewed analytics-pipeline readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Owen Brooks will close the action item before 2025-06-27.
- Update runbook, release checklist, and dashboard annotation for analytics-pipeline.

## Meeting MTG-0369 - 2025-06-20 - SLO Review
- Facilitator: Maya Chen
- Attendees: Mateo Garcia, Victor Silva, Theo Martin, Ben Carter, Ravi Patel, Owen Brooks
- Focus service: order-ledger
- Related evidence: ATLAS-5623, PR-9067, PD-2024

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Blocker: QA needs production-like seed data before approving PR-9067. The workaround is documented but not yet rehearsed by on-call.
- Blocker: QA needs production-like seed data before approving PR-9067. The workaround is documented but not yet rehearsed by on-call.
- The team reviewed order-ledger readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.

### Decisions and Actions
- Owner Sara Novak will close the action item before 2025-07-04.
- Update runbook, release checklist, and dashboard annotation for order-ledger.

## Meeting MTG-0370 - 2025-06-27 - KT Working Session
- Facilitator: Kim Tan
- Attendees: Yara Haddad, Nora Singh, Ravi Patel, Mateo Garcia, Jon Bell, Fatima Noor
- Focus service: loyalty-service
- Related evidence: ATLAS-2369, PR-9990, PD-2500

### Discussion
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Blocker: QA needs production-like seed data before approving PR-9990. The workaround is documented but not yet rehearsed by on-call.
- Risk: loyalty-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2369.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Risk: loyalty-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2369.

### Decisions and Actions
- Owner Mateo Garcia will close the action item before 2025-07-11.
- Update runbook, release checklist, and dashboard annotation for loyalty-service.

## Meeting MTG-0371 - 2025-07-04 - Architecture Council
- Facilitator: Luca Moretti
- Attendees: Aisha Khan, Fatima Noor, Sara Novak, Nora Singh, Luca Moretti, Yara Haddad
- Focus service: cart-service
- Related evidence: ATLAS-1624, PR-6176, PD-2370

### Discussion
- Risk: cart-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-1624.
- Blocker: QA needs production-like seed data before approving PR-6176. The workaround is documented but not yet rehearsed by on-call.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Blocker: QA needs production-like seed data before approving PR-6176. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Iris Wang will close the action item before 2025-07-18.
- Update runbook, release checklist, and dashboard annotation for cart-service.

## Meeting MTG-0372 - 2025-07-11 - Architecture Council
- Facilitator: Mateo Garcia
- Attendees: Owen Brooks, Yara Haddad, Grace Kim, Iris Wang, Anika Sharma, Ben Carter
- Focus service: search-recommendations
- Related evidence: ATLAS-5452, PR-6908, PD-2651

### Discussion
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- The team reviewed search-recommendations readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Blocker: QA needs production-like seed data before approving PR-6908. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Luca Moretti will close the action item before 2025-07-25.
- Update runbook, release checklist, and dashboard annotation for search-recommendations.

## Meeting MTG-0373 - 2025-07-18 - Release Readiness
- Facilitator: Aisha Khan
- Attendees: Jon Bell, Ravi Patel, Grace Kim, Yara Haddad, Kim Tan, Ben Carter
- Focus service: payment-orchestrator
- Related evidence: ATLAS-3067, PR-17707, PD-2539

### Discussion
- Blocker: QA needs production-like seed data before approving PR-17707. The workaround is documented but not yet rehearsed by on-call.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Blocker: QA needs production-like seed data before approving PR-17707. The workaround is documented but not yet rehearsed by on-call.
- Blocker: QA needs production-like seed data before approving PR-17707. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Victor Silva will close the action item before 2025-08-01.
- Update runbook, release checklist, and dashboard annotation for payment-orchestrator.

## Meeting MTG-0374 - 2025-07-25 - KT Working Session
- Facilitator: Iris Wang
- Attendees: Yara Haddad, Owen Brooks, Elena Petrova, Grace Kim, Victor Silva, Kim Tan
- Focus service: notification-service
- Related evidence: ATLAS-4261, PR-11562, PD-2255

### Discussion
- Blocker: QA needs production-like seed data before approving PR-11562. The workaround is documented but not yet rehearsed by on-call.
- Risk: notification-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4261.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Blocker: QA needs production-like seed data before approving PR-11562. The workaround is documented but not yet rehearsed by on-call.
- The team reviewed notification-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.

### Decisions and Actions
- Owner Nora Singh will close the action item before 2025-08-08.
- Update runbook, release checklist, and dashboard annotation for notification-service.

## Meeting MTG-0375 - 2025-08-01 - Customer Escalation Review
- Facilitator: Anika Sharma
- Attendees: Ravi Patel, Theo Martin, Samir Rao, Jon Bell, Dmitri Volkov, Noah Evans
- Focus service: order-ledger
- Related evidence: ATLAS-3514, PR-10943, PD-2602

### Discussion
- Blocker: QA needs production-like seed data before approving PR-10943. The workaround is documented but not yet rehearsed by on-call.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Blocker: QA needs production-like seed data before approving PR-10943. The workaround is documented but not yet rehearsed by on-call.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Blocker: QA needs production-like seed data before approving PR-10943. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Nora Singh will close the action item before 2025-08-15.
- Update runbook, release checklist, and dashboard annotation for order-ledger.

## Meeting MTG-0376 - 2025-08-08 - Release Readiness
- Facilitator: Mateo Garcia
- Attendees: Iris Wang, Luca Moretti, Samir Rao, Jon Bell, Mateo Garcia, Ravi Patel
- Focus service: order-ledger
- Related evidence: ATLAS-3516, PR-9566, PD-2241

### Discussion
- Blocker: QA needs production-like seed data before approving PR-9566. The workaround is documented but not yet rehearsed by on-call.
- Blocker: QA needs production-like seed data before approving PR-9566. The workaround is documented but not yet rehearsed by on-call.
- The team reviewed order-ledger readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Blocker: QA needs production-like seed data before approving PR-9566. The workaround is documented but not yet rehearsed by on-call.
- Risk: order-ledger ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-3516.

### Decisions and Actions
- Owner Dmitri Volkov will close the action item before 2025-08-22.
- Update runbook, release checklist, and dashboard annotation for order-ledger.

## Meeting MTG-0377 - 2025-08-15 - Incident Review
- Facilitator: Grace Kim
- Attendees: Nora Singh, Harper Lee, Grace Kim, Elena Petrova, Anika Sharma, Priya Nair
- Focus service: pricing-engine
- Related evidence: ATLAS-4147, PR-9873, PD-2424

### Discussion
- The team reviewed pricing-engine readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- The team reviewed pricing-engine readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Blocker: QA needs production-like seed data before approving PR-9873. The workaround is documented but not yet rehearsed by on-call.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Blocker: QA needs production-like seed data before approving PR-9873. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Harper Lee will close the action item before 2025-08-29.
- Update runbook, release checklist, and dashboard annotation for pricing-engine.

## Meeting MTG-0378 - 2025-08-22 - Steering Review
- Facilitator: Ben Carter
- Attendees: Owen Brooks, Anika Sharma, Fatima Noor, Aisha Khan, Nora Singh, Theo Martin
- Focus service: inventory-reservation
- Related evidence: ATLAS-2169, PR-17109, PD-2632

### Discussion
- The team reviewed inventory-reservation readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Risk: inventory-reservation ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2169.
- Blocker: QA needs production-like seed data before approving PR-17109. The workaround is documented but not yet rehearsed by on-call.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.

### Decisions and Actions
- Owner Luca Moretti will close the action item before 2025-09-05.
- Update runbook, release checklist, and dashboard annotation for inventory-reservation.

## Meeting MTG-0379 - 2025-08-29 - Architecture Council
- Facilitator: Mateo Garcia
- Attendees: Iris Wang, Kim Tan, Ben Carter, Mateo Garcia, Aisha Khan, Owen Brooks
- Focus service: cart-service
- Related evidence: ATLAS-1199, PR-18741, PD-2243

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Risk: cart-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-1199.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.

### Decisions and Actions
- Owner Sara Novak will close the action item before 2025-09-12.
- Update runbook, release checklist, and dashboard annotation for cart-service.

## Meeting MTG-0380 - 2025-09-05 - KT Working Session
- Facilitator: Ravi Patel
- Attendees: Ravi Patel, Noah Evans, Harper Lee, Elena Petrova, Owen Brooks, Jon Bell
- Focus service: pricing-engine
- Related evidence: ATLAS-2327, PR-17410, PD-2402

### Discussion
- Blocker: QA needs production-like seed data before approving PR-17410. The workaround is documented but not yet rehearsed by on-call.
- Risk: pricing-engine ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2327.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Blocker: QA needs production-like seed data before approving PR-17410. The workaround is documented but not yet rehearsed by on-call.
- Blocker: QA needs production-like seed data before approving PR-17410. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Harper Lee will close the action item before 2025-09-19.
- Update runbook, release checklist, and dashboard annotation for pricing-engine.

## Meeting MTG-0381 - 2025-09-12 - Release Readiness
- Facilitator: Maya Chen
- Attendees: Ravi Patel, Nora Singh, Harper Lee, Sara Novak, Mateo Garcia, Priya Nair
- Focus service: checkout-api
- Related evidence: ATLAS-1962, PR-11979, PD-2702

### Discussion
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Blocker: QA needs production-like seed data before approving PR-11979. The workaround is documented but not yet rehearsed by on-call.
- Blocker: QA needs production-like seed data before approving PR-11979. The workaround is documented but not yet rehearsed by on-call.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Risk: checkout-api ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-1962.

### Decisions and Actions
- Owner Anika Sharma will close the action item before 2025-09-26.
- Update runbook, release checklist, and dashboard annotation for checkout-api.

## Meeting MTG-0382 - 2025-09-19 - Steering Review
- Facilitator: Maya Chen
- Attendees: Priya Nair, Luca Moretti, Mateo Garcia, Harper Lee, Nora Singh, Theo Martin
- Focus service: cart-service
- Related evidence: ATLAS-6029, PR-14049, PD-2682

### Discussion
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Risk: cart-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-6029.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Blocker: QA needs production-like seed data before approving PR-14049. The workaround is documented but not yet rehearsed by on-call.
- Risk: cart-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-6029.

### Decisions and Actions
- Owner Samir Rao will close the action item before 2025-10-03.
- Update runbook, release checklist, and dashboard annotation for cart-service.

## Meeting MTG-0383 - 2025-09-26 - Architecture Council
- Facilitator: Owen Brooks
- Attendees: Grace Kim, Kim Tan, Ravi Patel, Dmitri Volkov, Sara Novak, Iris Wang
- Focus service: pricing-engine
- Related evidence: ATLAS-6058, PR-7457, PD-2106

### Discussion
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Risk: pricing-engine ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-6058.
- Blocker: QA needs production-like seed data before approving PR-7457. The workaround is documented but not yet rehearsed by on-call.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.

### Decisions and Actions
- Owner Ravi Patel will close the action item before 2025-10-10.
- Update runbook, release checklist, and dashboard annotation for pricing-engine.

## Meeting MTG-0384 - 2025-10-03 - Customer Escalation Review
- Facilitator: Noah Evans
- Attendees: Harper Lee, Elena Petrova, Fatima Noor, Luca Moretti, Sara Novak, Ben Carter
- Focus service: analytics-pipeline
- Related evidence: ATLAS-1167, PR-7755, PD-2193

### Discussion
- The team reviewed analytics-pipeline readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- The team reviewed analytics-pipeline readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Blocker: QA needs production-like seed data before approving PR-7755. The workaround is documented but not yet rehearsed by on-call.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.

### Decisions and Actions
- Owner Jon Bell will close the action item before 2025-10-17.
- Update runbook, release checklist, and dashboard annotation for analytics-pipeline.

## Meeting MTG-0385 - 2025-10-10 - Incident Review
- Facilitator: Luca Moretti
- Attendees: Ben Carter, Fatima Noor, Dmitri Volkov, Maya Chen, Grace Kim, Elena Petrova
- Focus service: tax-service
- Related evidence: ATLAS-1451, PR-17913, PD-2684

### Discussion
- Blocker: QA needs production-like seed data before approving PR-17913. The workaround is documented but not yet rehearsed by on-call.
- The team reviewed tax-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Blocker: QA needs production-like seed data before approving PR-17913. The workaround is documented but not yet rehearsed by on-call.
- Blocker: QA needs production-like seed data before approving PR-17913. The workaround is documented but not yet rehearsed by on-call.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Ravi Patel will close the action item before 2025-10-24.
- Update runbook, release checklist, and dashboard annotation for tax-service.

## Meeting MTG-0386 - 2025-10-17 - Release Readiness
- Facilitator: Yara Haddad
- Attendees: Yara Haddad, Victor Silva, Ben Carter, Luca Moretti, Anika Sharma, Aisha Khan
- Focus service: checkout-api
- Related evidence: ATLAS-1201, PR-5209, PD-2615

### Discussion
- Risk: checkout-api ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-1201.
- Blocker: QA needs production-like seed data before approving PR-5209. The workaround is documented but not yet rehearsed by on-call.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- The team reviewed checkout-api readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- The team reviewed checkout-api readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.

### Decisions and Actions
- Owner Fatima Noor will close the action item before 2025-10-31.
- Update runbook, release checklist, and dashboard annotation for checkout-api.

## Meeting MTG-0387 - 2025-10-24 - Architecture Council
- Facilitator: Yara Haddad
- Attendees: Samir Rao, Harper Lee, Noah Evans, Theo Martin, Ravi Patel, Dmitri Volkov
- Focus service: cart-service
- Related evidence: ATLAS-6043, PR-13680, PD-2762

### Discussion
- Blocker: QA needs production-like seed data before approving PR-13680. The workaround is documented but not yet rehearsed by on-call.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Risk: cart-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-6043.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.

### Decisions and Actions
- Owner Luca Moretti will close the action item before 2025-11-07.
- Update runbook, release checklist, and dashboard annotation for cart-service.

## Meeting MTG-0388 - 2025-10-31 - Incident Review
- Facilitator: Aisha Khan
- Attendees: Sara Novak, Samir Rao, Anika Sharma, Maya Chen, Jon Bell, Iris Wang
- Focus service: loyalty-service
- Related evidence: ATLAS-4598, PR-11061, PD-2534

### Discussion
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Blocker: QA needs production-like seed data before approving PR-11061. The workaround is documented but not yet rehearsed by on-call.
- Risk: loyalty-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4598.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Owen Brooks will close the action item before 2025-11-14.
- Update runbook, release checklist, and dashboard annotation for loyalty-service.

## Meeting MTG-0389 - 2025-11-07 - KT Working Session
- Facilitator: Ben Carter
- Attendees: Yara Haddad, Nora Singh, Samir Rao, Elena Petrova, Owen Brooks, Noah Evans
- Focus service: analytics-pipeline
- Related evidence: ATLAS-4796, PR-7814, PD-2786

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Risk: analytics-pipeline ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4796.
- Risk: analytics-pipeline ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4796.
- Blocker: QA needs production-like seed data before approving PR-7814. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Samir Rao will close the action item before 2025-11-21.
- Update runbook, release checklist, and dashboard annotation for analytics-pipeline.

## Meeting MTG-0390 - 2025-11-14 - Architecture Council
- Facilitator: Elena Petrova
- Attendees: Noah Evans, Jon Bell, Theo Martin, Anika Sharma, Ben Carter, Priya Nair
- Focus service: inventory-reservation
- Related evidence: ATLAS-5040, PR-13267, PD-2630

### Discussion
- Blocker: QA needs production-like seed data before approving PR-13267. The workaround is documented but not yet rehearsed by on-call.
- Risk: inventory-reservation ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5040.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- The team reviewed inventory-reservation readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Blocker: QA needs production-like seed data before approving PR-13267. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Kim Tan will close the action item before 2025-11-28.
- Update runbook, release checklist, and dashboard annotation for inventory-reservation.

## Meeting MTG-0391 - 2025-11-21 - Incident Review
- Facilitator: Ravi Patel
- Attendees: Mateo Garcia, Luca Moretti, Jon Bell, Nora Singh, Fatima Noor, Noah Evans
- Focus service: inventory-reservation
- Related evidence: ATLAS-4846, PR-15527, PD-2814

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Ravi Patel will close the action item before 2025-12-05.
- Update runbook, release checklist, and dashboard annotation for inventory-reservation.

## Meeting MTG-0392 - 2025-11-28 - SLO Review
- Facilitator: Theo Martin
- Attendees: Sara Novak, Kim Tan, Grace Kim, Maya Chen, Elena Petrova, Dmitri Volkov
- Focus service: payment-orchestrator
- Related evidence: ATLAS-1459, PR-18474, PD-2644

### Discussion
- Blocker: QA needs production-like seed data before approving PR-18474. The workaround is documented but not yet rehearsed by on-call.
- Blocker: QA needs production-like seed data before approving PR-18474. The workaround is documented but not yet rehearsed by on-call.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Blocker: QA needs production-like seed data before approving PR-18474. The workaround is documented but not yet rehearsed by on-call.
- Risk: payment-orchestrator ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-1459.

### Decisions and Actions
- Owner Noah Evans will close the action item before 2025-12-12.
- Update runbook, release checklist, and dashboard annotation for payment-orchestrator.

## Meeting MTG-0393 - 2025-12-05 - SLO Review
- Facilitator: Ravi Patel
- Attendees: Ravi Patel, Aisha Khan, Theo Martin, Owen Brooks, Grace Kim, Yara Haddad
- Focus service: order-ledger
- Related evidence: ATLAS-3774, PR-12751, PD-2091

### Discussion
- Risk: order-ledger ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-3774.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Risk: order-ledger ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-3774.

### Decisions and Actions
- Owner Maya Chen will close the action item before 2025-12-19.
- Update runbook, release checklist, and dashboard annotation for order-ledger.

## Meeting MTG-0394 - 2025-12-12 - Customer Escalation Review
- Facilitator: Fatima Noor
- Attendees: Ben Carter, Iris Wang, Nora Singh, Anika Sharma, Owen Brooks, Noah Evans
- Focus service: analytics-pipeline
- Related evidence: ATLAS-5098, PR-11168, PD-2810

### Discussion
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Risk: analytics-pipeline ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5098.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Risk: analytics-pipeline ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-5098.

### Decisions and Actions
- Owner Luca Moretti will close the action item before 2025-12-26.
- Update runbook, release checklist, and dashboard annotation for analytics-pipeline.

## Meeting MTG-0395 - 2025-12-19 - SLO Review
- Facilitator: Victor Silva
- Attendees: Anika Sharma, Aisha Khan, Nora Singh, Owen Brooks, Harper Lee, Fatima Noor
- Focus service: notification-service
- Related evidence: ATLAS-4578, PR-8214, PD-2865

### Discussion
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Blocker: QA needs production-like seed data before approving PR-8214. The workaround is documented but not yet rehearsed by on-call.
- Risk: notification-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4578.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.

### Decisions and Actions
- Owner Luca Moretti will close the action item before 2026-01-02.
- Update runbook, release checklist, and dashboard annotation for notification-service.

## Meeting MTG-0396 - 2025-12-26 - KT Working Session
- Facilitator: Yara Haddad
- Attendees: Mateo Garcia, Yara Haddad, Anika Sharma, Ravi Patel, Dmitri Volkov, Jon Bell
- Focus service: payment-orchestrator
- Related evidence: ATLAS-4691, PR-10415, PD-2332

### Discussion
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Blocker: QA needs production-like seed data before approving PR-10415. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Sara Novak will close the action item before 2026-01-09.
- Update runbook, release checklist, and dashboard annotation for payment-orchestrator.

## Meeting MTG-0397 - 2026-01-02 - Steering Review
- Facilitator: Ben Carter
- Attendees: Sara Novak, Elena Petrova, Noah Evans, Priya Nair, Maya Chen, Iris Wang
- Focus service: search-recommendations
- Related evidence: ATLAS-3804, PR-14359, PD-2236

### Discussion
- Blocker: QA needs production-like seed data before approving PR-14359. The workaround is documented but not yet rehearsed by on-call.
- Risk: search-recommendations ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-3804.
- Blocker: QA needs production-like seed data before approving PR-14359. The workaround is documented but not yet rehearsed by on-call.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- The team reviewed search-recommendations readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.

### Decisions and Actions
- Owner Kim Tan will close the action item before 2026-01-16.
- Update runbook, release checklist, and dashboard annotation for search-recommendations.

## Meeting MTG-0398 - 2026-01-09 - SLO Review
- Facilitator: Owen Brooks
- Attendees: Anika Sharma, Nora Singh, Noah Evans, Yara Haddad, Kim Tan, Mateo Garcia
- Focus service: order-ledger
- Related evidence: ATLAS-4550, PR-12447, PD-2806

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Blocker: QA needs production-like seed data before approving PR-12447. The workaround is documented but not yet rehearsed by on-call.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Risk: order-ledger ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4550.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.

### Decisions and Actions
- Owner Theo Martin will close the action item before 2026-01-23.
- Update runbook, release checklist, and dashboard annotation for order-ledger.

## Meeting MTG-0399 - 2026-01-16 - Release Readiness
- Facilitator: Jon Bell
- Attendees: Aisha Khan, Victor Silva, Sara Novak, Kim Tan, Priya Nair, Elena Petrova
- Focus service: pricing-engine
- Related evidence: ATLAS-3309, PR-10800, PD-2032

### Discussion
- Risk: pricing-engine ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-3309.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- The team reviewed pricing-engine readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.

### Decisions and Actions
- Owner Nora Singh will close the action item before 2026-01-30.
- Update runbook, release checklist, and dashboard annotation for pricing-engine.

## Meeting MTG-0400 - 2026-01-23 - Steering Review
- Facilitator: Anika Sharma
- Attendees: Elena Petrova, Iris Wang, Noah Evans, Maya Chen, Luca Moretti, Priya Nair
- Focus service: pricing-engine
- Related evidence: ATLAS-4019, PR-8765, PD-2188

### Discussion
- Risk: pricing-engine ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4019.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Blocker: QA needs production-like seed data before approving PR-8765. The workaround is documented but not yet rehearsed by on-call.
- The team reviewed pricing-engine readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.

### Decisions and Actions
- Owner Yara Haddad will close the action item before 2026-02-06.
- Update runbook, release checklist, and dashboard annotation for pricing-engine.

## Meeting MTG-0401 - 2026-01-30 - Steering Review
- Facilitator: Yara Haddad
- Attendees: Jon Bell, Mateo Garcia, Maya Chen, Aisha Khan, Anika Sharma, Iris Wang
- Focus service: search-recommendations
- Related evidence: ATLAS-2392, PR-5787, PD-2220

### Discussion
- Risk: search-recommendations ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2392.
- Risk: search-recommendations ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2392.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Risk: search-recommendations ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2392.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Elena Petrova will close the action item before 2026-02-13.
- Update runbook, release checklist, and dashboard annotation for search-recommendations.

## Meeting MTG-0402 - 2026-02-06 - Release Readiness
- Facilitator: Sara Novak
- Attendees: Fatima Noor, Luca Moretti, Dmitri Volkov, Ravi Patel, Mateo Garcia, Jon Bell
- Focus service: notification-service
- Related evidence: ATLAS-4927, PR-10659, PD-2476

### Discussion
- Risk: notification-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4927.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Kim Tan will close the action item before 2026-02-20.
- Update runbook, release checklist, and dashboard annotation for notification-service.

## Meeting MTG-0403 - 2026-02-13 - Incident Review
- Facilitator: Ben Carter
- Attendees: Owen Brooks, Kim Tan, Nora Singh, Ben Carter, Sara Novak, Victor Silva
- Focus service: notification-service
- Related evidence: ATLAS-4581, PR-5223, PD-2788

### Discussion
- Risk: notification-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4581.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Anika Sharma will close the action item before 2026-02-27.
- Update runbook, release checklist, and dashboard annotation for notification-service.

## Meeting MTG-0404 - 2026-02-20 - Incident Review
- Facilitator: Fatima Noor
- Attendees: Kim Tan, Theo Martin, Mateo Garcia, Noah Evans, Sara Novak, Samir Rao
- Focus service: order-ledger
- Related evidence: ATLAS-2264, PR-9956, PD-2461

### Discussion
- Blocker: QA needs production-like seed data before approving PR-9956. The workaround is documented but not yet rehearsed by on-call.
- Blocker: QA needs production-like seed data before approving PR-9956. The workaround is documented but not yet rehearsed by on-call.
- Blocker: QA needs production-like seed data before approving PR-9956. The workaround is documented but not yet rehearsed by on-call.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Blocker: QA needs production-like seed data before approving PR-9956. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Harper Lee will close the action item before 2026-03-06.
- Update runbook, release checklist, and dashboard annotation for order-ledger.

## Meeting MTG-0405 - 2026-02-27 - Release Readiness
- Facilitator: Jon Bell
- Attendees: Priya Nair, Jon Bell, Ravi Patel, Dmitri Volkov, Noah Evans, Theo Martin
- Focus service: loyalty-service
- Related evidence: ATLAS-2561, PR-12877, PD-2249

### Discussion
- Risk: loyalty-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2561.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Risk: loyalty-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2561.
- Blocker: QA needs production-like seed data before approving PR-12877. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Ben Carter will close the action item before 2026-03-13.
- Update runbook, release checklist, and dashboard annotation for loyalty-service.

## Meeting MTG-0406 - 2026-03-06 - KT Working Session
- Facilitator: Sara Novak
- Attendees: Luca Moretti, Noah Evans, Anika Sharma, Samir Rao, Mateo Garcia, Dmitri Volkov
- Focus service: notification-service
- Related evidence: ATLAS-4871, PR-12168, PD-2721

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Jon Bell will close the action item before 2026-03-20.
- Update runbook, release checklist, and dashboard annotation for notification-service.

## Meeting MTG-0407 - 2026-03-13 - Architecture Council
- Facilitator: Yara Haddad
- Attendees: Fatima Noor, Nora Singh, Theo Martin, Priya Nair, Kim Tan, Anika Sharma
- Focus service: notification-service
- Related evidence: ATLAS-4196, PR-10602, PD-2858

### Discussion
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Blocker: QA needs production-like seed data before approving PR-10602. The workaround is documented but not yet rehearsed by on-call.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Risk: notification-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4196.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Jon Bell will close the action item before 2026-03-27.
- Update runbook, release checklist, and dashboard annotation for notification-service.

## Meeting MTG-0408 - 2026-03-20 - Customer Escalation Review
- Facilitator: Fatima Noor
- Attendees: Luca Moretti, Mateo Garcia, Ravi Patel, Owen Brooks, Sara Novak, Jon Bell
- Focus service: checkout-api
- Related evidence: ATLAS-2223, PR-17784, PD-2231

### Discussion
- Blocker: QA needs production-like seed data before approving PR-17784. The workaround is documented but not yet rehearsed by on-call.
- The team reviewed checkout-api readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Risk: checkout-api ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2223.
- The team reviewed checkout-api readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Risk: checkout-api ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2223.

### Decisions and Actions
- Owner Iris Wang will close the action item before 2026-04-03.
- Update runbook, release checklist, and dashboard annotation for checkout-api.

## Meeting MTG-0409 - 2026-03-27 - Incident Review
- Facilitator: Elena Petrova
- Attendees: Ravi Patel, Yara Haddad, Harper Lee, Anika Sharma, Samir Rao, Owen Brooks
- Focus service: analytics-pipeline
- Related evidence: ATLAS-2560, PR-12156, PD-2407

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- The team reviewed analytics-pipeline readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Blocker: QA needs production-like seed data before approving PR-12156. The workaround is documented but not yet rehearsed by on-call.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Blocker: QA needs production-like seed data before approving PR-12156. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Victor Silva will close the action item before 2026-04-10.
- Update runbook, release checklist, and dashboard annotation for analytics-pipeline.

## Meeting MTG-0410 - 2026-04-03 - Architecture Council
- Facilitator: Maya Chen
- Attendees: Mateo Garcia, Nora Singh, Jon Bell, Sara Novak, Elena Petrova, Noah Evans
- Focus service: cart-service
- Related evidence: ATLAS-3879, PR-9882, PD-2478

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- The team reviewed cart-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- The team reviewed cart-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Ben Carter will close the action item before 2026-04-17.
- Update runbook, release checklist, and dashboard annotation for cart-service.

## Meeting MTG-0411 - 2026-04-10 - Customer Escalation Review
- Facilitator: Theo Martin
- Attendees: Maya Chen, Harper Lee, Elena Petrova, Kim Tan, Nora Singh, Samir Rao
- Focus service: pricing-engine
- Related evidence: ATLAS-3244, PR-8209, PD-2858

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Blocker: QA needs production-like seed data before approving PR-8209. The workaround is documented but not yet rehearsed by on-call.
- The team reviewed pricing-engine readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- The team reviewed pricing-engine readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.

### Decisions and Actions
- Owner Mateo Garcia will close the action item before 2026-04-24.
- Update runbook, release checklist, and dashboard annotation for pricing-engine.

## Meeting MTG-0412 - 2026-04-17 - Architecture Council
- Facilitator: Jon Bell
- Attendees: Yara Haddad, Iris Wang, Maya Chen, Ravi Patel, Owen Brooks, Jon Bell
- Focus service: tax-service
- Related evidence: ATLAS-3762, PR-18264, PD-2148

### Discussion
- Risk: tax-service ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-3762.
- The team reviewed tax-service readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.

### Decisions and Actions
- Owner Fatima Noor will close the action item before 2026-05-01.
- Update runbook, release checklist, and dashboard annotation for tax-service.

## Meeting MTG-0413 - 2026-04-24 - Architecture Council
- Facilitator: Sara Novak
- Attendees: Maya Chen, Iris Wang, Kim Tan, Anika Sharma, Grace Kim, Yara Haddad
- Focus service: analytics-pipeline
- Related evidence: ATLAS-1093, PR-5003, PD-2158

### Discussion
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- The team reviewed analytics-pipeline readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Risk: analytics-pipeline ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-1093.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- Risk: analytics-pipeline ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-1093.

### Decisions and Actions
- Owner Ravi Patel will close the action item before 2026-05-08.
- Update runbook, release checklist, and dashboard annotation for analytics-pipeline.

## Meeting MTG-0414 - 2026-05-01 - Architecture Council
- Facilitator: Maya Chen
- Attendees: Fatima Noor, Ben Carter, Jon Bell, Luca Moretti, Ravi Patel, Grace Kim
- Focus service: search-recommendations
- Related evidence: ATLAS-3417, PR-14598, PD-2460

### Discussion
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- The team reviewed search-recommendations readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Blocker: QA needs production-like seed data before approving PR-14598. The workaround is documented but not yet rehearsed by on-call.
- The team reviewed search-recommendations readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- Blocker: QA needs production-like seed data before approving PR-14598. The workaround is documented but not yet rehearsed by on-call.

### Decisions and Actions
- Owner Samir Rao will close the action item before 2026-05-15.
- Update runbook, release checklist, and dashboard annotation for search-recommendations.

## Meeting MTG-0415 - 2026-05-08 - SLO Review
- Facilitator: Owen Brooks
- Attendees: Mateo Garcia, Ravi Patel, Maya Chen, Victor Silva, Ben Carter, Jon Bell
- Focus service: order-ledger
- Related evidence: ATLAS-4300, PR-11422, PD-2382

### Discussion
- Risk: order-ledger ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4300.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- Blocker: QA needs production-like seed data before approving PR-11422. The workaround is documented but not yet rehearsed by on-call.
- Risk: order-ledger ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-4300.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.

### Decisions and Actions
- Owner Aisha Khan will close the action item before 2026-05-22.
- Update runbook, release checklist, and dashboard annotation for order-ledger.

## Meeting MTG-0416 - 2026-05-15 - Customer Escalation Review
- Facilitator: Aisha Khan
- Attendees: Yara Haddad, Mateo Garcia, Harper Lee, Victor Silva, Noah Evans, Owen Brooks
- Focus service: search-recommendations
- Related evidence: ATLAS-2699, PR-18502, PD-2580

### Discussion
- Risk: search-recommendations ownership is unclear during incident handoff. Action: add owner mapping to Confluence and link ATLAS-2699.
- Customer impact review: support escalations mention latency, payment retry, tax quote mismatch, and delayed confirmation emails.
- The team reviewed search-recommendations readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.
- KT note: new engineers should trace Jira, PR, PagerDuty, Grafana, and database evidence before changing checkout routing.
- The team reviewed search-recommendations readiness. Decision: keep the feature flag staged until Grafana p95, database lag, and support volume stay green for one week.

### Decisions and Actions
- Owner Maya Chen will close the action item before 2026-05-29.
- Update runbook, release checklist, and dashboard annotation for search-recommendations.
