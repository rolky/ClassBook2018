import glob

class FileName():
	def __init__(self, string):
		self.string = string
		
	def is_of_type(self, *extensions):
		"""Returns True if the the file is of the type extensions provided"""
		for ext in extensions:
			splits = self.string.split(".")
			if splits[-1] in extensions:
				return True
			else:
				return False
				
def get_images_list():
	images_list = glob.glob("./*.*")
	for filename in images_list:
		filename = FileName(filename)
		if filename.is_of_type("md","py","html"):
			#then remove it from the images list
			images_list.remove(filename.string)
	return images_list
	
def get_html_of_images(images_list):
	html = ""
	tag = "<img src={} class='image-fluid'>\n"
	for image in images_list:
		html += tag.format(image)
	return html

if __name__ == "__main__":
	images_list = get_images_list()
	html = get_html_of_images(images_list)
	f = open('index.html','w')
	f.write(html)
	f.close()
	print("done")
			
