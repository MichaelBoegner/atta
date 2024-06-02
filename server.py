from flask import Flask, request, render_template
import psycopg2
import pprint

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

#initiate Flask and receive calls
app = Flask(__name__)

def start_db_connection():
    conn_string = "host='localhost' dbname='test' user='michaelboegner' password=''"
	# print the connection string we will use to connect
    print("Connecting to database\n	->%s %", conn_string)

	# get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)

	# conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()
    return cursor

cursor = start_db_connection()

@app.route('/', methods=['GET'])
def display_template():
    cursor.execute("SELECT * FROM wins")
    data = cursor.fetchall()
    return render_template('template.html', data=data)

@app.route('/events', methods=['POST'])
def event_watcher():
    print("RECEIVED EVENT. REQUEST:",request.json.get('challenge'), "------------END RECEIVED JSON DATA------------")
    if request.json.get('challenge'):
        resp = request.json.get('challenge')
    else:
        if request.json.get('event'):
            event_msg_to_database = request.json['event']['text']

        cursor.execute("select * from information_schema.tables where table_name=%s", ('wins',))
        if bool(cursor.rowcount):
            insert_data(event_msg_to_database, cursor)            
        else:
            create_table_wins(cursor)
            insert_data(event_msg_to_database, cursor)
        
        resp = "POST / HTTP/1.1 200" 
    return resp

