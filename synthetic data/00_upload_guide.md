# Synthetic Data Pack - Project Atlas

This folder contains fictional, upload-ready data for a one-year project called Project Atlas.

Project Atlas is a retail checkout and order platform modernization that ran from 2025-05-01 to 2026-04-30. The project moved checkout traffic from a legacy monolith to a service-based architecture, added observability, reduced checkout latency, and handled several production incidents.

All files are synthetic. Names, email addresses, ticket IDs, incident IDs, pull requests, commits, and metrics are invented for local testing.

## Upload Order

Upload these files to Base one by one:

1. `01_jira_issues_2025_2026.csv`
2. `02_microsoft_teams_project_channel.md`
3. `03_email_conversations.md`
4. `04_github_repos_prs_commits_branches_releases.csv`
5. `05_grafana_traffic_metrics.csv`
6. `06_database_health_checks.csv`
7. `07_confluence_project_docs.md`
8. `08_pagerduty_incidents.csv`

Each file is below the 10 MB upload limit and uses a supported format: CSV or Markdown.

## Good Questions To Ask After Upload

- Give me KT for Project Atlas as a new backend engineer.
- What are the main risks, blockers, and unresolved questions?
- Which Jira tickets were related to PagerDuty incidents?
- Summarize the checkout latency trend and the database health issues.
- What did the team decide about idempotency, feature flags, and rollback?
- Which GitHub PRs and releases changed checkout routing?
- What should the next on-call engineer check first?
- Create a handoff brief for the Atlas checkout cutover.

## Source Coverage

- Jira issues: epics, stories, bugs, blockers, sprint dates, owners.
- Microsoft Teams: project decisions, daily handoff notes, risks, action items.
- Email conversations: architecture reviews, launch approvals, vendor dependencies, customer impact.
- GitHub repositories: repos, branches, pull requests, commits, releases.
- Grafana traffic metrics: requests, sessions, active users, p95/p99 latency, error rate, uptime, CPU, memory, conversion.
- Database health checks: storage, connections, slow queries, replication lag, cache hit rate, index bloat.
- Confluence: architecture, onboarding, runbook, release checklist, decisions.
- PagerDuty: incidents, severity, root cause, customer impact, action items.

