import os
from flask import Flask, render_template, request, url_for, redirect

from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/Users/Hp/Desktop/web/ml-flask-/deep_learning_mnsit/static'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            demo = 'No file part'
            return render_template('index.html', ans=demo)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            demo = 'No selected file'
            return render_template('index.html', ans=demo)
        if not(allowed_file(file.filename)):
            demo = 'File not supported'
            return render_template('index.html', ans=demo)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_location = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_location)
            return render_template('index.html', file=filename)
    return render_template('index.html', ans='Insert file')


@app.route('/display/<filename>')
def display_image(filename):
    #print('display_image filename: ' + filename)
    return redirect(url_for('static', filename=filename), code=301)


app.run(debug=True)
