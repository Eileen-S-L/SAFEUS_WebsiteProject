import unittest
from ProductionCode.drugshelperfuncs import *
import subprocess

class TestCommandLine(unittest.TestCase):

    def test_no_arguments(self):
        '''Checks that running the script with no arguments displays usage instructions.'''
        result = subprocess.Popen(['python3', 'ProductionCode/command_line.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = result.communicate()
        self.assertIn(b'To filter the dataset by year use:', stdout)

    def test_missing_substance(self):
        '''Checks that running the script without the required --substance argument displays usage instructions.'''
        result = subprocess.Popen(['python3', 'ProductionCode/command_line.py', '--year', '2010'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = result.communicate()
        self.assertIn(b'To filter the dataset by year use:', stdout)

    def test_year_search(self):
        '''Checks that searching by a valid year and substance returns expected results.'''
        result = subprocess.Popen(['python3', 'ProductionCode/command_line.py', '--year', '2010', '--substance', 'opioids'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = result.communicate()
        self.assertIn(b'2010,', stdout)

    def test_state_search(self):
        '''Checks that searching by a valid state and substance returns expected results.'''
        result = subprocess.Popen(['python3', 'ProductionCode/command_line.py', '--state', 'California', '--substance', 'opioids'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = result.communicate()
        self.assertIn(b'[(California', stdout)

    def test_invalid_year(self):
        '''Checks that searching by an invalid year outside the valid range (2002 - 2018) returns the appropriate error message.'''
        result = subprocess.Popen(['python3', 'ProductionCode/command_line.py', '--year', '2025', '--substance', 'opioids'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = result.communicate()
        self.assertIn(b'We only have data from 2002 to 2018. Please input one of these years :)', stdout)
        
    def test_invalid_state_name(self):
        '''Checks that searching by an invalid state name (non-U.S. state names) returns the appropriate error message.'''
        result = subprocess.Popen(['python3', 'ProductionCode/command_line.py', '--state', 'Nigeria', '--substance', 'opioids'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = result.communicate()
        self.assertIn(b'That state does not exist in the USA', stdout)
    
    def test_too_many_arguments(self):
        '''Checks that running the script with too many arguments displays usage instructions.'''
        result = subprocess.Popen(['python3', 'ProductionCode/command_line.py', '--year', '2010', '--state', 'California', '--substance', 'opioids', '--extra', 'arg'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = result.communicate()
        self.assertIn(b'To filter the dataset by year use:', stdout) 
        
    
        
        