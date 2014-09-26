# CommonMark.py - setup.py
from distutils.core import setup

setup(
	name = "CommonMark-py",
	packages = ['CommonMark'],
	scripts=['bin/CommonMark.py'],
	version = "0.4.9",
	description = "Python parser for the CommonMark Markdown spec",
	author = "Bibek Kafle <bkafle662@gmail.com>, Roland Shoemaker <rolandshoemaker@gmail.com>",
	author_email = "rolandshoemaker@gmail.com",
	url = "https://github.com/rolandshoemaker/CommonMark-py",
	download_url = "https://github.com/rolandshoemaker/CommonMark-py/tarball/v0.4.9",
	keywords = ["markup", "markdown", "commonmark"],
	classifiers = ["Programming Language :: Python",
	"Programming Language :: Python :: 2",
	"Programming Language :: Python :: 3",
	"Development Status :: 4 - Beta",
	"Environment :: Other Environment",
	"Environment :: Console",
	"Intended Audience :: Developers",
	"License :: OSI Approved :: BSD License",
	"Operating System :: OS Independent",
	"Topic :: Documentation",
	"Topic :: Internet :: WWW/HTTP :: Dynamic Content",
	"Topic :: Software Development :: Documentation",
	"Topic :: Software Development :: Libraries :: Python Modules",
	"Topic :: Text Processing :: Markup",
	"Topic :: Utilities"])