import csv

import os
data_file = os.path.join(os.path.dirname(__file__), "..", "Data", "Minidrugdataset.csv")


def load_drugdata():
    '''loads the data and returns a list format'''
    data_list = []
    with open (data_file, mode= 'r') as filing:
        csv_reader = csv.DictReader(filing)
        for row in csv_reader:
            data_list.append(row)
    return data_list
            
def search_by_state(state_name):
    '''returns results(row from dataset) based on state as input'''
    data = load_drugdata()
    results = [row for row in data if row['State'].strip().lower() == state_name.lower()]
    if len(results) == 0:
        print("No records found for state:", state_name)
    return results

def search_by_year(year):
    ''''returns results (row from dataset) based on year as input'''
    data = load_drugdata()
    results = [row for row in data_list if row['Year'].strip() == str(year)]
    if len(results) == 0:
        print("No records found for year:", year)
    return results


print(load_drugdata())

    
    
