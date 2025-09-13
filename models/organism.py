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

    def __post_init__(self) -> None:
        for trait in self.traits:
            trait.values.set_reference(self.genus, self.species, trait.column_id)

    def __str__(self) -> str:
        traits_str = "\n".join(str(trait) for trait in self.traits)
        return f"{self.genus} {self.species} {traits_str}"
