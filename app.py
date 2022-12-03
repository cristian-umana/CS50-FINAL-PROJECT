from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

#hello hi
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

    return render_template("launch.html")

@app.route("/listen")
def listen():
    
    stories = db.execute("SELECT * FROM post ORDER BY post_time")

    advice = db.execute("SELECT * FROM reply ORDER BY reply_time")

    return render_template("listen.html", stories=stories, advice=advice)


@app.route("/tell")
def tell():

    return render_template("tell.html")


@app.route("/tell_story", methods=["GET", "POST"])
def tell_story():

    if request.method == "POST":

        story = request.form.get("tell_story")

        tags = request.form.getlist("tell_tags")

        db.execute("INSERT INTO post(post_entry) VALUES(?)", request.form.get("tell_story"))

        id = db.execute("SELECT post_id FROM post WHERE post_entry = ?", story)[0]["post_id"]

        db.execute("INSERT INTO tags(post_id, tag) VALUES(?, ?)", id, tags)

        return render_template("tell_story.html", story=story)

    else:
        return render_template("tell_story.html")


@app.route("/tell_advice", methods=["GET", "POST"])
def tell_advice():

    if request.method == "POST":

        story = request.form.get("tell_advice")

        tags = request.form.getlist('tell_tags')

        print(tags)

        db.execute("INSERT INTO reply(reply_entry) VALUES(?)", request.form.get("tell_advice"))

        id = db.execute("SELECT reply_id FROM reply WHERE reply_entry = ?", story)[0]["reply_id"]

        for tag in tags: 
             db.execute("INSERT INTO tags(reply_id, tag) VALUES(?, ?)", id, tag)

        return render_template("tell_advice.html", story=story)

    else:
        return render_template("tell_advice.html")



@app.route("/listen_story", methods=["GET", "POST"])
def listen_story():

    tags = request.form.get("listen_tags")

    stories = db.execute("SELECT * FROM post JOIN tags ON post.post_id = tags.post_id WHERE tags.tag = ? ORDER BY post_time", tags)

    return render_template("listen_story.html", stories=stories)


@app.route("/listen_advice", methods=["GET", "POST"])
def listen_advice():

    tags = request.form.getlist("listen_tags")

    advice = db.execute("SELECT * FROM reply JOIN tags ON reply.reply_id = tags.reply_id WHERE tags.tag = ? ORDER BY reply_time", tags)

    return render_template("listen_advice.html", advice=advice)