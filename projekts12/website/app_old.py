# from flask import Flask, request
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)

# @app.route('/')
# def index():
#     return 'Hello, this is the index page!'

# @app.route('/api/send_message', methods=['POST'])
# def send_message():
#     # Get plain text data from the request
#     user_message = request.data.decode('utf-8')

#     # Your logic to process the user's message and generate a response
#     # For simplicity, we'll echo the user's message in this example
#     bot_response = 'You said: ' + user_message
#     print("Received message:", repr(user_message))

#     return str(bot_response)

# if __name__ == '__main__':
#     app.run(port=5000,debug=True)

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return 'Hello, this is the index page!'

@app.route('/api/send_message', methods=['POST'])
def send_message():
    data = request.get_json()
    user_message = data.get('message', '')

    # Your logic to process the user's message and generate a response
    # For simplicity, we'll echo the user's message in this example
    bot_response = 'You said: ' + user_message

    return jsonify({'message': bot_response})

if __name__ == '__main__':
    app.run(debug=True)
