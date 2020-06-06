# PyPi imports
import argparse
from validators import url


class cli:
	
	help_messages = {
		'url': 'root URL where the scraper will start',
		'download-documents': 'switch whether or not download \
			documents',
		'fetch-tables': 'switch whether or not to return tables'
	}
	
	def __init__(self, args):
		self.__parser = argparse.ArgumentParser()
		self.__init_parser()
		self.params = self.__parser.parse_args(args)
		self.active_features = self.__aggregate_features()
		# Next steps validate the inputs or generate error message.
		# Would like to turn this into custom exception class
		error_message = self.__validate_inputs()
		if len(error_message) > 0:
			raise(ValueError("\n".join(error_message)))
		
	def __init_parser(self):
		""" Add arguments to the parser """
		# Positional arguments
		self.__parser.add_argument('url', metavar='url', action='store',
			type=str, default=None, help=self.help_messages['url']
		)
		# Options
		self.__parser.add_argument('-d', '--download-documents',
			action='store_true', default=False, 
			help=self.help_messages['download-documents']
		)
		self.__parser.add_argument('-f', '--fetch-tables',
			action='store_true', default=False,
			help=self.help_messages['fetch-tables']
		)
			
	def __validate_inputs(self, error_message=[]):
		""" Placeholder to later validate the command line inputs """
		if url(self.params.url) is not True:
			error_message.append("URL not valid. Please correct.")	
		return error_message
		
	def __aggregate_features(self, active_features=[]):
		for param, value in self.params.__dict__.items():
			if value is True:
				active_features.append(param)
		return active_features
