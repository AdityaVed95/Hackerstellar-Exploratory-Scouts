from flask import Flask, render_template, url_for, request, session, redirect , send_file
from flask_session import Session

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello"