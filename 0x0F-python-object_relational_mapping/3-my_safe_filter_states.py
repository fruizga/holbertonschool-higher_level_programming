#!/usr/bin/python3
"""safe filter states"""
import MySQLdb
import sys


if __name__ == '__main__':

    d_b = MySQLdb.connect(host="localhost\
    ", port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    cur = d_b.cursor()
    cur.execute("SELECT * from states WHERE name = %s ORDER BY id ASC",
                (argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    d_b.close()
