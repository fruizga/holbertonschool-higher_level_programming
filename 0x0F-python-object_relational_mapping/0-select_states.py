#!/usr/bin/python3
import MySQLdb
from sys import argv


if __name__ == '__main__':

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = mydb.cursor()
    cur.execute("SELECT * from states")
    states = cur.fetchall()
    for records in states:
        print(records)
    cur.close()
    db.close()
