from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_app.models import user
from flask_app.models import team
from flask_app.models import weapon

@app.route('/all-teams/')
def display_teams():
    if 'user_id' not in session:
        return redirect('/')
    else:
        data={
            'id' : session['user_id']
        }
        logged_in_user = user.User.get_user_by_id(data)
        all_teams = team.Team.get_all_teams()
        print("***************ALL TEAMS*********************",all_teams)
        for results in all_teams:
            print(results.id)
            team_data={
                'id' : [results.id]
            }
            # print("*******************************",results)
        # club = team.Team.get_team_with_users(team_data)
        # club = team.Team.get_teams_made_by_user(data)
        return render_template('all_teams.html', logged_in_user = logged_in_user, all_teams=all_teams)

@app.route('/create/team/')
def create_team_page():
    if 'user_id' not in session:
        return redirect('/')
    else:
        data = {
            'id' : session['user_id']
        }
        logged_in_user = user.User.get_user_by_id(data)
        all_weapons = weapon.Weapon.get_all_weapons()
        return render_template('create_team.html', logged_in_user = logged_in_user, all_weapons = all_weapons)

@app.route('/create/team/form/', methods=['post'])
def form_team():
    team_data = {
            'team_name' : request.form['team_name'],
            'user_id' : session['user_id'], 
            'weapon_id' : request.form['weapon_id']
        }
    is_valid = team.Team.validate_team(team_data)
    if not is_valid:
        return redirect('/create/team/')
    else:
        
        # *************************************************************
        if not is_valid:
            flash('Please enter in valid info.')
            return redirect('/')
        else:
            team.Team.create_team(team_data)
            return redirect('/all-teams/')

@app.route('/join/<int:team_id>/form/', methods=['post'])
def join_team(team_id):
    val_data = {
        'user_id' : session['user_id'], 
        "team_id" : team_id
        }
    # print("*********************************", team_data)
    is_valid = team.Team.validate_join(val_data)
    if not is_valid:
        return redirect(f'/team/{team_id}/view/')
    else:
        team_data = {
            'user_id' : session['user_id'], 
            'weapon_id' : request.form['weapon_id'],
            "team_id" : team_id
        }
        team.Team.join_team(team_data)
        return redirect('/all-teams/')

@app.route('/team/<int:team_id>/view/')
def view_team(team_id):
    if 'user_id' not in session:
        return redirect('/')
    else:
        data = {
            'id' : session['user_id']
        }
        team_data = {
            'id' : team_id
        }
        logged_in_user = user.User.get_user_by_id(data)

        # all_users = user.User.get_all_users()
        # club = team.Team.get_a_team(team_data)

        all_weapons = weapon.Weapon.get_all_weapons()

        # members = team.Team.get_members(team_data)

        club = team.Team.get_team_with_users(team_data)
        print("*****************", club.on_team)
        return render_template('view_team.html', logged_in_user = logged_in_user, club = club, all_weapons=all_weapons)

@app.route('/team/<int:team_id>/delete/')
def delete_team(team_id):
    team_data={
        'id':team_id
    }
    team.Team.delete_team(team_data)
    return redirect('/all-teams/')

@app.route('/team/<int:team_id>/leave')
def leave_team(team_id):
    betrayer_data={
        'user_id': session['user_id'],
        'team_id': team_id
    }
    print(betrayer_data)
    team.Team.leave_team(betrayer_data)
    return redirect(f'/team/{team_id}/view')