import time
import os
import sys

import step1
import step2
import step3
import step4

import utils


def do(format, skips=[False, False, False, False], screen=True):
    conn, cur = utils.cnct()

    # Coded by EncryptEx - github.com/EncryptEx
    cur.execute(
        """CREATE TABLE IF NOT EXISTS "movies" ("id" TEXT NOT NULL,"country" TEXT, "rating" TEXT, UNIQUE('id'))"""
    )

    try:
        fh1 = open("ratings.tsv", encoding="utf8")
        fh2 = open("title.tsv", encoding="utf8")
    except FileNotFoundError:
        exit(127)

    f = open("results.txt", "w+")
    # print("Today is", time.ctime(time.time()) + ", a good day to scan datasets. :)")
    towrite = " -- FILM's AVERAGE PER COUNTRY -- " + time.ctime(time.time())
    f.write(towrite)
    f.close()

    if not skips[0]:
        step1.do(fh2, screen)
    if not skips[1]:
        step2.do(fh1)
    if not skips[2]:
        step3.do()
    if not skips[3]:
        step4.do(format, screen)


if __name__ == "__main__":
    # running this file
    skips = []
    skips[0] = sys.argv.find("--no-first")
    skips[1] = sys.argv.find("--no-second")
    skips[2] = sys.argv.find("--no-third")
    skips[3] = sys.argv.find("--no-fourth")
    index = sys.argv.find("-f")
    if index:
        format = sys.argv[index + 1]
    else:
        format = "json"
    do(format, skips, False)
