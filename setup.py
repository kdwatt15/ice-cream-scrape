import setuptools
"""
with open("README.md", "r") as f:
	long_description = f.read()
	f.close
"""
with open("requirements.txt", "r") as f:
	install_requires = f.readlines()
	f.close
	
setuptools.setup(
	name="icecreamscrape",
	version="0.0.1",
	author="Kevin Watt",
	author_email="kdwatt15@gmail.com",
	description="CLI for bulk actions against Intralinks instances.",
	#long_description=long_description,
	long_description_content_type="test/markdown",
	packages=setuptools.find_packages(include=["icecreamscrape"]),
	package_dir={'': 'lib'},
	install_requires=install_requires,
	license="None",
	python_requires=">=3.5"
)
