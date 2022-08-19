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
        self.items = {}

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
        query = "select * from lists where users_id = %(users_id)s and start_date > curdate() ORDER BY start_date DESC;"
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
        query = "SELECT * FROM lists LEFT JOIN items ON items.lists_id = lists.id LEFT JOIN categories ON items.categories_id = categories.id where lists.id= %(id)s ORDER BY categories.name ASC;"
        results = connectToMySQL('camping_list_schema').query_db(query, data)
        # create class instance of List
        list = cls(results[0])
        items = {'eating/drinking': [], 'fire' : [], 'kids' : [], 'miscellaneous': [], 'personal care' : [], 'pets' : [], 'recreation': [], 'sleeping' : [], 'tools' : []}
        for result in results:
            item_data = { 
                'id': result['items.id'],
                'name': result['items.name'],
                'created_at': result['items.created_at'],
                'updated_at': result['updated_at'],
                'lists_id': result['lists_id'],
                'weight': result['weight'],
                'is_packed': result['is_packed'],
                'categories_id': result['categories_id'],
                }
            item = Item(item_data)
            item.category_name = result['categories.name']
            for this_key_name in items:
                if item.category_name == this_key_name:
                    items[this_key_name].append(item)
        list.items = items
        return list

    @classmethod
    def update_list(cls, data):
        print(data)

        list_query = "update lists set name=%(name)s, notes=%(notes)s, start_date=%(start_date)s, end_date=%(end_date)s, zip_code=%(zip_code)s where id=%(list_id)s;"
        result = connectToMySQL('camping_list_schema').query_db(list_query, data)

        for item in data['items']:
            if item[1] == "1":
                Item.associate_item_with_list( { 'list_id': data['list_id'], 'item_id': item[0] })
            else:
                Item.delete_item( { 'items_id': item[0] } )

        return result

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
    
    @classmethod
    def delete_list(cls, data):
        query = "DELETE FROM lists WHERE id = %(id)s;"
        return connectToMySQL('camping_list_schema').query_db(query, data)

    @classmethod
    def total_item_weight(cls, data):
        query = "SELECT * FROM items WHERE lists_id = %(id)s"
        results = connectToMySQL('camping_list_schema').query_db(query, data)
        total_weight = 0
        for result in results:
            this_weight = result['weight']
            total_weight += float(this_weight)
        return total_weight