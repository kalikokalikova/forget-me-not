from config.mysqlconnection import connectToMySQL
from flask_app.models.item import Item
from flask import flash

class List:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.owner = data['users_id']
        self.notes = data['notes']
        self.start_date = data['start_date']
        self.end_date = data['end_date']
        self.zip_code = data['zip_code']
        self.items = []

    @classmethod
    def save(cls, data):
        query = "insert into lists (name, users_id, notes, start_date, end_date, zip_code) values ( %(name)s, %(users_id)s, %(notes)s, %(start_date)s, %(end_date)s, %(zip_code)s );"
        list_id = connectToMySQL('camping_list_schema').query_db(query, data)
        if list_id:
            # create default items and attach to list
            items = Item.create_default_items(list_id)
        return list_id

    @classmethod
    def get_upcoming_trips(cls, data):
        query = "select * from lists where users_id = %(users_id)s and start_date > curdate();"
        results = connectToMySQL('camping_list_schema').query_db(query, data)
        if len(results) == 0:
            return []
        else:
            trip_list = []
            for this_trip_dictionary in results:
                this_trip_object = cls(this_trip_dictionary)
                trip_list.append(this_trip_object)
            return trip_list

    @classmethod
    def get_all(cls, data):
        query = "select * from lists where users_id = %(users_id)s order by start_date desc;"
        results = connectToMySQL('camping_list_schema').query_db(query, data)
        if len(results) == 0:
            return []
        else:
            trip_list = []
            for this_trip_dictionary in results:
                this_trip_object = cls(this_trip_dictionary)
                trip_list.append(this_trip_object)
            return trip_list

    @classmethod
    def get_by_id(cls, data):
        # query with join to get all the items associated with this list
        query = "select * from lists left join items on items.lists_id = lists.id where lists.id=%(id)s;"
        results = connectToMySQL('camping_list_schema').query_db(query, data)
        # create class instance of List
        list = cls(results[0])
        if results[0]['items.id'] == None: # List has no items
            return list # Return list where items is an empty list
        else: # Create list of items and append to List instance
            items = []
            for result in results:
                item_data = { 
                    'id': result['items.id'],
                    'name': result['items.name'],
                    'created_at': result['items.created_at'],
                    'updated_at': result['updated_at'],
                    'lists_id': result['lists_id'],
                    'weight': result['weight'],
                    'is_packed': result['is_packed'],
                    'categories_id': result['categories_id'] }
                item = Item(item_data)
                items.append(item)
            list.items = items
            return list # Return a List instance with array of items attached

    @classmethod
    def update_list(cls, danta):
        pass

    @staticmethod
    def validate_inputs(data):
        is_valid = True
        if len(data['name']) < 2:
            is_valid = False
            flash("Trip name must be at least 2 characters.")
        if data['start_date'] > data['end_date']:
            is_valid = False
            flash("Start date must be before end date.")
        return is_valid