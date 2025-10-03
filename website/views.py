from flask import Blueprint, render_template, url_for, jsonify
import json
uf = url_for

bp = Blueprint
rt = render_template

views = bp('views', __name__)

@views.route("/")
def home():
    with open('website/static/data.json') as f:
        data = json.load(f)
    return render_template("base.html",  data=data)
