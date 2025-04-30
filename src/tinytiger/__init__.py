import sys
import logging

from tinytiger.cli import parse_args
from tinytiger.classifier import SimpleClassifier


def configure_logging(verbosity):
    """Configure logging based on verbosity level."""
    log_levels = [logging.WARNING, logging.INFO, logging.DEBUG]
    # Ensure verbosity is within available levels
    verbosity = min(verbosity, len(log_levels) - 1)

    logging.basicConfig(
        level=log_levels[verbosity],
        format="%(levelname)s: %(message)s",
        stream=sys.stderr,
    )


def main() -> None:
    """Main entry point for the application."""
    args = parse_args()
    configure_logging(args.verbose)

    logging.info("Initializing Worcestershire sauce classifier")
    classifier = SimpleClassifier()

    # Determine input source
    if args.infile:
        logging.info(f"Reading product names from file: {args.infile}")
        try:
            input_stream = open(args.infile, "r")
        except FileNotFoundError:
            logging.error(f"File not found: {args.infile}")
            sys.exit(1)
    else:
        logging.info("Waiting for product names from stdin...")
        input_stream = sys.stdin

    try:
        for line in input_stream:
            product_name = line.strip()
            if not product_name:
                continue

            logging.debug(f"Classifying: {product_name}")
            is_worcestershire = classifier.classify(product_name)
            # Output format: "1 Title" or "0 Title"
            print(f"{1 if is_worcestershire else 0} {product_name}")
    finally:
        # Close the file if we opened one
        if args.infile and input_stream != sys.stdin:
            input_stream.close()
