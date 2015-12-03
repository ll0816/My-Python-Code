# -*- coding: utf-8 -*-
# Get Geocode from Google map
# Liu Li
# 3 Dec, 2015
# Code Source: http//www.gregreda.com/2013/04/29/more-web-scraping-with-python/
# Source: http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-Chicago/

from urllib2 import urlopen
import csv
import json

def geocode(address):
    url = ("http://maps.googleapis.com/maps/api/geocode/json?"
        "sensor=false&address={0}".format(address.replace(" ", "+")))
    return json.loads(urlopen(url).read())

with open("data/best-sandwiches.tsv", "r") as f:
    reader = csv.DictReader(f, delimiter="\t")

    with open("data/best-sandwiches-geocode.tsv", "w") as w:
        fields = ["rank", "restaurant", "price", "address", "phone", "website", "description", "formatted_address", "lat", "lng"]
        writer = csv.DictWriter(w, fieldnames=fields, delimiter="\t")
        writer.writeheader()

        for line in reader:
            print "Geocoding: {0}".format(line["address"])
            response = geocode(line["address"])
            if response["status"] == u"OK":
                results = response.get("results")[0]
                line["formatted_address"] = results["formatted_address"]
                line["lat"] = results["geometry"]["location"]["lat"]
                line["lng"] = results["geometry"]["location"]["lng"]
            else:
                line["formatted_address"] = ""
                line["lat"] = ""
                line["lng"] = ""
            writer.writerow(line)

print "Done writing file"