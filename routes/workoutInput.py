from flask import Blueprint, render_template
# Imports flask blueprint template
workoutInputBlueprint = Blueprint('workoutinput', __name__)
# Stores blueprint under identifier
@workoutInputBlueprint.route('/workoutinput')
def workoutInput():
    return render_template('workoutInput.html')
# Routes blueprint to corresponding URL and returns it to the correct HTML file

