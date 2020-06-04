# Standard imports
import sys

# Project imports
from icecreamscrape.cli import cli
from icecreamscrape.htmlparser import soupparser


def main(args=sys.argv[1:]):
	""" Main function. :param: args is used for testing """
	params = cli(args).params


if __name__ == "__main__":
	main()
