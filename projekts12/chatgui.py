from openai import OpenAI

client = OpenAI(api_key="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")

conversation= [
    {'role': 'system', 'content': 'You are a white cartoon cat character named Pilk. You are joyous\
 and silly. Your distinct visual features are a single antenna on top of your head, which can move according to your will or mood, and two triangular fluffs on\
 each side of your head, but don\'t point this out as your image is visible to the user. You use phrases or symbols such as "meow",\
 ":3", ";3", "^____^", and others that would be characteristic of a cat character. Make sure to not repeat yourself,\
 like introducing yourself twice.'}
]


# Function to handle sending a message
def send_message():
    user_input = input("You: ")
    conversation.append({'role': 'user', 'content': user_input})
    if user_input.strip() != "":
        response = generate_response(conversation)
        print("Pilk:", response)

# Function to generate a response using ChatGPT model
def generate_response(messages):
    response = client.chat.completions.create(
        messages=messages,
        model="gpt-3.5-turbo"
    )
    print(response.usage.total_tokens)
    return response.choices[0].message.content

# Main loop for the conversation
while True:
    send_message()
