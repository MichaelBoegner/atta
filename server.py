from flask import Flask, request, make_response
import psycopg2
import sys
import pprint

id = 0
def insert_data(to_database, id):
    conn_string = "host='localhost' dbname='test' user='michaelboegner' password=''"
	# print the connection string we will use to connect
    print("Connecting to database\n	->%s %", conn_string)

	# get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)

	# conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()
    print("Connected!\n")
    cursor.execute("CREATE TABLE wins (id int, message varchar(240));")

    id += 1
    cursor.execute(f"INSERT INTO wins VALUES ({id},'{to_database}');")
    cursor.execute("SELECT * FROM wins")

    records = cursor.fetchall()
    pprint.pprint(records)

#initiate Flask and receive calls
app = Flask(__name__)

@app.route('/', methods=['POST'])
def event_watcher():
    print("RECEIVED EVENT. REQUEST:",request.json['token'], "END RECEIVED JSON DATA------------")
    token_to_database = request.json['token']
    insert_data(token_to_database, id)
    
    if request.json.get('challenge'):
        resp = request.json.get('challenge')
    else: 
        resp = "great!"
    return resp

