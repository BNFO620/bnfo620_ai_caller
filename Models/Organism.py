"""
A single organism
"""


class Organism:
    genus: str
    species: str

    def __init__(self, genus: str, species: str):
        self.genus = genus
        self.species = species

    def __str__(self):
        return self.genus + " " + self.species
