from crewai import Task
from textwrap import dedent

class StudyTasks:
    def breakdown_task(self, agent, assignments, hours_per_day):
        return Task(
            description=dedent(f"""
                Analyze the following assignments and exams:
                {assignments}

                The student has {hours_per_day} hours available per day for studying.
                
                Break down each assignment into smaller, manageable study sessions.
                Create a draft schedule for the week.
            """),
            agent=agent,
            expected_output="A structured list of study sessions for the week."
        )

    def estimation_task(self, agent, draft_plan):
        return Task(
            description=dedent(f"""
                Review the draft plan:
                {draft_plan}
                
                Estimate the time required for each session.
                Distribute the sessions across the days of the week to ensure the total time per day does not exceed the limit.
                Spread out difficult subjects.
            """),
            agent=agent,
            expected_output="A daily schedule with time estimates for each task."
        )

    def focus_check_task(self, agent, timed_plan):
        return Task(
            description=dedent(f"""
                Review the timed plan:
                {timed_plan}
                
                Add distinct 10-15 minute breaks after every 45-60 minutes of study.
                Ensure that no day is overloaded. If a day is too heavy, flag it for adjustment.
                Ensure study times are not too late at night.
            """),
            agent=agent,
            expected_output="A revised weekly plan with breaks included and balanced workload."
        )

    def motivational_task(self, agent, balanced_plan):
        return Task(
            description=dedent(f"""
                Review the balanced plan:
                {balanced_plan}
                
                Add a short, encouraging motivational message for each day.
                Add one specific study tip relevant to the subjects being studied that day.
            """),
            agent=agent,
            expected_output="The final weekly study plan with motivational quotes and tips."
        )
