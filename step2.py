from utils import getNumOfLines, cnct


def do(fh1): 
    conn, cur = cnct()
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
                print("Nº of commits done so far:", tcommits, "(1k queries/commit)")
                print("Last line commited:", titleid)
                print("Real count of line:", reallinenum)
                print(str(100 * float(str(reallinenum)) / float(str(lastlinenumratings))) + "%")
                commits = 0
            time.sleep(0.01)