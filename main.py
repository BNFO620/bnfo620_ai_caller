"""
This is the main script. It initializes organism and AI model objects from provided reference data and config file.
"""

from config import settings
from csv import DictReader
from models import Organism, Trait, TraitValue
from utils import determine_traits, fetch_ai_responses, generate_prompts, output_results


def initialize_organisms(selected_traits) -> list[Organism]:
    new_organisms: list[Organism] = []

    # read organism names from the reference data file and create Organism objects for each one
    with open(settings.INPUT_FILE_PATH, "r") as file:
        reader = DictReader(file)
        for row in reader:
            # create traits for each organism
            organism_traits = []
            for selected_trait in selected_traits:
                organism_traits.append(Trait(
                    column_id=selected_trait.column_id,
                    name=selected_trait.name,
                    units=selected_trait.units,
                    value_format=selected_trait.value_format,
                    values=TraitValue(
                        reference_value="",
                        ai_response={}
                    )
                ))
            new_organisms.append(
                Organism(
                    row["Genus"],
                    row["Species"],
                    organism_traits
                )
            )
    return new_organisms


if __name__ == '__main__':
    chosen_traits = determine_traits()
    organisms = initialize_organisms(chosen_traits)
    print(f"Found {len(organisms)} organism(s) in {settings.INPUT_FILE_PATH}")

    # generate prompts for each organism trait
    for organism in organisms:
        prompts = generate_prompts(organism)

        # fetch response for each trait
        for trait_name, prompt in prompts.items():
            print(f"\n\nasking models for the {trait_name} of {organism.genus} {organism.species}...")
            ai_responses = fetch_ai_responses(prompt)

            # find trait by name and set ai_response
            for trait in organism.traits:
                if trait.name == trait_name:
                    trait.values.set_ai_response(ai_responses)
                    print(f"updated ai_response for {organism}")
                    break

        # output the results to a csv file
        output_results(organism)

    print(f"results saved in {settings.OUTPUT_FILE_PATH}")
