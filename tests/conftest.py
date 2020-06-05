# PyPi imports
import pytest

# Project imports
from icecreamscrape.htmlparser import soupparser
from icecreamscrape.webdriver import driver


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


@pytest.fixture
def sp():
	html = '<html><p>test</p><a class="test">test</a></html>'
	return soupparser(html=html)

@pytest.fixture
def webdriver():
	return driver()

