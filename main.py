from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    html = f"<h1>Deployed with Zeet!!</h1>"
    return html
     
@app.route('/receive', methods=['POST'])
def receive_message():
    data = request.get_json()
    message = data.get('message')
    # Process the message
    # Example: print the message and send a response back
    if message == 'Hello, server!':
        response_data = {'status': 'What is love?'}
    else:
        response_data = {'status': 'Message received'}
    return jsonify(response_data), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000)
