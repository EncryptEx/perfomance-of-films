import time
import os
import sqlite3
conn = sqlite3.connect('movies.sqlite')
cur = conn.cursor()


# clear screen function
def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


# get last line of file title.tsv
with open('title.tsv', 'rb') as f:
    f.seek(-2, os.SEEK_END)
    while f.read(1) != b'\n':
        f.seek(-2, os.SEEK_CUR)
    last_line = f.readline().decode().split()[0][2:].strip()


# Coded by EncryptEx - github.com/EncryptEx
cur.execute('''CREATE TABLE IF NOT EXISTS "movies" ("id" TEXT NOT NULL,"country" TEXT, "rating" TEXT, UNIQUE('id'))''')

clear()
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
except FileNotFoundError:
    print("Couldn't find ratings.tsv")
    quit()
try:
    fh2 = open("title.tsv", encoding="utf8")
except FileNotFoundError:
    print("Couldn't find title.tsv")
    quit()

f = open("results.txt", "w+")
print("Today is", time.ctime(time.time()) + ", a good day to scan datasets. :)")
towrite = " -- FILM's AVERAGE PER COUNTRY -- " + time.ctime(time.time())
f.write(towrite)
f.close()

cur.execute('''SELECT * FROM movies ORDER BY id DESC LIMIT 1''')
row = cur.fetchone()
if(row is None):
    name = 0
else:
    name = row[0]

times = None
commits = 0
# -----------
# Only modify this on debbugging :)
# Recomendable to set all to false
skip1 = input("Skip Step 1? (Y/N)")
if skip1.lower() in ['y', 'n']:
    if skip1 == "Y" or skip1 == "y":
        skip1 = True
    else:
        skip1 = False
else:
    print("Answer not correct")
    quit()
skip2 = input("Skip Step 2? (Y/N)")
if skip2.lower() in ['y', 'n']:
    if skip2.lower() == 'y':
        skip2 = True
    else:
        skip2 = False
else:
    print("Answer not correct")
    quit()
skip3 = input("Skip Step 3? (Y/N)")
if skip3.lower() in ['y', 'n']:
    if skip3.lower() == 'y':
        skip3 = True
    else:
        skip3 = False
else:
    print("Answer not correct")
    quit()
skip4 = input("Skip Step 4? (Y/N)")
if skip4.lower() in ['y', 'n']:
    if skip4.lower() == 'y':
        skip4 = True
    else:
        skip4 = False
else:
    print("Answer not correct")
    quit()
# -----------
if skip1:
    print("Skipped Step 1")
else:
    print("This process can take a loooot of time. Think that there're 10 Million films at the Dataset.")

    isfirstline = True
    for line in fh2:
        if(isfirstline):
            isfirstline = False
            continue

        splittedline = line.split()
        titleid = splittedline[0]
        if (int(str(titleid).strip("tt")) <= int(str(name).strip("tt"))):
            continue
        if (times is None):
            print("Program resumed from line:", titleid)
            times = 0
        country = line.split("       ")[0].split("\t")[4]
        times = times + 1
        cur.execute('''INSERT OR IGNORE INTO movies (id, country, rating) VALUES ( ?, ?, 0 )''', ( titleid, country ))
        if times >= 1000:
            times = 0
            conn.commit()
            commits = commits + 1
            if commits >= 10:
                clear()
                print("Nº of commits done so far:", commits, "each one includes 10k lines")
                print("Last line commited:", titleid)
                print(str(100 * float(str(titleid)[2:]) / float(str(last_line))) + "%")
                commits = 0
            time.sleep(0.5)
    clear()
    os.system("pause")
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