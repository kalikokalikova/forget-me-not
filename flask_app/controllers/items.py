from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.item import Item


# @app.route('/')
# def index():
#     data = { 'users_id': session['user_id'] }
#     upcoming_trips = List.get_upcoming_trips(data)
#     return render_template('index.html', upcoming_trips=upcoming_trips)

#route to add custom item to list