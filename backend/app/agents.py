from crewai import Agent
from langchain_ollama import ChatOllama
import os

# Keep the ollama/ prefix - LiteLLM needs it to route to Ollama correctly
model_name = os.getenv("LLM_MODEL", "ollama/llama3.2")

# Use ChatOllama - CrewAI will wrap this through LiteLLM which supports Ollama natively
llm = ChatOllama(
    model=model_name,
    base_url=os.getenv("OLLAMA_BASE_URL", "http://ollama:11434"),
    temperature=0.7,
    format="",  # Use default format to avoid special tokens
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
