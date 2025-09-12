"""
A trait can have many values (reference values, chatgpt values, gemini values)
"""
from dataclasses import dataclass
from config import settings
from csv import DictReader


@dataclass
class TraitValue:
    reference_value: str
    ai_response: dict[str, str] | None

    def __str__(self):
        return (f"\nReference Value: {self.reference_value}"
                f"\nAI Response: {self.ai_response}")

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
        # TODO: clean up ai_response
        self.ai_response = ai_response
