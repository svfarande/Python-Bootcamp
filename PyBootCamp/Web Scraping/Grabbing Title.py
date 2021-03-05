import requests
import bs4

result = requests.get("http://www.example.com/")
print(result)   # <Response [200]>
print(type(result))     # <class 'requests.models.Response'>
print(result.text)      # HTML structure of website in string format
print(type(result.text))    # <class 'str'>

soup = bs4.BeautifulSoup(result.text, "lxml")
print(soup)     # beautify the result
print(soup.select('title'))     # [<title>Example Domain</title>]
print(soup.select('p'))
# [<p>This domain is for use in illustrative examples in documents. You may use this
#     domain in literature without prior coordination or asking for permission.</p>,
#  <p><a href="https://www.iana.org/domains/example">More information...</a></p>]

# get text from which ever Tag you want using list indexing
print(soup.select('title')[0].getText())    # Example Domain
print(soup.select('p')[1].getText())    # More information...
print(type(soup.select('title')[0]))    # <class 'bs4.element.Tag'>
