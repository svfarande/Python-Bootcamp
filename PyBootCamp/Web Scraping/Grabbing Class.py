import requests
import bs4

'''
Syntax                      --> Match Results
soup.select(‘div’)          --> All elements with ‘div’ tag
soup.select(‘#some_id’)     --> Elements containing id=’some_id’
soup.select(‘.some_class’)  --> Elements containing class = ‘some_class’
soup.select(‘div span’)     --> Any elements named span within a div element.
soup.select(‘div > span’)   --> Any elements named span directly within a div element, 
                                with nothing in between.
'''

result = requests.get("https://en.wikipedia.org/wiki/Grace_Hopper")
soup = bs4.BeautifulSoup(result.text, "lxml")
print(soup.select('.toctext'))
'''
[<span class="toctext">Early life and education</span>, <span class="toctext">Career</span>, 
<span class="toctext">World War II</span>, .....]
'''
print(soup.select('.toctext')[2])   # <span class="toctext">World War II</span>
print(soup.select('.toctext')[2].text)  # World War II
for item in soup.select('.toctext'):    # will print all the text one by one
    print(item.text)
