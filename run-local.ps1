# Run from the repository root in a PowerShell terminal.
# First-time setup (run separately):
#   cd backend; py -3 -m venv .venv; .\.venv\Scripts\Activate.ps1; pip install -r requirements.txt
#   cd ..\frontend; npm install

Write-Host "Start the backend in Terminal 1:" -ForegroundColor Cyan
Write-Host "  cd backend"
Write-Host "  .\.venv\Scripts\Activate.ps1"
Write-Host "  uvicorn app.main:app --reload --host 127.0.0.1 --port 8000"
Write-Host ""
Write-Host "Start the frontend in Terminal 2:" -ForegroundColor Cyan
Write-Host "  cd frontend"
Write-Host "  npm run dev"
Write-Host ""
Write-Host "Then open the Vite URL (usually http://localhost:5173). API docs: http://127.0.0.1:8000/docs"
