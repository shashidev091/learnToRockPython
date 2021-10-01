from flask import Flask

app = Flask(__name__)


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
