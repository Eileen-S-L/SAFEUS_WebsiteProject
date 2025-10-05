#This is test_cl.py for team project -- commanline.py

import unittest
from ProductionCode.drugshelperfuncs import *

class SearchByState(unittest.Testcase):
    def setUp(self):
    load_drugdata() #load data for each test case
    def invalid_state_name(self):
    '''ensures that the function returns statement for invalid US state input'''
    expected = "Not a US State"
    result = search_by_state('Canada')
    self.asssertEqual(result,expected)

class SearchByName(unittest.Testcase):
    def setUp(self):
        load_drugdata()
    def invalid_year(self):
        '''ensures that function returns appropriate statement for invalid year input'''
        expected = "No records found for year: 2100"
        result = search_by_year("2100")
        self.assertEqual(result, expected)
