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

response = r.get("https://finance.yahoo.com/quote/AMC/")
response2 = r.get("https://finance.yahoo.com/quote/AMD/")

soup1 = BeautifulSoup(response.text, "html.parser")
string1 = soup1.find("div", class_="D(ib) Mend(20px)")
string1 = string1.find("span", class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")
string1 = string1.text



soup2 = BeautifulSoup(response2.text, "html.parser")
string2 = soup2.find("div", class_="D(ib) Mend(20px)")
string2 = string2.find("span", class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")
string2 = string2.text

popUp = Tk()
tkinter.messagebox.showinfo("Stocks", "AMC stock prices now: " + str(string1) + "\nAmd stocks now: " + str(string2))

popUp.mainloop()





