from os.path import join, dirname, realpath
from os import scandir, remove
from flask import Flask
from flask import render_template, request, redirect
from werkzeug.utils import secure_filename
from flask import send_from_directory
from work_with_word import Word


UPLOAD_FOLDER = join(dirname(realpath(__file__)), 'uploads')
# UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = ['docx']
# files = glob(join(dirname(realpath(__file__)), 'uploads'), doc)
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/')
def main():
    return render_template('selectFile.html')

@app.route('/', methods=["GET", "POST"])
def delet():
    for file in scandir(UPLOAD_FOLDER):
        remove(file.path)
    return render_template('selectFile.html')


@app.route('/selectFile', methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        if "file" not in request.files:
            # flash('Не могу прочитать файл')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            # flash('не выбран файл')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(join(app.config['UPLOAD_FOLDER'], filename))
            return render_template("success.html", name=file.filename)
    return render_template('selectFile.html')

@app.route('/success', methods=["GET", "POST"])
def begin_def():
    normal_form = request.form['normal_form']
    doc = Word('Text.doc', 'uploads')
    in_text = doc.word_read()
    if normal_form == '0':
        word_del = doc.del_word(in_text, 15)
        doc.word_write(word_del)
    else:
        word_norm = doc.norm_word(in_text)
        doc.word_write(word_norm)
    return render_template("download.html")

@app.route('/download', methods=['GET', 'POST'])
def download_file():
    return send_from_directory(app.config["UPLOAD_FOLDER"], "Text.doc")

if __name__ == '__main__':
    app.debug = True
    app.run()
