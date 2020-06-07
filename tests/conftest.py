# PyPi imports
import pytest
from bs4 import BeautifulSoup


def pytest_addoption(parser):
	parser.addoption(
		"--without-selenium", action="store_true", default=False,
		help="run without testing the web parser"
	)
	

def pytest_configure(config):
    config.addinivalue_line(
		"markers", 
		"selenium: mark test as requiring selenium"
	)


def pytest_collection_modifyitems(config, items):
	skip_selenium = pytest.mark.skip(
		reason="Selenium test env not configured"
	)
	if config.getoption("--without-selenium") is True:
		for item in items:
			if "selenium" in item.keywords:
				item.add_marker(skip_selenium)


class FakeDriver:

	def __init__(self):
		self.driver = NestedClass()
		
		
class NestedClass:
	
	def __init__(self):
		self.page_source = "<table><tr><td>1</td></tr><tr><td>2</td></tr></table>"
		
		
@pytest.fixture
def fake_driver():
	return FakeDriver()
	
	
@pytest.fixture
def table_soup():
	return BeautifulSoup(NestedClass().page_source, features='html.parser')
