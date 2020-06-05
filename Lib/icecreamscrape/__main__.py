# Standard imports
import sys

# Project imports
from icecreamscrape.cli import cli
from icecreamscrape.htmlparser import soupparser


def main(args=sys.argv[1:]):
	""" Main function. :param: args is used for testing """
	params = cli(args).params


def init():
	""" Init construction allows for testing """
	if __name__ == "__main__":
		sys.exit(main())


init()
