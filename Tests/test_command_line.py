import unittest
from ProductionCode.drugshelperfuncs import *
import subprocess

class TestCommandLine(unittest.TestCase):

    def test_no_arguments(self):
        result = subprocess.Popen(['python3', 'ProductionCode/command_line.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = result.communicate()
        self.assertIn(b'To filter the dataset by year use:', stdout)

    def test_missing_substance(self):
        result = subprocess.Popen(['python3', 'ProductionCode/command_line.py', '--year', '2010'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = result.communicate()
        self.assertIn(b'To filter the dataset by year use:', stdout)

    def test_year_search(self):
        result = subprocess.Popen(['python3', 'ProductionCode/command_line.py', '--year', '2010', '--substance', 'opioids'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = result.communicate()
        self.assertIn(b'2010,', stdout)

    def test_state_search(self):
        result = subprocess.Popen(['python3', 'ProductionCode/command_line.py', '--state', 'California', '--substance', 'opioids'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = result.communicate()
        self.assertIn(b'[(California', stdout)

    def test_invalid_year(self):
        result = subprocess.Popen(['python3', 'ProductionCode/command_line.py', '--year', '2025', '--substance', 'opioids'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = result.communicate()
        self.assertIn(b'We only have data from 2002 to 2018. Please input one of these years :)', stdout)
        
    def test_invalid_state_name(self):
        result = subprocess.Popen(['python3', 'ProductionCode/command_line.py', '--state', 'Nigeria', '--substance', 'opioids'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = result.communicate()
        self.assertIn(b'That state does not exist in the USA', stdout)
        
    
        
        