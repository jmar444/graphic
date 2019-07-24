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
#  MANDELBROT  #
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

#  ATTRACTOR CLIFORD  #
	xn, yn, xnp1, ynp1 = 0, 0, 0, 0
	image = Image.new("RGB", (5000, 5000), "black")
	arr = []
	a, b, c, d = 1.9020439391544657, 1.6841210628974497, -1.4806118282158707, 0.8309751239019039
#	print(a, b, c, d)
	for i in range(nit):
		xnp1, ynp1 = sin(a*yn)+c*cos(a*xn), sin(b*xn)+d*cos(b*yn)
		z = r.C2(xnp1*850, ynp1*850)
		currentcolor = r.C2(z+r.C2(0,250)).getpix(image)
		if currentcolor!='null':
			r.C2(z+r.C2(0,250)).draw(image, (currentcolor[0]+5,currentcolor[0]+5,currentcolor[0]+5))
#			print(currentcolor[0]-250,currentcolor[0]-250,currentcolor[0]-250)
		else: pass
		xn, yn = xnp1, ynp1
#	file.write(str(arr) + '\n')
	image.save('attractor/%f,%f,%f,%f.png' % (a, b, c, d))
		
#  ELIPSE  #		
#	image = Image.new("RGB", (1000, 1000), "white")
#	for i in range(3600):
#		a=r.fromelipse(200, math.pi*i/1800, 0.1)
#		a.draw(image)
#		print(a)
#	image.save('aga.png')


start_time = time.time()
for i in range(1):
	main(50000000)
print("--- %s  ---" % (time.time() - start_time))

