import requests
import bs4

response = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")
soup = bs4.BeautifulSoup(response.text, 'lxml')

print(soup.select('.thumbimage'))  # all tags containing class as image, then check which 1 do you
# want
Kasparov = soup.select('.thumbimage')[0]  # grab that image and store in object bs4.element.Tag
print(Kasparov)  # as this is bs4.element.Tag we can consider it as dictionary and get what we want
print(Kasparov['src'])  # will give you the URL of where the actual image is

image_link = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/'
                          'Kasparov_Magath_1985_Hamburg-2.png/'
                          '220px-Kasparov_Magath_1985_Hamburg-2.png')
image_file = open('my_pic.png', 'wb')  # match file extension with URL ; # wb = write binary
image_file.write(image_link.content)  # image_link.content is binary representation of image
image_file.close()
