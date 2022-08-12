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
    # We need to send the user id with this
    if List.validate_inputs(request.form):
        data = {
            'users_id': session['user_id'],
            'name': request.form['name'],
            'notes': request.form['notes'],
            'start_date': request.form['start_date'],
            'end_date': request.form['end_date'],
            'zip_code': request.form['zip_code']
            }
        List.save(data)
        return redirect('/all-lists')
    else:
        return redirect('/')

@app.route('/all-lists')
def all_lists():
    print("we wade it")
    return redirect('/')
    # lists = List.get_all()
    # if lists:
    #     return render_template('all_lists.html')
    # else:
    #     return redirect('/')