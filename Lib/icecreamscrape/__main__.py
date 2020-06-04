# Standard imports
import sys

# Project imports
from icecreamscrape.cli import cli
from htmlparsing import soupparser


def main():
	cli(sys.argv[1:])


if __name__ == "__main__":
	main()
