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
            trait_abbreviation = input("Choose your traits! Enter the exact column name of the trait: ")
            if trait_abbreviation in raw_traits and trait_abbreviation not in added_traits:
                trait_name = input("Enter the non-abbreviated name of the trait: ")
                units = input("If this trait has units enter the units of the trait, otherwise leave blank: ")
                added_traits.append(
                    Trait(
                        column_id=trait_abbreviation,
                        name=trait_name,
                        units=units,
                        values=None
                    )
                )
                print(f"{trait_name} added successfully!")
                more_traits = input("Do you want to add another trait? y/n: ").lower().strip("")
            else:
                print("Invalid trait name. Please try again.")
    print(f"You have added {len(added_traits)} trait(s) out of {len(raw_traits)} possible traits.")
    return added_traits
