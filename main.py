from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/your-flask-endpoint', methods=['POST'])
def receive_message():
    data = request.get_json()
    message = data.get('message')
    # Process the message
    # Example: print the message and send a response back
    print('Received message:', message)
    response_data = {'status': 'Message received'}
    return jsonify(response_data), 200

if __name__ == '__main__':
    app.run()
