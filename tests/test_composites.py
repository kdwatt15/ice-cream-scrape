# Standard imports
import os
import tempfile

# PyPi imports
import pytest

# Project imports
from icecreamscrape import composites
from icecreamscrape.composites import create_timestamped_dir
from icecreamscrape.composites import download_file
from icecreamscrape.composites import get_tables
from icecreamscrape.composites import init_header_list

def test_create_time_dir(monkeypatch):
	def mock_func(*args, **kwargs):
		pass
	monkeypatch.setattr(os, 'makedirs', mock_func)
	assert os.getcwd() in composites.create_timestamped_dir()
	
	
def test_init_header_list(monkeypatch):
	assert type(init_header_list()) is list
	
	
@pytest.mark.parametrize(
	('url'),
	(
		('https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf'),
		('https://google.com'),
		('bad_url')
	)
)
def test_download_files(url):
	tmpdir = tempfile.mkdtemp()
	download_file(['application/pdf; qs=0.001'], url, tmpdir)
	
	
"""
For download steps would like to spin up simple HTTP server.

The simple http server should be a class at the conftest level

Steps:
	- create temporary directory and host a text file
	- spin up the simple http server pointed at that directory
	- configure tests to use the server.
"""
		
def test_fetch_get_extract_tables(fake_driver, monkeypatch):
	""" Covers fetch_, get_, and extract_ functions """
	def skip_func(*args, **kwargs):
		pass
	monkeypatch.setattr(composites, 'write_tables', skip_func)
	composites.fetch_tables(fake_driver, True)
	
	
def test_get_tables(table_soup):
	table_list = get_tables(table_soup("table"))
	assert type(table_list[0]) is list
	
	
def test_write_tables():
	tmpdir = tempfile.mkdtemp()
	expected_file = os.path.join(tmpdir, 'table_1')
	composites.write_tables([[[1,2],[3,4]]], tmpdir)
