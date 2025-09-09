"""A single organism has many traits"""
from dataclasses import dataclass


@dataclass
class Trait:
    abbreviation: str
    name: str
    ref_value: str
    ai_value: str

    def __init__(self, abbreviation: str, name: str):
        self.abbreviation = abbreviation
        self.name = name

