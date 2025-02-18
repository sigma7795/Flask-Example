from flask import Blueprint, render_template, redirect, request, session
from database import DatabaseHandler
# Imports flask blueprint template
signupBlueprint = Blueprint('signup', __name__)
# Stores blueprint under identifier
@signupBlueprint.route('/signup')
def signup():
    return render_template('signup.html')
# Sets blurprint routing and URL

createUserBlueprint = Blueprint('createUser', __name__)
authenticateUserBlueprint = Blueprint('authenticateUser', __name__)
logoutBlueprint= Blueprint('logout', __name__)

@logoutBlueprint.route('/logout')
def logout():
    session.clear()
    return redirect('/')


@authenticateUserBlueprint.route('/authenticate', methods = ['post'])
def authenicateUser():
    db = DatabaseHandler('appData.db')
    username = request.form['username']
    password = request.form['password']

    if db.authenticateUser(username, password) == True:
        session['currentUser'] = username
        return redirect('/dashboard')
        
    else:
        return redirect('/')



@createUserBlueprint.route('/createUser', methods = ['post'])
def createUser():
    db = DatabaseHandler('appData.db')
    username = request.form['username']
    password = request.form['password']
    rePassword = request.form['rePassword']
    if password == rePassword:
        responce = db.createUser(username,password)
        if responce == True:
            return redirect('/')
        else:
             error_message = "Username already exists"
             return render_template("signup.html", error_message=error_message)
            
    else:
        error_message = "Passwords don't match"
        return render_template("signup.html", error_message=error_message)