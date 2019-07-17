from PIL import Image
def newGif(images, name='uni'):	
	gif = Image.new('RGB', (1000, 1000), 'white')
	gif.save(name+'.gif', format='GIF', save_all=True, append_images=images, duration=100, loop=0)