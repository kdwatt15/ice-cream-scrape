# Project imports
from icecreamscrape.webdriver import driver


def test_init_driver(webdriver):
	driver = webdriver.driver
	driver.get("http://google.com")
	assert driver.title == "Google", driver

