from flask import Blueprint, render_template 
# Imports flask blueprint template
graphViewerBlueprint = Blueprint('home', __name__)
# Creates blueprint and stores is under identifier
@graphViewerBlueprint.route('/')
def home():
    return render_template('graphviewer.html')
# Creates routing URL and creates template in html file

import pandas as pd
import matplotlib.pyplot as plt

s = pd.Series([1, 2, 3])
fig, ax = plt.subplots()
s.plot.line()
fig.savefig('my_plot.png')
