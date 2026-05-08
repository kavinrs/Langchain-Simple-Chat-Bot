@echo off
echo.
echo ==========================================
echo AI ChatBot - Complete Setup Guide
echo ==========================================
echo.

echo Checking prerequisites...
where node >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    echo [OK] Node.js is installed
) else (
    echo [ERROR] Node.js is not installed. Please install Node.js 16+ first.
    exit /b 1
)

where python >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    echo [OK] Python is installed
) else (
    echo [ERROR] Python is not installed. Please install Python 3.12+ first.
    exit /b 1
)

echo.
echo Setting up frontend...
cd frontend
call npm install
echo [OK] Frontend dependencies installed

echo.
echo Setting up backend...
cd ..
pip install -r requirements.txt 2>nul || echo [INFO] Install Python dependencies from pyproject.toml
echo [OK] Backend setup complete

echo.
echo ==========================================
echo Setup Complete!
echo ==========================================
echo.
echo To run the application:
echo.
echo 1. Start Redis server:
echo    redis-server
echo.
echo 2. In one terminal, start the backend:
echo    uvicorn main:app --reload
echo.
echo 3. In another terminal, start the frontend:
echo    cd frontend
echo    npm run dev
echo.
echo The frontend will be available at: http://localhost:3000
echo The backend API will be available at: http://localhost:8000
echo API Documentation at: http://localhost:8000/docs
echo.
pause
