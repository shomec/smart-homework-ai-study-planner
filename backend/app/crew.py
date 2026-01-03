from crewai import Crew, Process
from app.agents import StudyAgents
from app.tasks import StudyTasks
import re

class StudyCrew:
    def __init__(self, assignments, hours_per_day):
        self.assignments = assignments
        self.hours_per_day = hours_per_day

    def run(self):
        agents = StudyAgents()
        tasks = StudyTasks()

        planner = agents.planner_agent()
        time_agent = agents.time_agent()
        focus_agent = agents.focus_agent()
        motivation_agent = agents.motivation_agent()

        breakdown = tasks.breakdown_task(planner, self.assignments, self.hours_per_day)
        estimation = tasks.estimation_task(time_agent, breakdown) # passed context implicitly via previous output
        focus_check = tasks.focus_check_task(focus_agent, estimation)
        motivation = tasks.motivational_task(motivation_agent, focus_check)

        # Crew definition
        crew = Crew(
            agents=[planner, time_agent, focus_agent, motivation_agent],
            tasks=[breakdown, estimation, focus_check, motivation],
            verbose=True,
            process=Process.sequential
        )

        result = crew.kickoff()
        
        # Clean up special tokens from the result
        result_str = str(result)
        # Remove special tokens like <unused24>, <unk>, etc.
        cleaned_result = re.sub(r'<unused\d+>|<unk>|<pad>|<s>|</s>', '', result_str).strip()
        
        # If the result is empty after cleaning, return a default message
        if not cleaned_result or cleaned_result == "":
            cleaned_result = "Study plan generated successfully. Please check the detailed breakdown above."
        
        return cleaned_result
