from flask import Blueprint, render_template
# Imports flask blueprint template
workoutViewerBlueprint = Blueprint('workoutviewer', __name__)
# Stores blueprint under identifier
@workoutViewerBlueprint.route('/workoutviewer')
def workoutViewer():
    return render_template('workoutViewer.html')
# Routes blueprint to corresponding URL extension and returns template to corect HTML document