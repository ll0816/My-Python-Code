# -*- coding: utf-8 -*-
# extract information of 43rd congress members
# Liu Li
# 3 Dec, 2015

from bs4 import BeautifulSoup
import csv

soup = BeautifulSoup(open("data/43rd-congress.html"), 'lxml')
# print soup.prettify()

# remove the link contain in p from the soup
final_link = soup.p.a
final_link.decompose()

f = csv.writer(open("data/43rd_Congress_all.csv", "w"))   # Open the output file for writing before the loop
f.writerow(["Name", "Years", "Position", "Party", "State", "Congress", "Link"]) # Write column headers as the first line

trs = soup.find_all('tr')

for tr in trs:
    tds = tr.find_all("td")
    try: # This allows the program to continue after encountering an error.
        fullLink = tds[0].a.get('href')
        names = str(tds[0].get_text())
        years = str(tds[1].get_text())
        positions = str(tds[2].get_text())
        parties = str(tds[3].get_text())
        states = str(tds[4].get_text())
        congress = tds[5].get_text()
    except:
        continue

    f.writerow([names, years, positions, parties, states, congress, fullLink])