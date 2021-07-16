import math as m
from bs4 import BeautifulSoup
import random as rand
import requests as r
from http import HTTPStatus
import tkinter as tk
import time as t
import os
import json



def make_check_file(name):
    """
    Description:
    checks the name if its a file or not, if so we would make that file
    and name it that.
    :param name: name of file
    :return: none
    """
    try:
        f = open(name, "r")
        print("File " + name + " exists.")
    except:
        f = open(name, "w")
        print("File " + name + " has been created.")

    f.close()

def add_html_to_file(name, html_file):
    """
    Description:
    will append the information of the html onto the text file.
    :param name: name of the file
    :param html_file: the html file
    :return: if it has been successful or not
    """
    make_check_file(name)
    try:
        #need to relook at the with function
        with open(name, "w", encoding="utf-8") as f:
            f.write(html_file)
        return True
    except Exception as e:
        print(e)
        return False


def delete_file(name):
    """
    Description:
    deletes the file given in the parameter name
    :param name: name of the file given
    :return: True if delete, False if it doesn't exist or didn't work
    """
    if os.path.exists(name):
        os.remove(name)
    else:
        print("File does not exist")

    pass

def print_file(file):
    """
    Description:
    prints the given file
    :param file: the file that has html
    :return: True or false depends if its successful
    """
    #need to review how this works i just know it needs to go throuh this when getting html
    try:
        with open(file, "r", encoding="utf-8") as f:
            print(f.read())
        return True
    except Exception as e:
        print(e)
        return False



def requesting_website(website_name):
    """
    Description:
    takes the request of the website and returns an html string for use.
    :param website_name: the name of the website starting with www
    :return: the html string, it is not successful it is false
    """
    response = r.get(website_name)

    if response.status_code == HTTPStatus.OK:
        html = response.text
        return html
    else:
        print("There is an error in requesting the website")
        return False


def create_beaut_request(html_file):
    """
    Description:
    Gets a beautiful soup response and returns the beautiful object
    :param html_file: the name of the html to beautiful soup in
    :return: beautiful soup object
    """
    file = open(html_file, "r")
    souped = BeautifulSoup(file, "html.parser")
    print(souped.title)



# user_input = input()
# website = requesting_website(user_input)
# print("name of file")
# file_name = input()
# make_check_file(file_name)
# add_html_to_file(file_name, website)
# create_beaut_request(file_name)

# print("do you want to delete a file?")
# input_user = input()
# input_user = input_user.lower().strip()
# print(input_user)
# if(input_user == "yes"):
#     print("name of the file:")
#     inputs = input()
#     delete_file(inputs)
# else:
#     print("exiting")

response = r.get("https://www.worldometers.info/coronavirus/")
# response = r.get("https://www.google.com/search?client=firefox-b-d&q=amc+stocks")
# response = r.get("https://www.google.com/search?client=firefox-b-d&q=amd+stocks")
# response = r.get("https://www.google.com/search?client=firefox-b-d&q=weather+gatineau")
html = response.content
beautify = BeautifulSoup(response.content, "html.parser")
testString = beautify.find("div", class_="maincounter-number")
testString = testString.text
print(beautify.find("div", class_="maincounter-number"))
print("Coronovirus infected" + testString)
make_check_file("test.html")
add_html_to_file("test.html", html)
print(response.encoding)
try:
    testing = json.loads(response.content)
except Exception as e:
    print(e)
# testing = response.json()
