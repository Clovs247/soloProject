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
        SELCT * FROM map
        ;"""
        results = connectToMySQL(cls.db).query_db(query)
        maps = []
        for row in results:
            maps.apphend(cls(row))
        return maps
    

    # ****************************UPDATE*************************************

    # *****************************DELETE*************************************

    # *****************************CONNECTION*************************************
