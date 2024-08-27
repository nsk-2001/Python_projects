import json
import os
from flask import Flask, request, jsonify, render_template
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

app = Flask(__name__)

# Ensure the old database is removed
if os.path.exists("db.sqlite3"):
    os.remove("db.sqlite3")

# Load JSON training data
with open('training_data.json', 'r', encoding='utf-8') as f:
    training_data = json.load(f)

# Initialize ChatBot
chatbot = ChatBot('Chatpot')

# Set the trainer
trainer = ListTrainer(chatbot)

# Prepare the training data
training_pairs = []
for entry in training_data:
    inputs = entry['input']
    outputs = entry['output']
    
    if isinstance(inputs, str):
        inputs = [inputs]
    if isinstance(outputs, str):
        outputs = [outputs]
    
    for input_phrase in inputs:
        for output_phrase in outputs:
            trainer.train([input_phrase, output_phrase])

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data["message"]
    response = chatbot.get_response(user_input)
    return jsonify({"response": str(response)})

if __name__ == "__main__":
    app.run(debug=True)
