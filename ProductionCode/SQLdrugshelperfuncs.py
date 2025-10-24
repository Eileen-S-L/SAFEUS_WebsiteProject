import csv
import os

data_file = os.path.join(os.path.dirname(__file__), "..", "Data", "Minidrugdataset.csv") 
#data_file = '../Data/Minidrugdataset.csv' 

            
def search_by_state(state_name=None):
    """ Arguments: state name
    Return Value: returns string 
    Purpose: To give results (row from dataset) based on state as input"""
    if not state_name:
        return "Page not found. Go to the homepage and look at the directions for searching through the data."
    results = []
    if len(results) == 0:
        return "No records found for state " + state_name
        print(result)
    return results

def search_by_year(year=None):
    """ Arguments: year
    Return Value: returns string 
    Purpose: To give returns results (row from dataset) based on year as input"""
    if not year:
        return "Page not found. Go to the homepage and look at the directions for searching through the data."
    results = []
    if results == []:
        return "No records found for year: " + str(year)
    return results