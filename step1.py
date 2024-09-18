from utils import getNumOfLines, cnct, clear
import time


def do(fh2, screen):
    conn, cur = cnct()

    cur.execute("""SELECT * FROM movies ORDER BY id DESC LIMIT 1""")
    row = cur.fetchone()

    if row is None:
        name = 0
    else:
        name = row[0]

    times = None
    commits = 0

    lastlinenum = getNumOfLines("title.tsv")
    if screen:
        print(
            "This process can take a loooot of time. Think that there're",
            lastlinenum,
            "films at the Dataset.",
        )

    reallinenum = 0
    tcommits = 0
    for line in fh2:
        if reallinenum == 0:
            reallinenum = 1
            continue

        splittedline = line.split()
        titleid = splittedline[0]
        if int(str(titleid).strip("tt")) <= int(str(name).strip("tt")):
            reallinenum += 1
            continue
        reallinenum += 1
        if times is None:
            if screen:
                print("Program resumed from line:", titleid, "line count:", reallinenum)
            times = 0
        # get country correctly:

        csplittedline = line.split("\t")
        try:
            country = csplittedline[3]
        except IndexError:
            if screen:
                print("IndexError: with line", line.split("\t"), line)
            exit(1)
        times = times + 1
        cur.execute(
            """INSERT OR IGNORE INTO movies (id, country, rating) VALUES ( ?, ?, 0 )""",
            (titleid, country),
        )
        if times >= 1000:
            times = 0
            conn.commit()
            commits = commits + 1
            if screen and commits >= 10:
                tcommits += 10

                clear()
                print("Nº of commits done so far:", tcommits, "(1k queries/commit)")
                print("Last line commited:", titleid)
                print("Real count of line:", reallinenum)
                print(
                    str(100 * float(str(reallinenum)) / float(str(lastlinenum))) + "%"
                )
                commits = 0
            time.sleep(0.01)

    if screen:
        clear()
        print("")
        print("Finished Step 1! Finished at", time.ctime(time.time()))
    time.sleep(0.5)
    conn.commit()
