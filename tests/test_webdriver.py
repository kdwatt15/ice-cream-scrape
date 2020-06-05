# Project imports
from icecreamscrape.webdriver import driver


def test_init_driver(webdriver):
	driver = webdriver.driver
	try:
		driver.get("http://google.com")
	except:
		assert 1 == 0, driver
	assert driver.title == "Google", driver

