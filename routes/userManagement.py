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


@createUserBlueprint.route('/createUser', methods = ['post']) # Defines the route for creating a new user via POST request
def createUser():

    db = DatabaseHandler('appData.db') # Initializes the DatabaseHandler to interact with the database
    

    username = request.form['username']
    password = request.form['password']
    rePassword = request.form['rePassword']
    # Retrieve the values of username, password and rePassword submitted through the form
    

    if password == rePassword: # Check if the password and confirm password fields match
        response = db.createUser(username, password) # If the passwords match, create the user in the database
        
        if response == True: # If the user is successfully created, redirect to the homepage
            return redirect('/')
        else:
            error_message = "Username already exists"  # If the username already exists, show an error message
            return render_template("signup.html", error_message=error_message)
            
    else:
        error_message = "Passwords don't match" # If the passwords don't match, show an error message
        return render_template("signup.html", error_message=error_message)


@authenticateUserBlueprint.route('/authenticate', methods = ['post']) # Defines the route for authenticating the user via POST request
def authenticateUser():
    
    db = DatabaseHandler('appData.db') # Initializes the DatabaseHandler to interact with the database
    
    username = request.form['username'] # Retrieve the username and password from the form submitted via form on webpage
    password = request.form['password']
    
    if db.authenticateUser(username, password) == True: # Check if the provided username and password are valid using method previously written
        session['currentUser'] = username  # If authentication is successful, store the username in the session
        
        return redirect('/dashboard') # Redirect to the dashboard page
    else:

        return redirect('/') # If authentication fails, redirect to the login page


@logoutBlueprint.route('/logout') #Defines route for logging out
def logout():
    db = DatabaseHandler('appData.db') # Initializes the DatabaseHandler to interact with the database
    db.resetCurrentUser() #Resets the current user in the database
    session.clear() #Clears the session data
    return redirect('/') #User redirected to home page


