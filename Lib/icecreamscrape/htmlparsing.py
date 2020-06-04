# PyPi installs
from bs4 import BeautifulSoup

class soupparser:
	
	def __init__(self, html):
		self.soup = BeautifulSoup(html_doc, 'html.parser')
		


