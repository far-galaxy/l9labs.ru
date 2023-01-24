# -*- coding: utf-8 -*-
from flask import *

app = Flask(__name__)

# Index page
@app.route("/")
def index():
    return send_file("index.html")

# Files
keywords = {'js', 'media', 'robots.txt', 'favicon.ico', '.html'}

@app.route('/<path:path>', methods=['GET'])
def get_files(path):
    try:
        if [key for key in keywords if key in path] != []:
            return send_file(path)
        else:
            abort(404)
    except FileNotFoundError:
        abort(404)


# Moskvich Easter Egg
@app.route("/moskvich/<path:path>")
def moskvich(path):
    try:
        return send_file(f"moskvich/{path}")
    except FileNotFoundError:
        abort(404)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
