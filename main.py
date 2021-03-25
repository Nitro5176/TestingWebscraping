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

def menu():
    """
    Description:
    creates a menu for the user to go through
    :return: none
    """
    print()
    print("Please Select the following options:")
    print("1) name of website to go through.")
    print("2) name of file you wish to name it.")
    print("3) Printing the file")
    print("4: deleting a file")
    print("Please write 10 if you wish to end the program")


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



def traffic_for_main(input):
    """
    Description:
    Everything will be done in this function to reduce the main function
    :param input: the user inputs the value
    :return: only returns false if user wants to quit the program
    """

    input_string = int(input)

    if input_string == 1:
        print("Please enter website you want to get information from: ")
        input_user = input()
        input_website = requesting_website(input_user)
        print("Please enter where to place the html file: ")
        input_user = input()
        add_html_to_file(input_user, input_website)
        return True
    #not done
    elif input_string == 2:
        print("Please enter the name of the file you want to make: ")
        input_user = input()
        make_check_file(input_user)
        return True

    elif input_string == 3:
        print("Please enter the file you want to print out")
        input_user = input()
        print("Printing the file...")
        t.sleep(5)
        print_file(input_user)
        return True

    elif input_string == 4:
        print("Please enter the file you want to delete")
        input_user = input()
        flag = delete_file(input_user)
        print("Deleting..." + input_user)
        t.sleep(5)
        if flag:
            print("Deletion is successful")
        else:
            print("Deletion is unsuccessful")
        return True

    elif input_string == 10:
        print("Exiting program...")
        t.sleep(3)
        return False



def main():
    """
    Description:
    the job of this function is to make request calls and web scrape through a
    webpage on html
    :return: none
    """
    flag = True

    while flag:
        menu()
        #will needed to come back and check if its a number or not
        user = input()
        traffic = traffic_for_main(user)
        if traffic == False:
            flag = False
        t.sleep(5)


# user_input = input()
# website = requesting_website(user_input)
# print("name of file")
# file_name = input()
# make_check_file(file_name)
# add_html_to_file(file_name, website)
# create_beaut_request(file_name)
#
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
