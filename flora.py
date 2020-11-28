"""
Digital flora L-system
"""

import random


class Plant(object):
	def __init__(self, seed, a, b, c):
		self.seed = seed
		self.a = a
		self.b = b
		self.c = c
		
	def grow(self, iter=1):