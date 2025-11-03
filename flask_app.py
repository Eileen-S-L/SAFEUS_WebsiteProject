'''
The eventual location for the Flask app interface for the project.
'''
from flask import Flask
import csv
from ProductionCode.datasource import *
from flask import Flask, render_template, request
from ProductionCode.core import *


#from ProductionCode.SQLdrugshelperfuncs import *

#datasource code
data = DataSource()

app = Flask(__name__)
""" Arguments: route
    Return Value: String/explaination of the website
    Purpose: To explain to users how to use routes to view data"""

@app.route('/')
def homepage():
    return render_template("index.html", title = "Cocaine in 2002")
    #return "Welcome to the homepage! <br> <br> How to view the data: <br> Go to route '/' and put in a Substance and then / to insert your substance name,<br> Then type in '/state/*a state*' to see data per state <br> Or Type in route '/year/*a year*' to view the data according to year"



""" Arguments: route and how to view the slashes
    Return Value: All the data from rows with the inputted year
    Purpose: To allow users to see drug data by year"""
@app.route('/substance/<substance>/year/<year>', strict_slashes = False)
@app.route('/Substance/<substance>/Year/<year>', strict_slashes = False)
@app.route('/Year/<year>/Substance/<substance>', strict_slashes = False)
@app.route('/year/<year>/substance/<substance>', strict_slashes = False)
def displaydatabyyear(substance, year):
    year = str(year).strip()
    substance = str(substance).strip()
    return str(data.get_data_by_year(substance, year))


@app.route('/substance/<substance>/state/<state>', strict_slashes = False)
@app.route('/Substance/<substance>/State/<state>', strict_slashes = False)
@app.route('/State/<state>/Substance/<substance>', strict_slashes = False)
@app.route('/state/<state>/substance/<substance>', strict_slashes = False)
def displaydatabystate(substance, state):
    state = str(state).strip()
    substance = str(substance).strip()
    return str(data.get_data_by_state(substance, state))

""" Arguments: e
    Return Value: Instructions on how to get to an actual page
    Purpose: Tell users that they went to the wrong/nonexistent page and tell them how to get to a correct/real one"""
@app.errorhandler(404)
def page_not_found(e):
    return "Page not found. Go to the homepage and look at the directions for searching through the data."

""" Arguments: e
    Return Value: A message stating that there is an error
    Purpose: To catch an error within the python code"""
@app.errorhandler(500)
def python_bug(e):
    return "You made an error! Go back through your code to find it!"

""" Arguments: random word
    Return Value: None
    Purpose: To create an error within the code so the 500 error test can pass and be tested"""
@app.route('/wrong/<random>', strict_slashes = False)
def wrongfunction(random):
    raise Exception("Intentional error for testing 500 handler")

""" Arguments: route
    Return Value: Site page where you can view the data for a particular chosen state
    Purpose: To allow users to view the data by the state"""
@app.route('/statedata')
def homedatapage():
    row = int(request.args['statechoice'])
    statedata = get_data_by_year('cocaine', '2002')[row]
    return render_template("statedatapage.html", statedatadisplay = statedata, statedisplay = statedata[0] )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5221)