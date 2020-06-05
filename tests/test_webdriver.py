# PyPi imports
import pytest

# Project imports
from icecreamscrape.webdriver import driver

@pytest.mark.selenium
def test_init_driver(webdriver):
	webdriver.driver.get("http://google.com")
	assert webdriver.driver.title == "Google"


