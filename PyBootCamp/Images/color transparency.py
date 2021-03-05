from PIL import Image

# RGBA - Red, Green, Blue, Alpha
# All RGBA have values from 0 to 255
# In case of Alpha 0, image is completely transparent and 255 is opaque

red = Image.open('red_color.jpg')
blue = Image.open('blue_color.jpg')

# to change transparency you can use putalpha(<int from 0 to 255>)
red.show()  # before dark
red.putalpha(128)
red.show()  # after light

blue.show()
blue.putalpha(128)
blue.show()

# to get purple
blue.paste(im=red, box=(0, 0), mask=red)
blue.show()
# usually pasting one image on another will hide the below one but as we have adjusted
# transparency using putalpha() hence we get to see effect of both colors which is purple
blue.save('purple_color.png')
purple = Image.open('purple_color.png')
purple.show()
