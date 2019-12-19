#!/usr/bin/python3
"""
    list all cities and their states
"""


import MySQLdb
from sys import argv


if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )
    cur = conn.cursor()
    cur.execute("""
    SELECT city.id, city.name, state.name
    FROM cities city
    LEFT JOIN states state
    ON city.state_id = state.id
    ORDER BY city.id ASC
    """)
    for row in cur.fetchall():
        print(row)
    cur.close()
    conn.close()
