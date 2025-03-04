import datetime
from flask import Blueprint, redirect, render_template, session
from database import DatabaseHandler
# Imports flask blueprint template
dashboardBlueprint = Blueprint('dashboard', __name__)

def calculateCalories(exercises, foods):

    #to do
    #1 Make a new route for calculating calories
        #This will have a form containing date, age, height etc.
    #2 when this is run POST the form data to the route and then pull back exercise and food details as we have done already
    #3 calculate the total calories and then render a template passing in this value and anything else you want too.
    totalCals = 0

    for food in foods:
        totalCals += int(food[3])

    print(totalCals)
    
    # print(food)
    # print(exercises)
    return 1

# Creates bluepring and stores it under an identifier
@dashboardBlueprint.route('/dashboard')
def dashboard():
    ##Pull back any data for today's date
    currentUser = session.get('currentUser')

    if not(currentUser):
        return redirect("/")
    
    db = DatabaseHandler("appData.db")
    today = datetime.datetime.now().date()
    exercises = db.getWorkouts(currentUser, today)
    food = db.getFood(currentUser, today)


    cals = calculateCalories(exercises,food)
    return render_template('dashboard.html', testData = "this is some data")
# Sets URL extension and returns to html file

