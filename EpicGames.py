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
        #since the page only has 40 games per page, we want to stop at the 40th page
        count += 1
        try:
            # getting the values of the games
            tempAnchor = i.find("a")
            #look for the div with the matching class to get the values
            discounted = i.find("div", class_="css-b0xoos")
            discountedPrice = i.find("span", class_="css-z3vg5b")
            actualPrice = i.find("div", class_="css-1rcj98u")
            #split the aria-label to a string splitting them by comma's ","
            tempTitle = tempAnchor["aria-label"].split(",")
            linkOfDiscounted = "https://www.epicgames.com" + tempAnchor["href"]
            pictureLink = i.find("img")
        except:
            print("error")
        #checks if the game  discounted
        if discounted is not None:
            discountedGames = {
                "title": tempTitle[0],
                "discountedPrice": discountedPrice.text,
                "actualPrice": actualPrice.text,
                "discounted": discounted.text,
                "linkOfDiscounted": linkOfDiscounted,
                "pictureLink": pictureLink["data-image"]
            }
            #make a list of games that are discounted
            listOfDiscountedGames.append(discountedGames)
        #if the loop reaches 40 games in that page, exit.
        if count == 40:
            break
    #return a list of games
    return listOfDiscountedGames

#http request to a page
response = r.get("https://www.epicgames.com/store/en-US/browse?sortBy=releaseDate&sortDir=DESC&count=40")
#count, is for string to add the next page after the first response
count = 0
#next page in epic games
counted = 40
#all listed games are added
discountedGames = []
#flag to end the loop
flag = True
while flag:
    string = "https://www.epicgames.com/store/en-US/browse?sortBy=releaseDate&sortDir=DESC&count=40"
    string1 = ""
    #on the first request we only want 40 games
    if count == 0:
        response = r.get(string)
    #if the first page is counted already, we go to the next page
    elif count > 0:
        string1 = string + "&start=" + str(counted)
        response = r.get(string1)
    else:#testing purposes
        break
    #grab the games with the request
    discountedGamesCheck = gameCollect(response)
    #if no games are found in the page, exit
    if len(discountedGamesCheck) == 0:
        flag = False
    discountedGames.append(discountedGamesCheck)
    #goes to the next page
    count += 1
    counted += 40
    #sleep so i don't spam request the page
    t.sleep(5)

#open a file name gamesOnSale and append it to it (if not exist it creates)
f = open("gamesOnSale.txt", "a")
for i in discountedGames:
    for j in i:
        #printing the value of the dictionarry nested in the list
        f.write("Title of game: " + str(j["title"]) + "\n" +
                "Discounted by: " + str(j["discounted"]) + "\n" +
                "Actual price: " + str(j["actualPrice"]) + "\n" +
                "Discounted Price: " + str(j["discountedPrice"]) + "\n" +
                "Link to game in epic games: " + str(j["linkOfDiscounted"]) + "\n" +
                "Link to the image in epic games: " + str(j["pictureLink"]) + "\n" + "\n"
                )
        #testing purposes
        print("********************************************")
        print("Title of game: " + str(j["title"]))
        print("Discounted by: " + str(j["discounted"]))
        print("Actual price: " + str(j["actualPrice"]))
        print("Discounted Price: " + str(j["discountedPrice"]))
        print("Link to game in epic games: " + str(j["linkOfDiscounted"]))
        print("Link to the image in epic games: " + str(j["pictureLink"]))
        print("********************************************")
f.close()

