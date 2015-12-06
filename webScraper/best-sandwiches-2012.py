#!/usr/bin/python
# -*- coding: utf-8 -*-
# Scraper for best sandwiches of 2012 in Chicago. Generate flat-formated tsv file.
# Liu Li
# 12-03-2015
# Code Source: http//www.gregreda.com/2013/04/29/more-web-scraping-with-python/
# Source: http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-Chicago/

from bs4 import BeautifulSoup
from urllib2 import urlopen
import csv
import re

base_url = ("http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-Chicago/")
html = urlopen(base_url).read()
soup = BeautifulSoup(html, "lxml")
sammies = soup.find_all("div", "sammy")
# collect the individual links of the top 50 sandwich in Chicago
sammy_urls = [div.a["href"] for div in sammies]

# create a handle of tsv file with open and write the header
with open("data/best-sandwiches.tsv", "w") as f:
    fieldnames = ("rank", "restaurant", "price", "address", "phone", "website", "description")
    output = csv.writer(f, delimiter = "\t")
    output.writerow(fieldnames)

    for url in sammy_urls:
        # when iterate through the links, adjust the links to a uniform pattern
        url = url.replace("http://www.chicagomag.com", "")
        page = urlopen("http://www.chicagomag.com{0}".format(url))
        soup = BeautifulSoup(page.read(), 'lxml')

        # find the info of rank and restaurant name in headline
        headline = soup.find("h1", "headline").text.split(".")
        rank = headline[0]
        try:
            restaurant = headline[1]
        except IndexError:
            rank = "16"
            restaurant = headline[0]

        # find the info of price, address, price in element p with class addy, exactly extract them by using Regex
        addy = soup.find("p", "addy").em.text

        # search for the phone number by Regex
        if re.search('[0-9\-]{12}',addy):
            phone = re.findall('[0-9\-]{12}',addy)[0]
        # extract the price and address but exclude the phone number
            priceAndAddress = re.findall('(.+)[0-9\-]{12}',addy)[0].partition(" ")
        else:
            phone = ""
            priceAndAddress = addy.partition(" ")

        price = priceAndAddress[0].strip()
        # remove the symbol . at the end of some price
        if re.search('\.$', price):
            price = price[0:-1]

        address = priceAndAddress[2].strip()
        # remove the website at the end of some addresses
        if re.search('.com$', address):
            address = ",".join(address.split(",")[0:-1])
        # remove symbol , at the end of some addresses
        if re.search('\,$', address):
            address = re.findall('(.*)\,$', address)[0]
        # complement the city name of the addresses
        if len(address.split(',')) == 1:
            address = address + ", Chicago"
        # extract the descriptions of the sandwich restaurants in the plain element p
        description = soup.find("p", attrs={'class': None}).text.strip().replace('\n', '')

        # extract the website contained in element p with class addy
        if soup.find("p", "addy").em.a:
            website = soup.find("p", "addy").em.a["href"].strip()
        else:
            website = ""

        # write the collected info into tsv and convert utf-8 int0 ascii
        output.writerow([x.encode('ascii', 'ignore') for x in [rank, restaurant, price, address, phone, website, description]])

    print "Done Writing File."
