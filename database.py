import sqlite3 as sql #imports sqlite3 
import datetime
from flask import Flask, render_template, request, redirect #importing flask

class DatabaseHandler:
    def __init__(self, databaseName): #Creates database
        self.name = databaseName #Names database
        self.CurrentUser = None

    def getCurrentUser(self):
        return self.CurrentUser

    def resetCurrentUser(self):
        self.CurrentUser = None

    def createTables(self):
        connection = sql.connect(self.name) #Connects to database

        connection.execute('''CREATE TABLE IF NOT EXISTS user (
                        
                            username text primary key not null,
                            password text not null,
                            CHECK (length(password) >= 8) 
                           
                           );''') #Adds username and password checks
        
        connection.close() #Disconnects from database

    def createUser(self, username, password):

        
        connection = sql.connect(self.name) #Connects to database 
        try:

            connection.execute('''INSERT INTO user 
                           VALUES (?,?)''', (username, password)) #Creates new user by enterring new username and password into table
        
            connection.commit() #Commits changes to database

            connection.close() #Disconnects from database
            self.currentUser = username
            return True 
                        
        except Exception as e: #e means error, cant see errors with this
            print(e) #displays error to user
            connection.close() ##Disconnects from database
            return False

    def authenticateUser(self, username, password):
        connection = sql.connect(self.name) #Connects to database
        cursor = connection.cursor()
        cursor.execute('''SELECT username FROM user WHERE username = ? AND password = ? ;''', (username, password)) #Selects username and password
        result = cursor.fetchone()
        connection.close() #Disconnects from database

        if result != None:
            return True #User exists so return 'True'
            self.CurrentUser = username
        
        else: 
            return False #User does not exist so return 'False'
        

    def createWorkoutTables(self):
        try:
            connection = sql.connect(self.name)
            connection.execute('''
                               create table if not exists workout (
                                exerciseID INTEGER PRIMARY KEY AUTOINCREMENT,
                                username text,
                                workoutName text,
                                workoutType text,
                                distance INTEGER,
                                time INTEGER,
                                date DATE,
                               FOREIGN KEY (username) REFERENCES user(username) ON DELETE CASCADE
                               );''') #Creates table for workouts
        except Exception as e:
            print(e) #Prints error
        finally:
            connection.close() #Disconnects from database
    

    def createWorkout(self, username, workoutName, workoutType, workoutDistance, workoutTime):
        try:
            currentDate = datetime.datetime.now().date() #Gets current date
            connection = sql.connect(self.name) #Connects to database
            connection.execute('''INSERT INTO workout
                               (username, workoutName, workoutType, distance, time, date)
                               VALUES (?,?,?,?,?,?)''', (username, workoutName, workoutType, workoutDistance, workoutTime, currentDate)) 
                               #Creates new workout by enterring corresponding values into table
            
            connection.commit() #Commits changes to database

            connection.close() #Disconnects from database
            return True #Returns True if workout is created successfully
        

        except Exception as e: #e means error, cant see errors with this
            print(e) #displays error to user
            connection.close() ##Disconnects from database
            return False
    
    def getWorkouts(self, username, date = None):
        try:
            connection = sql.connect(self.name)
            cursor = connection.cursor()
            if date:
                cursor.execute('''SELECT workoutName, workoutType, distance, time FROM workout WHERE username = ? AND date = ?''', (username,date))
            else:
                cursor.execute('''SELECT workoutName, workoutType, distance, time FROM workout WHERE username = ?''', (username,))
            workouts = cursor.fetchall()
        except Exception as e:
            print(e)
            workouts = None
        finally:
            connection.close()
            return workouts
    
    def createFoodTables(self):
        try:
            connection = sql.connect(self.name) #Connects to database
            connection.execute('''
                               create table if not exists food (
                                foodID INTEGER PRIMARY KEY AUTOINCREMENT, 
                                username TEXT,
                                foodName TEXT,
                                foodCalories integer,
                                mealType TEXT,
                                date DATE,
                               FOREIGN KEY (username) REFERENCES user(username) ON DELETE CASCADE
                               );''') #Creates table for food with given fields
        except Exception as e:
            print(e) #Prints error
        finally:
            connection.close() #Disconnects from database
    

    def createFood(self, username, foodName, foodCalories, mealType):
        try:
            currentDate = datetime.datetime.now().date()
            connection = sql.connect(self.name) #Connects to database
            connection.execute('''INSERT INTO food
                               (username, foodName, foodCalories, mealType, date)
                               VALUES (?,?,?,?,?)''', (username, foodName, foodCalories, mealType, currentDate))
            
            connection.commit() #Commits changes to database
            connection.close() #Disconnects from database
            return True 
            
            

        except Exception as e: #e means error, cant see errors with this
            print(e) #displays error to user
            connection.close() ##Disconnects from database
            return False
    
    def getFood(self, username, date): 
        try:
            connection = sql.connect(self.name)
            cursor = connection.cursor()
            if date:
                cursor.execute('''SELECT * FROM food WHERE username = ? AND date = ?''', (username,date))
            else:
                cursor.execute('''SELECT * FROM food WHERE username = ?''', (username,))
            foods = cursor.fetchall()
        except Exception as e:
            print(e)
            foods = None
        finally:
            connection.close()
            return foods


    def getOldWorkouts(self, username, date):
        try:
            date = str(date)
            connection = sql.connect(self.name)
            cursor = connection.cursor()
            cursor.execute('''SELECT distance, workoutType, time FROM workout WHERE username = ? and date = ?''', (username, date))
            oldWorkouts = cursor.fetchall()
        except Exception as e:
            print(e) 
            oldWorkouts = None 
        finally:
            connection.close()
            return oldWorkouts

    def getOldFoods(self, username, date):
        date = request.form['date']
        try:
            date = str(date)
            connection = sql.connect(self.name)
            cursor = connection.cursor()

            # print("date", date)
            print("user:", username)
            # cursor.execute('''select * from food''')
            cursor.execute('''SELECT foodCalories FROM food WHERE username = ? and date = ?;''', (username, date))
            foodCaloriesForDay = cursor.fetchall()
            print("old food!" , foodCaloriesForDay)
        except Exception as e:
            print(e) 
            foodCaloriesForDay = None 
        finally:
            connection.close()
            return foodCaloriesForDay