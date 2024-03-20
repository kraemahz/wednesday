"""This is a cli file that can serve as a starting point for a Python console
script.
"""
import argparse
import logging
import sys

from typing import List
from wednesday import __version__

__author__ = "Subsequent"
__copyright__ = "Subsequent"
__license__ = "MIT"

_logger = logging.getLogger(__name__)


# ---- CLI ----
# The functions defined in this section are wrappers around the main Python
# API allowing them to be called directly from the terminal as a CLI
# executable/script.


def parse_args(args: List[str]) -> argparse.Namespace:
    """Parse command line parameters."""
    parser = argparse.ArgumentParser(description="Just a Fibonacci demonstration")
    parser.add_argument(
        "--version",
        action="version",
        version=f"wednesday {__version__}",
    )

    parser.add_argument(
        "-v",
        "--verbose",
        dest="loglevel",
        help="set loglevel to INFO",
        action="store_const",
        const=logging.INFO,
    )
    parser.add_argument(
        "-d",
        "--debug",
        dest="loglevel",
        help=argparse.SUPPRESS,
        action="store_const",
        const=logging.DEBUG,
    )
    return parser.parse_args(args)


def setup_logging(loglevel: int):
    """Setup basic logging"""
    logformat = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
    logging.basicConfig(
        level=loglevel, stream=sys.stdout, format=logformat, datefmt="%Y-%m-%d %H:%M:%S"
    )


def main(args: List[str]):
    """Main function"""
    args = parse_args(args)
    setup_logging(args.loglevel)


def run():
    """Command line entrypoint."""
    main(sys.argv[1:])


if __name__ == "__main__":
    run()
