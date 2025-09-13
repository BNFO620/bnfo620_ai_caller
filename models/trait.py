"""A single organism has many traits"""
from dataclasses import dataclass, field
from .traitvalue import TraitValue


@dataclass
class Trait:
    column_id: str
    name: str
    units: str | None
    value_format: str
    values: TraitValue

    def __str__(self) -> str:
        return (f"\n{self.column_id} ({self.name}) "
                f"\n{self.values}")
