# Large Synthetic Data Pack - Project Atlas 2018-2026

This folder contains a fictional, upload-ready 8-year project history for Project Atlas, a retail checkout and order-platform modernization program.

The dataset is intentionally large and cross-linked so Base can be tested across multi-project upload, hybrid retrieval, Ask AI, KT Brief, knowledge graph, Study Studio artifacts, source citations, connector coverage, dashboard analytics, risk queues, activity logs, audio overview scripts, video storyboards, slide decks, flashcards, and infographics.

All data is synthetic. Names, companies, Jira IDs, PR IDs, commits, release IDs, incidents, metrics, customers, and emails are invented for local demo/testing.

## Time Range

- Start: 2018-06-01
- End: 2026-05-15
- Program length: almost 8 years
- Total upload files: 20
- Total generated size: 12.2 MB

## Upload Order

Base supports selecting multiple files at once. Select all files in this folder except this guide, or upload in this order:

1. `01_jira_issues_2018_2026.csv` (5,201 lines)
2. `02_jira_sprints_epics_roadmap_2018_2026.csv` (577 lines)
3. `03_microsoft_teams_project_channel_2018_2026.md` (1,303 lines)
4. `04_email_conversations_2018_2026.md` (3,843 lines)
5. `05_github_repos_prs_commits_branches_releases_2018_2026.csv` (7,601 lines)
6. `06_github_release_notes_2018_2026.md` (1,633 lines)
7. `07_grafana_service_metrics_2018_2026.csv` (4,993 lines)
8. `08_database_health_checks_2018_2026.csv` (2,497 lines)
9. `09_confluence_knowledge_base_2018_2026.md` (4,995 lines)
10. `10_pagerduty_incidents_2018_2026.csv` (901 lines)
11. `11_support_customer_escalations_2018_2026.csv` (2,601 lines)
12. `12_decisions_risks_actions_2018_2026.csv` (1,601 lines)
13. `13_deployments_feature_flags_experiments_2018_2026.csv` (2,401 lines)
14. `14_oncall_runbook_notes_2018_2026.md` (2,915 lines)
15. `15_traceability_matrix_2018_2026.csv` (1,401 lines)
16. `16_meeting_transcripts_2018_2026.md` (7,075 lines)
17. `17_architecture_decision_records_2018_2026.md` (4,899 lines)
18. `18_security_compliance_audit_findings_2018_2026.csv` (1,601 lines)
19. `19_product_analytics_experiments_2018_2026.csv` (2,601 lines)
20. `20_checkout_channel_session_metrics_2018_2026.csv` (17,437 lines)

Each file is below the 10 MB upload limit and uses a supported type: CSV or Markdown.

## Best Test Questions

- Give me a KT brief for a new backend engineer joining Project Atlas in 2026.
- Summarize the full 8-year timeline by phase, with major risks and decisions.
- Which services had the most incidents and what recurring causes appear?
- Find the strongest source evidence for checkout latency regressions.
- Which Jira tickets, PRs, incidents, and runbooks are connected to payment retry storms?
- Create a release-readiness brief for the 2025 checkout cutover.
- What should the next on-call engineer inspect first?
- Generate quiz questions about the Atlas migration risks.
- Create an audio overview about handoff risks and incident history.
- Generate an infographic about source coverage, risks, incidents, and metrics.
- Build a slide deck outline for an executive project review.

## Connector Coverage Included

- Jira issues, epics, sprint/roadmap records
- Microsoft Teams channel conversations
- Email conversation threads
- GitHub repos, PRs, commits, branches, reviews, releases
- Grafana service metrics and SLO signals
- Database health checks
- Confluence architecture, ADR, runbook, postmortem, and onboarding pages
- PagerDuty incidents and action items
- Support/customer escalations
- Decisions, risks, blockers, actions, traceability, deployments, and feature flags
- Security/compliance audit findings
- Product analytics experiments and checkout channel session metrics
- Weekly meeting transcripts and architecture decision records

## Known Synthetic Themes

- checkout-api cutover and feature flag rollout
- payment-orchestrator idempotency and retry behavior
- database lag, index bloat, slow queries, and migration locks
- PagerDuty incidents linked to Jira and GitHub evidence
- support escalations caused by latency, payment retry, tax, coupon, loyalty, and mobile session issues
- security/compliance evidence gaps and audit traceability
- product experiment tradeoffs tied to latency, conversion, and support volume
- runbook and KT gaps that should appear in Ask AI and Study Studio outputs
