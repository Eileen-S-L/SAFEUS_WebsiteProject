# import pandas as pd
# #helper function for reading columns by the state name
# def searchstatename(state):
#     df = pd.read_csv("drugs-1.csv",
#                     dtype = {"State": str})

# #helper function for reading colums by the year
# def searchbyyear():

imprort csv

data_file = "minidrugs2.csv"

def load_drugdata():
    data_list = []
    with open (data_file, mode= 'r') as data_file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data_list.append(row)
    return data_list
            
def search_by_state(state):
    data = load_drugdata()
    results = [row for row in data if row['State'].strip().lower() == state_name.lower()]
    if len(results) == 0:
        print("No records found for state:", state_name)
    return results

def search_by_year(year):
    data = load_drugdata()
    
    
