from flask import Flask
from flask.templating import render_template
app = Flask(__name__)

@app.route('/')
def board():
    return render_template('index.html', cols = 8, rows = 8, color1 = 'pink', color2 = 'aqua')

@app.route('/<rows>')
def row_count(rows):
    return render_template('index.html', rows = int(rows), cols = 8, color1 = 'pink', color2 = 'aqua')

@app.route('/<rows>/<cols>')
def makshift(rows, cols):
    return render_template('index.html', rows = int(rows), cols = int(cols), color1 = 'pink', color2 = 'aqua')

@app.route('/<rows>/<cols>/<color1>/<color2>')
def sensei(rows, cols, color1, color2):
    return render_template('index.html', rows = int(rows), cols = int(cols), color1 = color1, color2 = color2)


if __name__ == '__main__':
    app.run(debug = True)