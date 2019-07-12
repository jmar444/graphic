import r
import math as m

def line(a, b, color=(0,0,0)):
	result = []
	def f(x):
		k = (a.im-b.im)/(a.re-b.re)
		c = a.im - k*a.re
		return k*x+c
	for x in range(int(a.re), int(b.re)):
		result.append(r.C2(x,f(x)))
	return dict(zip(result, [color for i in range(len(result))]))