from config.mysqlconnection import connectToMySQL

class Item:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.weight = data['weight']
        self.is_packed = data['is_packed']
        self.category = data['categories_id']
        self.list_id = data['lists_id']

    DEFAULT_ITEMS = [
        { 'name': 'sleeping bag', 'weight': 2.0, 'is_packed': 0, 'categories_id': 2 },
        { 'name': 'tent', 'weight': 2.0, 'is_packed': 0, 'categories_id': 2 },
        { 'name': 'tarp', 'weight': 2.0, 'is_packed': 0, 'categories_id': 2 },
        { 'name': 'stakes', 'weight': 2.0, 'is_packed': 0, 'categories_id': 2 },
        { 'name': 'air mattress', 'weight': 2.0, 'is_packed': 0, 'categories_id': 2 },
        { 'name': 'sleeping pad', 'weight': 2.0, 'is_packed': 0, 'categories_id': 2 },
        { 'name': 'cot', 'weight': 2.0, 'is_packed': 0, 'categories_id': 2 },
        { 'name': 'blanket', 'weight': 2.0, 'is_packed': 0, 'categories_id': 2 },
        { 'name': 'pillow', 'weight': 2.0, 'is_packed': 0, 'categories_id': 2 },
        { 'name': 'mattress pump', 'weight': 2.0, 'is_packed': 0, 'categories_id': 3 },
        { 'name': 'hammer', 'weight': 2.0, 'is_packed': 0, 'categories_id': 4 },
        { 'name': 'knife', 'weight': 2.0, 'is_packed': 0, 'categories_id': 4 },
        { 'name': 'lantern', 'weight': 2.0, 'is_packed': 0, 'categories_id': 4 },
        { 'name': 'flashlight', 'weight': 2.0, 'is_packed': 0, 'categories_id': 4 },
        { 'name': 'roasting sticks', 'weight': 2.0, 'is_packed': 0, 'categories_id': 4 },
        { 'name': 'lighter', 'weight': 2.0, 'is_packed': 0, 'categories_id': 4 },
        { 'name': 'multitool', 'weight': 2.0, 'is_packed': 0, 'categories_id': 4 },
        { 'name': 'headlamp', 'weight': 2.0, 'is_packed': 0, 'categories_id': 4 },
        { 'name': 'navigation device', 'weight': 2.0, 'is_packed': 0, 'categories_id': 4},
        { 'name': 'phone charger', 'weight': 2.0, 'is_packed': 0, 'categories_id': 4 },
        { 'name': 'mattress repair kit', 'weight': 2.0, 'is_packed': 0, 'categories_id': 4 },
        { 'name': 'can opener', 'weight': 2.0, 'is_packed': 0, 'categories_id': 4 },
        { 'name': 'bottle opener', 'weight': 2.0, 'is_packed': 0, 'categories_id': 3 },
        { 'name': 'fire starter', 'weight': 2.0, 'is_packed': 0, 'categories_id': 5 },
        { 'name': 'wood', 'weight': 2.0, 'is_packed': 0, 'categories_id': 5 },
        { 'name': 'kindling', 'weight': 2.0, 'is_packed': 0, 'categories_id': 5 },
        { 'name': 'first aid kit', 'weight': 2.0, 'is_packed': 0, 'categories_id': 2 },
        { 'name': 'bear spray', 'weight': 2.0, 'is_packed': 0, 'categories_id': 2 },
        { 'name': 'sunscreen', 'weight': 2.0, 'is_packed': 0, 'categories_id': 2 },
        { 'name': 'citronella candle', 'weight': 2.0, 'is_packed': 0, 'categories_id': 2 },
        { 'name': 'shampoo/conditioner', 'weight': 2.0, 'is_packed': 0, 'categories_id': 2 },
        { 'name': 'hairbrush', 'weight': 2.0, 'is_packed': 0, 'categories_id': 2 },
        { 'name': 'toothbrush', 'weight': 2.0, 'is_packed': 0, 'categories_id': 2 },
        { 'name': 'toothpaste', 'weight': 2.0, 'is_packed': 0, 'categories_id': 2 },
        { 'name': 'soap', 'weight': 2.0, 'is_packed': 0, 'categories_id': 2 },
        { 'name': 'towel', 'weight': 2.0, 'is_packed': 0, 'categories_id': 2 },
        { 'name': 'hair dryer', 'weight': 2.0, 'is_packed': 0, 'categories_id': 2 },
        { 'name': 'sunglasses', 'weight': 2.0, 'is_packed': 0, 'categories_id': 2 },
        { 'name': 'hat', 'weight': 2.0, 'is_packed': 0, 'categories_id': 2 },
        { 'name': 'jacket', 'weight': 2.0, 'is_packed': 0, 'categories_id': 2 },
        { 'name': 'clothes', 'weight': 2.0, 'is_packed': 0, 'categories_id': 2 },
        { 'name': 'clothesline', 'weight': 2.0, 'is_packed': 0, 'categories_id': 2 },
        { 'name': 'broom and dustpan', 'weight': 2.0, 'is_packed': 0, 'categories_id': 2 },
        { 'name': 'toilet paper', 'weight': 2.0, 'is_packed': 0, 'categories_id': 2 },
        { 'name': 'prescription meds', 'weight': 2.0, 'is_packed': 0, 'categories_id': 2 },
        { 'name': 'chapstick', 'weight': 2.0, 'is_packed': 0, 'categories_id': 2 },
        { 'name': 'santitation trowel', 'weight': 2.0, 'is_packed': 0, 'categories_id': 2 },
        { 'name': 'baby wipes', 'weight': 2.0, 'is_packed': 0, 'categories_id': 2 },
        { 'name': 'quarters for shower', 'weight': 2.0, 'is_packed': 0, 'categories_id': 2 },
        { 'name': 'swimming suit', 'weight': 2.0, 'is_packed': 0, 'categories_id': 6 },
        { 'name': 'bike', 'weight': 2.0, 'is_packed': 0, 'categories_id': 6 },
        { 'name': 'helmet', 'weight': 2.0, 'is_packed': 0, 'categories_id': 6 },
        { 'name': 'fishing pole', 'weight': 2.0, 'is_packed': 0, 'categories_id': 6 },
        { 'name': 'camp chairs', 'weight': 2.0, 'is_packed': 0, 'categories_id': 6 },
        { 'name': 'hiking boots', 'weight': 2.0, 'is_packed': 0, 'categories_id': 6 },
        { 'name': 'hiking backpack', 'weight': 2.0, 'is_packed': 0, 'categories_id': 6 },
        { 'name': 'hammock', 'weight': 2.0, 'is_packed': 0, 'categories_id': 6 },
        { 'name': 'book', 'weight': 2.0, 'is_packed': 0, 'categories_id': 6 },
        { 'name': 'board game', 'weight': 2.0, 'is_packed': 0, 'categories_id': 6 },
        { 'name': 'beach towels', 'weight': 2.0, 'is_packed': 0, 'categories_id': 6 },
        { 'name': 'water bottle', 'weight': 2.0, 'is_packed': 0, 'categories_id': 7 },
        { 'name': 'camp stove', 'weight': 2.0, 'is_packed': 0, 'categories_id': 7 },
        { 'name': 'water filter', 'weight': 2.0, 'is_packed': 0, 'categories_id': 7 },
        { 'name': 'mess kit', 'weight': 2.0, 'is_packed': 0, 'categories_id': 7 },
        { 'name': 'paper towels', 'weight': 2.0, 'is_packed': 0, 'categories_id': 7 },
        { 'name': 'utensils', 'weight': 2.0, 'is_packed': 0, 'categories_id': 7 },
        { 'name': 'cups', 'weight': 2.0, 'is_packed': 0, 'categories_id': 7 },
        { 'name': 'plates', 'weight': 2.0, 'is_packed': 0, 'categories_id': 7 },
        { 'name': 'bowls', 'weight': 2.0, 'is_packed': 0, 'categories_id': 7 },
        { 'name': 'table cloth', 'weight': 2.0, 'is_packed': 0, 'categories_id': 7 },
        { 'name': 'ice', 'weight': 2.0, 'is_packed': 0, 'categories_id': 7 },
        { 'name': 'cooler', 'weight': 2.0, 'is_packed': 0, 'categories_id': 7 },
        { 'name': 'pots and pans', 'weight': 2.0, 'is_packed': 0, 'categories_id': 7 },
        { 'name': 'stove fuel', 'weight': 2.0, 'is_packed': 0, 'categories_id': 7 },
        { 'name': 'dish scrubber', 'weight': 2.0, 'is_packed': 0, 'categories_id': 7 },
        { 'name': 'dish basin', 'weight': 2.0, 'is_packed': 0, 'categories_id': 7 },
        { 'name': 'dish soap', 'weight': 2.0, 'is_packed': 0, 'categories_id': 7 },
        { 'name': 'hand sanitizer', 'weight': 2.0, 'is_packed': 0, 'categories_id': 7 },
        { 'name': 'camp table', 'weight': 2.0, 'is_packed': 0, 'categories_id': 7 },
        { 'name': 'cooking utensils', 'weight': 2.0, 'is_packed': 0, 'categories_id': 7 },
        { 'name': 'cutting board', 'weight': 2.0, 'is_packed': 0, 'categories_id': 7 },
        { 'name': 'cooking knife', 'weight': 2.0, 'is_packed': 0, 'categories_id': 7 },
        { 'name': 'trash bags', 'weight': 2.0, 'is_packed': 0, 'categories_id': 7 },
        { 'name': 'dish towel', 'weight': 2.0, 'is_packed': 0, 'categories_id': 7 },
        { 'name': 'coffee maker', 'weight': 2.0, 'is_packed': 0, 'categories_id': 7 },
        { 'name': 'food storage bags', 'weight': 2.0, 'is_packed': 0, 'categories_id': 7 },
        { 'name': 'foil', 'weight': 2.0, 'is_packed': 0, 'categories_id': 7 },
        { 'name': 'toys', 'weight': 2.0, 'is_packed': 0, 'categories_id': 8 },
        { 'name': 'food bowl', 'weight': 2.0, 'is_packed': 0, 'categories_id': 9 },
        { 'name': 'water bowl', 'weight': 2.0, 'is_packed': 0, 'categories_id': 9 },
        { 'name': 'leash', 'weight': 2.0, 'is_packed': 0, 'categories_id': 9 },
        { 'name': 'pet food', 'weight': 2.0, 'is_packed': 0, 'categories_id': 9 },
        { 'name': 'dog towel', 'weight': 2.0, 'is_packed': 0, 'categories_id': 9 },
        { 'name': 'dog run', 'weight': 2.0, 'is_packed': 0, 'categories_id': 9 },
        { 'name': 'poop bags', 'weight': 2.0, 'is_packed': 0, 'categories_id': 9 }
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