#!/usr/bin/python3
""" Lists all states from the database hbtn_0e_0_usa """
import mysql.connector
import sys

if __name__ == "__main__":
    config = {
        "host": "localhost",
        "user": sys.argv[1],
        "password": sys.argv[2],
        "database": sys.argv[3],
        "port": 3306,
    }

    try:
        db = mysql.connector.connect(**config)
        cursor = db.cursor()
        query = "SELECT * FROM states"
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        cursor.close()
        db.close()
    except mysql.connector.Error as error:
        print("Error:", error)
