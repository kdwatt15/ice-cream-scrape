# PyPi imports
import pytest
import mock
import subprocess

# Project imports
from icecreamscrape import __main__
from icecreamscrape.__main__ import main


def test_pos_init():
	""" Checks that init triggers init when name is __main__ """
	with mock.patch.object(__main__, "main", return_value=True):
		with mock.patch.object(__main__, "__name__", "__main__"):
			with mock.patch.object(__main__.sys,'exit') as mock_exit:
				__main__.init()
				assert mock_exit.call_args[0][0] == True
				
				
def test_neg_init():
	""" Tests that init does not run main on package import """
	with mock.patch.object(__main__, "__name__", "not-main"):
		assert __main__.init() is None
	

def test_main():
	""" Tests the main function given test arguments """
	main(args=['http://google.com'])
	
	

