from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Ensure the upload folder exists
UPLOAD_FOLDER = 'static/uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    about = request.form.get('about')
    photo = request.files.get('photo')

    if photo:
        photo_name = photo.filename
        photo.save(os.path.join(UPLOAD_FOLDER, photo_name))
    else:
        return "Error: Photo is required!", 400

    # Save the text data to a file
    entry = f"Name: {name} | Message: {about} | Photo: {photo_name}\n"
    with open('responses.txt', 'a', encoding='utf-8') as f:
        f.write(entry)

    return "<h1>Memory Saved! ❤️</h1><p>Thank you for being part of the family.</p><a href='/'>Go Back</a>"

@app.route('/view-memories-secret')
def admin_view():
    if os.path.exists('responses.txt'):
        with open('responses.txt', 'r', encoding='utf-8') as f:
            data = f.read()
    else:
        data = "No messages yet."
    return f"<html><body style='background:#1a001a;color:white;padding:20px;'><pre>{data}</pre></body></html>"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)