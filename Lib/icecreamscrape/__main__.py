# Standard imports
import sys

# Project imports
from icecreamscrape.cli import cli
from icecreamscrape.webdriver import driver_factory
from icecreamscrape import composites as comps
from icecreamscrape.composites import create_timestamped_dir


def main(args=sys.argv[1:]):
	""" Main function. :param: args is used for testing """
	user_inputs = cli(args)
	url = user_inputs.params.url
	active_features = user_inputs.active_features
	if len(active_features) > 0:
		time_dir = create_timestamped_dir()
		with driver_factory(url) as driver:
			for feature in active_features:
				getattr(sys.modules[comps.__name__],
					feature)(driver, time_dir)
	

def init():
	""" Init construction allows for testing """
	if __name__ == "__main__":
		sys.exit(main())


init()
