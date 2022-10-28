import bcrypt
from flask_app import app
from flask_app.models import user
from flask import render_template, redirect, request, session, flash
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    if "user_id" not in session:
        return render_template("index.html")
    else:
        return redirect('/dashboard/')

@app.route("/register")
def register_form():
    if 'user_id' not in session:
        return render_template("register.html")
    else:
        return redirect('/dashboard/')

@app.route('/register/', methods=['post'])
def register():
    is_valid = user.validate(request.form)
    if not is_valid:
        return redirect('/')
    else:
        new_user = {
            'username': request.form['username'],
            'email': request.form['email'],
            'password': bcrypt.generate_password_hash(request.form['password'])
        }
        id = user.create_user(new_user)
        if not id:
            flash('Something Went Terribly Wrong')
            return redirect('/')
        else:
            session["user_id"] = id
            return redirect('/dashboard/')

@app.route("/login")
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
    id = user.get_user_by_email(data)
    if not id:
        flash("That email isn't in our database yet. Please Register")
        return redirect('/')
    if not bcrypt.check_password_hash(id.password, request.form['password']):
        flash("Wrong Password")
        return redirect('/')
    else:
        session['user_id'] = id.id
        return redirect ('/dashboard/')

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
        logged_in_user = user.get_user_by_id(data)
        all_users = user.get_all_users()
        
        return render_template('dashboard.html', logged_in_user = logged_in_user, all_users = all_users)