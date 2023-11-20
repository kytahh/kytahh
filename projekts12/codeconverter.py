from openai import OpenAI

client = OpenAI(api_key="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")

conversation= [
    {'role': 'system', 'content': 'You give advice in coding, code, and convert code according to requests.'}
]


# Function to handle sending a message
def send_message():
    user_input = ''' convert this to use json instead of plain text:

document.addEventListener('DOMContentLoaded', function () {
    // Function to send user input to the server and display the response
    function sendMessage() {
        var userInput = document.getElementById('user-input').value;
        document.getElementById('chat-container').innerHTML += '<div class="alert alert-primary" role="alert">You: ' + userInput + '</div>';

        // Send the user input to the Python backend using fetch
        fetch('http://localhost:5000/api/send_message', {
            method: 'POST',
            headers: {
                'Content-Type': 'text/plain'
            },
            body: userInput
        })
        .then(response => {response.text();
            console.log('Raw Response:', response);
        })
        .then(data => {
            console.log('Raw Response:', data);
            
            // Display the server's response
            document.getElementById('chat-container').innerHTML += '<div class="alert alert-success" role="alert">Bot: ' + data + '</div>';
        })
        .catch(error => {
            console.error('Error sending message:', error);
            
            // Print known data
            console.log('Known data:', userInput);

            // Optionally, you can also log the raw response (if available)
            if (error.response) {
                error.response.text().then(rawResponse => {
                    console.log('Raw response:', rawResponse);
                });
        }});

        // Clear the user input field
        document.getElementById('user-input').value = '';
    }

    // Event listener for the send button
    document.getElementById('send-btn').addEventListener('click', function () {
        sendMessage();
    });

    // Event listener for the enter key in the input field
    document.getElementById('user-input').addEventListener('keypress', function (e) {
        if (e.which === 13) {
            sendMessage();
        }
    });
});'''
    conversation.append({'role': 'user', 'content': user_input})
    if user_input.strip() != "":
        response = generate_response(conversation)
        print("Code:", response)

# Function to generate a response using ChatGPT model
def generate_response(messages):
    response = client.chat.completions.create(
        messages=messages,
        model="gpt-4"
    )
    print(response.usage.total_tokens)
    with open('projekts12/code_out.txt','w') as file:
        file.write(response.choices[0].message.content)
    return response.choices[0].message.content

# Main loop for the conversation
def main():
    send_message()

if __name__=="__main__":
    main()
