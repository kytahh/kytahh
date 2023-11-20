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
});

// document.addEventListener('DOMContentLoaded', function () {
//     // Function to send user input to the server and display the response
//     function sendMessage() {
//         var userInput = document.getElementById('user-input').value;
//         document.getElementById('chat-container').innerHTML += '<div class="alert alert-primary" role="alert">You: ' + userInput + '</div>';

//         // Send the user input to the Python backend using fetch
//         fetch('http://localhost:5000/api/send_message', {
//             method: 'POST',
//             headers: {
//                 'Content-Type': 'application/json'
//             },
//             body: JSON.stringify({ message: userInput })
//         })
//         .then(response => response.json())
//         .then(data => {
//             // Display the server's response
//             document.getElementById('chat-container').innerHTML += '<div class="alert alert-success" role="alert">Bot: ' + data.message + '</div>';
//         })
//         .catch(error => {
//             console.error('Error sending message:', error);
//         });

//         // Clear the user input field
//         document.getElementById('user-input').value = '';
//     }

//     // Event listener for the send button
//     document.getElementById('send-btn').addEventListener('click', function () {
//         sendMessage();
//     });

//     // Event listener for the enter key in the input field
//     document.getElementById('user-input').addEventListener('keypress', function (e) {
//         if (e.which === 13) {
//             sendMessage();
//         }
//     });
// });
