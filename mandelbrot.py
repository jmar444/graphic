import drw
import r
import time

	# c = complex(-0.7269, 0.1889)
	# c = complex(-0.8, 0.156)
	# c = complex(-0.4, 0.6)
	# c = complex(0.285, 0.01)

keys = drw.emptykeys(2000, 2000)

def fMandel(c, n, z=0):
	for i in range(n):
		if (z*z.conjugate()).real > 4:
			return i
		else:
			z = z*z + c
	return 0

def mandel(cntr, width, nit, colorf, mxy=1000):
	result = {}
	for key in keys:
		a = width/mxy*key+cntr
		n = fMandel(a, nit)
		result.update({key:colorf(n, nit)})
	#print(result.values())
	return result

def julia(cntr, width, nit, colorf, mxy=1000, c = r.C2(-0.7269, 0.1889)):
	result = {}
	for key in keys:
		a = width/mxy*key+cntr
		n = fMandel(c, nit, a)
		result.update({key:colorf(n, nit)})
	return result

def colortrivial(n, maxit): return (n, n, n)


