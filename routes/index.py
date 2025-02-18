from flask import Blueprint, render_template 
# Imports flask template
homeBlueprint = Blueprint('home', __name__)
# Creates blueprint and stores is under identifier
#routing
@homeBlueprint.route('/')
def home():
    return render_template('index.html')
# Creates routing URL and creates template in html file

