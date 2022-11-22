from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user
from flask_app.models import weapon


class Team:
    db = "Splatoon3Hub"
    def __init__(self, data):
        self.id = data['id']
        self.team_name = data['team_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.creator_id = data['creator_id']
        self.on_team = []
        # self.creator= None


# **************************************CREATE******************************

    @classmethod
    def create_team(cls, team_data):
        query = """
        INSERT INTO team
        (team_name, creator_id)
        VALUES
        (%(team_name)s, %(user_id)s)
        ;"""
        team_id =  connectToMySQL(cls.db).query_db(query, team_data)
        # print("&&&&&&&&&&&&&&&&&&", team_id)
        team_data["team_id"] = team_id
        cls.join_team(team_data)
        return team_id


    @classmethod
    def join_team(cls, data):
        query="""
        INSERT INTO loadout
        (team_id, user_id, weapon_id)
        VALUES
        (%(team_id)s,%(user_id)s,%(weapon_id)s)
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
            team_now = cls(row)
            data = {
                'team_id': team_now.id
            }
            team_now.on_team = cls.get_members(data)
            roster.append(team_now)
        return roster

    @classmethod
    def get_a_team(cls, data):
        query = """
        SELECT * FROM team
        WHERE id = %(id)s
        ;"""
        results = connectToMySQL(cls.db).query_db(query, data)
        # print(results)
        roster = []
        if len(results)<1:
            return False
        else:
            # print("&&&&&&&&&&&&&&&", results)
            team_now = cls(results)
            team_data={
                'team_id': team_now.id
            }
            team_now.on_team = cls.get_members(team_data)
            roster.append(team_now)
            return cls(results[0])

    
    @classmethod
    def get_teams_made_by_user(cls, data):
        query = """
        SELECT * FROM team
        WHERE creator_id = %(creator_id)s
        ;"""
        results = connectToMySQL(cls.db).query_db(query, data)
        return results

    @classmethod
    def get_team_with_users(cls, data):
        query = """
        SELECT * FROM team
        LEFT JOIN loadout
        ON loadout.team_id = team.id
        LEFT JOIN user 
        ON loadout.user_id = user.id
        WHERE team.id = %(id)s
        ;"""
        results = connectToMySQL(cls.db).query_db(query, data)
        club = cls(results[0])
        for row_from_db in results:
            user_data = {
                "id":row_from_db["user.id"],
                "username":row_from_db["username"],
                "email":row_from_db["email"],
                "password": "",
                "created_at":row_from_db["user.created_at"],
                "updated_at":row_from_db["user.updated_at"]
            }
            teammember = user.User(user_data)
            weap_data = {
                "team_id":data["id"],
                "user_id":teammember.id
            }
            teammember.weapon = weapon.Weapon.get_user_with_weapon(weap_data)
            club.on_team.append(teammember)
            # print("&&&&&&&&&&&&&&&&&&", len(club.on_team))
        return club

    @classmethod
    def get_members(cls,data):
        query="""
        SELECT * FROM loadout
        JOIN user 
        ON loadout.user_id = user.id
        WHERE loadout.team_id = %(team_id)s
        ;"""
        results = connectToMySQL(cls.db).query_db(query, data)
        members=[]
        for row in results:
            members.append(user.User(row))
        return members

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

    @classmethod
    def leave_team(cls, data):
        query="""
        DELETE FROM loadout
        WHERE user_id = %(user_id)s
        AND team_id = %(team_id)s
        ;"""
        return connectToMySQL(cls.db).query_db(query, data)



# ***********************************VALIDATE***************************************
    @staticmethod
    def validate_team(team_data):
        is_valid = True
        query="""
        SELECT * FROM team
        WHERE team_name = %(team_name)s
        ;"""
        results = connectToMySQL(Team.db).query_db(query, team_data)
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^", results)
        if len(results)<=1:
            is_valid = False
            flash("Please don't copy the name of another team.")
        if results == team_data['team_name']:
            is_valid = False
            flash("The team name that you've chosen already exists, please choose another.")
        if len(team_data['team_name'])<=1:
            is_valid=False
            flash("The name of this team needs to be at least 2 characters.")
            
        return is_valid

    @staticmethod
    def validate_join(canidate):
        query="""
        SELECT * FROM loadout
        WHERE user_id = %(user_id)s
        AND team_id = %(team_id)s
        ;"""
        results = connectToMySQL(Team.db).query_db(query, canidate)
        if len(results)>0:
            flash("You can't join the same team twice")
            return False
        
        return True



    