import os
import requests
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Instagram API credentials - these should be securely stored in environment variables
INSTAGRAM_ACCESS_TOKEN = os.getenv('INSTAGRAM_ACCESS_TOKEN')
INSTAGRAM_USER_ID = os.getenv('INSTAGRAM_USER_ID')

# Post schedule dictionary to simulate scheduled posts (in a real application, this would be handled by a scheduler like Celery)
scheduled_posts = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/post_now', methods=['POST'])
def post_now():
    image_url = request.form['image_url']
    caption = request.form['caption']
    post_to_instagram(image_url, caption)
    return redirect(url_for('index'))

@app.route('/schedule_post', methods=['POST'])
def schedule_post():
    image_url = request.form['image_url']
    caption = request.form['caption']
    post_time = request.form['post_time']

    # Convert post_time string to datetime object
    post_time_obj = datetime.strptime(post_time, '%Y-%m-%d %H:%M')

    # Store scheduled post
    scheduled_posts[post_time_obj] = {'image_url': image_url, 'caption': caption}

    return redirect(url_for('index'))

def post_to_instagram(image_url, caption):
    """Post image to Instagram using Graph API."""
    endpoint = f'https://graph.facebook.com/v14.0/{INSTAGRAM_USER_ID}/media'
    image_upload_payload = {
        'image_url': image_url,
        'caption': caption,
        'access_token': INSTAGRAM_ACCESS_TOKEN
    }

    # Upload the image
    response = requests.post(endpoint, data=image_upload_payload)
    if response.status_code == 200:
        creation_id = response.json().get('id')

        # Publish the image
        publish_endpoint = f'https://graph.facebook.com/v14.0/{INSTAGRAM_USER_ID}/media_publish'
        publish_payload = {
            'creation_id': creation_id,
            'access_token': INSTAGRAM_ACCESS_TOKEN
        }

        publish_response = requests.post(publish_endpoint, data=publish_payload)
        if publish_response.status_code == 200:
            print("Post successful!")
        else:
            print(f"Error publishing post: {publish_response.text}")
    else:
        print(f"Error uploading image: {response.text}")

if __name__ == "__main__":
    app.run(debug=True)