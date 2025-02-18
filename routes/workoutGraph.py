from flask import Blueprint, render_template
# Imports flask blueprint template
workoutGraphBlueprint = Blueprint('workoutgraph', __name__)
# Stores blueprint under identifier
@workoutGraphBlueprint.route('/workoutgraph')
def workoutGraph():
    return render_template('workoutGraph.html')
# Routes blueprint to corresponding URL extension and returns template to HTML file