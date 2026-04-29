from flask import Flask, render_template, request, os

app = Flask(__name__)

# Folder for user-uploaded photos
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

    photo_name = "No Photo"
    if photo:
        photo_name = photo.filename
        photo.save(os.path.join(UPLOAD_FOLDER, photo_name))

    # Save to responses.txt
    entry = f"Name: {name} | Message: {about} | Photo: {photo_name}\n"
    with open('responses.txt', 'a') as f:
        f.write(entry)

    return "<h1>Memory Saved! ❤️</h1><a href='/'>Go Back</a>"

# SECRET ADMIN PANEL
@app.route('/my-secret-admin-panel')
def admin_view():
    try:
        if os.path.exists('responses.txt'):
            with open('responses.txt', 'r') as f:
                data = f.read()
        else:
            data = "No messages yet."
        return f"<html><body><h1>Batch Messages</h1><pre>{data}</pre><br><a href='/'>Back</a></body></html>"
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)