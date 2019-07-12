import r
import matrix
import drw
import geometry as g
from PIL import Image
import time
import mandelbrot

def main():
	dic = mandelbrot.mandel(r.C2(-0.5), 2, 500, mandelbrot.colortrivial)
	a = drw.Layer(1000, 1000, dic)
	image = Image.new("RGB", (1000, 1000), "white")
	a.drawlayer(image)
	image.save('test.png')
	image.show()

start_time = time.time()
main()
print("--- %s  ---" % (time.time() - start_time))

