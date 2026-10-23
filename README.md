# CREOVANTA — AI Content Creator Marketplace

**Tagline:** Create Beyond Imagination. Connect Beyond Limits.

A full-stack ByteXL hackathon prototype for discovering AI-native creators, showcasing portfolios and workflows, creating creative briefs, and tracking applications/collaborations.

## Included features

- React + Vite responsive UI with CREOVANTA navy/violet/cyan/coral design system.
- FastAPI REST API with interactive Swagger docs at `/docs`.
- SQLite persistence by default; SQLAlchemy models are PostgreSQL-compatible via `DATABASE_URL`.
- Password hashing using PBKDF2, signed JWT sessions, and role/ownership checks.
- 12 fictional demo creators, 24 demo portfolio projects, and 8 demo briefs seeded automatically.
- Creator discovery search, combinable skills/tools/content-type/specialization/verification filters, and sorting.
- Creator profile editor and portfolio create/edit/delete workflows.
- Brand brief create/edit/save-draft/publish workflow with budget, deadline, creative requirements, and licensing fields.
- Rule-based AI brief builder that works without paid API keys and clearly identifies itself as a fallback.
- Creator applications, brand application review/status updates, collaboration status tracking, and activity log.
- Verification evidence submission and admin review endpoints.
- Dashboard metrics and demo activity charts; payment processing is explicitly not implemented.
- Pytest API tests.

## Requirements

- Python 3.10+
- Node.js 20+ recommended
- VS Code (recommended)

## Run locally on Windows / VS Code

Open the `creovanta` folder in VS Code. Use two terminals.

### 1. Start the backend

```powershell
cd backend
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
Copy-Item .env.example .env
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

If PowerShell blocks activation, run this once in the terminal session:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

The backend creates `backend/creovanta.db` and seeds demo content the first time it starts. API docs: http://127.0.0.1:8000/docs

### 2. Start the frontend

In a second terminal:

```powershell
cd frontend
npm install
Copy-Item .env.example .env
npm run dev
```

Open the URL Vite prints (usually http://localhost:5173). The frontend reads `VITE_API_URL` from `frontend/.env`; its default is `http://localhost:8000`.

## Demo accounts

All demo accounts use password `DemoPass123!`.

| Role | Email |
|---|---|
| Creator | `creator1@demo.creovanta.app` |
| Brand / Agency | `brand@demo.creovanta.app` |
| Admin | `admin@demo.creovanta.app` |

The sign-in dialog has one-click demo role shortcuts. Seeded names, portfolios, briefs, analytics charts, and rates are fictional demo data, not real users, earnings, or performance results.

## Main demo flow for judges

1. Open **Discover Creators** and search/filter by tool, skill, and content type.
2. Open a creator profile and inspect AI tools, workflow, portfolio projects, availability, rate disclosure, and evidence status.
3. Sign in as **Brand** and generate an editable brief from a natural-language campaign idea.
4. Save a draft or publish a brief with budget/deadline and explicit commercial rights.
5. Sign in as **Creator**, apply to a published brief, then switch back to Brand to review applications.
6. Accept an application to create a collaboration, then move it through statuses in **Collaboration Hub**.
7. Explain that verification signals reflect evidence review status and that payment processing is not connected.

## API highlights

- `POST /api/auth/register`, `POST /api/auth/login`, `GET /api/auth/me`
- `GET /api/creators` with `search`, `skills`, `tools`, `specialization`, `content_type`, `aspect_ratio`, `availability`, `experience_level`, `verified`, `sort`, `page`, `page_size`
- `GET /api/creators/{creator_id}`, `GET/PUT /api/creators/me/profile`
- `POST /api/portfolio`, `GET/PUT/DELETE /api/portfolio/{project_id}`
- `GET/POST /api/briefs`, `GET/PUT/DELETE /api/briefs/{brief_id}`, `POST /api/briefs/{brief_id}/publish`
- `POST /api/briefs/{brief_id}/applications`, `GET /api/briefs/{brief_id}/applications`, `PATCH /api/applications/{application_id}`
- `GET /api/collaborations`, `PATCH /api/collaborations/{collaboration_id}`
- `POST /api/ai/brief-builder`
- `POST /api/verification/evidence`, `GET /api/verification/pending`, `PATCH /api/verification/{evidence_id}`
- `GET /api/analytics/dashboard`, `GET /api/health`

## Data model overview

- `User` has one optional `CreatorProfile` and a role (`creator`, `brand`, or `admin`).
- `CreatorProfile` stores searchable creator information and has many `PortfolioProject` records.
- `CreativeBrief` belongs to a brand user and stores campaign scope, budget, deadline, deliverables, and licensing/disclosure fields.
- `Application` connects a creator profile to a brief. Accepting an application creates a `Collaboration` record.
- `Collaboration` stores status and a JSON activity log. `VerificationEvidence` stores submissions and review state.

## Tests

From `backend` with its virtual environment activated:

```powershell
pytest -q
```

## Important prototype limitations

- AI brief generation uses deterministic templates/rules, not a hosted generative model.
- Portfolio media uses a URL field; uploads and cloud media storage are not wired up.
- There is no payment processor, escrow, real-time chat, or contract-signing integration.
- Demo analytics contain illustrative seeded chart data; the API labels the dataset as demo.
- SQLite is the local default. Set a PostgreSQL `DATABASE_URL` and use a production migration workflow before deployment.
- Before public deployment, replace `JWT_SECRET`, set production CORS origins, add rate limiting, configure secure cookies/HTTPS as appropriate, and perform a security review.

## Project structure

```text
creovanta/
  backend/
    app/
      database.py
      main.py
      models.py
      schemas.py
    tests/test_api.py
    requirements.txt
    .env.example
  frontend/
    src/main.jsx
    src/styles.css
    index.html
    package.json
    .env.example
  README.md
  .gitignore
```
