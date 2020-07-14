# Standard library of SQLITE
import sqlite3

# Function to create database


def connect():
    try:
        conn = sqlite3.connect("Store.db")  # Name of the db file
        cur = conn.cursor()  # Create cursor object
        cur.execute(        # Execute SQL Query
            """CREATE TABLE IF NOT EXISTS store (
                name TEXT, quantity INTEGER, price REAL
            )""" # Create table with 3 columns
        )  
        conn.commit()  # Save the changes
        conn.close()  # Close connection
        print("Database created.")
    except:
        print("Failed to create database.")

def insert(name, quantity, price):
    try:
        conn = sqlite3.connect("Store.db")
        cur = conn.cursor()
        cur.execute( # Execute SQL Query
            """INSERT INTO store VALUES (?,?,?)""", (name, quantity, price) # Insert rows into table
        )
        conn.commit()
        conn.close()
        print("Succesfull inserted row.")
    except:
        print("Failed to insert row.")

def view():
    try:
        conn = sqlite3.connect("Store.db")
        cur = conn.cursor()
        cur.execute(
            """SELECT * FROM store"""
        )
        rows = cur.fetchall()
        conn.commit()
        conn.close()
        return rows # View data
    except:
        print("Failed to return the rows.")

def delete_data():
    try:
        conn = sqlite3.connect("Store.db")
        cur = conn.cursor()
        cur.execute(
            """DELETE FROM store"""
        )
        conn.commit()
        conn.close()
        print("Deleted.")
    except:
        print("Failed to delete.")

def delete_row(name="", quantity="", price=""):
    try:
        conn = sqlite3.connect("Store.db")
        cur = conn.cursor()
        cur.execute(
            """DELETE FROM store WHERE name=? OR quantity=? OR price=?""",(
                name, quantity, price # delete row
            )
        )
        conn.commit()
        conn.close()
        print("Deleted row.")
    except:
        print("Failed to delete the row")