import r
import matrix

DEFAULT_WIDTH = 1000
DEFAULT_HEIGHT = 1000

def emptydict(x=DEFAULT_WIDTH, y=DEFAULT_HEIGHT):
	return dict(zip(list(r.c2(i, j) for i in range(x) for j in range(y)), [[0,0,0] for k in range(x*y)]))

class layer():
	def __init__(self, x=DEFAULT_WIDTH, y=DEFAULT_HEIGHT, d=0):
		if !d:
			emptydict()
		else: self.layer = d
		self.width = x
		self.height = y

	def __add__(self, other):
		result = {}
		for key in self.layer.keys():
			arr1 = self.layer[key]
			arr2 = other.layer[key]
			result.update({key : [max(arr1[0], arr2[0]), 
								  max(arr1[1], arr2[1]), 
								  max(arr1[2], arr2[2]) ]})
		return layer(self.width, self.height, result)

	def __mul__(self, other):
		result = {}
		for key in self.layer.keys():
			arr1 = self.layer[key]
			arr2 = other.layer[key]
			result.update({key : [min(arr1[0], arr2[0]),
								  min(arr1[1], arr2[1]),
								  min(arr1[2], arr2[2]) ]})
		return layer(self.width, self.height, result)

	def manipulate(self, f):
		result = emptydict(self.width, self.height)
		keys = self.layer.keys()
		for key in keys:
			_key = f(key)
			if _key in keys:
				result[_key]=self.layer[key]
			else: pass
		return layer(self.width, self.height, result)

	def drawlayer():


