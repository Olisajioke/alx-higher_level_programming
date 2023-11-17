#!/usr/bin/python3
"""module that lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    my_db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                            passwd=sys.argv[2], port=3306, db=sys.argv[3])
    my_cursor = my_db.cursor()
    my_cursor.execute("SELECT * FROM states")
    my_rows = my_cursor.fetchall()
    for row in my_rows:
        print(row)
    my_cursor.close()
    my_db.close()
