# Standard imports
from os import getcwd
from os.path import join

# PyPi imports
from selenium.webdriver import Chrome, ChromeOptions


class driver:
	
	def __init__(self):
		self.driver = self.__init_driver()
	
	def __init_driver(self):
		options = ChromeOptions()
		options.experimental_options["useAutomationExtension"] = False
		options.add_experimental_option(
			'excludeSwitches', ['enable-logging']
		)
		options.headless = True
		# https://stackoverflow.com/questions/43571119/loading-of-unpacked-extensions-is-disabled-by-the-administrator
		return Chrome(
			executable_path = join(getcwd(), "bin", "chromedriver"),
			options = options
		)
		
