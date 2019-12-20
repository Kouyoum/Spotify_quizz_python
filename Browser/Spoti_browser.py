# IMPORT MODULES FOR ALL THE PROJECT
import spotipy, requests, json, time, pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import random as random
import time as time
import sys
import os
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

# IMPORT QUESTIONS
# from Interaction_API import Quizz

# IMPORT FLASK AND MODULES FOR HTML
import webbrowser
from threading import Timer
from flask import Flask, render_template, request, url_for
from IPython.display import HTML
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import Navbar, Subgroup, View

# Import of our modules
import Quizz_test
import Backend
import authorization

# cid ="11e754c7548240e7a02e1b59ec07b2f9"
# secret = "c3922e0fbd1b4c57ba9f0c32366a7fe8"
# username = "11100731824"

#AUTHORIZATION FLOW WHICH WILL DISAPPEAR, REPLACED BY AUTH FUNCTION
sp, token = authorization.authorization()
username = Backend.find_username_user()
#print(token)
#print(sp)



""" STRART OF THE APP"""
app = Flask("Flask")

# For the navigation bar and other styling purposes
Bootstrap(app)
nav = Nav(app)

# sp, token = authorization.authorization()

""" ROUTES"""
@nav.navigation('mysite_navbar')
def create_navbar():
    home_view = View('Home', 'home')
    about_view = View('About our Project', 'about')
    summary_view = View('Summary', 'summary')
    #misc_subgroup = Subgroup('Other', about_view, summary_view)

    return Navbar('Python Project',
                    home_view,
                    about_view,
                    summary_view)



"""Main page, start of the quizz"""
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


def open_browser():
    """
    """
    webbrowser.open_new('http://127.0.0.1:5090/')

count = 0

@app.route("/question1", methods = ['POST', 'GET'])
def question1():
    #genre = Quizz_test.question1()
    # answers = Backend.get_genres()
    # #genre_cat = HTML(answers.to_html(classes = 'table table-striped'))
    correct1, id, track, artist = Quizz_test.question1_a()
    link = "https://open.spotify.com/embed/track/" + id
    global count
    count = 0
    if request.method == 'POST':
        answer1 = request.form['answer1']
        correct1 = request.form['correct1']
        link = request.form['link']

        ratio = Quizz_test.question1_b(answer1, correct1)

        return render_template("answer1.html", correct1 = correct1, answer1 = answer1, count = count, link = link, ratio = ratio)

    return render_template("question1.html", track = track, artist = artist, link = link, correct1 = correct1)




@app.route("/question2", methods = ['POST', 'GET'])
def question2():
    answers, artists, correct2, id = Quizz_test.question2()

    link = "https://open.spotify.com/embed/track/" + id
    global count
    if request.method == 'POST':
        answer2 = request.form['answer2']
        correct2 = request.form['correct2']
        link = request.form['link']
        # modify the count variable
        if answer2 == correct2:
            count += 1

        return render_template("answer2.html", correct2 = correct2, answer2 = answer2, count = count, link = link)

    return render_template("question2.html", answers = answers, correct2 = correct2, link = link)


@app.route("/question3", methods = ['POST', 'GET'])
def question3():
    album, artist, answers, correct3, id = Quizz_test.question3()

    link = "https://open.spotify.com/embed/track/" + id
    global count
    if request.method == 'POST':
        answer3 = request.form['answer3']
        correct3 = request.form['correct3']
        album = request.form['album']
        artist = request.form['artist']
        link = request.form['link']
        # modify the count variable
        if answer3 == correct3:
            count += 1

        return render_template("answer3.html", correct3 = correct3, answer3 = answer3, album = album, artist = artist, count = count, link = link)

    return render_template("question3.html", answers = answers, correct3 = correct3, album = album, artist = artist, link = link)


@app.route("/question4", methods = ['POST', 'GET'])
def question4():
    """
    Question on explicit content
    """
    correct4, answers = Quizz_test.question4()
    global count

    if request.method == 'POST':
        # use getlist to see the list of checkboxes checked by the user
        answer4 = request.form['answer4']
        correct4 = request.form['correct4']

        if answer4 == correct4:
            count += 1

        return render_template("answer4.html", answer4 = answer4, correct4 = correct4, count = count)

    return render_template("question4.html", correct4 = correct4, answers = answers)


@app.route("/question6", methods = ['POST', 'GET'])
def question6():
    answers, correct6, id = Quizz_test.question6()
    link = "https://open.spotify.com/embed/track/" + id
    global count

    if request.method == 'POST':
        answer6 = request.form['answer6']
        correct6 = request.form['correct6']
        link = request.form['link']
        global count
        if answer6 == correct6:
            count += 1
        return render_template("answer6.html", correct6 = correct6, answer6 = answer6, count = count, link = link)

    return render_template("question6.html", answers = answers, correct6 = correct6, link = link)



@app.route("/end", methods = ['POST', 'GET'])
def end():
    global count
    return render_template("end.html", count = count)


@app.route("/summary", methods = ['POST', 'GET'])
def summary():
    user_tracks = Backend.user_top_tracks()
    # here, we keep the most important attributes
    summary = user_tracks.loc[:,['Track', 'Artist', 'Explicit', 'Album Name', 'Album Year']]
    # Pandas Dataframe transformed to fit the HTML format
    html_user_tracks = HTML(summary.to_html(classes = 'table table-striped'))

    #sp.user_playlist_create(username, name='TOP 50 TRACKS', public = True)
    #sp.user_playlist_add_tracks(username, playlist_id= Backend.playlist()['Playlist ID'][0], tracks= user_tracks['Track ID'], position=None)
    return render_template("summary.html", html_user_tracks = html_user_tracks)

# https://medium.com/fintechexplained/flask-host-your-python-machine-learning-model-on-web-b598151886d



# ROUTES SPOTIFY
# @app.route("/spotify")
# def spoti_access():
#     genres = sp.recommendation_genre_seeds()
#     rand = random.sample(genres["genres"],4)
#
#     # genre_test = genres['genres'][i-1]
#     return str(rand)

# @app.route("/test")
# def test():
#     return test(inform_me())

# GIVE OUT INFORMATION ABOUT THE BROWSER, QUIZZ
@app.route("/about")
def about():
    return render_template('about.html')






if __name__ == "__main__":
    # Timer(1, open_browser).start();
    app.run(port = 5090, debug=True)
