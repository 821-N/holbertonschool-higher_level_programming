#!/usr/bin/python3
import MySQLdb
from sys import argv

conn = MySQLdb.connect(
    host="localhost",
    user=argv[1],
    passwd=argv[2],
    db=argv[3]
)
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")
for row in cur.fetchall():
    print(row)
cur.close()
conn.close()
