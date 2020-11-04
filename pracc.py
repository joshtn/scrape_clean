# Load libraries
import re
import pandas as pd
import requests
from bs4 import BeautifulSoup as bs


# Load webpage

# Load the webpage content
r = requests.get("https://keithgalli.github.io/web-scraping/webpage.html")

# Convert to a beautiful soup object
webpage = bs(r.content)


# FIRST TASK --------

# Grab all of the social links from the webpage
# 3 different ways: find/find_all, select, ...
socials = webpage.find("ul", attrs={"class": "socials"})
children = socials.findChildren("li", recursive=False)
for child in children:
    print(child.a["href"])

# with select
links = webpage.select("ul.socials a")
links_clean = [link["href"] for link in links]
print(links_clean)

# 3rd way
links = webpage.select("li.social a")
links_clean = [link["href"] for link in links]
print(links_clean)


# SCAPING TABLE into a Pandas DataFrame
table = webpage.select("table.hockey-stats")[0]
columns = table.find("thead").find_all("th")
column_names = [c.string for c in columns]

table_rows = table.find("tbody").find_all("tr")
l = []
for tr in table_rows:
    td = tr.find_all("td")
    row = [str(tr.get_text()).strip() for tr in td]
    l.append(row)

print(l)
#df = pd.DataFrame(1, columns=column_names)
# df.head()

# GRAB ALL THE FUN FACTS THAT USE THE WORD 'IS'
#fun_facts = webpage.find("ul", attrs={"class": "fun-facts"})
#fun_facts_is = fun_facts.find_all("li", string=re.compile("is"))
#print([li.text for li in fun_facts_is])
# only return 2 when there should be more....
# right way
facts = webpage.select("ul.fun-facts li")
facts_w_is = [fact.find(string=re.compile("is")) for fact in facts]
facts_w_is = [fact.find_parent().get_text() for fact in facts_w_is if fact]
print(facts_w_is)


# DOWNLOADING IMAGES
# need to append a base path
url = "https://keithgalli.github.io/web-scraping/"
images = webpage.select("div.row div.column img")
image_url = images[0]["src"]
full_url = url + image_url

#img_data = requests.get(full_url).content
# with open("lake_como.jpg", "wb") as handler:
#    handler.write(img_data)
# bortkommenterade för har redan laddat ner bilden.


# SOLVING MYSTERY CHALLENGE
files = webpage.select("div.block a")
relative_files = [f["href"] for f in files]

for f in relative_files:
    full_url = url + f
    page = requests.get(full_url)
    bs_page = bs(page.content)
    secret_word_element = bs_page.find("p", attrs={"id": "secret-word"})
    secret_word = secret_word_element.string
    print(secret_word)
