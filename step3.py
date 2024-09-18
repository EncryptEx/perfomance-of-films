from utils import cnct


def do():
    conn, cur = cnct()
    print("Fast proccess, it only deletes the films without a rating.")
    cur.execute('''DELETE FROM movies WHERE rating = "\\N"''')
    conn.commit()
