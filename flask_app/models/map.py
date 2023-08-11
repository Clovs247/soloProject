from flask_app.config.mysqlconnection import connectToMySQL



class Map:
    db="splatoon3hub"
    def __init__(self, data):
        self.id = data['id']
        self.map_name = data['map_name']
        self.map_image = data['map_image']
        
    # ****************************CREATE*************************************

    # *****************************READ************************************

    @classmethod
    def get_all_maps(cls):
        query="""
        SELECT * FROM map
        ;"""
        results = connectToMySQL(cls.db).query_db(query)
        maps = []
        for row in results:
            maps.append(cls(row))
        return maps
    
    @classmethod
    def get_map_by_id(cls, data):
        query="""
        SELECT * FROM map
        WHERE id = %(id)s
        ;"""
        results = connectToMySQL(cls.db).query_db(query, data)
        return results

    # ****************************UPDATE*************************************

    # *****************************DELETE*************************************

    # *****************************CONNECTION*************************************
