from flask import Flask, render_template, request, send_from_directory
import os

app = Flask(__name__)

# Папка, в которой хранятся изображения
app.config['UPLOAD_FOLDER'] = 'static'


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/graphics', methods=["GET", "POST"])
def count():
    if request.method == 'POST':
        x = request.form['cnt']

        return render_template('graphics.html', result=x)
    else:
        return render_template('graphics.html')


if __name__ == '__main__':
    app.run(debug=True)