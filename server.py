from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)
app.my_vars = {'page_count': 0, 'button_count': 0, 'trust': False}

ADMIN_EMAIL = "a@b.com"
ADMIN_PWD = "pwd"


@app.route("/")
def counter_home_page():
    app.my_vars['page_count'] += 1
    count = app.my_vars['page_count']
    button_count = app.my_vars['button_count']
    trust = app.my_vars['trust']
    return render_template("home.html",
                           count_variable_visible_in_template=count,
                           i_trust_you=trust,
                           button_count=button_count)


@app.route("/increment")
def button_pressed():
    app.my_vars['button_count'] += 1
    return redirect(url_for('counter_home_page'))


@app.route("/login", methods=["GET", "POST"])
def login():
    method = request.method
    email = request.form.get("email")
    password = request.form.get("password")
    if method == "POST" and email == ADMIN_EMAIL and password == ADMIN_PWD:
        app.my_vars['trust'] = True
        return redirect(url_for('counter_home_page'))
    return render_template("login.html")


@app.route("/useless")
def handle():
    return "Doesn't matter if the work's incomplete."

if __name__ == "__main__":
    app.debug = True
    app.run()
