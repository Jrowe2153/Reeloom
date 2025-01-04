from flask import Flask, request, jsonify

app = Flask(__name__)

# Set your verify token here (make sure this matches the one you created on Facebook)
VERIFY_TOKEN = 'your_secure_verify_token_here'

# Webhook verification endpoint
@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        # Retrieve the 'hub.verify_token' and 'hub.challenge' from the request
        verify_token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')

        # Check if the token matches the one you set up in your app
        if verify_token == VERIFY_TOKEN:
            return str(challenge)  # Respond with the challenge to verify the webhook
        else:
            return 'Invalid verify token', 403  # Respond with an error if the token is invalid

    if request.method == 'POST':
        # Handle incoming POST requests from Facebook (event notifications)
        data = request.get_json()

        # Process the data (e.g., for Instagram Insights, posts, etc.)
        print('Received data: ', data)  # You can log or process this data further as needed
        return 'EVENT RECEIVED', 200


if __name__ == '__main__':
    # Run your Flask app
    app.run(debug=True, host='0.0.0.0', port=5000)