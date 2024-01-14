from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    movies = range(8)
    return render_template("homepage.html", movies=movies)