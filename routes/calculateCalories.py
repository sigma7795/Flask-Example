from flask import Flask, request, redirect, url_for, render_template ,app, Blueprint, session
from database import DatabaseHandler
# Imports flask blueprint template
calorieCalculatorBlueprint = Blueprint('calorieCalculator', __name__)
# # Stores blueprint under identifier
@calorieCalculatorBlueprint.route('/calorietotal')
def calorieDetails():
    return render_template('calorieTotal.html')
# Routes blueprint to corresponding URL extension and returns to correct HTML file

caloriePageCalculatorBlueprint = Blueprint('caloriePageCalculator', __name__)
@caloriePageCalculatorBlueprint.route('/caloriepagecalculator',  methods=['post'])
def calorieinputtotal():
    totalCalories = 0
    db = DatabaseHandler('appData.db') # Initializes the DatabaseHandler to interact with the database
    userWeight = request.form['userWeight']
    userWeight = int(userWeight)
    userHeight = request.form['userHeight']
    userHeight = int(userHeight)
    userAge = request.form['userAge']
    userAge = int(userAge)
    userGender = request.form['userGender']
    date = request.form['date'] #Could be currentDate
    username = session.get("currentUser")
    # return(db.getOldWorkouts(username, date), db.getOldFoods(username, date))
    
    foodCaloriesForDay = db.getOldFoods(username, date)
    workoutDetailsForDay = db.getOldWorkouts(username, date)
    


    totalFoodCals = 0
    totalWorkoutDistance = 0
    totalWorkoutTime = 0

    for row in foodCaloriesForDay:
        totalFoodCals += int(row[0])

    for row in workoutDetailsForDay:
        totalWorkoutDistance += int(row[0])
    
    for row in workoutDetailsForDay:
        totalWorkoutTime += int(row[2])


    print("total cals", totalFoodCals)
    print('total workout distance', totalWorkoutDistance)
    print()

    if userGender.lower() == 'male':
        
        if workoutDetailsForDay[0][1] == 'run':
            workoutCaloriesForDay = userWeight*workoutDetailsForDay[0][0]*1.036
            totalCalories = (totalFoodCals) - ((9.65*userWeight) + (5.73*userHeight) - (5.08*userAge) + 260) - workoutCaloriesForDay
        
        elif workoutDetailsForDay[0][1] == 'swim':
            workoutCaloriesForDay = 523*workoutDetailsForDay[0][2]
            totalCalories = (totalFoodCals) - ((9.65*userWeight) + (5.73*userHeight) - (5.08*userAge) + 260) - workoutCaloriesForDay
        
        else: 
            workoutCaloriesForDay = 7*userWeight*workoutDetailsForDay[0][2]/60
            totalCalories = (totalFoodCals) - ((9.65*userWeight) + (5.73*userHeight) - (5.08*userAge) + 260) - workoutCaloriesForDay
    else:
        
        if workoutDetailsForDay[0][1] == 'run':
            workoutCaloriesForDay = userWeight*workoutDetailsForDay[0][0]*0.825
            totalCalories = (totalFoodCals) - ((7.38*userWeight) + (6.07*userHeight) - (2.31*userAge) + 43) - workoutCaloriesForDay
        
        elif workoutDetailsForDay[0][1] == 'swim':
            workoutCaloriesForDay = 523*workoutDetailsForDay[0][2]
            totalCalories = (totalFoodCals) - ((7.38*userWeight) + (6.07*userHeight) - (2.31*userAge) + 43) - workoutCaloriesForDay
        
        else:
            workoutCaloriesForDay = 7*userWeight*workoutDetailsForDay[0][2]/60
            totalCalories = (totalFoodCals) - ((7.38*userWeight) + (6.07*userHeight) - (2.31*userAge) + 43) - workoutCaloriesForDay
    
    return render_template("dayView.html",date = date, totalFoodCals = totalCalories, totalWorkoutDistance = totalWorkoutDistance, totalWorkoutTime = totalWorkoutTime)
