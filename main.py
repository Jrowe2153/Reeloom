from flask import Flask, request
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import time

app = Flask(__name__)
scheduler = BackgroundScheduler()

# Example function to repost media (you'll want to replace this with actual reposting logic)
def repost_media(media_url, caption, poster_name):
    # Logic to repost the media (e.g., via Instagram API)
    print(f"Reposting: {media_url} with caption: {caption} (Original poster: {poster_name})")

# Route to handle media posting
@app.route('/post_media', methods=['POST'])
def post_media():
    media_url = request.form['media_url']
    caption = request.form['caption']
    schedule_time = request.form.get('schedule_time')
    action = request.form['action']

    # For now, let's assume the poster's name is fetched from the media URL (you'll need real logic)
    poster_name = "example_user"  # Replace with actual logic to get the original poster's name

    # If no scheduling time, post immediately
    if action == "now":
        repost_media(media_url, caption, poster_name)
        return f"Post has been made now! Credit: {poster_name}"

    # If the post is scheduled, schedule the repost
    if action == "schedule" and schedule_time:
        schedule_datetime = datetime.fromisoformat(schedule_time)
        delay = (schedule_datetime - datetime.now()).total_seconds()

        if delay > 0:
            scheduler.add_job(repost_media, 'date', run_date=schedule_datetime, args=[media_url, caption, poster_name])
            return f"Post scheduled for {schedule_datetime}. Credit: {poster_name}"
        else:
            return "Please choose a future time to schedule the post."

    return "Invalid action."

# Start the scheduler
scheduler.start()

if __name__ == "__main__":
    app.run(debug=True)