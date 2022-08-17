from config.mysqlconnection import connectToMySQL

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
        { 'name': 'tarp', 'weight': 2.0, 'is_packed': 0, 'categories_id': 2 },
        { 'name': 'stakes', 'weight': 1.0, 'is_packed': 0, 'categories_id': 2 },
        { 'name': 'air mattress', 'weight': 10.0, 'is_packed': 0, 'categories_id': 2 },
        { 'name': 'sleeping pad', 'weight': 1.5, 'is_packed': 0, 'categories_id': 2 },
        { 'name': 'cot', 'weight': 10.0, 'is_packed': 0, 'categories_id': 2 },
        { 'name': 'blanket', 'weight': 1.0, 'is_packed': 0, 'categories_id': 2 },
        { 'name': 'pillow', 'weight': 0.5, 'is_packed': 0, 'categories_id': 2 },
        { 'name': 'mattress pump', 'weight': 1.0, 'is_packed': 0, 'categories_id': 3 },
        { 'name': 'hammer', 'weight': 1.0, 'is_packed': 0, 'categories_id': 4 },
        { 'name': 'knife', 'weight': 0.2, 'is_packed': 0, 'categories_id': 4 },
        { 'name': 'lantern', 'weight': 2.0, 'is_packed': 0, 'categories_id': 4 },
        { 'name': 'flashlight', 'weight': 0.5, 'is_packed': 0, 'categories_id': 4 },
        { 'name': 'roasting sticks', 'weight': 0.5, 'is_packed': 0, 'categories_id': 4 },
        { 'name': 'lighter', 'weight': 0.2, 'is_packed': 0, 'categories_id': 4 },
        { 'name': 'multitool', 'weight': 0.3, 'is_packed': 0, 'categories_id': 4 },
        { 'name': 'headlamp', 'weight': 0.2, 'is_packed': 0, 'categories_id': 4 },
        { 'name': 'navigation device', 'weight': 0.1, 'is_packed': 0, 'categories_id': 4},
        { 'name': 'phone charger', 'weight': 0.1, 'is_packed': 0, 'categories_id': 4 },
        { 'name': 'mattress repair kit', 'weight': 0.1, 'is_packed': 0, 'categories_id': 4 },
        { 'name': 'can opener', 'weight': 0.2, 'is_packed': 0, 'categories_id': 4 },
        { 'name': 'bottle opener', 'weight': 0.2, 'is_packed': 0, 'categories_id': 3 },
        { 'name': 'fire starter', 'weight': 0.1, 'is_packed': 0, 'categories_id': 5 },
        { 'name': 'wood', 'weight': 15.0, 'is_packed': 0, 'categories_id': 5 },
        { 'name': 'kindling', 'weight': 3.0, 'is_packed': 0, 'categories_id': 5 },
        { 'name': 'first aid kit', 'weight': 0.2, 'is_packed': 0, 'categories_id': 2 },
        { 'name': 'bear spray', 'weight': 0.5, 'is_packed': 0, 'categories_id': 2 },
        { 'name': 'sunscreen', 'weight': 0.5, 'is_packed': 0, 'categories_id': 2 },
        { 'name': 'citronella candle', 'weight': 1.0, 'is_packed': 0, 'categories_id': 2 },
        { 'name': 'shampoo/conditioner', 'weight': 0.5, 'is_packed': 0, 'categories_id': 2 },
        { 'name': 'hairbrush', 'weight': 0.5, 'is_packed': 0, 'categories_id': 2 },
        { 'name': 'toothbrush', 'weight': 0.1, 'is_packed': 0, 'categories_id': 2 },
        { 'name': 'toothpaste', 'weight': 0.1, 'is_packed': 0, 'categories_id': 2 },
        { 'name': 'soap', 'weight': 0.1, 'is_packed': 0, 'categories_id': 2 },
        { 'name': 'towel', 'weight': 1.0, 'is_packed': 0, 'categories_id': 2 },
        { 'name': 'hair dryer', 'weight': 3.0, 'is_packed': 0, 'categories_id': 2 },
        { 'name': 'sunglasses', 'weight': 0.5, 'is_packed': 0, 'categories_id': 2 },
        { 'name': 'hat', 'weight': 0.1, 'is_packed': 0, 'categories_id': 2 },
        { 'name': 'jacket', 'weight': 2.0, 'is_packed': 0, 'categories_id': 2 },
        { 'name': 'clothes', 'weight': 5.0, 'is_packed': 0, 'categories_id': 2 },
        { 'name': 'clothesline', 'weight': 0.1, 'is_packed': 0, 'categories_id': 2 },
        { 'name': 'broom and dustpan', 'weight': 1.0, 'is_packed': 0, 'categories_id': 2 },
        { 'name': 'toilet paper', 'weight': 1.0, 'is_packed': 0, 'categories_id': 2 },
        { 'name': 'prescription meds', 'weight': 0.2, 'is_packed': 0, 'categories_id': 2 },
        { 'name': 'chapstick', 'weight': 0.01, 'is_packed': 0, 'categories_id': 2 },
        { 'name': 'santitation trowel', 'weight': 1.5, 'is_packed': 0, 'categories_id': 2 },
        { 'name': 'baby wipes', 'weight': 0.2, 'is_packed': 0, 'categories_id': 2 },
        { 'name': 'quarters for shower', 'weight': 0.2, 'is_packed': 0, 'categories_id': 2 },
        { 'name': 'swimming suit', 'weight': 0.1, 'is_packed': 0, 'categories_id': 6 },
        { 'name': 'bike', 'weight': 18.0, 'is_packed': 0, 'categories_id': 6 },
        { 'name': 'helmet', 'weight': 1.0, 'is_packed': 0, 'categories_id': 6 },
        { 'name': 'fishing pole', 'weight': 1.0, 'is_packed': 0, 'categories_id': 6 },
        { 'name': 'camp chairs', 'weight': 5, 'is_packed': 0, 'categories_id': 6 },
        { 'name': 'hiking boots', 'weight': 2.0, 'is_packed': 0, 'categories_id': 6 },
        { 'name': 'hiking backpack', 'weight': 2.0, 'is_packed': 0, 'categories_id': 6 },
        { 'name': 'hammock', 'weight': 0.5, 'is_packed': 0, 'categories_id': 6 },
        { 'name': 'book', 'weight': 0.5, 'is_packed': 0, 'categories_id': 6 },
        { 'name': 'board game', 'weight': 0.5, 'is_packed': 0, 'categories_id': 6 },
        { 'name': 'beach towels', 'weight': 2.0, 'is_packed': 0, 'categories_id': 6 },
        { 'name': 'water bottle', 'weight': 0.5, 'is_packed': 0, 'categories_id': 7 },
        { 'name': 'camp stove', 'weight': 5.0, 'is_packed': 0, 'categories_id': 7 },
        { 'name': 'water filter', 'weight': 0.5, 'is_packed': 0, 'categories_id': 7 },
        { 'name': 'mess kit', 'weight': 2.0, 'is_packed': 0, 'categories_id': 7 },
        { 'name': 'paper towels', 'weight': 1.0, 'is_packed': 0, 'categories_id': 7 },
        { 'name': 'utensils', 'weight': 1.0, 'is_packed': 0, 'categories_id': 7 },
        { 'name': 'cups', 'weight': 1.0, 'is_packed': 0, 'categories_id': 7 },
        { 'name': 'plates', 'weight': 1.0, 'is_packed': 0, 'categories_id': 7 },
        { 'name': 'bowls', 'weight': 1.0, 'is_packed': 0, 'categories_id': 7 },
        { 'name': 'table cloth', 'weight': 0.5, 'is_packed': 0, 'categories_id': 7 },
        { 'name': 'ice', 'weight': 5.0, 'is_packed': 0, 'categories_id': 7 },
        { 'name': 'cooler', 'weight': 5.0, 'is_packed': 0, 'categories_id': 7 },
        { 'name': 'pots and pans', 'weight': 5.0, 'is_packed': 0, 'categories_id': 7 },
        { 'name': 'stove fuel', 'weight': 5.0, 'is_packed': 0, 'categories_id': 7 },
        { 'name': 'dish scrubber', 'weight': 0.2, 'is_packed': 0, 'categories_id': 7 },
        { 'name': 'dish basin', 'weight': 1.0, 'is_packed': 0, 'categories_id': 7 },
        { 'name': 'dish soap', 'weight': 0.5, 'is_packed': 0, 'categories_id': 7 },
        { 'name': 'hand sanitizer', 'weight': 0.1, 'is_packed': 0, 'categories_id': 7 },
        { 'name': 'camp table', 'weight': 5.0, 'is_packed': 0, 'categories_id': 7 },
        { 'name': 'cooking utensils', 'weight': 2.0, 'is_packed': 0, 'categories_id': 7 },
        { 'name': 'cutting board', 'weight': 2.0, 'is_packed': 0, 'categories_id': 7 },
        { 'name': 'cooking knife', 'weight': 0.2, 'is_packed': 0, 'categories_id': 7 },
        { 'name': 'trash bags', 'weight': 1.0, 'is_packed': 0, 'categories_id': 7 },
        { 'name': 'dish towel', 'weight': 0.5, 'is_packed': 0, 'categories_id': 7 },
        { 'name': 'coffee maker', 'weight': 2.0, 'is_packed': 0, 'categories_id': 7 },
        { 'name': 'food storage bags', 'weight': 0.5, 'is_packed': 0, 'categories_id': 7 },
        { 'name': 'foil', 'weight': 1.0, 'is_packed': 0, 'categories_id': 7 },
        { 'name': 'toys', 'weight': 3.0, 'is_packed': 0, 'categories_id': 8 },
        { 'name': 'food bowl', 'weight': 1.0, 'is_packed': 0, 'categories_id': 9 },
        { 'name': 'water bowl', 'weight': 1.0, 'is_packed': 0, 'categories_id': 9 },
        { 'name': 'leash', 'weight': 0.2, 'is_packed': 0, 'categories_id': 9 },
        { 'name': 'pet food', 'weight': 2.0, 'is_packed': 0, 'categories_id': 9 },
        { 'name': 'dog towel', 'weight': 0.4, 'is_packed': 0, 'categories_id': 9 },
        { 'name': 'dog run', 'weight': 0.1, 'is_packed': 0, 'categories_id': 9 },
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

    # This method does not save any items to the database
    # It adds the new list id to each item (creates association) and returns that list to the edit list route so the user can check or uncheck default items.
    @classmethod
    def create_default_items(cls, list_id):
        default_items_for_new_list = []
        for default_item in cls.DEFAULT_ITEMS:
            default_item['lists_id'] = list_id
            default_items_for_new_list.append(default_item)
        return default_items_for_new_list

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
