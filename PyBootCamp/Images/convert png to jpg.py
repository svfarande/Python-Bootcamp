# convert from png to jpg
# png - RGBA
# jpg - RGB

from PIL import Image

# current image
blue_png = Image.open('C:\\Users\\svfarande\\onedrive\\Documents\\Study '
                      'MAterial\\Python\\PyCharm Projects\\PyBootCamp\\Images\\blue_color.png')

blue_jpg = blue_png.convert('RGB')

# new image
blue_jpg.save('C:\\Users\\svfarande\\onedrive\\Documents\\Study MAterial\\Python\\PyCharm '
              'Projects\\PyBootCamp\\Images\\blue_color.jpg')
