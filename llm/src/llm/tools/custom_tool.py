from typing import Type

from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from typing import List
import json
import pandas as pd

class Appointment(BaseModel):
    """Input schema for MyCustomTool."""

    appointment: str = Field(..., description="JSON string of appointment information.")


class UpdateCSV(BaseTool):
    name: str = "csv_update"
    essential_keys: List[str] = ['name', 'age','gender','sport','time']
    description: str = (
        "This is used to update csv using pandas based on provided dictionary. The keys in the dictionary will be determine to which columns or csv updated."
    )
    args_schema: Type[BaseModel] = Appointment

    def _run(self, appointment: str) -> str:
        info = json.loads(appointment)
        print("Extracted information - ",info)
        missing_keys = [ x for x in info.keys() if x in self.essential_keys]
        print("Missing information - ",missing_keys)
        # Implementation goes here
        try:
            #Update user csv
            user_csv_path = "src/llm/knowledge/appointments.csv"
            user_df = pd.read_csv(user_csv_path)
            # columns

            user_df.loc[len(user_df)] = [str(len(user_df)+1), info['user_name'], info['age'], info['gender'], info['sport'], info['timee']]
            user_df.to_csv(user_csv_path, index=False)

            return "All csv has been updated."
        except Exception as e:
            return e
        