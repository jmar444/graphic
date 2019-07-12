import math as m
from PIL import Image
pi = m.pi

class C2(complex):
	def __init__(self, re=0, im=0):
		self.re = self.real
		self.im = self.imag
		self.phi = m.atan2(self.imag, self.real)
		self.ro = m.hypot(self.real, self.imag)

	def draw(self, image, color):
		x = int(self.real) + (image.size[0])//2
		y = -int(self.imag) + (image.size[1])//2
		try:
			image.putpixel((x, y), color)
		except:
			pass