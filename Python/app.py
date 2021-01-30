from flask import Flask, render_template, request, redirect, url_for

# create app
app = Flask(__name__)

# first view
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        return render_template("page1.html", username=username, password=password)
    items = ["menu1", "menu2", "menu3", "menu4", "menu5"]
    return render_template("index.html", items=items)


@app.route("/page1")
def page():
    return render_template("page1.html")


if __name__ == "__main__":
    app.run(debug=True)