import unittest
from command_line import *
#from ProductionCode.datasource import *
import subprocess

# Command line tests
class TestCommandLine(unittest.TestCase):

    def test_no_arguments(self):
        """ Arguments: self
        Return Value: None
        Purpose: Checks that running the script without any arguments displays usage instructions."""
        result = subprocess.Popen(['python3', 'command_line.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = result.communicate()
        self.assertIn(b'To filter the dataset by year use:', stdout)

    def test_missing_substance(self):
        """ Arguments: self
        Return Value: None
        Purpose: Checks that searching by year without specifying a substance returns usage instructions."""
        result = subprocess.Popen(['python3', 'command_line.py', '--year', '2010'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = result.communicate()
        self.assertIn(b'To filter the dataset by year use:', stdout)

    def test_only_substance(self):
        """ Arguments: self
        Return Value: None
        Purpose: Checks that searching by substance without specifying year or state returns usage instructions."""
        result = subprocess.Popen(['python3', 'command_line.py', '--substance', 'cocaine'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = result.communicate()
        self.assertIn(b'To filter the dataset by year use:', stdout)
        
    def test_year_search(self):
        """Arguments: self
        Return Value: None
        Purpose: Checks that searching by a valid year and substance returns expected results."""
        result = subprocess.Popen(['python3', 'command_line.py', '--year', '2010', '--substance', 'cocaine'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = result.communicate()
        self.assertIn(b'2010,', stdout)

    def test_search_by_state(self):
        """Arguments: self
        Return Value: None
        Purpose: Checks that searching by a valid state and substance returns expected results."""
        result = subprocess.Popen(['python3', 'command_line.py', '--state', 'California', '--substance', 'cocaine'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = result.communicate()
        self.assertIn(b"[('California'", stdout)

    def test_invalid_year(self):
        """Arguments: self
        Return Value: None
        Purpose: Checks that searching by an invalid year returns the appropriate error message."""
        result = subprocess.Popen(['python3', 'command_line.py', '--year', '2025', '--substance', 'cocaine'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = result.communicate()
        self.assertIn(b'We only have data from 2002 to 2018. Please input one of these years :)', stdout)
        
    def test_invalid_state_name(self):
        """Arguments: self
        Return Value: None
        Purpose: Checks that searching by an invalid state name (non-U.S. state names) returns the appropriate error message."""
        result = subprocess.Popen(['python3', 'command_line.py', '--state', 'Nigeria', '--substance', 'cocaine'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = result.communicate()
        self.assertIn(b"Nigeria does not exist in the USA", stdout)
    
    def test_too_many_arguments(self):
        """Arguments: self
        Return Value: None
        Purpose: Checks that providing too many arguments returns usage instructions."""
        result = subprocess.Popen(['python3', 'command_line.py', '--year', '2010', '--state', 'California', '--substance', 'cocaine', '--extra', 'arg'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = result.communicate()
        self.assertIn(b'To filter the dataset by year use:', stdout) 
        
    def test_state_with_spaces(self):
        """Arguments: self
        Return Value: None
        Purpose: Checks that searching by a state name with spaces works correctly."""
        result = subprocess.Popen(['python3', 'command_line.py', '--state', 'New York', '--substance', 'cocaine'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = result.communicate()
        self.assertIn(b"[('New York'", stdout)
        
    def test_substance_case_insensitivity(self):
        """Arguments: self
        Return Value: None
        Purpose: Checks that substance search is case insensitive."""
        result = subprocess.Popen(['python3', 'command_line.py', '--year', '2010', '--substance', 'coCaine'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = result.communicate()
        self.assertIn(b'2010,', stdout)
        

