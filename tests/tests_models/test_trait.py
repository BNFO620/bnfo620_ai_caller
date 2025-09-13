import unittest
from models import Trait, TraitValue


class TestTrait(unittest.TestCase):
    """Test cases for Trait class"""

    def setUp(self):
        """Set up test fixtures before each test method"""
        self.empty_trait = Trait(column_id="", name="",  units=None, value_format="", values=TraitValue(reference=None, results={}))

    def test_trait_initialization(self):
        """Test Trait initialization with different values"""
        # Test without values
        column_id = "Ven"
        name = "ventral scale count"
        units = None
        value_format = "number-number"
        values = TraitValue(reference=None, results={})
        trait = Trait(column_id=column_id, name=name, units=units, value_format=value_format, values=values)

        self.assertEqual(trait.column_id, column_id)
        self.assertEqual(trait.name, name)
        self.assertEqual(trait.units, units)
        self.assertEqual(trait.value_format, value_format)
        self.assertEqual(trait.values, values)

        # Test with values
        column_id = "SC"
        name = "subcaudal scale count"
        units = None
        value_format = "number-number"
        values = TraitValue(reference="10-20", results={
            "model1": "10-20",
            "model2": "15-25",
            "model3": "10-20",
            "model4": "15-25"
        })
        trait = Trait(column_id=column_id, name=name, units=units, value_format=value_format, values=values)

        self.assertEqual(trait.column_id, column_id)
        self.assertEqual(trait.name, name)
        self.assertEqual(trait.units, units)
        self.assertEqual(trait.value_format, value_format)
        self.assertEqual(trait.values, values)

    def test_string_representation(self):
        """Test the string representation of Trait"""
        column_id = "MSR"
        name = "dorsal scale count"
        units = None
        value_format = "number-number"
        values = TraitValue(reference="10-20", results={
            "model1": "10-20",
            "model2": "15-25",
            "model3": "10-20",
            "model4": "15-25"
        })
        trait = Trait(column_id=column_id, name=name, units=units, value_format=value_format, values=values)

        result_str = str(trait)
        self.assertIn("MSR (dorsal scale count)", result_str)
        self.assertIn("Reference: 10-20", result_str)
        self.assertIn("Results:", result_str)
        self.assertIn("model1", result_str)
        self.assertIn("model2", result_str)
        self.assertIn("model3", result_str)
        self.assertIn("model4", result_str)


if __name__ == '__main__':
    unittest.main()
