from flask_app.config.mysqlconnection import connectToMySQL

class Sub:
    db = "Splatoon3Hub"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.image = data['image']

    
    # *****************************READ************************************

    @classmethod
    def get_all_subs(cls):
        query="""
        SELECT * FROM sub
        ;"""
        results = connectToMySQL(cls.db).query_db(query)
        subs = []
        for row in results:
            subs.append(cls(row))
        return subs

    @classmethod
    def get_sub_by_id(cls, data):
        query="""
        SELECT * FROM sub
        WHERE id = %(id)s
        ;"""
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    # *****************************CONNECTION*************************************

    # @classmethod
    # def get_weapon_with_sub(cls, data):
    #     query = """
    #     SELECT * FROM sub
    #     LEFT JOIN weapon ON
    #     weapon.sub_id = sub.id
    #     WHERE %()
    #     ;"""