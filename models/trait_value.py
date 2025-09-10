"""
A trait can have many values (reference values, chatgpt values)
"""
from dataclasses import dataclass


@dataclass
class TraitValue:
    reference_value: str
    ai_values: dict[str, str] | None

    def __str__(self):
        return (f"Reference Value: {self.reference_value}\n "
                f"AI Response: {self.ai_values}")
