"""Collect, grade and release feedback through a CLI app."""

# Add CLI compatibility
import argparse

from traitlets.config import get_config

# Interface with nbgrader's database and extensions
from nbgrader.apps import NbGraderAPI

# """Create config object to specify options for nbgrader"""
from nbgrader_config import c as config



def main(assignment, submission):
    """Collect, grade and release feedback of specified assignment."""
    raise NotImplementedError()

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Will collect, grade and release feedback of \
        new student submissions",
     formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    HELP_STR = '''The root directory for the course files (that includes the `source`,
`release`, `submitted`, `autograded`, etc. directories). Defaults to the
current working directory.
'''
    parser.add_argument("-A", "--assignment", action="store_true", help=help)
    parser.add_argument("-S", "--submission", action="store_true", help=help)
    args = parser.parse_args()

    api = NbGraderAPI(config=config)

    main(args.assignment, args.submission)
