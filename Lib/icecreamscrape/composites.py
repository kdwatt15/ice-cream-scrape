# Standard imports

# Project imports

def download_documents(driver):
	print(f'Download: {driver.title}')
	
	
def fetch_tables(driver):
	driver.get("http://bing.com")
	print(f'Fetch: {driver.title}')
