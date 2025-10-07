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
        self.assertEqual(result[0]['\ufeffState'], 'Alabama')

class SearchByName(unittest.TestCase):
    def setUp(self):
        load_drugdata()
    def test_invalid_year(self):
        '''ensures that function returns appropriate statement for invalid year input'''
        expected = "No records found for year: 2100"
        result = search_by_year("2100")
        self.assertEqual(result, expected)

# Command line test
class TestMain():
    def test_main_year_n(self):
        code = subprocess.Popen(['python3','command_line.py', '--year', '2002'],stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf8')
        output, err = code.communicate()
        result = [{'\ufeffState': 'Alabama', 'Year': '2002', 'Population.12-17': '380805'}, {'\ufeffState': 'Alaska', 'Year': '2002', 'Population.12-17': '69400'}, {'\ufeffState': 'Arizona', 'Year': '2002', 'Population.12-17': '485521'}, {'\ufeffState': 'Arkansas', 'Year': '2002', 'Population.12-17': '232986'}, {'\ufeffState': 'California', 'Year': '2002', 'Population.12-17': '3140739'}, {'\ufeffState': 'Colorado', 'Year': '2002', 'Population.12-17': '385648'}, {'\ufeffState': 'Connecticut', 'Year': '2002', 'Population.12-17': '295157'}, {'\ufeffState': 'Delaware', 'Year': '2002', 'Population.12-17': '66477'}, {'\ufeffState': 'District of Columbia', 'Year': '2002', 'Population.12-17': '33192'}, {'\ufeffState': 'Florida', 'Year': '2002', 'Population.12-17': '1346297'}, {'\ufeffState': 'Georgia', 'Year': '2002', 'Population.12-17': '748467'}, {'\ufeffState': 'Hawaii', 'Year': '2002', 'Population.12-17': '103803'}, {'\ufeffState': 'Idaho', 'Year': '2002', 'Population.12-17': '128028'}, {'\ufeffState': 'Illinois', 'Year': '2002', 'Population.12-17': '1082396'}, {'\ufeffState': 'Indiana', 'Year': '2002', 'Population.12-17': '541577'}, {'\ufeffState': 'Iowa', 'Year': '2002', 'Population.12-17': '246347'}, {'\ufeffState': 'Kansas', 'Year': '2002', 'Population.12-17': '241178'}, {'\ufeffState': 'Kentucky', 'Year': '2002', 'Population.12-17': '327727'}, {'\ufeffState': 'Louisiana', 'Year': '2002', 'Population.12-17': '406965'}, {'\ufeffState': 'Maine', 'Year': '2002', 'Population.12-17': '108861'}, {'\ufeffState': 'Maryland', 'Year': '2002', 'Population.12-17': '476696'}, {'\ufeffState': 'Massachusetts', 'Year': '2002', 'Population.12-17': '508325'}, {'\ufeffState': 'Michigan', 'Year': '2002', 'Population.12-17': '895753'}, {'\ufeffState': 'Minnesota', 'Year': '2002', 'Population.12-17': '446545'}, {'\ufeffState': 'Mississippi', 'Year': '2002', 'Population.12-17': '257508'}, {'\ufeffState': 'Missouri', 'Year': '2002', 'Population.12-17': '491394'}, {'\ufeffState': 'Montana', 'Year': '2002', 'Population.12-17': '81697'}, {'\ufeffState': 'Nebraska', 'Year': '2002', 'Population.12-17': '152465'}, {'\ufeffState': 'Nevada', 'Year': '2002', 'Population.12-17': '184670'}, {'\ufeffState': 'New Hampshire', 'Year': '2002', 'Population.12-17': '113457'}, {'\ufeffState': 'New Jersey', 'Year': '2002', 'Population.12-17': '719658'}, {'\ufeffState': 'New Mexico', 'Year': '2002', 'Population.12-17': '176611'}, {'\ufeffState': 'New York', 'Year': '2002', 'Population.12-17': '1562426'}, {'\ufeffState': 'North Carolina', 'Year': '2002', 'Population.12-17': '685632'}, {'\ufeffState': 'North Dakota', 'Year': '2002', 'Population.12-17': '54387'}, {'\ufeffState': 'Ohio', 'Year': '2002', 'Population.12-17': '987986'}, {'\ufeffState': 'Oklahoma', 'Year': '2002', 'Population.12-17': '302673'}, {'\ufeffState': 'Oregon', 'Year': '2002', 'Population.12-17': '297076'}, {'\ufeffState': 'Pennsylvania', 'Year': '2002', 'Population.12-17': '1028108'}, {'\ufeffState': 'Rhode Island', 'Year': '2002', 'Population.12-17': '85295'}, {'\ufeffState': 'South Carolina', 'Year': '2002', 'Population.12-17': '345629'}, {'\ufeffState': 'South Dakota', 'Year': '2002', 'Population.12-17': '69742'}, {'\ufeffState': 'Tennessee', 'Year': '2002', 'Population.12-17': '473558'}, {'\ufeffState': 'Texas', 'Year': '2002', 'Population.12-17': '2018953'}, {'\ufeffState': 'Utah', 'Year': '2002', 'Population.12-17': '229447'}, {'\ufeffState': 'Vermont', 'Year': '2002', 'Population.12-17': '53924'}, {'\ufeffState': 'Virginia', 'Year': '2002', 'Population.12-17': '607438'}, {'\ufeffState': 'Washington', 'Year': '2002', 'Population.12-17': '528622'}, {'\ufeffState': 'West Virginia', 'Year': '2002', 'Population.12-17': '139163'}, {'\ufeffState': 'Wisconsin', 'Year': '2002', 'Population.12-17': '482686'}, {'\ufeffState': 'Wyoming', 'Year': '2002', 'Population.12-17': '45377'}]
        self.assertEqual(result, output)
        
        code.terminate()
    def test_main_state_n(self):
        code = subprocess.Popen(['python3', 'command_line.py', '--state', 'alabama'],stdin=subprocess.PIPE, 
        stdout=subprocess.PIPE, encoding='utf8') 
        output, err = code.communicate()
        result = [{'\ufeffState': 'Alabama', 'Year': '2002', 'Population.12-17': '380805'}, {'\ufeffState': 'Alabama', 'Year': '2003', 'Population.12-17': '381563'}, {'\ufeffState': 'Alabama', 'Year': '2004', 'Population.12-17': '380150'}, {'\ufeffState': 'Alabama', 'Year': '2005', 'Population.12-17': '384026'}, {'\ufeffState': 'Alabama', 'Year': '2006', 'Population.12-17': '386639'}, {'\ufeffState': 'Alabama', 'Year': '2007', 'Population.12-17': '383012'}, {'\ufeffState': 'Alabama', 'Year': '2008', 'Population.12-17': '379377'}, {'\ufeffState': 'Alabama', 'Year': '2009', 'Population.12-17': '375942'}, {'\ufeffState': 'Alabama', 'Year': '2010', 'Population.12-17': '386718'}, {'\ufeffState': 'Alabama', 'Year': '2011', 'Population.12-17': '385060'}, {'\ufeffState': 'Alabama', 'Year': '2012', 'Population.12-17': '383469'}, {'\ufeffState': 'Alabama', 'Year': '2013', 'Population.12-17': '382134'}, {'\ufeffState': 'Alabama', 'Year': '2014', 'Population.12-17': '380801'}, {'\ufeffState': 'Alabama', 'Year': '2015', 'Population.12-17': '378330'}, {'\ufeffState': 'Alabama', 'Year': '2016', 'Population.12-17': '375632'}, {'\ufeffState': 'Alabama', 'Year': '2017', 'Population.12-17': '373065'}, {'\ufeffState': 'Alabama', 'Year': '2018', 'Population.12-17': '371033'}]
        self.assertEqual(result, output)

    def test_main_state_invalid(self):
        code = subprocess.Popen(['python3', 'comand_line.py', '--state', 'China'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        encoding='utf8')
        output, err = code.communicate()
        self.assertEqual(output.strip(), 'To filter the dataset by year use: python3 command_line.py --year \"chosen year\" \nTo filter the dataset by state name use: python3 command_line.py --state \"chosen state\"')