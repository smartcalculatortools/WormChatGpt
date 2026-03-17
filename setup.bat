@echo off
echo =========================================
echo The Architect 2099 - Setup Script
echo =========================================

cd backend

echo.
echo [1/3] Creating virtual environment...
python -m venv venv

echo.
echo [2/3] Activating virtual environment...
call venv\Scripts\activate.bat

echo.
echo [3/3] Installing dependencies...
pip install --upgrade pip
pip install -r requirements.txt

echo.
echo =========================================
echo Setup Complete!
echo =========================================
echo.
echo To run the application:
echo   cd the_architect_2099
echo   run.bat
echo.

pause
