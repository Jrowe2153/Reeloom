from flask import Flask, render_template, request
from instabot import Bot
from werkzeug.utils import secure_filename  # Correct import

app = Flask(__name__)

# Initialize the bot
bot = Bot()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/post', methods=['POST'])
def post_to_instagram():
    username = request.form['username']
    password = request.form['password']
    caption = request.form['caption']
    hashtags = request.form['hashtags']
    image_url = request.form['image_url']

    # Log in to Instagram
    bot.login(username=username, password=password)

    # Combine the caption with hashtags
    full_caption = f"{caption} {hashtags}"

    # Post the image with the caption
    bot.upload_photo(image_url, caption=full_caption)

    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=False)  # Disable debug mode for production