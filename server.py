from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def counter_home_page():
    return render_template("home.html")


@app.route("/useless")
def handle():
    return "Doesn't matter if the work's incomplete."

if __name__ == "__main__":
    app.debug = True
    app.run()
