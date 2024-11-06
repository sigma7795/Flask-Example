from flask import Blueprint, render_template

workoutPageBlueprint = Blueprint('workoutpage', __name__)

@workoutPageBlueprint.route('/workoutpage')
def workoutPage():
    return render_template('workoutpage.html')

