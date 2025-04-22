from bs4 import BeautifulSoup
import requests
import sys
from spire.pdf import *
#https://www.ratemyprofessors.com/search/professors/18846?q=*
#https://www.ratemyprofessors.com/ShowRatings.jsp?tid=[Professor ID]

teacher = open("Teachers.txt")
teacherInfo = {}
for line in teacher:
    temp = line.split(" ")
    teacherInfo[temp[0].upper().strip()] = temp[1].strip()

#print(teacherInfo["STEVEGOLD"])
#givenTeacher = input("Enter Professor First and Last Name: ").replace(" ", "").upper()
def modifyComment(comment):
    a = ""
    for i in range(0, len(comment), 80):
        a += comment[i:i+80] + "\n"
    return a

def scrapeData(givenTeacher):

    url = teacherInfo[givenTeacher]
    print(f"Link: {url}")
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    response = requests.get(url, headers=headers)

    file = open("response.txt", "w")

    file.write(response.text)

    file.close()

    file = open("output.txt", "w")

    def count_tags(a):
        d = {}
        for x in range(len(a)):
            temp = a[x]
            counter = 0
            for y in range(len(a)):
                if (a[x] == a[y]):
                    counter+=1
            d[a[x]] = counter
        return d

    filehandle = open("response.txt")
    soup = BeautifulSoup(filehandle, 'html.parser')

    time = 2025

    proftags = soup.find_all("span", {"class": "Tag-bs9vf4-0 bmtbjB"})
    temp = []
    for mytag in proftags:
        temp.append(mytag.get_text())

    tags = count_tags(temp)

    rating = soup.find("div", {"class": "RatingValue__Numerator-qw8sqy-2 duhvlP"})
 
    wta = soup.find_all("div", {"class": "FeedbackItem__FeedbackNumber-uof32n-1 ecFgca"})

    comments = soup.find_all("div", {"class": "Comments__StyledComments-dzzyvm-0 jpfwLX"})

    quality = soup.find_all("div", {"class": "CardNumRating__CardNumRatingNumber-sc-17t4b9u-2"})

    timestamp = soup.find_all("div", {"class": "TimeStamp__StyledTimeStamp-sc-9q2r30-0 czvMwn RatingHeader__RatingTimeStamp-sc-1dlkqw1-4 hjIitS"})
    iteration = 2 * len(comments)
    relative = True
    if (len(comments) < 3):
        relative = False


    year = []
    for x in range(len(timestamp)):
        if (relative):
            if (int(timestamp[x].get_text()[9::]) == time or int(timestamp[x].get_text()[9::]) >= time - 2):
                year.append(timestamp[x].get_text())
        else:
            year.append(timestamp[x].get_text())
    
    if (relative):
        iteration = len(year)


    file.write(soup.title.string)
    file.write(f"\nRating: {rating.get_text()}\n")
    file.write(f"Would Take Again: {wta[0].get_text()}\n")
    file.write(f"Difficulty: {wta[1].get_text()}\n")

    file.write(f"\nTags: \n")
    for key, values in tags.items():
        file.write(f"{key}: {values}\n")

    commentfile = open("Comments.txt", "w")

    commentfile.write("Most Recent Comments:\n")
    for x in range(0,iteration,2):
        commentfile.write(f"{(x//2)+1}. Rating: {quality[x].get_text()} Difficulty: {quality[x+1].get_text()} Time: {year[x]}\n{comments[x//2].get_text()}\n\n")
    



    #CardNumRating__CardNumRatingNumber-sc-17t4b9u-2 gcFhmN
    #CardNumRating__CardNumRatingNumber-sc-17t4b9u-2 bUneqk

givenTeacher = str(sys.argv[1]).replace(" ", "").upper()
scrapeData(givenTeacher)
#print(modifyComment("Solid professor, learned a lot. I highly recommend using a second device when taking his quizzes, he won't hesitate to summon you to office hours if he catches you switching tabs. Him and his TA's actively check the canvas log files to catch cheaters on his canvas quizzes."))

