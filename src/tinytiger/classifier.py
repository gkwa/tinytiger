import logging


class ClassifierInterface:
    """Interface for product name classifiers."""

    def classify(self, product_name: str) -> bool:
        """Classify a product name as Worcestershire sauce or not."""
        raise NotImplementedError("Subclasses must implement classify method")


class SimpleClassifier(ClassifierInterface):
    """Simple rule-based classifier for Worcestershire sauce products."""

    def __init__(self):
        self.worcestershire_brands = ["lea & perrin", "w sauce", "wizard"]

    def classify(self, product_name: str) -> bool:
        """
        Classify a product name as Worcestershire sauce or not.

        Args:
            product_name: The name of the product to classify

        Returns:
            True if the product is Worcestershire sauce, False otherwise
        """
        # Convert to lowercase for case-insensitive matching
        name = product_name.lower()

        # Check if it explicitly contains 'worcestershire'
        if "worcestershire" in name:
            logging.debug("Match: contains 'worcestershire'")
            return True

        # Check for specific brand names commonly associated with Worcestershire sauce
        for brand in self.worcestershire_brands:
            if brand in name:
                logging.debug(f"Match: contains brand '{brand}'")
                return True

        logging.debug("No match found")
        return False
