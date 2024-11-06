from flask import Blueprint, render_template

workoutInputBlueprint = Blueprint('workoutinput', __name__)

@workoutInputBlueprint.route('/workoutinput')
def workoutInput():
    return render_template('workoutinput.html')