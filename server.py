from flask import Flask, request, render_template
from helpers import start_db_connection, insert_data, create_table_wins

#initiate Flask and receive calls
app = Flask(__name__)

cursor = start_db_connection()

@app.route('/', methods=['GET'])
def display_template():
    cursor.execute("SELECT * FROM wins")
    data = cursor.fetchall()
    return render_template('template.html', data=data)

@app.route('/events', methods=['POST'])
def event_watcher():
    print("RECEIVED EVENT. REQUEST:",request.json, "------------END RECEIVED JSON DATA------------")
    if 'challenge' in request.json:
        resp = request.json.get('challenge')
    else:
        if 'event' in request.json:
            resp = "POST /events HTTP/1.1 200" 
            if 'text' in request.json['event']:
                to_database = {
                    'event_msg': request.json['event']['text'],
                    'event_user': request.json['event']['user']
                }
                print("to_database dict - - - - - - -- - -- \n", to_database['event_user'])
                cursor.execute("select * from information_schema.tables where table_name=%s", ('wins',))
                if bool(cursor.rowcount):
                    insert_data(to_database, cursor)            
                else:
                    create_table_wins(cursor)
                    insert_data(to_database, cursor)
        else:
            resp= "Not an acceptable event type."
        
    return resp
