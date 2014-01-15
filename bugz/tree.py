# -*- coding: utf-8 -*-
import argparse
import os
import sys
import glob
import fnmatch
import copy

DEBUG = False
#DEBUG = True

class Tree:
	def __init__(self):
		self.elem = None
		self.left = None
		self.right = None
	def insert(self, elem):
		if self.elem is None:
			self.elem = elem
			return
		if elem.isEqual(self.elem):
			self.elem.Update(elem)
			return
		if elem.isAbove(self.elem):
			if DEBUG:
				print "%s is above than %s" %(str(elem), str(self.elem))
			t = Tree()
			t.elem = self.elem
			t.left = self.left
			t.right = None#self.right
			self.elem = elem
			self.left = t
			
			if self.right is None:
				return
			el = []
			self.right.elements(el)
			self.right = None
			for e in el:
				self.insert(e)

			return
		if self.elem.isAbove(elem):
			if DEBUG:
				print "insert %s to left of %s" %(str(elem), str(self.elem))
			if self.left is None:
				self.left = Tree()
			self.left.insert(elem)
			return
		if self.right is None:
			self.right = Tree()
		if DEBUG:
			print "insert %s to right of %s" %(str(elem), str(self.elem))
		self.right.insert(elem)
		return
	def Echo(self):
		self.EchoIndent(0)
	def EchoIndent(self, indent):
		print '  ' * indent + str(self.elem)
		if self.left is not None:
			self.left.EchoIndent(indent + 1)
		if self.right is not None:
			self.right.EchoIndent(indent)
	def elements(self, elems):
		if self.elem is None:
			return
		elems.append(self.elem)
		if self.left is not None:
			self.left.elements(elems)
		if self.right is not None:
			self.right.elements(elems)
if __name__ == '__main__':
	main()
