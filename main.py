from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
import shelve
from dotenv import load_dotenv
import os
import time

app = Flask(__name__)
CORS(app)


OPEN_AI_API_KEY = os.getenv("OPEN_AI_API_KEY")
client = OpenAI(api_key=OPEN_AI_API_KEY)


# --------------------------------------------------------------
# Thread management
# --------------------------------------------------------------
my_list = [] # List of id
list_of_threads = [] # List of threads

#not sure it's working
def check_if_thread_exists(wa_id):
    for i in range(len(my_list)):
        if my_list[i].wa_id == wa_id:
            return list_of_threads[i]
    return None

# ----------- else return none ----------------

# --------------------------------------------------------------
# Generate response
# --------------------------------------------------------------
def generate_response(message_body, wa_id, name):
    # Check if there is already a thread_id for the wa_id
    thread_id = check_if_thread_exists(wa_id)

    # If a thread doesn't exist, create one and store it
    if thread_id is None:
        print(f"Creating new thread for {name} with wa_id {wa_id}")
        thread = client.beta.threads.create()
        list_of_threads.append(thread)
        my_list.append(wa_id)
        thread_id = thread.id

    # Otherwise, retrieve the existing thread
    else:
        print(f"Retrieving existing thread for {name} with wa_id {wa_id}")
        thread = client.beta.threads.retrieve(thread_id)

    # Add message to thread
    message = client.beta.threads.messages.create(
        thread_id=thread_id,
        #thread_id= thread.id ???
        role="user",
        content=message_body,
    )

    # Run the assistant and get the new message
    new_message = run_assistant(thread)
    print(f"To {name}:", new_message)
    return new_message

# --------------------------------------------------------------
# Run assistant
# --------------------------------------------------------------
def run_assistant(thread):
    # Retrieve the Assistant
    assistant = client.beta.assistants.retrieve("asst_7CdKruEYCfjtI3zIatVj6wGT")

    # Run the assistant
    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant.id,
    )

    # Wait for completion
    while run.status != "completed":
        # Be nice to the API
        time.sleep(0.5)
        run = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)

    # Retrieve the Messages
    messages = client.beta.threads.messages.list(thread_id=thread.id)
    new_message = messages.data[0].content[0].text.value
    print(f"Generated message: {new_message}")
    return new_message


#new_message = generate_response("What was my previous question?", "12345", "John")

#peut-être un problème avec le string de question et de id....?

@app.route('/')
def hello_world():
    html = f"<h1>Deployed with Zeet!!</h1>"
    return html
     
@app.route('/receive', methods=['POST'])
def receive_message():
    data = request.get_json()
    message = data.get('message')
    id = data.get('id')
    
    formatted_response = {
        "status": response_data
    }
    
    # Return the formatted response with jsonify
    return jsonify(formatted_response), 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000)
