# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 21:54:33 2020

@author: Arjun
"""

from flask import Flask,render_template 
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("home.html")
@app.route('/hello')
def hello():
    return 'Hello, World'
@app.route('/hello/arjun')
def arjun():
    return 'Ssupp Bitches???'
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)
@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id
@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)
@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

if __name__ == "__main__":
    app.run()