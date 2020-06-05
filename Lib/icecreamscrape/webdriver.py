# Standard imports
from os import getcwd
from os.path import join, dirname

# PyPi imports
from selenium.webdriver import Chrome, ChromeOptions
import chromedriver_binary


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
		executable_path = join(dirname(chromedriver_binary.__file__), "chromedriver")
		try:
			return Chrome(
				executable_path = executable_path,
				options = options
			)
		except:
			return executable_path
		
