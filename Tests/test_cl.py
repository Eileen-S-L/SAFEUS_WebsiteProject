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
        self.assertEqual(result,expected)

class SearchByName(unittest.TestCase):
    def setUp(self):
        load_drugdata()
    def test_invalid_year(self):
        '''ensures that function returns appropriate statement for invalid year input'''
        expected = "No records found for year: 2100"
        result = search_by_year("2100")
        self.assertEqual(result, expected)

