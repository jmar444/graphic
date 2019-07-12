import math as m
from PIL import Image
pi = m.pi

class C2:
	def __init__(self, re=0, im=0):
		self.re = re
		self.im = im
		self.phi = m.atan2(self.im, self.re)
		self.ro = m.hypot(self.re, self.im)

	def __str__(self):
		_re = str(self.re)
		_im = ['', '+'][self.im >= 0] + str(self.im)
		return _re + _im + 'i'

	def __add__(self, other):
		self, other = toC2(self), toC2(other)
		return C2(self.re+other.re, self.im+other.im)

	def __sub__(self, other):
		self, other = toC2(self), toC2(other)
		return C2(self.re-other.re, self.im-other.im)

	def __mul__(self, other):
		self, other = toC2(self), toC2(other)
		return C2(self.re*other.re - self.im*other.im,
				  self.re*other.im + self.im*other.re)

	def __eq__(self, other):
		return (self.re==other.re) and (self.im==other.im)

	def __hash__(self):
		return hash(str(self))

	def __neg__(self):
		return C2(-self.re, -self.im)

	def __abs__(self):
		return self.ro

	def __pow__(self, n):
		return self.ro * (m.cos(n*self.phi)+C2(im=1)*m.sin(n*self.phi))

	def conflux(self):
		return C2(self.re, -self.im)

	def draw(self, image, color):
		x = int(self.re) + (image.size[0])//2
		y = -int(self.im) + (image.size[1])//2
		try:
			image.putpixel((x, y), color)
		except:
			pass

def toC2(other):
	if type(other) is C2:
		pass
	else:
		other = C2(other)
	return other

class Q4:
	def __init__(self, b=0, c=0, d=0, a=0):
		self.a = a
		self.b = b
		self.c = c
		self.d = d

	def __str__(self):
		_a = str(self.a)
		_b = ['', '+'][self.b >= 0] + str(self.b)
		_c = ['', '+'][self.c >= 0] + str(self.c)
		_d = ['', '+'][self.d >= 0] + str(self.d)
		return _a + _b + 'i' + _c + 'j' + _d + 'k'

	def __add__(self, other):
		return Q4(self.a+other.a, self.b+other.b, self.c+other.c, self.d+other.d)

	def __sub__(self, other):
		return Q4(self.a-other.a, self.b-other.b, self.c-other.c, self.d-other.d)

	def __mul__(self, other):
		return Q4(self.a*other.a - self.b*other.b - self.c*other.c - self.d*other.d,
				  self.a*other.b + self.b*other.a + self.c*other.d - self.d*other.c, 
				  self.a*other.c - self.b*other.d + self.c*other.a + self.d*other.b, 
				  self.a*other.d + self.b*other.c - self.c*other.b + self.d*other.a)

	def __neg__(self):
		return q4(-self.a, -self.b, -self.c, -self.d)

	def __abs__(self):
		return m.sqrt(self.a*self.a + self.b*self.b + self.c*self.c + self.d*self.d)

	def conflux(self):
		return Q4(self.a, -self.b, -self.c, -self.d)

