# PyPi installs
from bs4 import BeautifulSoup

class soupparser:
	
	def __init__(self, html):
		self.soup = BeautifulSoup(html, 'html.parser')
		
	def filtered_find_all(self, filter_=(lambda x: x is not None), **kargs):
		return list(filter(filter_, self.soup(**kargs)))
		
		


