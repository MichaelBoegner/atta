from flask import render_template
import pprint
import psycopg2

def start_db_connection():
    conn_string = "host='localhost' dbname='test' user='michaelboegner' password=''"
    print("Connecting to database\n	->%s %", conn_string)
    conn = psycopg2.connect(conn_string)
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