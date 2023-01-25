# -*- coding: utf-8 -*-
from flask import *
from utils import *

app = Flask(__name__)

# Index page
@app.route("/")
def index():
    return send_file("index.html")


# Stuff page
@app.route("/stuff")
def stuff_index():
    page = request.args.get('page')
    if page == None:
        return send_file("stuff/index.html")
    else:
        return send_file("stuff/video.html")


@app.route("/stuff/index.json")
def stuff_index_json():
    return get_stuff_index()


# Files
keywords = {'css', 'js', 'media', 'robots', 'favicon', 'html'}


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
