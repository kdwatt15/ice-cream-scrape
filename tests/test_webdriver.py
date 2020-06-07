# PyPi imports
import pytest

# Project imports
from icecreamscrape.webdriver import driver_factory

@pytest.mark.selenium
def test_driver_factory():
	with driver_factory('http://google.com') as d:
		assert d.driver.title == 'Google'


