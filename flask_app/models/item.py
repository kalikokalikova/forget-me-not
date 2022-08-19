from config.mysqlconnection import connectToMySQL
from flask import flash

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

    DEFAULT_ITEMS = [
        { 'name': 'sleeping bag', 'weight': 2.0, 'is_packed': 0, 'categories_id': 2 },
        { 'name': 'tent', 'weight': 3.5, 'is_packed': 0, 'categories_id': 2 },
        { 'name': 'stakes', 'weight': 1.0, 'is_packed': 0, 'categories_id': 2 },
        { 'name': 'sleeping pad', 'weight': 1.5, 'is_packed': 0, 'categories_id': 2 },
        { 'name': 'knife', 'weight': 0.2, 'is_packed': 0, 'categories_id': 4 },
        { 'name': 'flashlight', 'weight': 0.5, 'is_packed': 0, 'categories_id': 4 },
        { 'name': 'lighter', 'weight': 0.2, 'is_packed': 0, 'categories_id': 5 },
        { 'name': 'multitool', 'weight': 0.3, 'is_packed': 0, 'categories_id': 4 },
        { 'name': 'headlamp', 'weight': 0.2, 'is_packed': 0, 'categories_id': 4 },
        { 'name': 'first aid kit', 'weight': 0.2, 'is_packed': 0, 'categories_id':3 },
        { 'name': 'sunscreen', 'weight': 0.5, 'is_packed': 0, 'categories_id':3 },
        { 'name': 'towel', 'weight': 1.0, 'is_packed': 0, 'categories_id':3 },
        { 'name': 'sunglasses', 'weight': 0.5, 'is_packed': 0, 'categories_id':3 },
        { 'name': 'hat', 'weight': 0.1, 'is_packed': 0, 'categories_id':3 },
        { 'name': 'jacket', 'weight':3.0, 'is_packed': 0, 'categories_id':3 },
        { 'name': 'clothes', 'weight': 5.0, 'is_packed': 0, 'categories_id':3 },
        { 'name': 'toilet paper', 'weight': 1.0, 'is_packed': 0, 'categories_id':3 },
        { 'name': 'prescription meds', 'weight': 0.2, 'is_packed': 0, 'categories_id':3 },
        { 'name': 'chapstick', 'weight': 0.01, 'is_packed': 0, 'categories_id':3 },
        { 'name': 'santitation trowel', 'weight': 1.5, 'is_packed': 0, 'categories_id':3 },
        { 'name': 'wood', 'weight': 15.0, 'is_packed': 0, 'categories_id': 5 },
        { 'name': 'baby wipes', 'weight': 0.2, 'is_packed': 0, 'categories_id':3 },
        { 'name': 'swimming suit', 'weight': 0.1, 'is_packed': 0, 'categories_id': 6 },
        { 'name': 'hiking boots', 'weight': 2.0, 'is_packed': 0, 'categories_id': 6 },
        { 'name': 'hiking backpack', 'weight': 2.0, 'is_packed': 0, 'categories_id': 6 },
        { 'name': 'water bottle', 'weight': 0.5, 'is_packed': 0, 'categories_id': 7 },
        { 'name': 'camp stove', 'weight': 5.0, 'is_packed': 0, 'categories_id': 7 },
        { 'name': 'mess kit', 'weight': 2.0, 'is_packed': 0, 'categories_id': 7 },
        { 'name': 'paper towels', 'weight': 1.0, 'is_packed': 0, 'categories_id': 7 },
        { 'name': 'utensils', 'weight': 1.0, 'is_packed': 0, 'categories_id': 7 },
        { 'name': 'cups', 'weight': 1.0, 'is_packed': 0, 'categories_id': 7 },
        { 'name': 'bowls', 'weight': 1.0, 'is_packed': 0, 'categories_id': 7 },
        { 'name': 'cooler', 'weight': 5.0, 'is_packed': 0, 'categories_id': 7 },
        { 'name': 'pots and pans', 'weight': 5.0, 'is_packed': 0, 'categories_id': 7 },
        { 'name': 'stove fuel', 'weight': 5.0, 'is_packed': 0, 'categories_id': 7 },
        { 'name': 'hand sanitizer', 'weight': 0.1, 'is_packed': 0, 'categories_id': 7 },
        { 'name': 'cooking knife', 'weight': 0.2, 'is_packed': 0, 'categories_id': 7 },
        { 'name': 'trash bags', 'weight': 1.0, 'is_packed': 0, 'categories_id': 7 },
        { 'name': 'dish towel', 'weight': 0.5, 'is_packed': 0, 'categories_id': 7 },
        { 'name': 'coffee maker', 'weight': 2.0, 'is_packed': 0, 'categories_id': 7 },
        { 'name': 'food storage bags', 'weight': 0.5, 'is_packed': 0, 'categories_id': 7 },
        { 'name': 'water bowl', 'weight': 1.0, 'is_packed': 0, 'categories_id': 9 },
        { 'name': 'leash', 'weight': 0.2, 'is_packed': 0, 'categories_id': 9 },
        { 'name': 'pet food', 'weight': 2.0, 'is_packed': 0, 'categories_id': 9 },
        { 'name': 'poop bags', 'weight': 0.2, 'is_packed': 0, 'categories_id': 9 }
    ]
    
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
    def create_default_items(cls, list_id):
        item_ids = []
        for default_item in cls.DEFAULT_ITEMS:
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