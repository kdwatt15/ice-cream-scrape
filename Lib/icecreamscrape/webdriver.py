# Standard imports
from os import getcwd
from os.path import join, dirname

# PyPi imports
from selenium.webdriver import Chrome, ChromeOptions
import chromedriver_binary
from chromedriver_binary.utils import get_chromedriver_filename


class driver:
	
	def __init__(self):
		exe_path = self.__find_exe()
		options = self.__init_options()
		self.driver = Chrome(
			executable_path = exe_path, options = options
		)
		
	def __init_options(self):
		options = ChromeOptions()
		options.experimental_options["useAutomationExtension"] = False
		options.add_experimental_option(
			'excludeSwitches', ['enable-logging']
		)
		options.headless = True
		# https://stackoverflow.com/questions/43571119/loading-of-unpacked-extensions-is-disabled-by-the-administrator
		return options
		
	def __find_exe(self):
		return join(
			dirname(chromedriver_binary.__file__),
			get_chromedriver_filename()
		)
