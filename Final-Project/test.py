
############## use requests and bs4 to open and story web data ###################
import requests, bs4

# URL = 'https://bcp.org'
URL = 'https://en.wikipedia.org/wiki/Stanford_University'

# get info from website
res = requests.get(URL)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
# print(type(soup))
# print(soup)
elem = soup.select('td')
attrib = soup.has_attr('href')
print(attrib)
# print(len(elem))
# print(elem)
# print(type(elem))
# dump into excel