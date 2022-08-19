from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.item import Item

@app.route("/add_item", methods = ["POST"])
def add_item_to_db():
    if not Item.validate_item_inputs(request.form):
        list_id = request.form['lists_id']
        return redirect(f"/view_trip/{list_id}")
    else:
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

#routes to page to edit individual item
@app.route("/edit_item/<int:id>")
def edit_item(id):
    if "user_id" not in session: 
        return redirect ("/register_or_login")
    data = {
        'items_id' : id
    }
    return render_template("edit_item.html", item = Item.get_item_by_id(data))

#edits item in db
@app.route("/edit_item_in_db", methods = ["POST"])
def edit_item_in_db():
    if not Item.validate_item_inputs(request.form):
        item_id = request.form["items_id"]
        return redirect(f"/edit_item/{item_id}")
    else:
        data = {
            'name' : request.form['name'],
            'weight' : request.form['weight'],
            'is_packed' : request.form['is_packed'],
            'categories_id' : request.form['categories_id'],
            'lists_id' : request.form['lists_id'],
            'items_id' : request.form['items_id']
        }
        list_id = data['lists_id']
        Item.edit_item_in_db(data)
        return redirect(f"/view_trip/{list_id}")

#delete item in db
@app.route("/delete_item/<int:item_id>/<int:lists_id>")
def delete_item(item_id, lists_id):
    if "user_id" not in session: 
        return redirect ("/register_or_login")
    data = {
        "items_id" : item_id,
        "lists_id" : lists_id
    }
    list_id = data['lists_id']
    Item.delete_item(data)
    return redirect(f"/view_trip/{list_id}")