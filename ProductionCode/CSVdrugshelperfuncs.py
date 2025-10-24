'''
We probably need to refractor this file into Datasource.py format and add more function
'''
import csv
import os

data_file = os.path.join(os.path.dirname(__file__), "..", "Data", "Minidrugdataset.csv") 
#data_file = '../Data/Minidrugdataset.csv' 

def load_drugdata():
    """ Arguments: None
    Return Value: The data as a list
    Purpose: loads the data and returns a list format"""
    data_list = []
    with open (data_file, mode= 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data_list.append(row)
    return data_list
            
def search_by_state(state_name=None):
    """ Arguments: state name
    Return Value: returns string 
    Purpose: To give results (row from dataset) based on state as input"""
    if not state_name:
        return "Page not found. Go to the homepage and look at the directions for searching through the data."
    data = load_drugdata()
    results = []
    for row in data:
        if row['\ufeffState'].strip().lower() == str(state_name).strip().lower():
            results.append(row)
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
    data = load_drugdata()
    results = []
    for row in data:
        if row['Year']==str(year).strip():
            results.append(row)
    if results == []:
        return "No records found for year: " + str(year)
    return results
