import r
import matrix
import drw
import geometry as g
from PIL import Image
import time
import mandelbrot
import gif
import math
import random as rnd

def sin(x): return math.sin(x)
def cos(x): return math.cos(x)

#file = open('txt.txt', 'w')


def main(nit):
#	#dic = mandelbrot.mandel(-0.5, 2, 500, mandelbrot.colortrivial, 2000)
#	images = []
#	e = complex(0.1, 0.1)
#	for i in range(-5, 6):
#		dic = mandelbrot.julia(0, 3, 500, mandelbrot.colortrivial, 1000, c=e*i)
#		file.write(str(dic) + '\n')
#		a = drw.Layer(2000, 2000, dic)
#		image = Image.new("RGB", (1000, 1000), "white")
#		a.drawlayer(image)
#		images.append(image)
#	gif.newGif(images)

# ATTRACTOR CLIFORD #
	xn, yn, xnp1, ynp1 = 0, 0, 0, 0
	image = Image.new("RGB", (1000, 1000), "white")
	arr = []
	a, b, c, d = [2-4*rnd.random() for i in range(4)]
	print(a, b, c, d)
	for i in range(nit):
		xnp1, ynp1 = sin(a*yn)+c*cos(a*xn), sin(b*xn)+d*cos(b*yn)
		z = r.C2(xnp1*200, ynp1*200)
		z.draw(image, (0,0,0))
		xn, yn = xnp1, ynp1
#	file.write(str(arr) + '\n')
	image.save('attractor/%f,%f,%f,%f.png' % (a, b, c, d))
		

start_time = time.time()
for i in range(20):
	main(1000000)
print("--- %s  ---" % (time.time() - start_time))

