"""
    Author : Thibault Chenevière
    Date : 17/09/2021
"""

from flask import Flask, render_template, url_for, request, flash

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template('signup.html')

@app.route("/postLogin", methods=['GET', 'POST'])
def post_login():
    print(request.form)

    return "hello word"

if __name__ == "__main__":
    app.run(debug=True)