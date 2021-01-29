from flask import Flask, render_template

# create app
app = Flask(__name__)

# first view
@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()