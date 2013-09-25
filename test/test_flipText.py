#!/usr/bin/python

import unittest
import os
import sys

sys.path.append(os.path.join('..', 'flipText'))

from flipText import flipText

class testFileParsing(unittest.TestCase):

	def test_normal_file(self):
		flipText('test1.txt', 'test1out.txt')
		with open('test1out.txt') as f:
			fixed_text = f.readlines()
		expected_text = ['John Mills\tare you\table?\n', 'biz\tbar\tfoo\n']
		self.assertEqual(expected_text, fixed_text)
		os.remove('test1out.txt')

	def test_blank_lines(self):
		flipText('test2.txt', 'test2out.txt')
		with open('test2out.txt') as f:
			fixed_text = f.readlines()
		expected_text = ['\n', '\n', 'John Mills\tare you\table?\n', '\n', '\n', 'biz\tbar\tfoo\n', '\n', '\n']
		self.assertEqual(expected_text, fixed_text)
		os.remove('test2out.txt')				

	def test_double_tabs(self):
		flipText('test3.txt', 'test3out.txt')
		with open('test3out.txt') as f:
			fixed_text = f.readlines()
		expected_text = ['John Mills\tare you\t\table?\n', 'biz\t\tbar\tfoo\n', '\n', '\n']
		self.assertEqual(expected_text, fixed_text)
		os.remove('test3out.txt')

if __name__ == '__main__':
	unittest.main()
