@echo off
echo =========================================
echo The Architect 2099 - Starting Backend
echo =========================================

cd backend

echo Installing dependencies...
pip install -r requirements.txt

echo Setting environment variables...
set DATABASE_URL=postgresql+asyncpg://architect:architect_pass@localhost:5432/architect_db
set SECRET_KEY=your-secret-key-here
set DEBUG=true

echo Starting FastAPI server...
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
