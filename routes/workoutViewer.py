from flask import Blueprint, render_template, session
from database import DatabaseHandler
# Imports flask blueprint template
workoutViewerBlueprint = Blueprint('workoutviewer', __name__)
# Stores blueprint under identifier
@workoutViewerBlueprint.route('/graphviewer')
def workoutViewer():
    db = DatabaseHandler('appData.db')
    workouts = db.getWorkouts(session['currentUser'])
    return render_template('workoutViewer.html')
# Routes blueprint to corresponding URL extension and returns template to corect HTML document