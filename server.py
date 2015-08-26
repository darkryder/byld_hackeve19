from flask import Flask, render_template
app = Flask(__name__)
app.my_vars = {'page_count': 0}


@app.route("/")
def counter_home_page():
    app.my_vars['page_count'] += 1
    count = app.my_vars['page_count']
    return render_template("home.html",
                           count_variable_visible_in_template=count)


@app.route("/useless")
def handle():
    return "Doesn't matter if the work's incomplete."

if __name__ == "__main__":
    app.debug = True
    app.run()
