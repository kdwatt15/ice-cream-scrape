# Project imports
from icecreamscrape.cli import cli


def test_pos_init():
	test_cli = cli(args=['http://google.com'])
	assert test_cli.params.url == 'http://google.com'
	
	
def test_neg_init():
	try:
		test_cli = cli(args=['badurl'])
	except ValueError as e:
		assert type(e) is ValueError

	
