import json

from model import ChatModel

from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)

# Enable cors requests
CORS(app) 

#Initiate model
clf = ChatModel()

@app.route('/')
def index():
    """Check if api is working."""
    return json.dumps({'status': 'OK'})

@app.route('/query', methods=['POST'])
def query():
    """Endpoint for receiving bot response"""
    query = request.json
    conversations = query['lastConversations']
    # Get dialog in format according to documentation
    input_data = '    '.join(conversations)
    bot_answer = clf.get_reply(input_data)
    return json.dumps({'botResponse': bot_answer})

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=80,
        debug=True,
    )
