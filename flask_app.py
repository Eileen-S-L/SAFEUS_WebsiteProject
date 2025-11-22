'''
The eventual location for the Flask app interface for the project.
'''
from flask import Flask
from ProductionCode.datasource import *
from flask import Flask, render_template, request


#datasource includes sets of searching_functions
data = DataSource()

app = Flask(__name__)

""" Arguments: route '/'
    Return Value: String/explaination of the website
    Purpose: To explain to users how to use routes to view data"""
@app.route('/')
def homepage():
    return render_template("index.html")

@app.route('/start_explore', strict_slashes=False)
def Explorepage():
    return render_template("start_explore.html")

""" Arguments: route '/about'
    Return Value: A website page explaining the data
    Purpose: To allow users to learn about the origins of the data"""
@app.route('/about', strict_slashes = False)
def aboutthedata():
    return render_template("about.html")

""" Arguments: route
    Return Value: the data by substance and year
    Purpose: To give users a page where they can view the data by year and substance"""
@app.route('/year/<year>/substance/<substance>', strict_slashes = False)
def displaydatabyyear(year, substance):
    year = str(year)
    substance = str(substance).strip()
    search_result=data.get_data_by_year(substance, year)
    Html_template='data_results.html'
    return render_template(Html_template, result=search_result, type = year, sub = substance, subname = substance.title())

""" Arguments: route
    Return Value: the data by substance and state
    Purpose: To give users a page where they can view the data by state and substance"""
@app.route('/state/<state>/substance/<substance>', strict_slashes = False)
def displaydatabystate(state, substance):
    state = str(state).strip()
    substance = str(substance).strip()
    search_result=data.get_data_by_state(substance, state)
    Html_template='data_results.html'
    return render_template(Html_template, result=search_result, type = state.title(), sub = substance, subname = substance.title())


""" Arguments: route
    Return Value: a search box for year
    Purpose: To give users a place to search for data by year"""
@app.route('/year', strict_slashes = False)
def search_year_online():
    return render_template("search_year.html", yeardisplay='Seach By Year')

""" Arguments: route
    Return Value: a search box for state
    Purpose: To give users a place to search for data by state"""
@app.route('/state', strict_slashes = False)
def search_state_online():
    return render_template("search_state.html", statedisplay='Search By State')

""" Arguments: e
    Return Value: Instructions on how to get to an actual page
    Purpose: Tell users that they went to the wrong/nonexistent page and tell them how to get to a correct/real one"""
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html", title = "404 Not Found")

""" Arguments: e
    Return Value: A message stating that there is an error
    Purpose: To catch an error within the python code"""
@app.errorhandler(500)
def python_bug(e):
    return render_template("500.html", title = "500 Error")


""" Arguments: random word
    Return Value: None
    Purpose: To create an error within the code so the 500 error test can pass and be tested"""
@app.route('/wrong/<random>', strict_slashes = False)
def wrongfunction(random):
    raise Exception("Intentional error for testing 500 handler")

if __name__ == '__main__':
    app.run(debug= True, host='0.0.0.0', port=5221)