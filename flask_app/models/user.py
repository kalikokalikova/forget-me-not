from config.mysqlconnection import connectToMySQL
from flask import flash
import re
from flask_bcrypt import Bcrypt
from flask_app import app
bcrypt = Bcrypt(app)
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        data = {
            'first_name': data['first_name'],
            'last_name': data['last_name'],
            'email': data['email'],
            'password': bcrypt.generate_password_hash(data['password'])
        }

        query = "insert into users (first_name, last_name, email, password) values ( %(first_name)s, %(last_name)s, %(email)s, %(password)s );"
        return connectToMySQL('recipes_schema').query_db(query, data)

    @classmethod
    def get_all_users(cls):
        users = []
        query = "select * from users;"
        result = connectToMySQL('recipes_schema').query_db(query)
        if len(result) > 0:
            for user in result:
                users.append( cls(user) )
        return users

    @classmethod
    def get_user_by_email(cls, data):
        query = "select * from users where email = %(email)s;"
        result = connectToMySQL('recipes_schema').query_db(query, data)
        if len(result) > 0:
            return cls( result[0] )
        else:
            return False

    @classmethod
    def get_user_by_id(cls, data):
        query = "select * from users where id = %(id)s;"
        result = connectToMySQL('recipes_schema').query_db(query, data)
        if len(result) > 0:
            return cls( result[0] )
        else:
            return False

    @staticmethod
    def validate_registration(data):

        is_valid = True
        if len(data['first_name']) < 2:
            is_valid = False
            flash("First name must be at least 2 characters.","register")
        if len(data['last_name']) < 2:
            is_valid = False
            flash("Last name must be at least 2 characters.","register")
        if not EMAIL_REGEX.match(data['email']):
            is_valid = False
            flash("Invalid Email Address.","register")
        if len(data['password']) < 8:
            is_valid = False
            flash("Password must be at least 8 characters.","register")
        if data['password'] != data['confirm']:
            is_valid = False
            flash("Passwords do not match!","register")
        user = User.get_user_by_email(data={'email':data['email']})
        print(user)
        if user:
            is_valid = False
            flash("Email already taken", "register")

        return is_valid

    @staticmethod
    def validate_login(data):

        user = User.get_user_by_email(data)
        if not user:
            flash("invalid credentials", "login")
            return False

        if not bcrypt.check_password_hash(user.password, data['password']):
            flash("invalid credentials", "login")
            return False
        
        return user

