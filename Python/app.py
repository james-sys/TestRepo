from flask import Flask, render_template

# create app
app = Flask(__name__)

# first view
@app.route("/")
def index():
    items = ["menu1", "menu2", "menu3", "menu4", "menu5"]
    return render_template("index.html", items=items)


if __name__ == "__main__":
    app.run()