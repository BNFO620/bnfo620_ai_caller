"""
A trait can have many values (reference values, chatgpt values, gemini values)
"""
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

    def set_results(self, model: str, response: str) -> None:
        self.results[model] = response
