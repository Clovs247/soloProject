from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user
from flask_app.models import team

class Weapon:
    db = "Splatoon3Hub"
    def __init__(self, data):
        self.id = data['id']
        self.weapon_name = data['weapon_name']
        self.weapon_type = data['weapon_type']
        self.weapon_image = data['weapon_image']

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

    # ****************************UPDATE*************************************

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

    @classmethod
    def get_weapon_with_sub_and_special(cls, data):
        query = """
        SELECT * FROM weapon
        LEFT JOIN weapon_loadout
        ON weapon_loadout.weapon_id = weapon.id
        LEFT JOIN sub
        ON weapon_loadout.sub_id = sub.id
        LEFT JOIN special_weapon
        ON weapon_loadout.special_weapon_id = special_weapon.id 
        WHERE weapon_loadout.weapon_id = %(id)s
        ;"""
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return None
        return cls(results[0])
    
    # @classmethod
    # def get_all_weapons_with_sub(cls):
    #     query = """
    #     SELECT * FROM weapon
    #     LEFT JOIN sub 
    #     ON weapon.sub_id = sub.id
    #     ;"""
    #     results = connectToMySQL(cls.db).query_db(query)
    #     return results

    # @classmethod
    # def get_weapon_with_special(cls, data):
    #     query = """
    #     SELECT * FROM weapon
    #     LEFT JOIN special_weapon
    #     ON weapon.special_weapon_id = special_weapon.id
    #     WHERE weapon.id = %(id)s
    #     ;"""
    #     results = connectToMySQL(cls.db).query_db(query, data)
    #     if len(results) < 1:
    #         return None
    #     return cls(results[0])
    
    # @classmethod
    # def get_all_weapons_with_special(cls):
    #     query = """
    #     SELECT * FROM weapon
    #     LEFT JOIN special_weapon
    #     ON weapon.special_weapon_id = special_weapon.id
    #     ;"""
    #     results = connectToMySQL(cls.db).query_db(query)
    #     return results