from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user


class Team:
    db = "Splatoon3Hub"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = None
        self.on_team = []


# **************************************CREATE******************************

    @classmethod
    def save_team(cls, data):
        query = """
        INSERT INTO team
        (name, user_id)
        VALUES
        (%(name)s, %(user_id)s)
        ;"""
        return connectToMySQL(cls.db).query_db(query, data)


# **************************************READ******************************

    @classmethod
    def get_all_teams(cls):
        query = """
        SELECT * FROM team
        ;"""
        results = connectToMySQL(cls.db).query_db(query)
        roster = []
        for row in results:
            roster.append(cls(row))
        return roster

    @classmethod
    def get_a_team(cls, data):
        query = """
        SELCT * FROM team
        WHERE id = %(id)s
        ;"""
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results)<1:
            return False
        return cls(results[0])

    @classmethod
    def get_team_with_users(cls, data):
        query = """
        SELECT * FROM team
        LEFT JOIN user_has_team
        ON user_has_team.team_id = team.id
        LEFT JOIN user 
        ON user_has_team.user_id = user.id
        WHERE team.id = %(id)s
        ;"""
        results = connectToMySQL('user').query_db(query, data)
        team = cls(results[0])
        for row_from_db in results:
            user_data = {
                "id":row_from_db["user.id"],
                "username":row_from_db["user.username"],
                "email":row_from_db["user.email"],
                "created_at":row_from_db["created_at"],
                "updated_at":row_from_db["updated_at"]
            }
            team.on_team.append(user.User(user_data))
        return team


# **************************************UPDATE******************************

    # @classmethod
    # def update_team(cls, data):
    #     query = """
    #     UPDATE team SET
    #     name=%(name)s
    #     WHERE id = %(id)s
    #     ;"""
    #     return connectToMySQL(cls.db).query_db(query, data)

# **************************************DELETE******************************

    @classmethod
    def delete_team(cls, data):
        query = """
        DELETE FROM team
        WHERE id = %(id)s
        ;"""
        return connectToMySQL(cls.db).query_db(query, data)


    @staticmethod
    def validate_team(team_id):
        is_valid = True

        if len(team_id['name'])<=2:
            is_valid=False
            flash("The name of this team needs to be at least 2 characters.")
        
        return is_valid

