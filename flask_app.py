'''
The eventual location for the Flask app interface for the project.
'''
from flask import Flask
import csv
from ProductionCode.drugshelperfuncs import *

app = Flask(__name__)

""" Arguments: route
    Return Value: String/explaination of the website
    Purpose: To explain to users how to use routes to view data"""
@app.route('/')
def homepage():
    return "Welcome to the homepage! <br> <br> How to view the data: <br> Go to route '/' and put in a row/column to see data. Column 0 shows state names, column 1 shows year, and column 3 shows population size for ages 12-17 <br> Type in route '/year/*a year*' to view the data according to year"

""" Arguments: None
    Return Value: None
    Purpose: Loading the csv data into the code so it can be accessed"""
dummy_data = []
def load_data():
    with open('Data/Minidrugdataset.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            dummy_data.append(row)

""" Arguments: route and how to view the slashes in the route
    Return Value: The data by row and column number
    Purpose: To allow users to search for data by the colum and row number"""
@app.route('/<row>/<column>', strict_slashes = False)
def get_cell(row, column):
    return dummy_data[int(row)][int(column)]

""" Arguments: route and how to view the slashes
    Return Value: All the data from rows with the inputted year
    Purpose: To allow users to see drug data by year"""
@app.route('/year/<year>', strict_slashes = False)
def displaydatabyyear(year):
    return str(search_by_year(year))

@app.route('/state/{state}', strict_slashes = False)
def displaydatabystate(state):
    return str(search_by_state(str(state)))

if __name__ == '__main__':
    load_data()
    app.run()