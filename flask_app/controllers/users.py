import bcrypt
import random
from flask_app import app
from flask_app.models import user, weapon, map
from flask import render_template, redirect, request, session, flash
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    if "user_id" not in session:
        return render_template("unknown_dashboard.html")
    else:
        return redirect('/dashboard/')

@app.route("/register/form")
def register_form():
    if 'user_id' not in session:
        return render_template("register.html")
    else:
        return redirect('/dashboard/')

@app.route('/register/', methods=['post'])
def register():
    is_valid = user.User.validate(request.form)
    if not is_valid:
        return redirect('/register/form')
    else:
        new_user = {
            'username': request.form['username'],
            'email': request.form['email'],
            'password': bcrypt.generate_password_hash(request.form['password'])
        }
        id = user.User.create_user(new_user)
        if not id:
            flash('Something Went Terribly Wrong')
            return redirect('/register/form')
        else:
            session["user_id"] = id
            return redirect('/dashboard/')

@app.route("/login/form")
def login_form():
    if 'user_id' not in session:
        return render_template("login.html")
    else:
        return redirect('/dashboard/')

@app.route("/login/", methods = ['post'])
def login():
    data = {
        'email' : request.form['email']
    }
    id = user.User.get_user_by_email(data)
    if not id:
        flash("That email isn't in our database yet. Please Register")
        return redirect('/login/form')
    if not bcrypt.check_password_hash(id.password, request.form['password']):
        flash("Wrong Password")
        return redirect('/login/form')
    else:
        session['user_id'] = id.id
        return redirect ('/dashboard/')

@app.route('/edit/profile/')
def edit_user():
    if 'user_id' not in session:
        return redirect('/')
    else:
        user_data={
            'id': session['user_id']
        }
        logged_in_user = user.User.get_user_by_id(user_data)
        return render_template('edit_profile.html', logged_in_user=logged_in_user)

@app.route('/update/profile/', methods=['post'])
def update_user():
    is_valid=user.User.validate_update(request.form)
    if not is_valid:
        return redirect('/')
    else:
        user_data = {
            'id' : session['user_id'],
            'username' : request.form['username'],
            'email' : request.form['email']
        }
    user.User.update_user(user_data)
    return redirect('/dashboard/')

@app.route('/logout/')
def logout():
    session.clear()
    return redirect('/')

@app.route('/dashboard/')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    else:
        data = {
            'id' : session['user_id']
        }
        logged_in_user = user.User.get_user_by_id(data)
        all_users = user.User.get_all_users()
        
        return render_template('dashboard.html', logged_in_user = logged_in_user, all_users = all_users)


@app.route('/dashboard/maps/')
def all_maps():
    if 'user_id' not in session:
        return redirect('/')
    else:
        data = {
            'id' : session['user_id']
        }
        all_maps = map.Map.get_all_maps()
        logged_in_user = user.User.get_user_by_id(data)
        return render_template('all_maps.html', logged_in_user=logged_in_user, all_maps=all_maps)


@app.route('/dashboard/weapons/')
def all_weapons():
    if 'user_id' not in session:
        return redirect('/')
    else:
        data = {
            'id': session['user_id']
        }
        logged_in_user = user.User.get_user_by_id(data)
        all_weapons = weapon.Weapon.get_all_weapons_with_kit()
        return render_template('all_weapons.html', logged_in_user=logged_in_user, all_weapons = all_weapons)

@app.route('/view-weapon/<int:weapon_id>')
def view_weapon(weapon_id):
    weapon_selection = {
        'id' : weapon_id
    }
    arm = weapon.Weapon.get_weapon_with_sub_and_special(weapon_selection)
    print(arm)
    return render_template('view_weapon.html', arm = arm)

@app.route('/dashboard/randomize_weapon/')
def random_weapon():
    if 'user_id' not in session:
        return redirect('/')
    else:
        data = {
            'id': session['user_id']
        }
        logged_in_user = user.User.get_user_by_id(data)
        random_number ={
            'id' : random.randrange(0, 90)
        } 
        print(type(random_number))
        random_weapon = weapon.Weapon.get_weapon_with_sub_and_special((random_number))
        return render_template('randomize_weapon.html', logged_in_user=logged_in_user, random_weapon = random_weapon)

# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& UN-REGISTERED USERS &&&&&&&&&&&&&&&&&&&&&&&&&&&&&

@app.route('/new/dashboard/')
def new_dash():
    return render_template('unknown_dashboard.html')

@app.route('/new/dashboard/maps/')
def new_maps():
    all_maps = map.Map.get_all_maps()
    return render_template('unknown_maps.html', all_maps=all_maps)

@app.route('/new/dashboard/weapons/')
def new_weapon():
    all_weapons = weapon.Weapon.get_all_weapons_with_kit()
    return render_template('unknown_weapons.html', all_weapons = all_weapons)

@app.route('/new/dashboard/randomize_weapon/')
def new_randomize():
    random_number ={
        'id' : random.randrange(0, 91)
    } 
    random_weapon = weapon.Weapon.get_weapon_with_sub_and_special((random_number))
    return render_template('unknown_randomize_weapon.html', random_weapon = random_weapon)

@app.route('/new/view-weapon/<int:weapon_id>')
def new_view_weapon(weapon_id):
    weapon_selection = {
        'id' : weapon_id
    }
    arm = weapon.Weapon.get_weapon_with_sub_and_special(weapon_selection)
    print(arm)
    return render_template('unknown_view_weapon.html', arm = arm)