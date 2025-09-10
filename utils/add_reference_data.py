"""
Add each trait reference data to the organism object
"""
from csv import DictReader
from config import settings
from models import TraitValue


def add_reference_data(organisms):

    with open(settings.INPUT_FILE_PATH, "r") as file:
        reader = DictReader(file)
        rows = list(reader)

    for organism in organisms:
        matching_row = None

        for row in rows:
            # find the row that matches the organism's genus and species'
            if row["Genus"] == organism.genus and row["Species"] == organism.species:
                matching_row = row

        if matching_row:
            for trait in organism.traits:
                if trait.column_id in matching_row:
                    reference_value = matching_row[trait.column_id]

                    # add the reference value to the trait object
                    trait.values = TraitValue(
                        reference_value=str(reference_value),
                        ai_values=None
                    )
                else:
                    print(f"No reference value found for trait {trait.name} in row {matching_row}")
        else:
            print(f"No matching row found for organism {organism.genus} {organism.species}")

    return organisms
