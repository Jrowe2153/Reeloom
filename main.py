from flask import Flask, render_template, request, redirect, url_for
import os
from instabot import Bot

app = Flask(__name__)

# Initialize the Instagram bot
bot = Bot()

# Load Instagram credentials from environment variables
username = os.getenv("INSTAGRAM_USERNAME")
password = os.getenv("INSTAGRAM_PASSWORD")

# Login to Instagram
bot.login(username=username, password=password)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/post', methods=['POST'])
def post_video():
    video_url = request.form['video_url']
    caption = request.form['caption']

    # Post video to Instagram
    bot.upload_video(video_url, caption=caption)

    return render_template('success.html', video_url=video_url)

if __name__ == '__main__':
    # Run the Flask app with debug=False and accessible from external networks
    app.run(debug=False, host='0.0.0.0', port=5000)