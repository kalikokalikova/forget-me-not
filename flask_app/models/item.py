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
        { 'name': 'pillow', 'weight': 1, 'is_packed': 0, 'categories_id': 2 },
        { 'name': 'socks', 'weight': .5, 'is_packed': 0, 'categories_id': 3 },
        { 'name': 'gin', 'weight': .25, 'is_packed': 0, 'categories_id': 7 }
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