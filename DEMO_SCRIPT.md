# CREOVANTA — 3-Minute Judge Demo Script

## 0:00–0:20 — Introduce the problem
“AI creators can produce outstanding work, but brands need more than a thumbnail. They need to know the creator’s tools, skills, process, availability, and how the work can be used. CREOVANTA brings those details into one marketplace.”

## 0:20–0:55 — Discover creators
Open **Discover Creators**. Search for a tool such as Runway, choose a content type, and add a skill filter. Show that the result count changes and filters can be cleared. Open a creator profile and point out skills, tools, workflow, portfolio projects, disclosed rate range, and verification status.

Say: “Verification is evidence-based. A self-reported profile is not falsely presented as verified.”

## 0:55–1:35 — AI-assisted brief creation
Sign in using the **Brand** demo shortcut. Open **Creative Briefs** and enter an idea like: “I need a futuristic 20-second product advertisement for Instagram Reels with cinematic lighting and a premium look.” Generate suggestions. Show content type, style, platform, aspect ratio, required skills, and the missing-details checklist. Open the full brief editor and show budget, deadline, deliverables, commercial-use, license, disclosure, and revision fields.

Say: “The builder is a local fallback engine today, so the feature works without a paid API key. It never silently invents a budget, deadline, or agreed license.”

## 1:35–2:20 — Application and collaboration
Publish the brief. Sign in as **Creator**, open the brief, and submit an application. Switch back to the Brand demo, open the brief’s Applications action, and accept the application. Open **Collaboration Hub** and move the collaboration through In Progress, Submitted, Approved, or Completed.

Say: “The application and status changes are persisted in the database; this is not just a clickable mockup.”

## 2:20–2:45 — Explain the technology
Show the FastAPI docs at `http://127.0.0.1:8000/docs`. Briefly explain the React/Vite frontend, FastAPI REST endpoints, SQLAlchemy models, SQLite persistence, role checks, and seed data.

## 2:45–3:00 — Close honestly
“CREOVANTA makes AI-native creative work easier to discover, evaluate, brief, and track. Our prototype demonstrates the core marketplace workflow. Payments, hosted AI generation, and cloud media uploads are clearly identified as future integrations rather than claimed as completed.”

## Demo accounts
Password for all accounts: `DemoPass123!`
- Creator: `creator1@demo.creovanta.app`
- Brand: `brand@demo.creovanta.app`
- Admin: `admin@demo.creovanta.app`
