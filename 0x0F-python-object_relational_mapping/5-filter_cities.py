#!/usr/bin/python3
"""
    list all cities in a state'
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
    SELECT city.name
    FROM cities city
    LEFT JOIN states state
    ON city.state_id = state.id
    WHERE state.name = %s
    ORDER BY city.id ASC
    """, (argv[4],))
    print(", ".join([x[0] for x in cur.fetchall()]))
    cur.close()
    conn.close()
