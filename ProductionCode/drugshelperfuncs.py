import csv

data_file = "Minidrugdataset.csv"

def load_drugdata():
    data_list = []
    with open (data_file, mode= 'r') as data_file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data_list.append(row)
    return data_list
            
def search_by_state(state):
    data = load_drugdata()
    results = [row for row in data if row['State'].strip().lower() == state.lower()]
    return results

def search_by_year(year):
    data = load_drugdata()
    
    
