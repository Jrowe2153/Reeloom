from flask import Flask, render_template, request, redirect, url_for
import os
from dotenv import load_dotenv
from instabot import Bot

# Load environment variables from .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Create a route to the main page with the form
@app.route('/')
def index():
    return render_template('index.html')

# Create a route to handle the form submission and post to Instagram
@app.route('/post', methods=['POST'])
def post_to_instagram():
    # Get data from the form
    video_url = request.form['video_url']
    caption = request.form['caption']
    hashtags = request.form['hashtags']

    # Initialize Instagram bot using credentials from the .env file
    bot = Bot()
    bot.login(username=os.getenv('INSTAGRAM_USERNAME'), password=os.getenv('INSTAGRAM_PASSWORD'))

    # Post the video to Instagram
    bot.upload_video(video_url, caption=f"{caption} {hashtags}")

    return render_template('success.html', video_url=video_url, caption=caption, hashtags=hashtags)

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

