from flask import Flask, render_template, request, redirect
from database import DatabaseHandler
from routes.index import homeBlueprint
from routes.userManagement import signupBlueprint, createUserBlueprint, authenticateUserBlueprint, logoutBlueprint
from routes.dashboard import dashboardBlueprint
from routes.workoutPage import workoutPageBlueprint 
from routes.workoutInput import workoutInputBlueprint
from routes.calorieInput import calorieInputBlueprint
from routes.workoutViewer import workoutViewerBlueprint
from routes.workoutGraph import workoutGraphBlueprint

app = Flask(__name__)
app.config['SECRET_KEY'] = 'THISISABADKEY'
db = DatabaseHandler('appData.db') #OOP instance of database
# db.createTables()

##routing 
app.register_blueprint(homeBlueprint)
app.register_blueprint(signupBlueprint)
app.register_blueprint(createUserBlueprint)
app.register_blueprint(authenticateUserBlueprint)
app.register_blueprint(dashboardBlueprint)
app.register_blueprint(logoutBlueprint)
app.register_blueprint(workoutPageBlueprint)
app.register_blueprint(workoutInputBlueprint)
app.register_blueprint(calorieInputBlueprint)
app.register_blueprint(workoutViewerBlueprint)
app.register_blueprint(workoutGraphBlueprint)
#######
app.run(debug = True)