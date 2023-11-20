import openai
from openai import OpenAI

client = OpenAI(api_key="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")

conversation_history = [
    {'role': 'system', 'content': 'You are a helpful assistant.'},
    {'role': 'user', 'content': 'Hello, who won the world series in 2020?'}
]

def generate_response():
    response = client.completions.create(engine="gpt-3.5-turbo",
    messages=conversation_history,
    max_tokens=1024)
    return response["choices"][0]["text"]

def main():
    print("Chatbot: Hi there! I'm a helpful assistant. Ask me anything.")
    while True:
        user_input = input("You: ")
        
        # Add user input to the conversation history
        conversation_history.append({'role': 'user', 'content': user_input})

        chatbot_response = generate_response()

        # Print the assistant's response
        print("Chatbot:", chatbot_response)

if __name__ == "__main__":
    main()
