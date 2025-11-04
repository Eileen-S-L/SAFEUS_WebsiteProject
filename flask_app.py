'''
The eventual location for the Flask app interface for the project.
'''
from flask import Flask
from ProductionCode.datasource import *
from flask import Flask, render_template, request
# from ProductionCode.core import * we shouldn't need this anymore

#datasource code
data = DataSource()

app = Flask(__name__)
""" Arguments: route
    Return Value: String/explaination of the website
    Purpose: To explain to users how to use routes to view data"""

@app.route('/')
def homepage():
    # row = int(request.args['drugchoice'])
    # request.args['drugchoice']
    return render_template("index.html")


@app.route('/year/<year>/substance/<substance>', strict_slashes = False)
def displaydatabyyear(substance, year):
    year = str(year).strip()
    substance = str(substance).strip()
    return str(data.get_data_by_year(substance, year))


@app.route('/state/<state>/substance/<substance>', strict_slashes = False)
def displaydatabystate(substance, state):
    state = str(state).strip()
    substance = str(substance).strip()
    return str(data.get_data_by_state(substance, state))


@app.route('/year', strict_slashes = False)
def search_year_online(year):
    return render_template("yeardatapage.html")


@app.route('/state', strict_slashes = False)
def search_state_online(state_name):
    return render_template("statedatapage.html")

""" Arguments: e
    Return Value: Instructions on how to get to an actual page
    Purpose: Tell users that they went to the wrong/nonexistent page and tell them how to get to a correct/real one"""
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404errorpage.html", title = "404 Not Found")

""" Arguments: e
    Return Value: A message stating that there is an error
    Purpose: To catch an error within the python code"""
@app.errorhandler(500)
def python_bug(e):
    return render_template("500errorpage.html", title = "500 Error")


""" Arguments: random word
    Return Value: None
    Purpose: To create an error within the code so the 500 error test can pass and be tested"""
@app.route('/wrong/<random>', strict_slashes = False)
def wrongfunction(random):
    raise Exception("Intentional error for testing 500 handler")




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5121)