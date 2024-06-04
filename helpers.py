from flask import render_template
import pprint
import psycopg2

def start_db_connection():
    conn_string = "host='localhost' dbname='test' user='michaelboegner' password=''"
	# print the connection string we will use to connect
    print("Connecting to database\n	->%s %", conn_string)

	# get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)

	# conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()
    return cursor

def create_table_wins(cursor):
    print("creating table wins\n")
    cursor.execute("CREATE TABLE wins (id SERIAL, message varchar(240));")

def insert_data(to_database, cursor):
    cursor.execute(f"INSERT INTO wins (message) VALUES ('{to_database}');")
    cursor.execute("SELECT * FROM wins")

    data = cursor.fetchall()
    pprint.pprint(data)
    return data

def renderer(data):
    render_template('template.html', data=data)