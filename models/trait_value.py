"""
A trait can have many values (reference values, chatgpt values, gemini values)
"""
from dataclasses import dataclass
from config import settings
from csv import DictReader
from utils import parse_interval


@dataclass
class Interval:
    low: float | None
    high: float | None
    raw: str                # original "12-34" text


@dataclass
class ModelResult:
    interval: Interval      # parsed range if available
    raw: str                # raw model text
    error: str | None       # parse error


@dataclass
class TraitValue:
    reference: Interval | None
    results: dict[str, ModelResult]  # "model_name": result

    def __str__(self):
        output = f"\n\tReference Value: {self.reference}"
        output += "\n\tAI Responses:"

        for model, result in self.results.items():
            if result:
                output += f"{model}: {result}"
        return output

    def set_reference(self, genus: str, species: str, column_id: str) -> None:
        with open(settings.INPUT_FILE_PATH, "r") as file:
            reader = DictReader(file)
            rows = list(reader)
            matching_row = None

            for row in rows:
                if row["Genus"] == genus and row["Species"] == species:
                    matching_row = row
                    break

            if matching_row and column_id in matching_row:
                self.reference = parse_interval(matching_row[column_id])

    def set_results(self, model: str, response: str) -> None:
        interval_response = parse_interval(response)
        self.results = {
            model: ModelResult(interval_response, response, None)
        }
