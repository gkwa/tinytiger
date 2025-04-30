import argparse


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Classify product names as Worcestershire sauce or not"
    )

    parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        default=0,
        help="Increase verbosity (can be used multiple times)",
    )

    parser.add_argument(
        "--infile",
        type=str,
        help="Input file with product names (one per line). If not specified, reads from stdin.",
    )

    return parser.parse_args()
