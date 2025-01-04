from flask import Flask, request, jsonify
import hashlib
import json

app = Flask(__name__)

VERIFY_TOKEN = 'reeloom_secure_verify_token_8f5b48c4e2e0ed938f2f0b987b92c10b'

@app.route('/')
def home():
    return "Welcome to Reeloom's API!"

# Webhook verification
@app.route('/webhook', methods=['GET'])
def webhook_verification():
    # Facebook requires that we verify the token sent in the request
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.verify_token") == VERIFY_TOKEN:
        # Respond with the challenge sent by Facebook
        return request.args.get("hub.challenge"), 200
    else:
        # Return an error if tokens don't match
        return "Verification failed", 403

# Endpoint for receiving events
@app.route('/webhook', methods=['POST'])
def webhook():
    # Get the incoming data
    data = json.loads(request.data)

    # You can process the data here (e.g., log, analyze, etc.)
    print("Received data:", data)

    # Return a success response
    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    app.run(debug=True)