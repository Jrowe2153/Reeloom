import os
from flask import Flask, request, render_template, redirect, url_for
from instabot import Bot

# Initialize Flask app
app = Flask(__name__)

# Get Instagram credentials from environment variables
INSTAGRAM_USERNAME = os.getenv("INSTAGRAM_USERNAME")
INSTAGRAM_PASSWORD = os.getenv("INSTAGRAM_PASSWORD")

# Initialize the bot with credentials
bot = Bot()
bot.login(username=INSTAGRAM_USERNAME, password=INSTAGRAM_PASSWORD)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/post', methods=['POST'])
def post():
    # Get the URL and caption from the form
    media_url = request.form['media_url']
    caption = request.form['caption']

    # Repost the media with the caption
    try:
        bot.repost(media_url, caption=caption)
        return render_template('success.html', message="Post successfully reposted!")
    except Exception as e:
        return render_template('error.html', message=str(e))

if __name__ == '__main__':
    app.run(debug=False)  # Set debug=False for production environment