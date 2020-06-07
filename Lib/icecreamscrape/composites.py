# Standard imports
import csv
import os
import requests


# PyPi imports
from bs4 import BeautifulSoup
import datetime
from urllib.parse import urljoin
from urllib.parse import urlparse


def create_timestamped_dir():
	time_dir = os.path.join(
		os.getcwd(), 
		datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
	)
	os.makedirs(time_dir)
	return time_dir


def download_documents(webdriver, time_dir):
	driver = webdriver.driver
	soup = BeautifulSoup(driver.page_source, features='html.parser')
	hrefs = [href['href'] for href in soup(href=True)]
	header_list = init_header_list()
	for href in hrefs:
		url = urljoin(webdriver.root_url, href)
		download_file(header_list, url, time_dir)
		

def init_header_list():
	""" Reads the list of accepted header file types """
	fname = os.path.join(os.path.dirname(__file__), 'file-headers.txt')
	with open(fname, 'r') as f:
		content = f.readlines()
		return [line.replace('\n', '') for line in content]
		

def download_file(header_list, url, directory):
	try:
		response = requests.get(url, allow_redirects=True)
		if response.headers['Content-Type'] in header_list:
			file_path = os.path.join(directory, urlparse(url).path.split('/')[-1])
			open(file_path, 'wb').write(response.content)
	except:
		pass

	
def fetch_tables(webdriver, time_dir):
	driver = webdriver.driver
	soup = BeautifulSoup(driver.page_source, features='html.parser')
	table_list = get_tables(soup("table"))
	write_tables(table_list, time_dir)
	

def get_tables(table_set, table_list=[]):
	for table_soup in table_set:
		table_list.append(extract_table(table_soup))
	return table_list
	

def extract_table(table_soup, table=[]):
	rows = table_soup.find_all('tr')
	broken_rows = [row('td') for row in rows]
	for row in broken_rows:
		clean_row = [column.get_text().replace for column in row]
		table.append(clean_row)
	return table
	

def write_tables(table_list, directory):
	for index, table in enumerate(table_list):
		table_file = os.path.join(directory, f'table_{index}')
		with open(table_file, 'w', newline='') as csvfile:
			writer = csv.writer(csvfile, delimiter=',')
			writer.writerows(row for row in table)
