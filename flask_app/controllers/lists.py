from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.list import List


@app.route('/')
def index():
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
        #TODO needs to associate default items with this list in the list-items table
        # list.add_default_items({'list_id': list_id})
        # change this to create list, to make it less confusing
        return redirect(f'/edit_trip/{list_id}')
    else:
        #TODO some kind of error messaging
        return redirect('/')

@app.route('/trips')
def show_all_trip():
    data = { 'users_id': session['user_id'] }
    #TODO get trips in order of when they start
    lists = List.get_all(data)
    if lists:
        return render_template('all_trips.html', all_trips=lists)
    else:
        return redirect('/')

@app.route('/edit_trip/<id>')
def view_trip(id):
    trip = List.get_by_id({'id': id})
    if trip:
        return render_template('edit_trip.html', trip=trip)
    else:
        return redirect('/')