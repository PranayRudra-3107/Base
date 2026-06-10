# Base LinkedIn Copy

## Short Project Description

Base is a full-stack AI project intelligence and KT copilot that turns scattered engineering data into searchable team memory. It lets teams create project workspaces, ingest sources like Jira, GitHub code, Teams/email conversations, Confluence docs, Grafana metrics, database health checks, and PagerDuty incidents, then ask source-grounded questions through a RAG assistant.

The app includes hybrid semantic + keyword retrieval, a knowledge graph, connector sync, chat history, KT brief generation, study tools, and an AWS deployment with CI/CD through GitHub Actions.

## LinkedIn Post

I built Base, a full-stack AI project intelligence and knowledge transfer copilot.

The problem I wanted to solve: project context gets scattered across tickets, PRs, chats, docs, dashboards, incidents, and tribal knowledge. When a new engineer joins or a handoff happens, it takes too long to understand what changed, what is risky, who owns what, and where the evidence lives.

Base creates a project workspace and turns those sources into searchable project memory.

What it supports:
- Uploading and indexing project files
- Live-style connectors for GitHub, Jira, Teams, email, Confluence, Grafana, database health checks, and incident tools
- GitHub source-code indexing for architecture and data-flow questions
- RAG answers with source citations
- Hybrid semantic + keyword retrieval for exact IDs, PRs, filenames, and code terms
- Obsidian-style knowledge graph
- KT briefs, quizzes, flashcards, slide outlines, infographic briefs, and onboarding conversations
- AWS deployment using ECS, ECR, S3, CloudFront, IAM, and GitHub Actions CI/CD

This project helped me bring together backend engineering, frontend product design, AI/RAG architecture, cloud deployment, and DevOps into one realistic interview demo.

Business use case: reduce onboarding time, preserve project context across handoffs, and help teams understand complex projects faster.

Live demo:
https://d13xa0pqwvaoqw.cloudfront.net/

## Resume / Portfolio Line

Built Base, a full-stack AI project intelligence platform using FastAPI, OpenAI, vector search, JavaScript, AWS ECS/S3/CloudFront, and GitHub Actions to ingest engineering sources, generate knowledge graphs, and answer project handoff questions with source-grounded RAG.

## Image Captions

1. `base-linkedin-cover.png`  
   Base turns scattered project data into searchable team memory.

2. `base-linkedin-features.png`  
   The workspace combines connectors, RAG search, knowledge graphs, and KT generation.

3. `base-linkedin-architecture.png`  
   Data flows from sources into ingestion, chunking, vector search, and source-grounded AI answers.

4. `base-linkedin-impact.png`  
   The project demonstrates full-stack AI engineering, frontend craft, AWS deployment, and CI/CD.

## Hashtags

#AI #RAG #FullStackDevelopment #FastAPI #AWS #GitHubActions #VectorSearch #KnowledgeGraph #SoftwareEngineering #PortfolioProject
