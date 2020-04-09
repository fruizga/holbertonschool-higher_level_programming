#!/usr/bin/python3
"""states with a name starting with N"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, charset="utf8\
    ", user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    List = cur.fetchall()
    for i in List:
        if i[1][0] == 'N':
            print(i)
    cur.close()
    db.close()
