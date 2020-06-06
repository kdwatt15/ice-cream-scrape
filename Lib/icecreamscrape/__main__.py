# Standard imports
import sys

# Project imports
from icecreamscrape.cli import cli
from icecreamscrape.webdriver import driver_factory
from icecreamscrape import composites


def main(args=sys.argv[1:]):
	""" Main function. :param: args is used for testing """
	user_inputs = cli(args)
	url = user_inputs.params.url
	active_features = user_inputs.active_features
	with driver_factory(url) as driver:
		for feature in active_features:
			getattr(sys.modules[composites.__name__], feature)(driver)
	

def init():
	""" Init construction allows for testing """
	if __name__ == "__main__":
		sys.exit(main())


init()
