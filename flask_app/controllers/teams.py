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
    is_valid = team.Team.validate_team(request.form)
    if not is_valid:
        return redirect('/')
    else:
        team_data = {
            'name' : request.form['name'],
            'creator_id' : session['user_id']
        }
        # *************************************************************
        club = team.Team.create_team(team_data)
        if not club:
            flash('Please enter in valid info.')
            return redirect('/')
        else:
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
        club = team.Team.get_team_with_users(team_data)
        print("*****************", club)
        return render_template('view_team.html', logged_in_user = logged_in_user, club = club)
