#!/usr/bin/python3
import MySQLdb
from sys import argv


if __name__ == '__main__':

    d_b = MySQLdb.connect(host="localhost\
    ", port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    cur = d_b.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name FROM states,
    cities WHERE states.id = cities.state_id ORDER BY cities.id ASC""")
    states = cur.fetchall()
    for records in states:
        print(records)
    cur.close()
    d_b.close()
