"""
This is the main script. It initializes organism and AI model objects from provided reference data and config file.
"""
from models import Organism
from utils import determine_traits
from config import settings
from csv import DictReader
from utils.add_reference_data import add_reference_data


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
    chosen_traits = determine_traits()
    initialized_organisms = initialize_organisms(chosen_traits)
    add_reference_data(initialized_organisms)

    print(f"initialized_organisms: {initialized_organisms}")
