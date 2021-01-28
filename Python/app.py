from flask import Flask

# create app
app = Flask(__name__)

# first view
@app.route("/")
def index():
    return "Message for the app First View"


if __name__ == "__main__":
    app.run()