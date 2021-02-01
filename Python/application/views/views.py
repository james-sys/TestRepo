from flask import Blueprint, render_template, request

views = Blueprint("views", __name__)


@views.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        return render_template("page1.html", username=username, password=password)
    items = ["menu1", "menu2", "menu3", "menu4", "menu5"]
    return render_template("index.html", items=items)
