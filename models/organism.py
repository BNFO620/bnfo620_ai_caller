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

    def __str__(self):
        return (f"Genus: {self.genus}\n "
                f"Species: {self.species}\n"
                f"Traits: {self.traits}")
