"""A single organism has many traits"""
from dataclasses import dataclass
from .trait_value import TraitValue


@dataclass
class Trait:
    column_id: str
    name: str
    units: str | None
    values: TraitValue | None

    def __str__(self):
        return f"{self.name} ({self.column_id})"
