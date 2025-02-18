from flask import Blueprint, render_template
import matplotlib.pyplot as plt

# Imports flask blueprint template
workoutPageBlueprint = Blueprint('workoutpage', __name__)
# Stores blueprint under identifier
@workoutPageBlueprint.route('/workoutpage')
def workoutPage():
    return render_template('workoutPage.html')
# Routes blueprint to corresponding URL extension and returns to correct HTML document
