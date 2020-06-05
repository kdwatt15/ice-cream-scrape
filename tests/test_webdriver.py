# Project imports
from icecreamscrape.webdriver import driver

import os


def test_init_driver(webdriver):
	driver = webdriver.driver
	try:
		driver.get("http://google.com")
	except:
		
		assert 1 == 0, os.path.exists(os.path.join(driver, "chromedriver"))
	assert driver.title == "Google", driver

