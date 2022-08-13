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
        #TODO create and return classes here
        return results

    @classmethod
    def get_all(cls, data):
        query = "select * from lists where users_id = %(users_id)s;"
        results = connectToMySQL('camping_list_schema').query_db(query, data)
        #TODO create and return classes here
        return results

    @classmethod
    def get_by_id(cls, data):
        query = "select * from lists left join items on items.lists_id = lists.id where lists.id=%(id)s;"
        results = connectToMySQL('camping_list_schema').query_db(query, data)
        list = cls(results[0])
        items = []
        #TODO is the right way to do this? HALP I don't know
        for result in results:
            item_data = { 
                'id': ['items.id'],
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
        print(list.items)
        return list

    @staticmethod
    def validate_inputs(data):
        #TODO think about and write this code
        return True