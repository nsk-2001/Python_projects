import json
import os
import random
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

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
            training_pairs.append((input_phrase, output_phrase))

# Train the ChatBot with the prepared training pairs
for input_phrase, output_phrase in training_pairs:
    trainer.train([input_phrase, output_phrase])

# Chat loop
exit_conditions = ('.q', 'quit', 'exit')
print("Chatbot is ready! Type your message or '.q' to quit.")
while True:
    query = input("> ")
    if query.lower() in exit_conditions:
        break
    else:
        response = chatbot.get_response(query)
        print(f"🪴 {response}")
