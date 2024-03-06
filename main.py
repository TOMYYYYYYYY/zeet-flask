from flask import Flask, request, abort

app = Flask(__name__)

@app.route("/")
def hello_world():
    html = f"<h1>Deployed with Zeet!!</h1>"
    return html
	
@app.route('/receive_message', methods=['POST'])
def receive_message():
    message = request.json.get('message')
    # Faites quelque chose avec le message reçu
    return "Message reçu avec succès"
	
if __name__ == '__main__':
	app.run(host="0.0.0.0", port=3000)
