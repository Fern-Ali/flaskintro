from flask import Flask

app = Flask(__name__)


@app.route('/hello')
def say_hello():
    """Return simple "Hello" Greeting."""

    html = "<html><body><h1>Hello</h1></body></html>"
    return html


@app.route('/welcome')
def welcome():
    html = """
    <html><body><h1>Hello</h1>
    <p> Welcome to the site!</p></body></html>
    """
    return html

@app.route('/welcome/home')
def welcomehome():
    html = """
    <html><body><h1>Hello</h1>
    <p> Welcome home!</p></body></html>
    """
    return html


@app.route('/welcome/back')
def welcomeback():
    html = """
    <html><body><h1>Hello</h1>
    <p> Welcome back to the site!</p></body></html>
    """
    return html