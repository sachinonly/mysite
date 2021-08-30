import os
from flask import Flask, render_template, request, redirect, url_for, abort, send_file
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif','.pdf']
parent_dir = "C:/Personals/Learnings/Python/mysite/Heloworld"
directory = "uploads/"
UPLOAD_FOLDER = os.path.join(parent_dir, directory)
app.config['UPLOAD_PATH'] = UPLOAD_FOLDER
#app.config['UPLOAD_PATH'] = 'uploads'

@app.route('/')
def index():
    return render_template('upload_file.html')

@app.route('/', methods=['GET', 'POST'])
def upload_files():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        filename = secure_filename(uploaded_file.filename)
        if filename != '':
            file_ext = os.path.splitext(filename)[1]
            if file_ext not in app.config['UPLOAD_EXTENSIONS']:
                abort(400)
            uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
            return redirect('/downloadfile/'+ filename)
    return render_template('upload_file.html')
# Download API
@app.route("/downloadfile/<filename>", methods = ['GET'])
def download_file(filename):
    return render_template('download.html',value=filename)

@app.route('/return-files/<filename>')
def return_files_tut(filename):
    file_path = app.config['UPLOAD_PATH'] + filename
    return send_file(file_path, as_attachment=True, attachment_filename='')


if __name__ == '__main__':
    app.run(debug = True)