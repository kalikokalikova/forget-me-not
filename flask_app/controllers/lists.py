from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.list import List
from flask_app.models.item import Item
import requests
import os


@app.route('/')
def index():
    if "user_id" not in session: 
        return redirect ("/register_or_login")
    data = { 'users_id': session['user_id'] }
    upcoming_trips = List.get_upcoming_trips(data)
    return render_template('index.html', upcoming_trips=upcoming_trips)

# validate and save list route POST
@app.route('/save-list', methods=['post'])
def validate_and_save_list():
    if List.validate_inputs(request.form):
        data = {
            'users_id': session['user_id'],
            'name': request.form['name'],
            'notes': request.form['notes'],
            'start_date': request.form['start_date'],
            'end_date': request.form['end_date'],
            'zip_code': request.form['zip_code']
            }
        list_id = List.save(data)
        return redirect(f'/edit_trip/{list_id}')
    else:
        #get flashed messages from HTML
        return redirect('/')

@app.route('/trips')
def show_all_trip():
    if "user_id" not in session: 
        return redirect ("/register_or_login")
    data = { 'users_id': session['user_id'] }
    lists = List.get_all(data)
    if lists:
        return render_template('all_trips.html', all_trips=lists)
    else:
        return redirect('/')

@app.route('/edit_trip/<id>')
def edit_trip(id):
    if "user_id" not in session: 
        return redirect ("/register_or_login")
    trip = List.get_by_id({'id': id})
    

    
    if not trip: # if trip doesn't exist, db error, etc
        return redirect('/') # redirect to home with TODO error messaging
    if len(trip.items) == 0: # if trip has no items
        trip.items = Item.create_default_items( {'list_id': trip.id} )
    # if neither of these other two things is the case: trip has items associated in database
    return render_template('edit_trip.html', trip=trip)

@app.route('/update_list', methods=['post'])
def update_list():
    # create a dictionary from the form data that is mutable so I can pop out values
    form_data = request.form.to_dict()

    #It might make sense to move all this munging into the model TODO
    data = { # Popping these values out of the data so all that's left is the items to be updated
        'list_id': form_data.pop('list_id'),
        'name': form_data.pop('name'),
        'notes': form_data.pop('notes'),
        'start_date': form_data.pop('start_date'),
        'end_date': form_data.pop('end_date'),
        'zip_code': form_data.pop('zip_code')
    }

    items = [] # create empty array to hold the ids of items which are checked
    for item in form_data.items(): # Looping through the values left in the data (which should only be item tuples)
        items.append(item) # save item tuple to array

    data['items'] = items # attach array of item_ids to data to be sent to model method
    list_id = List.update_list(data)

    return redirect(f'/view_trip/{request.form["list_id"]}')

@app.route('/view_trip/<id>')
def view_trip(id):
    if "user_id" not in session: 
        return redirect ("/register_or_login")
    data = {
        'id': id
    }
    trip = List.get_by_id(data)
    total_weight = List.total_item_weight(data)
    return render_template('view_trip.html', trip=trip, total_weight=total_weight)

@app.route('/delete_trip/<int:id>')
def delete_trip(id):
    if "user_id" not in session: 
        return redirect ("/register_or_login")
    data = {
        "id" : id
    }
    List.delete_list(data)
    return redirect("/trips")

@app.route("/weather/<int:list_id>/<int:zip_code>")
def show_weather_report(list_id, zip_code):
    r = requests.get(f"http://api.openweathermap.org/data/2.5/forecast?zip={zip_code},us&appid={os.environ.get('WEATHER_API_KEY')}&units=imperial")
    trip = List.get_by_id({ 'id': list_id })
    print(r.json())
    return render_template("weather.html", forecast = r.json(), trip=trip)