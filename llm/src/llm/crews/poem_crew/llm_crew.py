from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from healthcare.tools.custom_tool import UpdateCSV

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

# Parameters
# You can replace with your own LLM, alternatively, it can be set in config.
llm = LLM(
    model="ollama/llama3:70b",
    base_url="http://localhost:11434"
)

@CrewBase
class AdminCrew:
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"
    csv_updater = UpdateCSV()

    @agent
    def sports_specialist(self) -> Agent:
        return Agent(config=self.agents_config["sports_specialist"], 
                     llm=llm, 
                     allow_delegation=False, 
                     max_iter=2, 
                     verbose=True)
    
    @agent
    def appointment_admin(self) -> Agent:
        return Agent(config=self.agents_config["appointment_admin"], 
                     llm=llm, 
                     allow_delegation=False, 
                     max_iter=2, 
                     verbose=True, 
                     tools=[self.csv_updater])

    @task
    def route_task(self) -> Task:
        return Task(
            config=self.tasks_config["route_task"],
        )

    @task
    def rag_task(self) -> Task:
        return Task(config=self.tasks_config["rag_task"])
    
    @task
    def extract_task(self) -> Task:
        return Task(config=self.tasks_config["extract_task"])
    
    @task
    def update_task(self) -> Task:
        return Task(config=self.tasks_config["update_task"])

    @task
    def update_task(self) -> Task:
        return Task(config=self.tasks_config["summarize_task"])

    @crew
    def crew(self, mode='route') -> Crew:
        """Creates the Healthhive crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge
        if mode == 'route':
            return Crew(
                agents=[self.sports_specialist()],
                tasks=[self.route_task()],
                process=Process.sequential,
                verbose=True,
            )
        elif mode == 'rag':
            return Crew(
                agents=[self.sports_specialist()],
                tasks=[self.rag_task()],
                process=Process.sequential,
                verbose=True,
            )
        elif mode == 'book':
            return Crew(
                agents=[self.appointment_admin()],
                tasks=[self.extract_task(), self.update_task(), self.summarize_task()],
                process=Process.sequential,
                verbose=True,
            )