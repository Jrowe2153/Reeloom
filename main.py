import os
from flask import Flask, render_template, request, redirect, url_for
import requests
from urllib.parse import quote as url_quote  # Updated import for URL encoding

app = Flask(__name__)

# Instagram API credentials from environment variables
INSTAGRAM_USERNAME = os.getenv('INSTAGRAM_USERNAME')
INSTAGRAM_PASSWORD = os.getenv('INSTAGRAM_PASSWORD')

# Define the Instagram post function (simplified for this example)
def post_to_instagram(video_url, caption):
    # You can integrate Instagram's API here for posting.
    # This is just a placeholder example for the post-to-Instagram logic.
    payload = {
        'username': INSTAGRAM_USERNAME,
        'password': INSTAGRAM_PASSWORD,
        'video_url': video_url,
        'caption': caption
    }

    # In a real scenario, you would make an API request to Instagram to post the video
    # For now, we mock the response (success or failure)
    response = {'status': 'success', 'message': 'Video posted successfully!'}
    return response

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get video URL and caption from the form
        video_url = request.form['video_url']
        caption = request.form['caption']

        # URL encode the video URL (for safety)
        encoded_url = url_quote(video_url)

        # Post to Instagram (simplified)
        response = post_to_instagram(encoded_url, caption)

        # Redirect to the success page with the response message
        if response['status'] == 'success':
            return render_template('success.html', message=response['message'])
        else:
            return render_template('error.html', message="Failed to post video.")

    return render_template('index.html')

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/error')
def error():
    return render_template('error.html')

if __name__ == '__main__':
    app.run(debug=True)