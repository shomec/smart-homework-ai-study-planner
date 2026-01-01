from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    
    plans = relationship("StudyPlan", back_populates="owner")

class StudyPlan(Base):
    __tablename__ = "study_plans"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    
    # Input data
    assignments = Column(JSON) # List of assignments
    preferences = Column(JSON) # Daily hours, etc.
    
    # Output
    generated_plan = Column(JSON) # The result from CrewAI
    
    created_at = Column(DateTime, default=datetime.utcnow)
    
    owner = relationship("User", back_populates="plans")
