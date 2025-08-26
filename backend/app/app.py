from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app.routers import auth

app = FastAPI(title="AI-Help-to-CV API")

# create tables (MVP)
Base.metadata.create_all(bind=engine)

origins = ["http://localhost:5173"]
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

app.include_router(auth.router)
