# CREOVANTA — ByteXL Hackathon Presentation Outline

## Slide 1 — The problem
**AI-native creativity is growing faster than the systems used to hire it.**
- Brands struggle to evaluate AI production skills from a generic profile alone.
- Workflows, tools, and usage rights can be unclear.
- Creative briefs and collaboration status are scattered across disconnected tools.

## Slide 2 — Our solution
**CREOVANTA: Create Beyond Imagination. Connect Beyond Limits.**
- A marketplace built for AI filmmakers, animators, generative artists, and creative agencies.
- Rich creator portfolios that expose tools, skills, process, output formats, and licensing context.
- Structured briefs and a visible application-to-collaboration workflow.

## Slide 3 — Product walkthrough
- Discover creators with combined search and filters.
- Open a creator profile and inspect portfolio projects, AI tools, workflow, and verification evidence status.
- Create a campaign brief with content type, style, platform, aspect ratio, budget, deadline, deliverables, and licensing.
- Generate a structured draft from a plain-language idea, then review/edit before publishing.

## Slide 4 — Differentiators
- **Workflow-aware portfolios:** not just finished work; tools and production steps are visible.
- **Evidence-based trust:** self-reported, pending, and reviewed evidence are distinguished.
- **Rights-aware briefs:** commercial use, license type, AI disclosure, and revision scope are explicit fields.
- **AI-assisted brief structure:** rule-based fallback runs without paid API credentials.

## Slide 5 — Architecture
- React + Vite frontend; reusable responsive components and accessible form controls.
- Python FastAPI REST API with Pydantic validation and Swagger/OpenAPI docs.
- SQLAlchemy relational models with SQLite local persistence; PostgreSQL-compatible configuration.
- Signed session tokens, password hashing, role checks, and ownership checks.
- Demo seed data and pytest API tests.

## Slide 6 — Value and next steps
- Reduces ambiguity before creative work begins.
- Helps brands shortlist creators based on relevant evidence and production fit.
- Future extensions: real media uploads, hosted AI provider, contracts, secure payments/escrow, real-time messaging, richer admin moderation, and production migrations.
- Payment processing is not connected in this prototype; demo figures are not real earnings.

## Slide 7 — Why it fits the brief
- Creator profiles and portfolios: highest-priority category.
- Creator discovery and combined filtering: second-highest priority.
- Creative brief definition with licensing and AI assistance.
- Working role-aware flows, responsive UI, API docs, seeded demo data, and test suite.
