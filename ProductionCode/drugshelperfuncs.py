import csv

import os
data_file = os.path.join(os.path.dirname(__file__), "..", "Data", "Minidrugdataset.csv") 
#data_file = '../Data/Minidrugdataset.csv' 

def load_drugdata():
    '''loads the data and returns a list format'''
    data_list = []
    with open (data_file, mode= 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data_list.append(row)
    return data_list
            
def search_by_state(state_name):
    '''returns results (row from dataset) based on state as input'''
    data = load_drugdata()
    results = []
    for row in data:
        if row['\ufeffState'].strip().lower() == state_name.lower():
            results.append(row)
    if len(results) == 0:
        return "No records found for state " + state_name
        print(result)
    return results

def search_by_year(year):
    ''''returns results (row from dataset) based on year as input'''
    data = load_drugdata()
    results = []
    for row in data:
        if row['Year']==str(year).strip():
            results.append(row)
    if results == []:
        return "No records found for year: " + str(year)
    return results

