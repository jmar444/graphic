import r
import matrix

DEFAULT_WIDTH = 1000
DEFAULT_HEIGHT = 1000

def emptydict(x=DEFAULT_WIDTH, y=DEFAULT_HEIGHT):
	return dict(zip(list(r.C2(i, j) for i in range(x) for j in range(y)), [[0,0,0] for k in range(x*y)]))

class Layer():
	def __init__(self, x=DEFAULT_WIDTH, y=DEFAULT_HEIGHT, d=0):
		if !d:
			emptydict()
		else: self.dict = d
		self.width = x
		self.height = y

	def __add__(self, other):
		result = {}
		for key in self.dict.keys():
			self_arr = self.dict[key]
			other_arr = other.dict[key]
			result.update({key : [max(self_arr[0], other_arr[0]), 
								  max(self_arr[1], other_arr[1]), 
								  max(self_arr[2], other_arr[2]) ]})
		return layer(self.width, self.height, result)

	def __mul__(self, other):
		result = {}
		for key in self.dict.keys():
			self_arr = self.dict[key]
			other_arr = other.dict[key]
			result.update({key : [min(self_arr[0], other_arr[0]),
								  min(self_arr[1], other_arr[1]),
								  min(self_arr[2], other_arr[2]) ]})
		return Layer(self.width, self.height, result)

	def manipulate(self, f):
		result = emptydict(self.width, self.height)
		keys = self.dict.keys()
		for key in keys:
			_key = f(key)
			if _key in keys:
				result[_key]=self.dict[key]
			else: pass
		return Layer(self.width, self.height, result)

	def drawlayer(self, image):
		keys = self.dict.keys()
		for key in keys:
			color = tuple(self.dict[key])
			key.draw(image, color)


