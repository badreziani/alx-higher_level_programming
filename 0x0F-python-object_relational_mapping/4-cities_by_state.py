#!/usr/bin/python3
"""4-cities_by_state module

lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3])

    cur = db.cursor()

    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    LEFT JOIN states
    ON cities.state_id = states.id
    ORDER BY cities.id
    """
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
