from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash


# Configure application
app = Flask(__name__)

# Custom filter
#app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
#app.config["SESSION_PERMANENT"] = False
#app.config["SESSION_TYPE"] = "filesystem"
#Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///posts.db")


@app.route("/")
def launch():
    #things go here
    return render_template("launch.html")

@app.route("/listen")
def listen():
    #things go here
    stories = db.execute("SELECT * FROM post ORDER BY post_time")

    return render_template("listen.html", stories=stories)


@app.route("/tell", methods=["GET", "POST"])
def tell():
    #things go here
    if request.method == "POST":

        story = request.form.get("tell")

        db.execute("INSERT INTO post(post_entry) VALUES(?)", request.form.get("tell"))

        return render_template("tell.html", story=story)

    else:
        return render_template("tell.html")


#@app.route("/tell", methods=["GET", "POST"])
#def tell():
    #things go here
#    return render_template("tell.html")

#@app.route("/listen", methods=["GET", "POST"])
#@login_required
#def listen():
    #things go here
#    return render_template("listen.html")