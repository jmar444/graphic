import math as m
from PIL import Image
pi = m.pi
def sh(x): return m.sinh(x)
def csh(x): return m.cosh(x)
def sin(x): return m.sin(x)
def cos(x): return m.cos(x)

class C2(complex):
	def __init__(self, re=0, im=0):
		self.re = self.real
		self.im = self.imag
		self.phi = m.atan2(self.imag, self.real)
		self.ro = m.hypot(self.real, self.imag)

	def draw(self, image, color=(0,0,0)):
		x = int(self.real) + (image.size[0])//2
		y = -int(self.imag) + (image.size[1])//2
		try:
			image.putpixel((x, y), color)
		except:
			pass

	def getpix(self, image):
		x = int(self.real) + (image.size[0])//2
		y = -int(self.imag) + (image.size[1])//2
		try:
			return image.getpixel((x, y))
		except:
			return 'null'

def fromelipse(c, phi, ro): return( C2(c*cos(phi)*csh(ro), c*sin(phi)*sh(ro)) )