import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
	name="ip-converter",
	version="1.0.0",
	author="José Luís",
	author_email="zeluis0712@gmail.com",
	description="A small app to convert your ip adresses or calculate subnet built with flask",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/JL07/IP-CONVERTER",
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3 :: 2"

	]
)