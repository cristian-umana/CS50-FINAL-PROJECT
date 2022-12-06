#import matplotlib.pyplot as plt
#import numpy as np
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request

# Configure applicationfasl
app = Flask(__name__)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///posts.db")

# Launch Page
@app.route("/")
def launch():

    return render_template("launch.html")


# About Page
@app.route("/about")
def about():

#Archived Implementation of PyPlot 

    #moodtable_raw = db.execute("SELECT tag FROM tags")

    #mt = []
    #for dic in moodtable_raw:
    #    mt.append(dic["tag"])
    #print(mt)

    return render_template("about.html")


# Listen Page
@app.route("/listen")
def listen():

    #query getting info from post.db, "tags" table
    moodgraph = db.execute("SELECT * FROM tags LIMIT 100")
    
    #query getting info from post.db, "posts" table
    stories = db.execute("SELECT * FROM post ORDER BY post_time DESC")

    #query getting info from post.db, "reply" table
    advice = db.execute("SELECT * FROM reply ORDER BY reply_time DESC")

    #pass stories, advice, moodgraph to listen.html
    return render_template("listen.html", stories=stories, advice=advice, moodgraph=moodgraph)

# Tell Page
@app.route("/tell")
def tell():

    return render_template("tell.html")

# Tell Story Page
@app.route("/tell_story", methods=["GET", "POST"])
def tell_story():

    #variable storing text entry
    story = request.form.get("tell_story")

    if request.method == "POST":

        #variable storing tag entries
        tags = request.form.getlist("tell_tags")

        #insert post entries
        db.execute("INSERT INTO post(post_entry) VALUES(?)", request.form.get("tell_story"))

        #variable storing new post id
        id = db.execute("SELECT post_id FROM post WHERE post_entry = ?", story)[0]["post_id"]

        #insert tag entries
        for tag in tags: 
            db.execute("INSERT INTO tags(post_id, tag) VALUES(?, ?)", id, tag)

        #direct to listen.html upon submit
        return redirect("/listen")

    else:
        #pass "story" to tell_story.html
        return render_template("tell_story.html", story=story)


# Tell Advice Page
@app.route("/tell_advice", methods=["GET", "POST"])
def tell_advice():

    #variable storing text entry
    story = request.form.get("tell_advice")

    if request.method == "POST":

        #variable storing tag entries
        tags = request.form.getlist('tell_tags')

        #insert post entries
        db.execute("INSERT INTO reply(reply_entry) VALUES(?)", request.form.get("tell_advice"))

        #variable storing new reply id
        id = db.execute("SELECT reply_id FROM reply WHERE reply_entry = ?", story)[0]["reply_id"]

        #insert tag entries
        for tag in tags: 
             db.execute("INSERT INTO tags(reply_id, tag) VALUES(?, ?)", id, tag)

        #direct to listen.html upon submit
        return redirect("/listen")

    else:
        #pass "story" to tell_advice.html
        return render_template("tell_advice.html", story=story)



@app.route("/listen_story", methods=["GET", "POST"])
def listen_story():

    #query getting info from post.db, "tags" table
    moodgraph = db.execute("SELECT * FROM tags LIMIT 100")

    #variable storing tag entry
    tags = request.form.get("listen_tags")

    #variable storing query info: post entry, date_time, tags where tag corresponds to user selected tag ("tags")
    stories = db.execute("SELECT * FROM post JOIN tags ON post.post_id = tags.post_id WHERE tags.tag = ? ORDER BY post_time DESC", tags)

    #pass "moodgraph" and "story" to listen_story.html
    return render_template("listen_story.html", stories=stories, moodgraph=moodgraph)


@app.route("/listen_advice", methods=["GET", "POST"])
def listen_advice():

    #query getting info from post.db, "tags" table
    moodgraph = db.execute("SELECT * FROM tags LIMIT 100")

    #variable storing tag entry
    tags = request.form.get("listen_tags")
   
    #variable storing query info: reply entry, date_time, tags where tag corresponds to user selected tag ("tags")
    advice = db.execute("SELECT * FROM reply JOIN tags ON reply.reply_id = tags.reply_id WHERE tags.tag = ? ORDER BY reply_time DESC", tags)

    #pass "moodgraph" and "story" to listen_advice.html
    return render_template("listen_advice.html", advice=advice, moodgraph=moodgraph)