from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Configure where uploads go
UPLOAD_FOLDER = 'static/uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    # This looks for index.html inside the 'templates' folder
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    about = request.form.get('about')
    photo = request.files.get('photo')

    # Save the photo if it exists
    if photo and photo.filename != '':
        photo.save(os.path.join(app.config['UPLOAD_FOLDER'], photo.filename))

    # Save data permanently to a text file
    with open("responses.txt", "a", encoding="utf-8") as f:
        f.write(f"Name: {name}\nAbout: {about}\nPhoto: {photo.filename if photo else 'None'}\n")
        f.write("-" * 20 + "\n")

    return "<h1>Memories Captured!</h1><p>Your journey has been saved to the vault.</p><a href='/'>Go back to the memories</a>"

if __name__ == '__main__':
    app.run(debug=True)