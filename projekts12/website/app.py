from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI

app = Flask(__name__)
CORS(app)

conversation = [
    {'role': 'system', 'content': 'You are a white cartoon cat named Pilk, who\'s joyous \
and silly and has a single antenna on top of it\'s head, which can move according to it\'s will or mood, but don\'t point this out. It use phrases or symbols such as "meow", \
":3", ";3", "^____^", and others that are be characteristic of a cat character. Respond briefly and Don\'t repeat yourself much.'}
    ]

@app.route('/')
def index():
    return 'Hello, this is the index page!'

@app.route('/api/send_message', methods=['POST'])
#receive api request, generate response with gpt, and send api response
def send_message():
    data = request.get_json()
    user_message = data.get('message', '')

    client = OpenAI(api_key="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")

    # Function to generate a response using ChatGPT model
    def generate_response(messages):
        response = client.chat.completions.create(
            messages=messages,
            model="gpt-3.5-turbo"
        )
        print(response.usage.total_tokens)
        return response.choices[0].message.content

    # user_input = input("You: ")
    user_input=user_message
    conversation.append({'role': 'user', 'content': user_input})
    if user_input.strip() != "":
        response = generate_response(conversation)
        # print("Pilk:", response)
    else:
        response = "I didn't catch that, come again?"

    bot_response=response

    return jsonify({'message': bot_response})

@app.route('/api/reset', methods=['GET'])
# reset the conversation on load
def reset_conversation():
    global conversation
    # Reset the conversation to the starting state
    conversation = [{'role': 'system', 'content': 'You are a white cartoon cat named Pilk, who\'s joyous \
and silly and has a single antenna on top of it\'s head, which can move according to it\'s will or mood, but don\'t point this out. It use phrases or symbols such as "meow", \
":3", ";3", "^____^", and others that are be characteristic of a cat character. Respond briefly and Don\'t repeat yourself much.'}
    ]
    return jsonify({'message': 'Conversation reset successfully'})

if __name__ == '__main__':
    app.run(debug=True)
