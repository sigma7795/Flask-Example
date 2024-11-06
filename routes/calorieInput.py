from flask import Blueprint, render_template

calorieInputBlueprint = Blueprint('calorieinput', __name__)

@calorieInputBlueprint.route('/calorieinput')
def calorieInput():
    return render_template('calorieinput.html')