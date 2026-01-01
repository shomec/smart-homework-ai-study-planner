from fastapi import APIRouter, HTTPException, BackgroundTasks
from pydantic import BaseModel
from app.crew import StudyCrew
import json
from uuid import uuid4

router = APIRouter(prefix="/plan", tags=["plan"])

class PlanRequest(BaseModel):
    assignments: str
    hours_per_day: float

from typing import Optional

class PlanResponse(BaseModel):
    plan_id: str
    status: str
    result: Optional[str] = None

# In-memory store for demo purposes (replace with DB for production)
plans = {}

@router.post("/create", response_model=PlanResponse)
def create_plan(request: PlanRequest, background_tasks: BackgroundTasks):
    plan_id = str(uuid4())
    plans[plan_id] = {"status": "processing", "result": None}
    
    background_tasks.add_task(run_crew, plan_id, request.assignments, request.hours_per_day)
    
    return {"plan_id": plan_id, "status": "processing"}

@router.get("/{plan_id}", response_model=PlanResponse)
def get_plan(plan_id: str):
    if plan_id not in plans:
        raise HTTPException(status_code=404, detail="Plan not found")
    
    return {"plan_id": plan_id, **plans[plan_id]}

import traceback

def run_crew(plan_id, assignments, hours_per_day):
    try:
        print(f"Starting crew for plan {plan_id}...")
        crew = StudyCrew(assignments, hours_per_day)
        result = crew.run()
        print(f"Crew run finished for {plan_id}")
        plans[plan_id]["status"] = "completed"
        plans[plan_id]["result"] = str(result)
    except Exception as e:
        print(f"Error executing crew for plan {plan_id}: {e}")
        traceback.print_exc()
        plans[plan_id]["status"] = "failed"
        plans[plan_id]["result"] = f"Error: {str(e)}"
