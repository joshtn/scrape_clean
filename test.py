# Load in necessary libraries
import re
import requests
from bs4 import BeautifulSoup as bs


# Load our first page

# Load the webpage content
r = requests.get("https://keithgalli.github.io/web-scraping/example.html")

# Convert to a beautiful soup object
soup = bs(r.content)

# Print out our html
# print(soup.prettify())


# START USING BEAUTIFUL SOUP TO SCRAPE

#find and find_all
first_header = soup.find("h2")  # finds first occurance of ...
# print(first_header)

headers = soup.find_all("h2")
print(headers)

# can pass in a list of elements to look for
headers_list = soup.find_all(["h1", "h2"])
print(headers_list)


# You can pass in attrib to the find/find_all function
paragraph = soup.find_all("p", attrs={"id": "paragraph-id"})
print(paragraph)


# You can nest find/find_all calls
body = soup.find('body')
div = body.find('div')
header = div.find('h1')
print(header)


# We can search specific strings in our find/find_all calls
parag = soup.find_all("p", string=re.compile("Some"))

hdrs = soup.find_all("h2", string=re.compile("(H|h)eader"))
# will return list with h2 containing word heder w/o case sensetive


# CSS SELECT
content = soup.select("div p")  # returns p's that are in div

bold_text = soup.select("p#paragraph-id b")
# the b inside p with id paragraph-id

parra = soup.select("body > p")  # direct decendants
print(parra)

for par in parra:
    print(parra.select("i"))

# Grab by element with specific property
soup.select("[align=middle]")


# GETTING A PROPERY OF HTML element
h = soup.find("h2")
print(header.string)

# If multiple child elements use get_text
div = soup.find("div")
print(div.get_text())

# Get a specific property from an element
link = soup.find("a")
link['href']

p = soup.select("p#paragraph-id")
p[0]['id']  # gives the id as a string

# CODE NAVIGATION

# Path syntax
soup.body.div.h1.string  # in this case gives 'HTML Webpage'

# Know the terms : Parent, Child, Sibling
# There are commands such as: find_next_parent()..
soup.body.find("div").find_next_siblings()
