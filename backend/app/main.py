from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import auth, plan
from app.database import engine
from app.models import Base

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Smart Homework AI Study Planner")

origins = [
    "http://localhost:5173",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(plan.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Smart Homework AI Study Planner API"}

@app.get("/health")
def health_check():
    return {"status": "ok"}
