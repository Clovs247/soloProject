from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user


class Team:
    db = "Splatoon3Hub"
    def __init__(self, data):
        self.id = data['id']
        self.on_team = []
        self.weapon = data['weapon']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save_team(cls, data):
        query = """
        INSERT INTO team
        (weapon, created_at, updated_at)
        VALUES
        (%(weapon)s, NOW(), NOW())
        ;"""
        return connectToMySQL('user').query_db(query, data)

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