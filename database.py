import sqlite3 as sql #imports sqlite3 

class DatabaseHandler:
    def __init__(self, databaseName): #Creates database
        self.name = databaseName #Names database

    def createTables(self):
        connection = sql.connect(self.name) #Connects to database

        connection.execute('''CREATE TABLE IF NOT EXISTS user (
                        
                            username text primary key, not null
                            password text not null 
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
            return True 
                        
        except Exception as e: #e means error, cant see errors with this
            print(e) #displays error to user
            connection.close() ##Disconnects from database
            return False

    def authenticateUser(self, username, password):
        connection = sql.connect(self.name) #Connects to database
        cursor = connection.cursor()
        cursor.execute('''SELECT username FROM user WHERE username = ? AND password = ? ;''', (username, password)) #Highlights username and password in table
        result = cursor.fetchone()
        connection.close() #Disconnects from database

        if result != None:
            return True #User exists so return 'True'
        
        else: 
            return False #User does not exist so return 'False'
        

    def createWorkoutTables(self):
        try:
            connection = sql.connect(self.name)
            connection.execute('''
                               create table workout (
                                username PRIMARY KEY,
                                workoutName text,
                                workoutType,
                                distance float,
                                time float,
                               )''')
        except Exception as e:
            print(e)
        finally:
            connection.close()
    
    def createWorkout(self, username, workoutName, workoutType, distance, time):
        try:
            connection = sql.connect(self.name)
            connection.execute('''INSERT INTO workout
                               VALUES (?,?,?,?,?,?)''', (username, workoutName, workoutType, distance, time))
            
            connection.commit() #Commits changes to database

            connection.close() #Disconnects from database
            return True 
        
        except Exception as e: #e means error, cant see errors with this
            print(e) #displays error to user
            connection.close() ##Disconnects from database
            return False