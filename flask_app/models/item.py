from config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import default_items

class Item:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.weight = data['weight']
        self.is_packed = data['is_packed']
        self.categories_id = data['categories_id']
        self.category_name = None
        self.list_id = data['lists_id']

    car = default_items.DEFAULT_CAR_ITEMS
    backpacking = default_items.DEFAULT_BACKPACKING_ITEMS
    RV = default_items.DEFAULT_RV_ITEMS

    @classmethod
    def save(cls, data):
        query = "insert into items (name, weight, is_packed, categories_id, lists_id) values ( %(name)s, %(weight)s, %(is_packed)s, %(categories_id)s, %(lists_id)s );"
        result = connectToMySQL('camping_list_schema').query_db(query, data)
        return result

    @classmethod
    def get_all_by_list_id(cls, data):
        query = "select * where lists_id = %(lists_id)s;"
        result = connectToMySQL('camping_list_schema').query_db(query, data)
        return result

    @classmethod
    def create_default_items(cls, list_id, trip_type):
        item_ids = []
        print(f"here is {trip_type}!!!!!!")
        if trip_type == "1":
            cls.default_list = cls.car
        elif trip_type == "2":
            cls.default_list = cls.backpacking
        elif trip_type == "3":
            cls.default_list = cls.RV
        for default_item in cls.default_list:
            default_item['lists_id'] = list_id
            item_id = Item.save(default_item)
            item_ids.append(item_id)
        #TODO there should be some kind of database exception checking here, return true or false. For now, just returning list of ids because that might be useful?
        return item_ids

    @classmethod
    def get_item_by_id(cls, data):
        query = "select * from items LEFT JOIN categories ON items.categories_id = categories.id where items.id=%(items_id)s;"
        results = connectToMySQL('camping_list_schema').query_db(query, data)
        this_item_object = cls(results[0])
        this_item_object.category_name = results[0]["categories.name"]
        return this_item_object
    
    @classmethod
    def edit_item_in_db(cls, data):
        query = "UPDATE items SET name = %(name)s, weight = %(weight)s, is_packed = %(is_packed)s, categories_id = %(categories_id)s WHERE items.id = %(items_id)s;"
        return connectToMySQL('camping_list_schema').query_db(query, data)

    @classmethod
    def delete_item(cls, data):
        query = "DELETE FROM items WHERE id = %(items_id)s;"
        return connectToMySQL('camping_list_schema').query_db(query, data)

    @classmethod
    def associate_item_with_list(cls, data):
        query = "update items set lists_id = %(list_id)s where id = %(item_id)s;"
        return connectToMySQL('camping_list_schema').query_db(query, data)

    @staticmethod
    def validate_item_inputs(data):
        is_valid = True
        if len(data['name']) < 2:
            is_valid = False
            flash("Item name must be two or more characters.")
        if len(data['weight']) < 1:
            is_valid = False
            flash("Item must have a weight")
        return is_valid