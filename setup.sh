#!/bin/bash

echo "=========================================="
echo "AI ChatBot - Complete Setup Guide"
echo "=========================================="
echo ""

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check if Node.js is installed
echo "${YELLOW}Checking prerequisites...${NC}"
if command -v node &> /dev/null; then
    echo "${GREEN}✓ Node.js is installed${NC}"
else
    echo "❌ Node.js is not installed. Please install Node.js 16+ first."
    exit 1
fi

# Check if Python is installed
if command -v python &> /dev/null || command -v python3 &> /dev/null; then
    echo "${GREEN}✓ Python is installed${NC}"
else
    echo "❌ Python is not installed. Please install Python 3.12+ first."
    exit 1
fi

echo ""
echo "${YELLOW}Setting up frontend...${NC}"
cd frontend
npm install
echo "${GREEN}✓ Frontend dependencies installed${NC}"

echo ""
echo "${YELLOW}Installing backend dependencies...${NC}"
cd ..
pip install -r requirements.txt 2>/dev/null || echo "Note: Install Python dependencies from pyproject.toml"
echo "${GREEN}✓ Backend setup complete${NC}"

echo ""
echo "${GREEN}=========================================="
echo "Setup Complete!"
echo "=========================================="
echo ""
echo "To run the application:"
echo ""
echo "1. Start Redis server:"
echo "   redis-server"
echo ""
echo "2. In one terminal, start the backend:"
echo "   uvicorn main:app --reload"
echo ""
echo "3. In another terminal, start the frontend:"
echo "   cd frontend"
echo "   npm run dev"
echo ""
echo "The frontend will be available at: http://localhost:3000"
echo "The backend API will be available at: http://localhost:8000"
echo "API Documentation at: http://localhost:8000/docs"
