# PyPi imports
import pytest
import mock
import os

# Project imports
from icecreamscrape import __main__
import icecreamscrape


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
	

def test_main_no_args():
	""" Tests the main function given test arguments """
	__main__.main(args=['http://google.com'])
	
@pytest.mark.selenium
def test_main_with_args(monkeypatch):
	""" Tests the main function given test arguments """
	def mock_func(*args, **kwargs):
		pass
	monkeypatch.setattr(os, 'makedirs', mock_func)
	monkeypatch.setattr(icecreamscrape.webdriver, 'driver_factory', 
		mock_func)
	monkeypatch.setattr(icecreamscrape.composites, 'download_documents',
		mock_func)
	monkeypatch.setattr(icecreamscrape.composites, 'fetch_tables',
		mock_func)
	__main__.main(args=['http://google.com', '-f'])
	
	

