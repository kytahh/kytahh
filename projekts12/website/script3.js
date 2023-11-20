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

    // Function to update character image
    function updateCharacterImage(imageSrc) {
        document.getElementById('character-image').src = imageSrc;
    }

    // Function to simulate typing animation
    function simulateTyping() {
        // Display image1 for 2 seconds before typing begins
        updateCharacterImage('static/pilk_thinking.png');
        setTimeout(function () {
            updateCharacterImage('static/pilk_typing.gif'); // Start typing animation
            // Simulate typing until a response is received
            var typingInterval = setInterval(function () {
                // Check if a response has been received
                if (responseReceived) {
                    clearInterval(typingInterval); // Stop the typing animation
                    updateCharacterImage('http://localhost:8080/static/pilk_default.png'); // Change back to the default image
                }
            }, 1000); // Adjust the interval as needed
        }, 2000); // Adjust the interval as needed
    }

    // Variable to track whether a response has been received
    var responseReceived = false;

    // Function to send user input to the server and display the response
    function sendMessage() {
        var userInput = document.getElementById('user-input').value;
        document.getElementById('chat-container').innerHTML += '<div class="alert alert-primary" role="alert">You: ' + userInput + '</div>';

        // Convert user input to JSON
        var userInputJSON = JSON.stringify({message: userInput});
        
        // Simulate typing animation after sending the message
        simulateTyping();

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

            // Set the flag to indicate that a response has been received
            responseReceived = true;
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
