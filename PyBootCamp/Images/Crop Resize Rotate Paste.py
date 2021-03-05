from PIL import Image

# Note actual image file stays unaffected only object of Image() is affected

computer = Image.open('example.jpg')
computer.show()  # opens the image
print(type(computer))   # <class 'PIL.JpegImagePlugin.JpegImageFile'>
print(computer.size)  # (1993, 1257) # (width, height) in pixels
print(computer.filename)  # example.jpg
print(computer.format_description)  # JPEG (ISO 10918)

pencils = Image.open('pencils.jpg')
pencils.show()
print(pencils.size)  # (1950, 1300)

# cropping of Image
# Top Left crop
x = 0
y = 0
# (x,y) can be considered as top left
w = 1950 / 3
h = 1300 / 10
# (w,h) can be considered as bottom right
pencils.crop((x, y, w, h)).show()

# Bottom Left crop
x = 0
y = 1100
w = 1950 / 3
h = 1300
pencils.crop((x, y, w, h)).show()

# Lets try to get computer by cropping
x = (1993 / 2) - 120
y = (1257 / 2) + 210
w = (1993 / 2) + 150
h = 1257

# pasting cropped computer into pencils in -

# top right corner
cropped_computer = computer.crop((x, y, w, h))
# we need to figure out where will the top right corner (box) of the cropped computer will go as
# below
cx = 1950 - (w - x)
cy = 0
pencils.paste(im=cropped_computer, box=(int(cx), int(cy)))
pencils.show()

# lets paste it bottom right also
cy = 1300 - (h - y)
pencils.paste(im=cropped_computer, box=(int(cx), int(cy)))
pencils.show()

# resize # make sure pass as tuple
computer.resize((3000, 500)).show()

# left rotate by degrees
computer.rotate(90).show()

# resize & rotate didn't affect original Image() object
computer.show()
