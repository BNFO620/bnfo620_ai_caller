"""
This is the main script. It initializes organism and AI model objects from provided reference data and config file.
"""
import asyncio

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
                organism_traits.append(
                    Trait(
                        column_id=selected_trait.column_id,
                        name=selected_trait.name,
                        units=selected_trait.units,
                        value_format=selected_trait.value_format,
                        values=TraitValue(reference=None, results={})
                    )
                )
            new_organisms.append(
                Organism(
                    row["Genus"],
                    row["Species"],
                    organism_traits
                )
            )
    print(f"Found {len(new_organisms)} organism(s) in {settings.INPUT_FILE_PATH}")
    return new_organisms


async def main():
    chosen_traits = determine_traits()
    organisms = initialize_organisms(chosen_traits)

    for organism in organisms:
        prompts = generate_prompts(organism)

        # fetch response for each trait
        for trait, prompt in prompts:
            responses = await fetch_ai_responses(prompt)

            # update the organism with the response
            for model, response in responses.items():
                trait.values.set_results(model, response)
                print(f"\nupdated: {organism}")
                break

        output_results(organism)

    print(f"all done! results saved in {settings.OUTPUT_FILE_PATH}")


if __name__ == '__main__':
    asyncio.run(main())
