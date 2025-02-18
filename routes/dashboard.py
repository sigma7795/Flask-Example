from flask import Blueprint, render_template
# Imports flask blueprint template
dashboardBlueprint = Blueprint('dashboard', __name__)
# Creates bluepring and stores it under an identifier
@dashboardBlueprint.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')
# Sets URL extension and returns to html file

