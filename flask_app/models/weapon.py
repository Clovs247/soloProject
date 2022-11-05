from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user
from flask_app.models import team

class Weapon:
    db = "Splatoon3Hub"
    def __init__(self, data):
        self.id = data['id']
        self.weapon_name = data['weapon_name']

    # ****************************CREATE*************************************



    # *****************************READ************************************

    @classmethod
    def get_all_weapons(cls):
        query="""
        SELECT * FROM weapon
        ;"""
        results = connectToMySQL(cls.db).query_db(query)
        weapons = []
        for row in results:
            weapons.append(cls(row))
        return weapons

    
    # ****************************UPDATE*************************************

    @classmethod
    def get_weapon_by_id(cls, data):
        query="""
        SELECT * FROM weapon
        WHERE id = %(id)s
        ;"""
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    # *****************************DELETE*************************************




    # *****************************CONNECTION*************************************


    @classmethod
    def get_user_with_weapon(cls, data):
        query = """
        SELECT * FROM weapon
        JOIN loadout
        ON loadout.weapon_id = weapon.id
        WHERE loadout.team_id = %(team_id)s
        AND loadout.user_id = %(user_id)s
        ;"""
        results = connectToMySQL(cls.db).query_db(query,data)
        if len(results) < 1:
            return None
        return cls(results[0])