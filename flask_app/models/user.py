
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import team
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class User:
    db = 'Splatoon3Hub'
    def __init__(self, data):
        self.id = data['id']
        self.username = data['username']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # self.team = []
        self.weapon = None
        self.created_teams = []
        self.characters = []
        # characters gathered from a join query
        # select usere where
        # join characters wehre user.id = user_id
        # create user instance, loop through to create instances of characters to append to user.characters list



#**********************Create***************************************

    @classmethod
    def create_user(cls, data):
        query = """
        INSERT INTO user
        (username, email, password)
        VALUES
        (%(username)s, %(email)s, %(password)s)
        ;"""
        return connectToMySQL(cls.db).query_db(query, data)



# *********************READ***************************************

    @classmethod
    def get_all_users(cls):
        query="""
        SELECT * FROM user
        ;"""
        results = connectToMySQL(cls.db).query_db(query)
        members = []
        for row in results:
            members.append(cls(row))
        return members



    @classmethod
    def get_user_by_id(cls, data):
        query = """
        SELECT * FROM user
        WHERE id = %(id)s
        ;"""
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])



    @classmethod
    def get_user_by_email(cls, data):
        query = """
        SELECT * FROM user
        WHERE email = %(email)s
        ;"""
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])



# *********************UPDATE***************************************

    @classmethod
    def update_user(cls, data):
        query = """
        UPDATE user SET
        username = %(username)s,
        email = %(email)s
        WHERE id = %(id)s
        ;"""
        return connectToMySQL(cls.db).query_db(query, data)



# *********************DELETE***************************************


    @classmethod
    def delete_user(cls, data):
        query = """
        DELETE FROM user
        WHERE id = %(id)s
        ;"""
        return connectToMySQL(cls.db).query_db(query, data)


#************************VALIDATE***********************************

    @staticmethod
    def validate(user):
            is_valid = True
            query = """
            SELECT * FROM user
            WHERE email = %(email)s
            ;"""
            results = connectToMySQL(User.db).query_db(query, user)
            if len(results)>= 1:
                is_valid=False
                flash("That email has already been entered into the database")
            if not EMAIL_REGEX.match(user['email']):
                is_valid=False
                flash("Invalid Email Format")
            if len(user['username'])<1:
                is_valid = False
                flash("First Name must contain at least 1 character")
            if len(user['username'])>10:
                is_valid = False
                flash("First Name must not contain more than 10 character")
            if len(user['password'])<8:
                is_valid = False
                flash("Password must have at least 8 characters")
            if user['password'] != user['confirm_password']:
                is_valid = False
                flash("Passwords are not matching, check your spelling.")
            return is_valid

    @staticmethod
    def validate_update(user):
            is_valid = True
            query = """
            SELECT * FROM user
            WHERE email = %(email)s
            ;"""
            results = connectToMySQL(User.db).query_db(query, user)
            if len(results)> 1:
                is_valid=False
                flash("That email has already been entered into the database")
            if not EMAIL_REGEX.match(user['email']):
                is_valid=False
                flash("Invalid Email Format")
            if len(user['username'])<1:
                is_valid = False
                flash("First Name must contain at least 1 character")
            if len(user['username'])>10:
                is_valid = False
                flash("First Name must not contain more than 10 character")
            return is_valid

# ***************************CONNECTION********************************
    
    @classmethod
    def get_user_with_team(cls, data):
        query = """
        SELECT * FROM user
        LEFT JOIN user_has_team ON user_has_team.user_id = user.id
        LEFT JOIN team ON user_has_team.team_id
        WHERE user.id = %(id)s
        ;"""
        results = connectToMySQL('user').query_db(query, data)
        user = cls(results[0])
        for row_from_db in results:
            team_data = {
                "id": row_from_db["id"],
                "weapon": row_from_db["weapon"],
                "created_at": row_from_db["created_at"],
                "updated_at": row_from_db["updated_at"]
            }
            user.team.append(team.Team(team_data))
        return user