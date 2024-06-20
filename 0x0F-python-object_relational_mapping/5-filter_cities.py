#!/usr/bin/python3
"""5-filter_cities module

takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa
"""

import MySQLdb
import sys

db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3])

cur = db.cursor()

query = """
    SELECT cities.name
    FROM cities
    LEFT JOIN states
    ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id
    """
cur.execute(query, (sys.argv[4],))
rows = cur.fetchall()
for idx, row in enumerate(rows):
    if idx != len(rows) - 1:
        print(f'{row[0]}, ', end='')
    else:
        print(row[0], end='')
print()
cur.close();
db.close();
