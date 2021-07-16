import math as m
from bs4 import BeautifulSoup
import random as rand
import requests as r
from http import HTTPStatus
import time as t
import os
import json
import PyQt5 as py


response = r.get("https://www.worldometers.info/coronavirus/")
coronovirusWorldWide = response.text

response = r.get("https://www.worldometers.info/coronavirus/country/canada/")
canadaCoronovirus = response.text
#
# with open("test.html", "w", encoding="utf-8") as file:
#     file.write(response.html)
#
# with open("test.html", "r", encoding="utf-8") as file:
#     soup = BeautifulSoup(file, "html.parser")
#     testString = soup.find("div", class_="maincounter-number")
#     testString = testString.text
#     print(soup.find("div", class_="maincounter-number"))
#     print("Coronovirus infected WorldWide" + testString)

#Testing if coronovirus stats shown worldwide
beautify = BeautifulSoup(coronovirusWorldWide, "html.parser")
testString = beautify.find("div", class_="maincounter-number")
testString = testString.text
print("Coronovirus infected WorldWide" + testString)

#testing if canada stats are shown
beautify = BeautifulSoup(canadaCoronovirus, "html.parser")
testString = beautify.find("div", class_="maincounter-number")
testString = testString.text
print("Canada wide infected Coronovirus" + testString)
