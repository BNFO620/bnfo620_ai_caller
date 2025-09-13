import unittest
from models import TraitValue


class TestTraitValue(unittest.TestCase):
    """Test cases for TraitValue class"""

    def setUp(self):
        """Set up test fixtures before each test method"""
        self.empty_trait_value = TraitValue(reference=None, results={})

    def test_trait_value_initialization(self):
        """Test TraitValue initialization with different values"""
        # Test with None values
        trait_value = TraitValue(reference=None, results={})
        self.assertIsNone(trait_value.reference)
        self.assertEqual(trait_value.results, {})

        # Test with actual values
        reference = "10-20"
        results = {"model1": "10-20"}
        trait_value = TraitValue(reference=reference, results=results)

        self.assertEqual(trait_value.reference, reference)
        self.assertEqual(trait_value.results, results)

    def test_string_representation(self):
        """Test the string representation of TraitValue"""
        reference = "10-20"
        results = {"model1": "10-20"}
        trait_value = TraitValue(reference=reference, results=results)

        result_str = str(trait_value)
        self.assertIn("Reference: 10-20", result_str)
        self.assertIn("Results:", result_str)
        self.assertIn("model1", result_str)

    def set_reference(self):
        # TODO: write a test for the set_reference method
        pass

    def test_set_results(self):
        """Test set_results"""
        self.empty_trait_value.set_results("model1", "15-25")

        self.assertIn("model1", self.empty_trait_value.results)
        result = self.empty_trait_value.results["model1"]
        self.assertEqual(result, "15-25")


if __name__ == '__main__':
    unittest.main()
