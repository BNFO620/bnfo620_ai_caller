"""
A single organism
"""
from dataclasses import dataclass
from .trait import Trait
from .trait_value import TraitValue


@dataclass
class Organism:
    genus: str
    species: str
    traits: list[Trait]

    def __post_init__(self):
        self.initialize_reference_values()

    def __str__(self):
        traits_str = "\n".join(str(trait) for trait in self.traits)
        return (f"\nGenus: {self.genus}"
                f"\nSpecies: {self.species}"
                f"\nTraits: \n{traits_str}")

    def initialize_reference_values(self):
        for trait in self.traits:
            trait.values.set_reference_value(self.genus, self.species, trait.column_id)
