#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    my_db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                            passwd=sys.argv[2], db=sys.argv[3], port=3306)
    my_cursor = my_db.cursor()
    my_cursor.execute("""SELECT cities.name FROM
                      cities INNER JOIN states ON states.id=cities.state_id
                      WHERE states.name=%s""", (sys.argv[4],))
    my_rows = my_cursor.fetchall()
    my_temp = list(row[0] for row in my_rows)
    print(*my_temp, sep=", ")
    my_cursor.close()
    my_db.close()
