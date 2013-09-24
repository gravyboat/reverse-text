#!/usr/bin/python

import unittest
from flipText import flipText
import os

class testFileParsing(unittest.TestCase):

	def test_normal_file(self):
		flipText('test1.txt', 'test1out.txt')
		with open('test1out.txt') as f:
			fixed_text = f.readlines()
		self.assertEqual("['John Mills\tare you\table?\n', 'biz\tbar\tfoo\n']", fixed_text)
		os.remove('test1out.txt')

	def test_blank_lines(self):
		flipText('test2.txt', 'test2out.txt')
		with open('test2out.txt') as f:
			fixed_text = f.readlines()
		self.assertEqual("['\n', '\n', 'John Mills\tare you\table?\n', '\n', '\n', 'biz\tbar\tfoo\n', '\n', '\n']", fixed_text)
		os.remove('test2out.txt')				

	def test_double_tabs(self):
		flipText('test3.txt', 'test2out.txt')
		with open('test1out.txt') as f:
			fixed_text = f.readlines()
		self.assertEqual("['John Mills\tare you\t\table?\n', 'biz\t\tbar\tfoo\n', '\n', '\n']", fixed_text)
		os.remove('test3out.txt')
