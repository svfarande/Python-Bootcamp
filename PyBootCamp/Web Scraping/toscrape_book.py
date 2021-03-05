# GOAL - Get a title of every book with 2 star rating on http://toscrape.com/
import requests
import bs4

'''
#   Experiments trying to figure out title of 1 book
base_url = 'https://books.toscrape.com/catalogue/page-{}.html'
print(base_url.format('1'))  # https://books.toscrape.com/catalogue/page-1.html
response = requests.get(base_url.format('1'))
soup = bs4.BeautifulSoup(response.text, 'lxml')
books = soup.select('.product_pod')
print(len(books))   # 20 # As there are 20 books
print(books[10])    # 11th book details
print(str(books[10]))
print('star-rating Two' in str(books[10]))  # True # bad way as this can be matched with anything
print(books[10].select('.star-rating.Two'))     # will give you list # Good way
# if there is space in class name remember to give '.' instead of space
print(books[10].select('.star-rating.Four'))     # will give you empty list and this can be hint
# to find book with star rating two

print(books[10].select('a')[1]['title'])
# we are selecting 'a' tag as required title is in that tag
# but selecting 'a' gives two 'a' tags as there are two 'a' tags in class '.product_pod'
# but the required book title is in 2nd 'a' tag which is at index [1]
# and as this is bs4.element.Tag as similar to dictionary 
# we can use ['title'] to grab the actual title of book
'''

for i in range(1, 51):
    print(f'\n*********************************\nBooks with 2 star rating on page {i} are - ')
    base_url = 'https://books.toscrape.com/catalogue/page-{}.html'
    response = requests.get(base_url.format(str(i)))
    soup = bs4.BeautifulSoup(response.text, 'lxml')
    books = soup.select('.product_pod')

    for book in books:
        if book.select('.star-rating.Two'):     # if the list is empty then if will be false
            print(book.select('a')[1]['title'])
