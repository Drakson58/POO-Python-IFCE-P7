import math

class Reta:


	def __init__(self, Xa, Xb, Ya, Yb):
		self.xa = Xa
		self.xb = Xb
		self.ya = Ya
		self.yb = Yb


	def getXa(self):
		return self.xa
	def getXb(self):
		return self.xb
	def getYa(self):
		return self.ya
	def getYb(self):
		return self.yb


	def calculaDistancia(self):
		return math.sqrt((self.xb - self.xa)**2 + (self.yb - self.ya)**2)