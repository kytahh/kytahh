document.addEventListener('DOMContentLoaded', function () {
    fetch('http://localhost:5000/api/reset', {
        method: 'GET',
    })
    .then(response => response.json())
    .then(data => {
        console.log('Reset successful:', data);
    })
    .catch(error => {
        console.error('Error resetting conversation:', error);
    });
    // Function to send user input to the server and display the response
    function sendMessage() {
        var userInput = document.getElementById('user-input').value;
        document.getElementById('chat-container').innerHTML += '<div class="alert alert-primary" role="alert">You: ' + userInput + '</div>';

        // Convert user input to JSON
        var userInputJSON = JSON.stringify({message: userInput});
        // Send the user input to the Python backend using fetch
        fetch('http://localhost:5000/api/send_message', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: userInputJSON
        })
        .then(response => response.json())
        .then(data => {
            console.log('Raw Response:', JSON.stringify(data));

            // Display the server's response
            document.getElementById('chat-container').innerHTML += '<div class="alert alert-success" role="alert">Pilk: ' + data.message + '</div>';
        })
        .catch(error => {
            console.error('Error sending message:', error);

            // Print known data
            console.log('Known data:', userInputJSON);

            // Optionally, you can also log the raw response (if available)
            if (error.response) {
                error.response.json().then(rawResponse => {
                    console.log('Raw response:', JSON.stringify(rawResponse));
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
});
