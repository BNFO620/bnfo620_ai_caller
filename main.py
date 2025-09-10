"""
This is the main script for this project.
"""
from models import Organism, Ai
from utils import determine_traits
from config import settings
from csv import DictReader

from utils.add_reference_data import add_reference_data


def initialize_ai_models() -> list[Ai]:
    ai_models: list[Ai] = []

    for model in settings.MODEL_INFO:
        ai_models.append(
            Ai(
                settings.MODEL_INFO[model]["name"],
                settings.MODEL_INFO[model]["version"],
                settings.MODEL_INFO[model]["url"],
                settings.MODEL_INFO[model]["key"],
                settings.MODEL_INFO[model]["client_name"]
            )
        )
    return ai_models


def initialize_organisms(traits) -> list[Organism]:
    organisms: list[Organism] = []

    # read organism names from the reference data file and create Organism objects for each one
    with open(settings.INPUT_FILE_PATH, "r") as file:
        reader = DictReader(file)
        for row in reader:
            organisms.append(
                Organism(
                    row["Genus"],
                    row["Species"],
                    traits
                )
            )
    return organisms


if __name__ == '__main__':
    initialized_ai_models = initialize_ai_models()
    chosen_traits = determine_traits()
    initialized_organisms = initialize_organisms(chosen_traits)
    add_reference_data(initialized_organisms)

    print(f"initialized_organisms: {initialized_organisms}")
