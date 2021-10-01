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


