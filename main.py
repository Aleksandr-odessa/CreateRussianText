from os.path import join, dirname, realpath
from os import scandir, remove
from flask import Flask
from flask import render_template, request, redirect
from werkzeug.utils import secure_filename
from flask import send_from_directory
from DocxReadWrite import DocxReadWrite
from text import TextSeparted, TextNormal, DeleteWord


app = Flask(__name__)


UPLOAD_FOLDER = join(dirname(realpath(__file__)), 'uploads')
ALLOWED_EXTENSIONS = ['docx']
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/')
def main():
    for file in scandir(UPLOAD_FOLDER):
        remove(file.path)
        # send_msg("файл удален", my)
    return render_template('selectFile.html')


@app.route('/selectFile', methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(join(app.config['UPLOAD_FOLDER'], filename))
            # send_msg("файл загружен", my)
            return render_template("success.html", name=file.filename)
    return render_template('selectFile.html')


@app.route('/success', methods=["GET", "POST"])
def select_function():
    doc = DocxReadWrite('Text.doc', 'uploads')
    in_text = doc.word_read()
    if 'normal_form' in request.form:
        text = TextNormal(in_text)
    elif 'del_form' in request.form:
        text = DeleteWord(in_text)
    elif 'separate' in request.form:
        if request.form['input']:
            text = TextSeparted(int(request.form['input']))
        else:
            text = TextSeparted(in_text)
    text_rez = text.main_function()
    doc.word_write(text_rez)
    return render_template("download.html")
    

@app.route('/download', methods=['GET', 'POST'])
def download_file():
    return send_from_directory(app.config["UPLOAD_FOLDER"], "Text.doc")


app.run()
