import sqlite3
conn = sqlite3.connect('movies.sqlite')
cur = conn.cursor()
import time
from os import system, name 
import re
import eel
# Coded by EncryptEx - github.com/EsncryptEx
cur.execute('''CREATE TABLE IF NOT EXISTS "movies" ("id" TEXT NOT NULL,"country" TEXT, "rating" TEXT, UNIQUE('id'))''')

cur.execute('''SELECT * FROM movies ORDER BY id DESC LIMIT 1''')
row = cur.fetchone()
name = row[0]

eel.init('web')
skip1 = True
skip2 = True
skip3 = True
skip4 = True



@eel.expose
def setsteps(a,b,c,d):
    print("I got a parameter: ", a, b,c,d)
    global skip1, skip2, skip3, skip4
    skip1 = a
    skip2 = b
    skip3 = c 
    skip4 = d

system("cls")
print("\n")
print("███████╗██╗██╗     ███╗   ███╗ █╗ ███████╗")
print("██╔════╝██║██║     ████╗ ████║ █║ ██╔════╝")
print("█████╗  ██║██║     ██╔████╔██║ ╚╝ ███████╗")
print("██╔══╝  ██║██║     ██║╚██╔╝██║    ╚════██║")
print("██║     ██║███████╗██║ ╚═╝ ██║    ███████║")
print("╚═╝     ╚═╝╚══════╝╚═╝     ╚═╝    ╚══════╝")
print("                                                                                                  ")
print("██████╗ ███████╗██████╗ ███████╗ ██████╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗ ██████╗███████╗    ")
print("██╔══██╗██╔════╝██╔══██╗██╔════╝██╔═══██╗██╔══██╗████╗ ████║██╔══██╗████╗  ██║██╔════╝██╔════╝    ")
print("██████╔╝█████╗  ██████╔╝█████╗  ██║   ██║██████╔╝██╔████╔██║███████║██╔██╗ ██║██║     █████╗      ")
print("██╔═══╝ ██╔══╝  ██╔══██╗██╔══╝  ██║   ██║██╔══██╗██║╚██╔╝██║██╔══██║██║╚██╗██║██║     ██╔══╝      ")
print("██║     ███████╗██║  ██║██║     ╚██████╔╝██║  ██║██║ ╚═╝ ██║██║  ██║██║ ╚████║╚██████╗███████╗    ")
print("╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝      ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝╚══════╝    ")
                                                                                                  
print("\n")
try:
    fh1 = open("ratings.tsv", encoding="utf8")
except: 
    print("Couldn't find ratings.tsv")
    quit()
try:
    fh2 = open("title.tsv", encoding="utf8")
except:
    print("Couldn't find title.tsv")
    quit()

f = open("results.txt", "w+")
print("Today is", time.ctime(time.time()) + ", a good day to scan datasets. :)")
towrite = " -- FILM's AVERAGE PER COUNTRY -- " + time.ctime(time.time())
f.write(towrite)
f.close()

times = None
commits = 0
#-----------
#Only modify this on debbugging :)
#Recomendable to set all to false
# skip1 = input("Skip Step 1? (Y/N)")
# if skip1 == "Y" or skip1 == "N" or skip1 == "y" or skip1 == "n": 
#     if skip1 == "Y" or skip1 == "y":
#         skip1 = True
#     else:
#         skip1 = False
# else:
#     print("Answer not correct") 
#     quit()
# skip2 = input("Skip Step 2? (Y/N)")
# if skip2 == "Y" or skip2 == "N" or skip2 == "y" or skip2 == "n": 
#     if skip2 == "Y" or skip2 == "y":
#         skip2 = True
#     else:
#         skip2 = False
# else:
#     print("Answer not correct") 
#     quit()
# skip3 = input("Skip Step 3? (Y/N)")
# if skip3 == "Y" or skip3 == "N" or skip3 == "y" or skip3 == "n": 
#     if skip3 == "Y" or skip3 == "y":
#         skip3 = True
#     else:
#         skip3 = False
# else:
#     print("Answer not correct") 
#     quit()
# skip4 = input("Skip Step 4? (Y/N)")
# if skip4 == "Y" or skip4 == "N" or skip4 == "y" or skip4 == "n": 
#     if skip4 == "Y" or skip4 == "y":
#         skip4 = True
#     else:
#         skip4 = False
# else:
#     print("Answer not correct") 
#     quit()
#-----------
if skip1:
    print("Skipped Step 1")
else:
    print("This process can take a loooot of time. Think that there're 10 Million films at the Dataset.")
    for line in fh2:       
        splittedline = line.split()
        titleid = splittedline[0]
        if (titleid <= name):
            continue
        if (times == None):
            print("Program resumed from line:", titleid)
            times = 0
        times = times + 1
        precountry = re.findall("\s[A-Z]+\s", line[18:])
        if (len(precountry) == 0):
            country = "none"
        else:
            if (len(precountry) > 1):
                country = str(precountry[0])
                country = country[4:6]
            else: 
                country = str(precountry)
                country = country[4:6]
                cur.execute('''INSERT OR IGNORE INTO movies (id, country, rating) VALUES ( ?, ?, 0 )''', ( titleid, country ))
        if times >= 2000:
            times = 0
            conn.commit()
            commits = commits + 1
            if commits >= 2000:
                print("Refreshed DB 2000 times.")
            time.sleep(0.5)
    system("cls")
    system("pause")
    print("Finished Step 1!")
if skip2:
    print("Skipped Step 2")
else: 
    print("This process can take a while. There will be like 4 Million Films to scan.")
    times = 0
    commits = 0
    for line in fh1:
        times = times + 1
        splittedline = line.split()
        titleid = splittedline[0]
        rating = splittedline[1]
        cur.execute('''UPDATE movies SET rating =? WHERE id=?''', ( rating, titleid ))
        if times >= 1000:
            times = 0
            conn.commit()
            commits = commits + 1
            if commits >= 1000:
                print("Refreshed DB 1000 times.")
            time.sleep(0.5)
if skip3:
    print("Skipped Step 3")
else:
    print("Fast proccess, it only deletes the films without a rating.")
    cur.execute('''DELETE FROM movies WHERE rating = "N"''')
    conn.commit()
if skip4:
    print("Skipped Step 4")
else:
    print("Finally, it calculates the country film average and it displays it. Also it saves on a file called: results.txt")
    cur.execute('''SELECT * FROM movies''')
    movies = list()
    for row in cur:
        movies.append((str(row[1]), str(row[2])))
    average = dict()
    timescountry = dict()
    final = dict()
    for country, rating in movies:
        average[country] = average.get(country, float(rating)) + float(rating)
        timescountry[country] = timescountry.get(country, 1) + 1
    for country, rating in movies:
        final[country] = float(average[country]) / float(timescountry[country])
    print("__________________")
    f = open("results.txt", "a")
    f.write("\n__________________\n")
    for country, rating in final.items(): 
        if country[0] == "/" or country[0] == " " or country[0] == "'" or country[0] == "\\":
            continue
        if country[1] == "/" or country[1] == " " or country[1] == "'" or country[1] == "\\":
            continue
        toprint = "Country:", country, "Average:", final[country]
        print(toprint)
        f.write(str(toprint) + "\n")
    print("__________________")
    f.write("\n__________________\n")
    f.close()
eel.start('index.html', size=(1000, 600))