from flask import Flask, render_template, request, redirect #importing flask
from routes.index import homeBlueprint #importing index from routes

from database import DatabaseHandler #importing database from database

from routes.userManagement import signupBlueprint, createUserBlueprint, authenticateUserBlueprint, logoutBlueprint #importing userManagement from routes


from routes.dashboard import dashboardBlueprint 
from routes.workoutInput import workoutInputBlueprint, createWorkoutBlueprint
from routes.calorieInput import calorieInputBlueprint, createFoodBlueprint #, displayFoodBlueprint
from routes.workoutViewer import workoutViewerBlueprint
from routes.workoutGraph import workoutGraphBlueprint
from routes.workoutInput import createWorkoutBlueprint
from routes.calculateCalories import caloriePageCalculatorBlueprint, calorieCalculatorBlueprint
app = Flask(__name__) #Creates website application instance of flask
app.config['SECRET_KEY'] = 'THISISABADKEY' #Creates secret key for website
db = DatabaseHandler('appData.db') #OOP instance of database
#db.createTables() runs user creation tables
#db.createWorkoutTables() runs creation workout tables
#db.createFoodTables() runs creation food tables

##routing 
app.register_blueprint(homeBlueprint)
app.register_blueprint(signupBlueprint)
app.register_blueprint(createUserBlueprint)
app.register_blueprint(authenticateUserBlueprint)
app.register_blueprint(dashboardBlueprint)
app.register_blueprint(logoutBlueprint)
app.register_blueprint(workoutInputBlueprint)
app.register_blueprint(calorieInputBlueprint)
app.register_blueprint(workoutViewerBlueprint)
app.register_blueprint(workoutGraphBlueprint)
app.register_blueprint(createWorkoutBlueprint)
app.register_blueprint(createFoodBlueprint)
app.register_blueprint(calorieCalculatorBlueprint)
app.register_blueprint(caloriePageCalculatorBlueprint)

# app.register_blueprint(displayFoodBlueprint)

#######
app.run(debug = True)
