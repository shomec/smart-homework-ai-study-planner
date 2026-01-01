from crewai import LLM, Agent
from langchain_ollama import OllamaLLM
import os

llm = LLM(
    model=os.getenv("OPENAI_MODEL_NAME", "ollama/gemma3:1b"),
    base_url=os.getenv("OPENAI_API_BASE", "http://ollama:11434"),
    api_key=os.getenv("OPENAI_API_KEY", "dummy")
)

class StudyAgents:
    def planner_agent(self):
        return Agent(
            role='Study Coordinator',
            goal='Create a comprehensive weekly study plan based on assignments and deadlines',
            backstory='You are an expert academic planner who excels at breaking down complex assignments into manageable study sessions.',
            llm=llm,
            verbose=True,
            allow_delegation=True
        )

    def time_agent(self):
        return Agent(
            role='Time Management Specialist',
            goal='Estimate task durations and distribute workload evenly avoiding burnout',
            backstory='You are a specialist in productivity and time estimation. You ensure students do not overcommit on a single day.',
            llm=llm,
            verbose=True,
            allow_delegation=False
        )

    def focus_agent(self):
        return Agent(
            role='Well-Being Guardian',
            goal='Ensure the study plan has adequate breaks and is age-appropriate',
            backstory='You care deeply about student mental health. You will reject plans that are too heavy or lack breaks.',
            llm=llm,
            verbose=True,
            allow_delegation=False
        )
    
    def motivation_agent(self):
        return Agent(
            role='Motivational Coach',
            goal='Add encouraging notes and study tips to the plan',
            backstory='You are a cheerful coach who wants to keep the student motivated with positive reinforcement.',
            llm=llm,
            verbose=True,
            allow_delegation=False
        )
