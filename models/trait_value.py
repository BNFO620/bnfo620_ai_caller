"""
A trait can have many values (reference values, chatgpt values)
"""
from dataclasses import dataclass


@dataclass
class TraitValue:
    reference_value: str
    ai_values: list[str] | None

    def __str__(self):
        return f"{self.reference_value} {self.ai_values}"
