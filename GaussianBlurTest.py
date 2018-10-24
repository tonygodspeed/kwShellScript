# coding=utf8
__author__ = 'Administrator'

from PIL import Image, ImageFilter


class MyGaussianBlur(ImageFilter.Filter):
	name = "GaussianBlur"

	def __init__(self, radius=100, bounds=None):
		self.radius = radius
		self.bounds = bounds

	def filter(self, image):
		if self.bounds:
			clips = image.crop(self.bounds).gaussian_blur(self.radius)
			image.paste(clips, self.bounds)
			return image
		else:
			return image.gaussian_blur(self.radius)


if __name__ == "__main__":
	simg = 'D:/1.jpg'
	dimg = 'D:/3.jpg'
	image = Image.open(simg)
	image = image.filter(MyGaussianBlur(radius=10))
	image.save(dimg)
	print dimg, 'success'
