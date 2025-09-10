"""
adds reference values and ai responses to the organism's trait object
"""
from csv import DictReader
from config import settings
from models import TraitValue


def add_values(organism, responses):

    with open(settings.INPUT_FILE_PATH, "r") as file:
        reader = DictReader(file)
        rows = list(reader)

        matching_row = None

        for row in rows:
            if row["Genus"] == organism.genus and row["Species"] == organism.species:
                matching_row = row

        if matching_row:
            for trait in organism.traits:
                if trait.column_id in matching_row:
                    reference_value = matching_row[trait.column_id]
                    trait.values = TraitValue(
                        reference_value=str(reference_value),
                        ai_response=responses
                    )
                else:
                    print(f"No reference value found for trait {trait.name} in row {matching_row}")
        else:
            print(f"No matching row found for organism {organism.genus} {organism.species}")

    return organism
