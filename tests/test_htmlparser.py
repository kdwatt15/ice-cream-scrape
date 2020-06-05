# PyPi imports
import pytest

# Project imports
from icecreamscrape.htmlparser import soupparser


def test_pos_soupparser_init():
	html = '<p>test</p>'
	test_soupparser = soupparser(html=html)
	assert test_soupparser is not None


def test_neg_soupparser_init():
	try:
		test_soupparser = soupparser(html=None)
	except TypeError as e:
		assert type(e) == TypeError


def test_filtered_find_all(sp):
	"""Tests for both posiitonal and keyword searches"""
	assert len(sp.filtered_find_all(name='a')) == 1


