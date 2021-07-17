import math as m
from bs4 import BeautifulSoup
import random as rand
import requests as r
from http import HTTPStatus
import time as t
import os
import json
from tkinter import *
import tkinter.messagebox



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
#finding the next div with the class name, we didnt need to find twice because it only had one tag inside it
testString1 = beautify.find("div", class_="maincounter-number")
testString1 = testString1.text
# print("Coronovirus infected WorldWide" + testString1)

#testing if canada stats are shown
beautify = BeautifulSoup(canadaCoronovirus, "html.parser")
testString2 = beautify.find("div", class_="maincounter-number")
testString2 = testString2.text
# print("Canada wide infected Coronovirus" + testString2)

popUp = Tk()
tkinter.messagebox.showinfo("Coronovirus Stats", "Worldwide Coronovirus Stats: " + testString1 + "\nCanada Coronovirus Stats: " + testString2)

popUp.mainLoop()