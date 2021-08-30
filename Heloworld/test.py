import os
from flask import Flask, render_template, request, redirect, abort, send_file
from werkzeug.utils import secure_filename
import cv2


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
    filewithnoextn = file_path.rsplit('.', 1)[0]
    suffix = '.jpg'
    convert_fileto_jpg = os.path.join(filewithnoextn + suffix)
    print ('convert_fileto_jpg:' , convert_fileto_jpg)
    #C:/Personals/Learnings/Python/mysite/Heloworld\uploads/DPC9_1301240005381084_25052021111421.pdfoutput.jpg
    print('file_path: ',file_path)
    file_path_inp = cv2.imread(file_path,1)

    cv2.imwrite(convert_fileto_jpg, file_path_inp)
    return send_file(convert_fileto_jpg, as_attachment=True, attachment_filename='')


if __name__ == '__main__':
    app.run(debug = True)