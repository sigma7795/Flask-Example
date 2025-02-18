from flask import Blueprint, render_template
# Imports flask blueprint template
calorieInputBlueprint = Blueprint('calorieinput', __name__)
# Stores blueprint under identifier
@calorieInputBlueprint.route('/calorieinput')
def calorieInput():
    return render_template('calorieInput.html')
# Routes blueprint to corresponding URL extension and returns to correct HTML file

