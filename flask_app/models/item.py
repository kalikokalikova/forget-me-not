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

    DEFAULT_ITEMS = [ # worry about categories later
        {
            'name': 'sleeping bag',
            'weight': 2.0,
            'is_packed': 0,
            'categories_id': 1
        },
        {
            'name': 'pillow',
            'weight': 1,
            'is_packed': 0,
            'categories_id': 1
        },
        {
            'name': 'socks',
            'weight': .5,
            'is_packed': 0,
            'categories_id': 1
        },
        {
            'name': 'gin',
            'weight': .25,
            'is_packed': 0,
            'categories_id': 1
        }
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
        for di in cls.DEFAULT_ITEMS:
            di['lists_id'] = list_id
            item_id = Item.save(di)
            item_ids.append(item_id)
        return item_ids