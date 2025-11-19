import unittest
from ProductionCode.datasource import *

# Datasource method tests  
class TestDataSourceMethods(unittest.TestCase):

    def setUp(self):
        """ Arguments: self
        Return Value: None
        Purpose: Sets up a DataSource instance for testing. """
        self.ds = DataSource()

    def test_get_data_by_year_valid(self):
        """ Arguments: self
        Return Value: None
        Purpose: Tests get_data_by_year with a valid year. """
        records = self.ds.get_data_by_year('cocaine', '2010')
        self.assertIsInstance(records, list)
        self.assertGreater(len(records), 0)

    def test_get_data_by_year_invalid(self):
        """ Arguments: self
        Return Value: None
        Purpose: Tests get_data_by_year with an invalid year. """
        result = self.ds.get_data_by_year('cocaine', '2025')
        self.assertListEqual(result, [])

    def test_get_data_by_state_valid(self):
        """ Arguments: self
        Return Value: None
        Purpose: Tests get_data_by_state with a valid state. """
        records = self.ds.get_data_by_state('cocaine', 'California')
        self.assertIsInstance(records, list)
        self.assertGreater(len(records), 0)

    def test_get_data_by_state_invalid(self):
        """ Arguments: self
        Return Value: None
        Purpose: Tests get_data_by_state with an invalid state. """
        result = self.ds.get_data_by_state('cocaine', 'Nigeria')
        self.assertListEqual(result, [])