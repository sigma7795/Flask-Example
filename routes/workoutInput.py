from flask import Blueprint, render_template, redirect, request, session
from database import DatabaseHandler
# Imports flask blueprint template
workoutInputBlueprint = Blueprint('workoutinput', __name__)
# Stores blueprint under identifier
@workoutInputBlueprint.route('/workoutinput')
def workoutInput():
    return render_template('workoutInput.html')
# Routes blueprint to corresponding URL and returns it to the correct HTML file

createWorkoutBlueprint = Blueprint('createWorkout', __name__)
@createWorkoutBlueprint.route('/workoutinput', methods = ['post'])
def createWorkout():
    db = DatabaseHandler('appData.db')
    username = session['currentUser']
    workoutName = request.form['workoutName']
    workoutType = request.form['workoutType']
    workoutDistance = request.form['workoutDistance']
    workoutTime = request.form['workoutTime']

    print(workoutName)

    response = db.createWorkout(username, workoutName, workoutType, workoutDistance, workoutTime)
    if response:
        return redirect('/workoutinput')
    else:
        error_message = "Invalid Response"
        return render_template("workoutInput.html", error_message=error_message)
    