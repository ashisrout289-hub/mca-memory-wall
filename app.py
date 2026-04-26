from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Configure upload folder
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

    # Save photo if it exists
    photo_name = "No Photo"
    if photo:
        photo_name = photo.filename
        photo.save(os.path.join(UPLOAD_FOLDER, photo_name))

    # Save text data to responses.txt
    entry = f"Name: {name} | Message: {about} | Photo: {photo_name}\n"
    with open('responses.txt', 'a') as f:
        f.write(entry)

    return "<h1>Thank you for the memory! ❤️</h1><a href='/'>Go Back</a>"

# --- THE SECRET ADMIN FIX ---
@app.route('/my-secret-admin-panel')
def admin_view():
    try:
        # We use 'r' to read the file
        if os.path.exists('responses.txt'):
            with open('responses.txt', 'r') as f:
                data = f.read()
        else:
            data = "No memories saved in the file yet!"
            
        return f"""
        <html>
            <body style="font-family: 'Poppins', sans-serif; padding: 40px; background-color: #f4f4f9;">
                <h1 style="color: #333;">Batch Memories (Admin Access)</h1>
                <hr>
                <div style="background: white; padding: 20px; border-radius: 10px; border: 1px solid #ddd;">
                    <pre style="white-space: pre-wrap; font-size: 16px;">{data}</pre>
                </div>
                <br>
                <a href="/" style="text-decoration: none; color: blue;">← Back to Home</a>
            </body>
        </html>
        """
    except Exception as e:
        return f"Error accessing data: {str(e)}"

if __name__ == "__main__":
    # Render uses the PORT environment variable
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)