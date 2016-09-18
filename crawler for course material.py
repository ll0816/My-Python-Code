#crawler for course material
# Liu L.
# Sep 12, 2016

#================================================================

import re, requests, urllib
from bs4 import BeautifulSoup

course_url = 'https://www.cs.cmu.edu/~./15381/'

content = requests.get(course_url).content

print content[:10]

soup = BeautifulSoup(content, 'html.parser')

tag_a = soup.findAll('a', target="_blank")

links = [tag['href'] for tag in tag_a]

video = [link for link in links if link.startswith('http')]
files = [link for link in links if not link.startswith('http')]
prefix = 'https://www.cs.cmu.edu/~./15381/'
legal_links = [''.join([prefix, link]) for link in files]

regex_name = re.compile('/([^/]*$)')
for url in legal_links:
    name = regex_name.search(url).group(1)
    urllib.urlretrieve(url, name)