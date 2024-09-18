import os
import sqlite3


def cnct():
    conn = sqlite3.connect('movies.sqlite')
    return (conn, conn.cursor())


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


# clear screen function
def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

