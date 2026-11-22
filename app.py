import flask
from flask import Flask, render_template, send_file
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/img/<path:path>')
def image(path):
    return send_file("img/" + path, mimetype='image/png')

@app.route('/Games')
def gamespage():
    folder = "games/"
    subfolders = [ f.path for f in os.scandir(folder) if f.is_dir() ]
    print(subfolders)
    return render_template("games.html", games=subfolders)

if __name__ == "__main__":
    app.run()