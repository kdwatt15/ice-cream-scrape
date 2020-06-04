# PyPi imports
import argparse
from validators import url


class cli:
	
	help_messages = {
		'url': 'root URL where the scraper will start'
	}
	
	def __init__(self, args):
		self.__parser = argparse.ArgumentParser()
		self.__init_parser()
		self.params = self.__parser.parse_args(args)
		self.__validate_inputs() # Raises error if anything is wrong with parameters
		
	def __init_parser(self):
		""" Add arguments to the parser """
		# Positional arguments
		self.__parser.add_argument('url', metavar='url', action='store',
			type=str, default=None, help=self.help_messages['url'])
			
	def __validate_inputs(self):
		""" Placeholder to later validate the command line inputs """
		if (url(self.params.url) is not True): raise(ValueError(
			"URL not valid. Please correct and try again.")
		)
