import requests as r
from bs4 import BeautifulSoup
import time as t

def gameCollect(response):
    # asking a response from the site to get the games

    # choosing the type to parse through the page
    soup = BeautifulSoup(response.text, "html.parser")

    # finds all the games under a list
    games = soup.find_all("li", class_="css-lrwy1y")
    # list of discounted games
    listOfDiscountedGames = []
    # iterating through the games
    count = 0;
    for i in games:
        count += 1
        try:
            # getting the values of the games
            tempAnchor = i.find("a")
            discounted = i.find("div", class_="css-b0xoos")
            discountedPrice = i.find("span", class_="css-z3vg5b")
            actualPrice = i.find("div", class_="css-1rcj98u")
            tempTitle = tempAnchor["aria-label"].split(",")
            linkOfDiscounted = "https://www.epicgames.com" + tempAnchor["href"]
            pictureLink = i.find("img")
        except:
            print("error")

        if discounted is not None:
            discountedGames = {
                "title": tempTitle[0],
                "discountedPrice": discountedPrice.text,
                "actualPrice": actualPrice.text,
                "discounted": discounted.text,
                "linkOfDiscounted": linkOfDiscounted,
                "pictureLink": pictureLink["data-image"]
            }
            listOfDiscountedGames.append(discountedGames)
        if count == 40:
            break
    return listOfDiscountedGames


response = r.get("https://www.epicgames.com/store/en-US/browse?sortBy=releaseDate&sortDir=DESC&count=40")
# responseError = r.get("https://www.epicgames.com/store/en-US/browse?sortBy=releaseDate&sortDir=DESC&count=40&start=920")
count = 0
counted = 40
discountedGames = []
flag = True
while flag:
    string = "https://www.epicgames.com/store/en-US/browse?sortBy=releaseDate&sortDir=DESC&count=40"
    string1 = ""
    if count == 0:
        response = r.get(string)
    elif count > 0:
        string1 = string + "&start=" + str(counted)
        response = r.get(string1)
    else:
        break

    discountedGamesCheck = gameCollect(response)

    if len(discountedGamesCheck) == 0:
        flag = False
    discountedGames.append(discountedGamesCheck)
    count += 1
    counted += 40
    t.sleep(5)

for i in discountedGames:
    for j in i:
        print("********************************************")
        print("Title of game: " + str(j["title"]))
        print("Discounted by: " + str(j["discounted"]))
        print("Actual price: " + str(j["actualPrice"]))
        print("Discounted Price: " + str(j["discountedPrice"]))
        print("Link to game in epic games: " + str(j["linkOfDiscounted"]))
        print("Link to the image in epic games: " + str(j["pictureLink"]))
        print("********************************************")

