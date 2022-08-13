from config.mysqlconnection import connectToMySQL
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

    @classmethod
    def save(cls, data):
        query = "insert into lists (name, users_id, notes, start_date, end_date, zip_code) values ( %(name)s, %(users_id)s, %(notes)s, %(start_date)s, %(end_date)s, %(zip_code)s );"
        result = connectToMySQL('camping_list_schema').query_db(query, data)
        return result

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
        query = "select * from lists where id=%(id)s;"
        results = connectToMySQL('camping_list_schema').query_db(query, data)
        #TODO create and return classes here
        return results[0]

    @staticmethod
    def validate_inputs(data):
        #TODO think about and write this code
        return True