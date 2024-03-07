#from flask import Flask, request, abort

#@app.after_request
#def add_cors_headers(response):
    #response.headers['Access-Control-Allow-Origin'] = 'http://127.0.0.1:5500'
    #response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    #response.headers['Access-Control-Allow-Methods'] = 'GET,POST,PUT,DELETE,OPTIONS'
    #return response
from flask import Flask, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route('/receive', methods=['POST'])
def receive():
    data = request.get_json()
    message = data.get('message')
    print('Message received:', message)
    return json.dumps({'status': 'success'}), 200

if __name__ == '__main__':
    app.run(debug=True)



#app = Flask(__name__)

@app.route("/")
def hello_world():
    html = f"<h1>Deployed Zeet!!</h1>"
    return html
	
#@app.route('https://hgjhek62v7.execute-api.us-west-2.amazonaws.com/receive')
#def receive():
    # Your code here
    #pass
	
	
if __name__ == '__main__':
	app.run(host="0.0.0.0", port=3000)
