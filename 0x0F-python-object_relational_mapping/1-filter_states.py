#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    my_db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = my_db.cursor()
    cur.execute("""SELECT * FROM states WHERE name
                LIKE BINARY 'A%' ORDER BY states.id""")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    my_db.close()
