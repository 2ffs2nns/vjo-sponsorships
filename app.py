from flask import Flask, render_template, request, redirect, url_for, flash
import os
import time
from prep_ip import get_ip
app = Flask(__name__)
app.secret_key = '' # update/set with wifi passwd

SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))

# Directory where images are stored
IMAGE_DIR = f'{SCRIPT_PATH}/static/images'
# Interval for rotating images (in seconds)
ROTATION_INTERVAL = 10
def get_image_files():
    """Get a list of image files from the IMAGE_DIR directory."""
    image_files = []
    for filename in os.listdir(IMAGE_DIR):
        if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
            image_files.append(filename)
    return image_files

@app.route('/')
def index():
    """Display the main page with rotating images."""
    image_files = get_image_files()
    return render_template('index.html', image_files=image_files, rotation_interval=ROTATION_INTERVAL)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    """Page for users to upload images and delete existing images."""
    image_files = get_image_files()
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        # If user does not select file, browser also submits an empty part without filename
        if file.filename == '':
            return redirect(request.url)
        if file:
            filename = file.filename
            file.save(os.path.join(IMAGE_DIR, filename))
            flash('Image uploaded successfully', 'success')
            return redirect(url_for('upload'))
    return render_template('upload.html', image_files=image_files)

@app.route('/delete', methods=['POST'])
def delete():
    """Delete selected images."""
    if request.method == 'POST':
        files_to_delete = request.form.getlist('image')
        for filename in files_to_delete:
            try:
                os.remove(os.path.join(IMAGE_DIR, filename))
            except FileNotFoundError:
                flash(f"File {filename} not found", 'error')
            else:
                flash(f"File {filename} deleted successfully", 'success')
    return redirect(url_for('upload'))

HOST_IP = get_ip()

if __name__ == '__main__':
    HOST_IP = get_ip()
    app.run(host=HOST_IP, port=8000, debug=True)
