"""
A trait can have many values (reference values, chatgpt values, gemini values)
"""
import json
from dataclasses import dataclass
from config import settings
from csv import DictReader


@dataclass
class TraitValue:
    reference_value: str
    ai_response: dict[str, str] | None

    def __str__(self):
        output = f"\n\tReference Value: {self.reference_value}"
        output += "\n\tAI Responses:"

        for model, response in self.ai_response.items():
            if response:
                parsed_response = json.loads(response)
                for trait, value in parsed_response.items():
                    output += f"\n\t\t{model}: {value}"

        return output

    def set_reference_value(self, genus: str, species: str, column_id: str):
        with open(settings.INPUT_FILE_PATH, "r") as file:
            reader = DictReader(file)
            rows = list(reader)
            matching_row = None

            for row in rows:
                if row["Genus"] == genus and row["Species"] == species:
                    matching_row = row
                    break

            if matching_row and column_id in matching_row:
                self.reference_value = str(matching_row[column_id])

    def set_ai_response(self, ai_response: dict[str, str]):
        self.ai_response = ai_response
