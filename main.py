from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Render the home page with a welcome message and form
    return render_template('index.html')

@app.route('/repost', methods=['POST'])
def repost():
    # You can implement repost functionality here, or just a placeholder
    return 'Reposting functionality goes here!'

if __name__ == '__main__':
    app.run(debug=False)