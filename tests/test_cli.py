# Project imports
from icecreamscrape.cli import cli


def test_pos_init():
	test_cli = cli(args=['http://google.com'])
	assert test_cli.params.url == 'http://google.com'


def test_neg_init():
	try:
		cli(args=['bad_url'])
	except ValueError as e:
		assert 'not a valid URL.' in str(e)
