from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from FastApi.app import router
from dotenv import load_dotenv

load_dotenv()
print("Hello World")
app=FastAPI()

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:3001", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

