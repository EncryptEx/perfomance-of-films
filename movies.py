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


def getNumOfLines(filename):
    # get last line of a file file
    with open(filename, 'rb') as f:
        f.seek(-2, os.SEEK_END)
        while f.read(1) != b'\n':
            f.seek(-2, os.SEEK_CUR)
        last_line = f.readline().decode().split()[0].strip()
        lastlinenum = 0
        print("Getting last line of", filename)

    f = open(filename, encoding="utf8")
    for line in f:
        # count till find the last line
        if(not line.startswith(last_line)):
            lastlinenum += 1
            continue
    print("File", filename, "has", lastlinenum, "lines")
    return lastlinenum


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


def nanswer():
    print("Answer not correct")
    quit()

# -----------
# Only modify this on debbugging :)
# Recomendable to set all to false/no


skip1 = input("Skip Step 1? (Y/N)")
if skip1.lower() in ['y', 'n']:
    if skip1 == "Y" or skip1 == "y":
        skip1 = True
    else:
        skip1 = False
else:
    nanswer()
skip2 = input("Skip Step 2? (Y/N)")
if skip2.lower() in ['y', 'n']:
    if skip2.lower() == 'y':
        skip2 = True
    else:
        skip2 = False
else:
    nanswer()
skip3 = input("Skip Step 3? (Y/N)")
if skip3.lower() in ['y', 'n']:
    if skip3.lower() == 'y':
        skip3 = True
    else:
        skip3 = False
else:
    nanswer()
skip4 = input("Skip Step 4? (Y/N)")
if skip4.lower() in ['y', 'n']:
    if skip4.lower() == 'y':
        skip4 = True
    else:
        skip4 = False
else:
    nanswer()
# -----------
if skip1:
    print("Skipped Step 1")
else:
    lastlinenum = getNumOfLines("title.tsv")
    print("This process can take a loooot of time. Think that there're", lastlinenum, "films at the Dataset.")

    reallinenum = 0
    tcommits = 0
    for line in fh2:
        if(reallinenum == 0):
            reallinenum = 1
            continue

        splittedline = line.split()
        titleid = splittedline[0]
        if (int(str(titleid).strip("tt")) <= int(str(name).strip("tt"))):
            reallinenum += 1
            continue
        if (times is None):
            print("Program resumed from line:", titleid, "line count:", reallinenum)
            times = 0
        # get country correctly:

        a = list()
        for element in line.split("  "):
            element = element.strip()
            if(element != '' and len(element) < 3):
                a.append(element)
        country = a[1]
        # country = line.split("       ")[0].split("\t")[3]
        times = times + 1
        cur.execute('''INSERT OR IGNORE INTO movies (id, country, rating) VALUES ( ?, ?, 0 )''', (titleid, country))
        if times >= 1000:
            times = 0
            conn.commit()
            commits = commits + 1
            if commits >= 10:
                tcommits += 10
                clear()
                print("Nº of commits done so far:", tcommits, "each one includes 10k lines")
                print("Last line commited:", titleid)
                print("Real count of line:", reallinenum)
                print(str(100 * float(str(reallinenum)) / float(str(lastlinenum))) + "%")
                commits = 0
            time.sleep(0.5)
    clear()
    # os.system("pause")
    time.sleep(0.5)
    print("")
    print("Finished Step 1! Finished at", time.ctime(time.time()))
    conn.commit()
if skip2:
    print("Skipped Step 2")

else:
    lastlinenumratings = getNumOfLines("ratings.tsv")
    print("This process can take a while. There will be like ", lastlinenumratings, " Films to scan.")
    times = reallinenum = commits = tcommits = 0
    for line in fh1:
        if (reallinenum == 0):
            reallinenum += 1
            continue
        reallinenum += 1
        times += 1
        splittedline = line.split()
        titleid = splittedline[0]
        rating = splittedline[1]
        cur.execute('''UPDATE movies SET rating =? WHERE id=?''', (rating, titleid))
        if times >= 1000:
            times = 0
            conn.commit()
            commits += 1
            tcommits += 1
            if commits >= 100:
                print("Nº of commits done so far:", tcommits, "each one includes 100k lines")
                print("Last line commited:", titleid)
                print("Real count of line:", reallinenum)
                print(str(100 * float(str(reallinenum)) / float(str(lastlinenumratings))) + "%")
                commits = 0
            time.sleep(0.5)
if skip3:
    print("Skipped Step 3")
else:
    print("Fast proccess, it only deletes the films without a rating.")
    cur.execute('''DELETE FROM movies WHERE rating = "\\N"''')
    conn.commit()
if skip4:
    print("Skipped Step 4")
else:
    print('''Finally, it calculates the country film average and it displays it.
    Also it saves on a file called: results.txt''')
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
    final = {k: v for k, v in sorted(final.items(), key=lambda item: item[1])}

    for country, rating in final.items():
        # if country in ["/", "", "\\N",]:
        #    continue
        toprint = "Country:", country, "Average:", final[country]
        print(toprint)
        f.write(str(toprint) + "\n")
    print("__________________")
    f.write("\n__________________\n")
    f.close()
