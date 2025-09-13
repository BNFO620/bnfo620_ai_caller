import unittest
from models import Organism, Trait, TraitValue


class TestOrganism(unittest.TestCase):
    """Test cases for Organism class"""

    def setUp(self):
        """Set up test fixtures before each test method"""
        self.empty_organism = Organism(genus="", species="", traits=[Trait(column_id="", name="",  units=None, value_format="", values=TraitValue(reference=None, results={}))])

    def test_organism_initialization(self):
        """Test Organism initialization with different values"""
        # Test with values
        genus = "Crotalus"
        species = "viridis"
        traits = [Trait(column_id="MSR", name="dorsal scale count",  units=None, value_format="number-number", values=TraitValue(reference="21–29", results={
            "model1": "10-20",
            "model2": "15-25",
            "model3": "10-20",
            "model4": "15-25"
        }))]
        organism = Organism(genus=genus, species=species, traits=traits)

        self.assertEqual(organism.genus, genus)
        self.assertEqual(organism.species, species)
        self.assertEqual(organism.traits, traits)


if __name__ == '__main__':
    unittest.main()
