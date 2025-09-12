"""A single organism has many traits"""
from dataclasses import dataclass
from .trait_value import TraitValue


@dataclass
class Trait:
    column_id: str
    name: str
    units: str | None
    value_format: str
    values: TraitValue

    def __str__(self):
        return (f"{self.column_id} ({self.name})"
                f"{self.values}")
