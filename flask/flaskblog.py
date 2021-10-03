from flask import Flask, render_template, url_for

app = Flask(__name__)

# dummy data
posts = [
    {
        'author': 'Shashi Bhagat',
        'title': 'Blog Post 1',
        'content': "First post content",
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Rabita Bhagat',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]


@app.route("/")
def hello():
    return """
    <h2>Hello Shashi!</h2>
    <style>
        body {
        background: black;
        } 
        h2 {
            color: #fff;
        }
    </style>
    """


"""
    - map two routes to the same function
"""


@app.route('/about')
@app.route('/about_new')
def about():
    return """
    <h2>About page!!!</h2>
    <style>
        body {
        background: black;
        } 
        h2 {
            text-align: center;
            color: #fff;
        }
    </style>
    """


@app.route("/home")
def home():
    return render_template("home.html", posts=posts, title="Home title")


@app.route("/about_page")
def about_page():
    return render_template("about.html", title="About page")
