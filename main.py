"""
This is the main script. It initializes organism and AI model objects from provided reference data and config file.
"""
from models import Organism
from utils import determine_traits
from config import settings
from csv import DictReader
from utils import add_values, fetch_ai_responses
from utils.generate_prompt import generate_prompts


def initialize_organisms(traits) -> list[Organism]:
    new_organisms: list[Organism] = []

    # read organism names from the reference data file and create Organism objects for each one
    with open(settings.INPUT_FILE_PATH, "r") as file:
        reader = DictReader(file)
        for row in reader:
            new_organisms.append(
                Organism(
                    row["Genus"],
                    row["Species"],
                    traits
                )
            )
    return new_organisms


if __name__ == '__main__':
    chosen_traits = determine_traits()
    organisms = initialize_organisms(chosen_traits)
    print(f"created {len(organisms)} organism(s).")

    # generate prompts for each organism and their traits
    for organism in organisms:
        prompts = generate_prompts(organism)
        print(f"generated {len(prompts)} prompt(s).")

        # use the prompt to fetch an AI response
        for prompt in prompts:
            response = fetch_ai_responses(prompt)
            print(f"response: {response}")
            add_values(organisms, response)


