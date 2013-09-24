#!/usr/bin/python

import unittest
from flipText import flipText

class testFileParsing(unittest.TestCase):

	def test_normal_file(self):
		flipText('test1.txt')
		with open('test1out.txt') as f:
			fixed_text = f.readlines()
		self.assertEqual('asdf', fixed_text)

	def test_white_space(self):
		flipText('test2.txt')
		with open('test2out.txt') as f:
			fixed_text = f.readlines()
		self.assertEqual('asdf', fixed_text)

	def test_weird_chars(self):
		flipText('test3.txt')
		with open('test1out.txt') as f:
			fixed_text = f.readlines()
		self.assertEqual('asdf', fixed_text)

