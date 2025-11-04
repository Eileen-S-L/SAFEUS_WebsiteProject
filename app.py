import ProductionCode.core as core
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    """Arguments: None
    Return Value: HTML string
    Purpose: Displays a welcome message and instructions on how to use the application."""
    return render_template('index.html')

@app.route('/state/<state_name>', strict_slashes = False)
def search_state_online(state_name):
    """Arguments: state_name
    Return Value: String representation of search results
    Purpose: Searches the dataset for records matching the given state name and returns the results as a string."""
    return str(core.search_by_state(state_name))

@app.route('/year/<year>', strict_slashes = False)
def search_year_online(year):
    """Arguments: year
    Return Value: String representation of search results
    Purpose: Searches the dataset for records matching the given year and returns the results as a string."""
    return str(core.search_by_year(year))

@app.route('/state', strict_slashes = False)
def state_page():
    """Arguments: None
    Return Value: HTML string
    Purpose: Renders the state search page."""
    return render_template('state_page.html')

@app.route('/year', strict_slashes = False)
def year_page():
    """Arguments: None
    Return Value: HTML string
    Purpose: Renders the year search page."""
    return render_template('year_page.html')

@app.route('/about', strict_slashes = False)
def about_page():
    """Arguments: None
    Return Value: HTML string
    Purpose: Renders the about page."""
    return render_template('about_page.html')

if __name__ == '__main__':
    app.run()