#This is test_cl.py for team project -- commanline.py

import unittest
from ProductionCode.drugshelperfuncs import *

class SearchByState(unittest.TestCase):
    def setUp(self):
        load_drugdata() #load data for each test case
    def test_invalid_state_name(self):
        '''ensures that the function returns statement for invalid US state input'''
        expected = "No records found for state Canada"
        result = search_by_state('Canada')
        self.assertEqual(result, expected)

    def test_valid_state_name(self):
        '''ensures that the function returns list of dictionaries for valid US state input'''
        result = search_by_state('Alabama')
        self.assertIsInstance(result, list)
        self.assertIsInstance(result[0], dict)
        self.assertIn(result[0]['State'], 'Alabama')

class SearchByName(unittest.TestCase):
    def setUp(self):
        load_drugdata()
    def test_invalid_year(self):
        '''ensures that function returns appropriate statement for invalid year input'''
        expected = "No records found for year: 2100"
        result = search_by_year("2100")
        self.assertEqual(result, expected)

# Command line test
def main_test_year_n(self):
    code = subprocess.Popen(['python3','--year', 'command_line.py', '2002'],stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf8')
    output, err = code.communicate()
    # self.assertEqual("column_1", output.strip())
    
    code.terminate()
def main_test_state_edge(self):
    code = subprocess.Popen(['python3','--state', 'command_line.py', 'alabama'],stdin=subprocess.PIPE, 
        stdout=subprocess.PIPE, encoding='utf8')
        
        output, err = code.communicate()
        # self.assertEqual("Usage: python3 basic_cl.py row column", output.strip())