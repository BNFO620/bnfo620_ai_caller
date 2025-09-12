"""
A single organism
"""
from dataclasses import dataclass
from .trait import Trait


@dataclass
class Organism:
    genus: str
    species: str
    traits: list[Trait]

    def __post_init__(self):
        self.initialize_reference_values()

    def __str__(self):
        traits_str = "\n".join(str(trait) for trait in self.traits)
        return (f"{self.genus} {self.species}"
                f"\n\n\t{traits_str}")

    def initialize_reference_values(self):
        for trait in self.traits:
            trait.values.set_reference(self.genus, self.species, trait.column_id)
