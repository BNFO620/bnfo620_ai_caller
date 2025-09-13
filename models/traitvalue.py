"""
A trait can have many values (reference values, chatgpt values, gemini values)
"""
import json
from dataclasses import dataclass
from config import settings
from csv import DictReader


@dataclass
class TraitValue:
    reference: str | None
    results: dict[str, str]

    def __str__(self) -> str:
        return (f"\tReference: {self.reference}\n"
                f"\tResults: {self.results}")

    def set_reference(self, genus: str, species: str, column_id: str) -> None:
        with open(settings.INPUT_FILE_PATH, "r") as file:
            rows = list(DictReader(file))

            for row in rows:
                if row["Genus"] == genus and row["Species"] == species:
                    if column_id in row:
                        self.reference = row[column_id]
                    return

    def set_results(self, results: dict) -> None:
        for model, response in results.items():
            parsed_response = json.loads(response)
            for value in parsed_response.values():
                self.results[model] = value
                break
