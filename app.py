import flask
from flask import Flask, render_template, send_file
import os, json

app = Flask(__name__)

# 404 first and foremost
@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")


@app.route("/")
def index():
    return render_template("index.html")

@app.route('/img/<path:path>')
def image(path):
    return send_file("img/" + path, mimetype='image/png')

@app.route('/Games')
def gamespage():
    folder = "games"
    subfolders = [ f.path for f in os.scandir(folder) if f.is_dir() ]
    with open("games/gamelist.txt") as g:
        Json = g.read()
        data = json.loads(Json)
    return render_template("games.html", 
                           games=subfolders, 
                           names=data["names"], 
                           gamelength=len(subfolders))

@app.route('/games/<path:path>')
def gamepage(path):
    return send_file("games/" + path)


if __name__ == "__main__":
    app.run()