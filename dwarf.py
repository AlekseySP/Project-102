import random
from nouns import *
from verbs import *
from adjectives import *

class Dwarf(object):
	def __init__(self,
	name,
	hit_points,
	action_points,
	wapon=None):
		self.name = name
		self.hp = hit_points
		self.ap = action_points
		self.wapon = wapon
		
	def say(self, words="Wha?"):
		self.words = words
		print(self.words)
		
	def respond(self, question):
		pass
		
	def thoughts(self):
		self.n = random.choice(nouns)
		self.v = random.choice(verbs)
		self.a = random.choice(adjectives)
		self.nd = nouns_dict[self.n]
		self.vd = verbs_dict[self.v]
		self.ad = adjectives_dict[self.a]
		print(f"I {self.v} {self.a} {self.n}")
		print(f"Torin {self.vd} {self.ad} {self.nd}")
		print()