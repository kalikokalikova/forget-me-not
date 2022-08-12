from flask_app import app
from flask import render_template, redirect, request, session

@app.route('/')
def index():
    return render_template('index.html')