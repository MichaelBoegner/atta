from flask import Flask, request, make_response
app = Flask(__name__)

@app.route('/', methods=['POST'])
def hello_world():
    if request.method == 'POST':
        return request.json['challenge']