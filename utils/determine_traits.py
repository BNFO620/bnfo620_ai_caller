from csv import DictReader
from config import settings
from models import Trait, TraitValue


def determine_traits() -> list[Trait]:
    added_traits: list[Trait] = []

    with open(settings.INPUT_FILE_PATH, "r") as file:
        reader = DictReader(file)
        raw_traits = reader.fieldnames[2:]
        print(raw_traits)
        more_traits = "y"

        while more_traits == "y" and len(added_traits) < len(raw_traits):
            trait_abbreviation = input("Enter the exact column name of the trait:\n")
            already_added = any(trait.column_id == trait_abbreviation for trait in added_traits)

            if trait_abbreviation in raw_traits and not already_added:
                trait_name = input("Enter the full name of the trait (e.g. ventral scale count):\n")
                units = input("Units (leave blank if none):\n")
                value_format = input('Expected value format (default: "number-number" or "number" or null):\n') or "number-number or number or null"

                added_traits.append(
                    Trait(
                        column_id=trait_abbreviation,
                        name=trait_name,
                        units=units,
                        value_format=value_format,
                        values=TraitValue(reference=None, results={})
                    )
                )
                more_traits = input(f"{trait_name} added successfully. Add another? y/n:\n").strip("").lower()
            else:
                print("Invalid or duplicate trait name. Please try again.")
    print(f"\n\nYou have added {len(added_traits)} trait(s) out of {len(raw_traits)} possible traits.")
    return added_traits
