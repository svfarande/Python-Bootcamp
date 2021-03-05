# TASK: Import any libraries you think you'll need to scrape a website.
import requests
import bs4

# TASK: Use requests library and BeautifulSoup to connect to
# http://quotes.toscrape.com/ and get the HMTL text from the homepage.
response = requests.get('http://quotes.toscrape.com/')
print(response.text)

# TASK: Get the names of all the authors on the first page.
soup = bs4.BeautifulSoup(response.text, 'lxml')
authors = set()     # use set to get unique ones
for author in soup.select('.author'):
    authors.add(author.text)
print(authors)

# TASK: Create a list of all the quotes on the first page.
quotes = []
for quote in soup.select('.text'):
    quotes.append(quote.text)
print(quotes)

# TASK: Inspect the site and use Beautiful Soup to extract the top ten tags from the requests text
# shown on the top right from the home page (e.g Love,Inspirational,Life, etc...).
# HINT: Keep in mind there are also tags underneath each quote, try to find a class only present
# in the top right tags, perhaps check the span.
for tag in soup.select('.tag-item'):
    print(tag.text)


# TASK: Notice how there is more than one page, and subsequent pages look like this
# http://quotes.toscrape.com/page/2/. Use what you know about for loops and string concatenation
# to loop through all the pages and get all the unique authors on the website.
# Keep in mind there are many ways to achieve this, also note that you will need to somehow
# figure out how to check that your loop is on the last page with quotes.
# For debugging purposes, I will let you know that there are only 10 pages,
# so the last page is http://quotes.toscrape.com/page/10/, but try to create a loop that is robust
# enough that it wouldn't matter to know the amount of pages beforehand, perhaps use try/except
# for this, its up to you!
base_URL = 'http://quotes.toscrape.com/page/{}'
page_number = 1
authors = set()
response = requests.get(base_URL.format(str(page_number)))
soup = bs4.BeautifulSoup(response.text, 'lxml')
''' WAY 1 -
while True:
    try:
        for author in soup.select('.author'):
            authors.add(author.text)
        check = soup.select('.next a')[0]['href']   # this will indicate to continue / break
        page_number += 1
        response = requests.get(base_URL.format(str(page_number)))
        soup = bs4.BeautifulSoup(response.text, 'lxml')
    except IndexError:
        break
'''
# WAY 2 -
while True:
    for author in soup.select('.author'):
        authors.add(author.text)
    if not soup.select('.next a'):  # for last page this (list) will be empty and if will be False
        break
    page_number += 1
    response = requests.get(base_URL.format(str(page_number)))
    soup = bs4.BeautifulSoup(response.text, 'lxml')
''' WAY 3 -
while True:
    for author in soup.select('.author'):
        authors.add(author.text)
    page_number += 1
    response = requests.get(base_URL.format(str(page_number)))
    soup = bs4.BeautifulSoup(response.text, 'lxml')
    if soup.select('.previous a')[0]['href'] == '/page/10/':    # for page after last page 
    # previous a href will be  /page/10/
        break
'''
# WAY 4 - will be to check for "No quotes found!" in response.text if true apply break :)
print(authors)
print(len(authors))     # 50
