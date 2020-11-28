

class Weapon(object):
	def __init__(self, cls, name, discription, damag, distance, duration):
		self.cls = cls
		self.name = name
		self.discr = discription
		self.dmg = damag
		self.dist = distance
		self.dur = duration


class Gun(object):
	def __init__(self):
		pass