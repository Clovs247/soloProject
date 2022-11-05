from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user
from flask_app.models import team

class weapon:
    db = "Splatoon3Hub"
    def __init__(self, id, name):
        self.id = id
        self.name = name

    # ****************************CREATE*************************************



    # *****************************READ************************************

    @classmethod
    def get_all_weapons(cls):
        query="""
        SELECT * FROM weapon
        ;"""
        results = connectToMySQL(cls.db).query_db(query)
        mainWep = []
        for row in results:
            mainWep.append(cls(row))
        return mainWep

    
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


