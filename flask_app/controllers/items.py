from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.item import Item


# @app.route('/')
# def index():
#     data = { 'users_id': session['user_id'] }
#     upcoming_trips = List.get_upcoming_trips(data)
#     return render_template('index.html', upcoming_trips=upcoming_trips)

#route to add custom item to list
@app.route("/add_item", methods = ["POST"])
def add_item_to_db():
    data = {
        'name' : request.form['name'],
        'weight' : request.form['weight'],
        'is_packed' : request.form['is_packed'],
        'categories_id' : request.form['categories_id'],
        'lists_id' : request.form['lists_id']
    }
    list_id = data['lists_id']
    Item.save(data)
    return redirect(f'/view_trip/{list_id}')