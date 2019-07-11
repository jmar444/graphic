import r
import matrix
import drw
from PIL import Image

def rotate90(x):
	return r.C2(0,1)*x

a = drw.Layer(1000, 1000, drw.emptydict(1000, 1000))

image = Image.new("RGB", (1000, 1000), "white")

a.drawlayer(image)

image.save('test.png')
image.show()