from flask import Flask, request, make_response
app = Flask(__name__)

@app.route('/', methods=['POST'])
def event_watcher():
    print("RECEIVED EVENT. REQUEST:",request.json, "END RECEIVED JSON DATA------------")
    if request.json.get('challenge'):
        resp = request.json.get('challenge')
    else: 
        resp = "great!"
    return resp