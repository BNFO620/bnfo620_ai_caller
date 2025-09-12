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
            trait_abbreviation = input("Choose your traits! Enter the exact column name of the trait:\n")
            if trait_abbreviation in raw_traits and trait_abbreviation not in added_traits:
                trait_name = input("Enter the non-abbreviated name of the trait (e.g. ventral scale count):\n")
                units = input("If this trait has units enter the units of the trait, otherwise leave blank:\n")
                value_format = input('Enter the expected format of the values for this trait (default: "number-number" or "number" or null):\n')
                if not value_format:
                    value_format = "number-number or number or null"
                added_traits.append(
                    Trait(
                        column_id=trait_abbreviation,
                        name=trait_name,
                        units=units,
                        value_format=value_format,
                        values=TraitValue(
                            reference=None,
                            results={}
                        )
                    )
                )
                more_traits = input(f"{trait_name} added successfully! Do you want to add another trait? y/n:\n").lower().strip("")
            else:
                print("Invalid trait name. Please try again.")
    print(f"\n\nYou have added {len(added_traits)} trait(s) out of {len(raw_traits)} possible traits.")
    return added_traits
