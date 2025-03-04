from flask import Blueprint, app, render_template, redirect, request, session
from database import DatabaseHandler
# Imports flask blueprint template
calorieInputBlueprint = Blueprint('calorieinput', __name__)
# Stores blueprint under identifier
@calorieInputBlueprint.route('/calorieinput')
def calorieInput():
    return render_template('calorieInput.html')
# Routes blueprint to corresponding URL extension and returns to correct HTML file

createFoodBlueprint = Blueprint('calorieInput', __name__)

@createFoodBlueprint.route('/calorieinput', methods = ['post'])
def createFood():
    db = DatabaseHandler('appData.db')
    username = session['currentUser']
    foodName = request.form['foodName']
    foodCalories = request.form['foodCalories']
    mealType = request.form['mealType']
    
    response = db.createFood(username, foodName, foodCalories, mealType)
    if response:
        return redirect('/calorieinput')
    else:
        error_message = "Invalid Response"
        return render_template("calorieInput.html", error_message=error_message)

