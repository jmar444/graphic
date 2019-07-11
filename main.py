import r
import matrix
import drw
from PIL import Image

def rotate90(x):
	return r.C2(0,1)*x

a = drw.Layer(999, 999, drw.emptydict(1000, 1000))
for i in range(-500, 501):
	a.edit(r.C2(i), (255,255,255))


image = Image.new("RGB", (1000, 1000), "white")

a.drawlayer(image)

image.save('test.png')
image.show()