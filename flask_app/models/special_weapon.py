from flask_app.config.mysqlconnection import connectToMySQL

class Special:
    db = "Splatoon3Hub"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.image = data['image']

    
    # *****************************READ************************************

    @classmethod
    def get_all_specials(cls):
        query="""
        SELECT * FROM special_weapon
        ;"""
        results = connectToMySQL(cls.db).query_db(query)
        specials = []
        for row in results:
            specials.append(cls(row))
        return specials

    @classmethod
    def get_special_by_id(cls, data):
        query="""
        SELECT * FROM special
        WHERE id = %(id)s
        ;"""
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    # *****************************CONNECTION*************************************