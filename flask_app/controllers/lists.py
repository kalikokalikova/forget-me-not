from flask_app import app
from flask import render_template, redirect, request, session

@app.route('/dashboard')
def index():
    return render_template('dashboard.html')