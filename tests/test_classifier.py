import unittest
from tinytiger.classifier import SimpleClassifier


class TestSimpleClassifier(unittest.TestCase):
    def setUp(self):
        self.classifier = SimpleClassifier()

    def test_explicit_worcestershire(self):
        """Test products with 'worcestershire' in the name."""
        self.assertTrue(self.classifier.classify("Lea & Perrins Worcestershire Sauce"))
        self.assertTrue(self.classifier.classify("Organic Worcestershire Sauce"))

    def test_brand_recognition(self):
        """Test recognition of Worcestershire brands without explicit mention."""
        self.assertTrue(self.classifier.classify("Lea & Perrins Original Sauce"))
        self.assertTrue(self.classifier.classify("W Sauce 2-Pack"))
        self.assertTrue(self.classifier.classify("The Wizard's Organic Sauce"))

    def test_non_worcestershire(self):
        """Test products that are not Worcestershire sauce."""
        self.assertFalse(self.classifier.classify("Heinz Tomato Ketchup"))
        self.assertFalse(
            self.classifier.classify("SPICE ENTHUSIAST")
        )  # This was misclassified earlier
        self.assertFalse(self.classifier.classify("Annie's Organic Mustard"))
