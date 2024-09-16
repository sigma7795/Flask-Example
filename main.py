from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'THISISABADKEY'


##routing
@app.route('/')
def home():
    return render_template('index.html') #names webpage what you want

@app.route('/signup')
def signup():
    return



#######
app.run(debug = True)