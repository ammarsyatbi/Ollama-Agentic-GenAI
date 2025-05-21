from pydantic import BaseModel
from typing import Any, Mapping, List
from crewai.flow import Flow, listen, start
from healthcare.crews.admin_crew.admin_crew import AdminCrew
from healthcare.crews.medical_crew.medical_crew import MedicalCrew

class ConverseState(BaseModel):
    route: str | None = None
    query: str | None = None
    inputs: List[Mapping[str, Any]] | None = None
    # inputs: str | None= ""


class RouterFlow(Flow[ConverseState]):
    @start("start")
    def converse(self):
        print("Starting the collector flow")
        self.state.route = "start"
        self.state.inputs = "\n".join(
            [
                f"user: {c['u']}" if 'u' in c else f"assistant: {c['a']}" for c in self.state.inputs
            ]
        )
        print(self.state.inputs)

    # crewai router still broken atm, use router when fixed.
    @listen(converse)
    def route_task(self):
        # inputs = "\n".join([ f"user: {c['u'] if 'u' in c else ''}\n assistant: {c['a'] if 'a' in c else ''}" for c in self.state.inputs])

        result = (
            AdminCrew().crew(mode='route').kickoff(inputs={"conversation": self.state.inputs})
        )
        result = str(result).strip()
        self.state.route = result
        print(f"route task - '{self.state.route}'")

    @listen(route_task)
    def run_task(self):
        print("run task")
        result = (
                AdminCrew()
                .crew(mode=self.state.route)
                .kickoff(
                    inputs={
                        "conversation": self.state.inputs,
                    }
                )
            )
        
        self.state.query = str(result)

    @listen(run_task)
    def complete_task(self):
        print("complete conversation")
        if self.state.query:
            return self.state.query
        return """Sorry. We could not understand your query. Could please rephrase your question?"""
        # extract
        # update csv
        # summarize