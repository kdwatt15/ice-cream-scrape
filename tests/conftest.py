# PyPi imports
import pytest

# Project imports
from icecreamscrape.htmlparser import soupparser
from icecreamscrape.webdriver import driver


@pytest.fixture
def sp():
	html = '<html><p>test</p><a class="test">test</a></html>'
	return soupparser(html=html)

@pytest.fixture
def webdriver():
	return driver()

