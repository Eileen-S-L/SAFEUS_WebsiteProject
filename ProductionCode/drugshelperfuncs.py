import csv

data_file = "Minidrugdataset.csv"

def load_drugdata():
    '''loads the data and returns a list format'''
    data_list = []
    with open (data_file, mode= 'r') as data_file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data_list.append(row)
    return data_list
            
def search_by_state(state):
    '''returns results(row from dataset) based on state as input'''
    data = load_drugdata()
    results = [row for row in data if row['State'].strip() == state.lower()]
    return results

def search_by_year(year):
    ''''returns results (row from dataset) based on year as input'''
    data = load_drugdata()
    results = [row for row in data if row['Year'].strip() == str(year)]
    return results

    
    
