#This is test_cl.py for team project -- commanline.py

import unittest
form ProductionCode.drugshelperfuncs import *

class SearchByState(unittest.Testcase):
  def setUp(self):
    load_drugdata() #load data for each test case
  def invalid_state_name(self):
    '''ensures that the function returns statement for invalid US state input'''
    expected = "Not a US State"
    result = search_by_state('Canada')
    self.asssertEqual(result,expected)
