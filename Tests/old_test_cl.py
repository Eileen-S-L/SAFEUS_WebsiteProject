#This is test_cl.py for team project -- commanline.py

import unittest
from ProductionCode.CSVdrugshelperfuncs import *
import subprocess

class SearchByState(unittest.TestCase):
    def setUp(self):
        load_drugdata() #load data for each test case
    def test_invalid_state_name(self):
        """ Arguments: self
        Return Value: None
        Purpose: ensures that the function returns statement for invalid US state input"""
        expected = "No records found for state Canada"
        result = search_by_state('Canada')
        self.assertEqual(result, expected)

    def test_valid_state_name(self):
        """ Arguments: self
        Return Value: None
        Purpose: ensures that the function returns list of dictionaries for valid US state input"""
        result = search_by_state('Alabama')
        self.assertIsInstance(result, list)
        self.assertIsInstance(result[0], dict)
        self.assertEqual(result[0]['\ufeffState'], 'Alabama')

    def test_search_by_state_not_entry(self):
        """ Arguments: self
        Return Value: None
        Purpose: Ensures that the function returns appropriate statement for empty input"""
        expected = search_by_state()
        result = "Page not found. Go to the homepage and look at the directions for searching through the data."
        self.assertEqual(result, expected)

    def test_search_by_state_empty_string(self):
        """ Arguments: self
        Return Value: None
        Purpose: Ensures the funtion doesn't crash for empty string input"""
        expected = search_by_state("")
        result = "Page not found. Go to the homepage and look at the directions for searching through the data."
        self.assertEqual(result, expected)

    def test_state_with_extra_spaces(self):
        """ Arguments: self
        Return Value: None
        Purpose: Ensures function still runs appropriately with extra spaces on year"""
        expected = [{'\ufeffState': 'New York', 'Year': '2002', 'Population.12-17': '1562426'}, {'\ufeffState': 'New York', 'Year': '2003', 'Population.12-17': '1571709'}, {'\ufeffState': 'New York', 'Year': '2004', 'Population.12-17': '1584677'}, {'\ufeffState': 'New York', 'Year': '2005', 'Population.12-17': '1587906'}, {'\ufeffState': 'New York', 'Year': '2006', 'Population.12-17': '1579916'}, {'\ufeffState': 'New York', 'Year': '2007', 'Population.12-17': '1559314'}, {'\ufeffState': 'New York', 'Year': '2008', 'Population.12-17': '1535172'}, {'\ufeffState': 'New York', 'Year': '2009', 'Population.12-17': '1509858'}, {'\ufeffState': 'New York', 'Year': '2010', 'Population.12-17': '1497645'}, {'\ufeffState': 'New York', 'Year': '2011', 'Population.12-17': '1474700'}, {'\ufeffState': 'New York', 'Year': '2012', 'Population.12-17': '1456617'}, {'\ufeffState': 'New York', 'Year': '2013', 'Population.12-17': '1440280'}, {'\ufeffState': 'New York', 'Year': '2014', 'Population.12-17': '1427531'}, {'\ufeffState': 'New York', 'Year': '2015', 'Population.12-17': '1416226'}, {'\ufeffState': 'New York', 'Year': '2016', 'Population.12-17': '1403019'}, {'\ufeffState': 'New York', 'Year': '2017', 'Population.12-17': '1375507'}, {'\ufeffState': 'New York', 'Year': '2018', 'Population.12-17': '1348363'}]
        result= search_by_state("  New York  ")
        self.assertEqual(result, expected)

    def test_search_by_state_case_sensitive(self):
        """ Arguments: self
        Return Value: None
        Purpose: Ensures function runs appropriately irrespective of lower/uppercase letters for state name"""
        expected = [{'\ufeffState': 'New York', 'Year': '2002', 'Population.12-17': '1562426'}, {'\ufeffState': 'New York', 'Year': '2003', 'Population.12-17': '1571709'}, {'\ufeffState': 'New York', 'Year': '2004', 'Population.12-17': '1584677'}, {'\ufeffState': 'New York', 'Year': '2005', 'Population.12-17': '1587906'}, {'\ufeffState': 'New York', 'Year': '2006', 'Population.12-17': '1579916'}, {'\ufeffState': 'New York', 'Year': '2007', 'Population.12-17': '1559314'}, {'\ufeffState': 'New York', 'Year': '2008', 'Population.12-17': '1535172'}, {'\ufeffState': 'New York', 'Year': '2009', 'Population.12-17': '1509858'}, {'\ufeffState': 'New York', 'Year': '2010', 'Population.12-17': '1497645'}, {'\ufeffState': 'New York', 'Year': '2011', 'Population.12-17': '1474700'}, {'\ufeffState': 'New York', 'Year': '2012', 'Population.12-17': '1456617'}, {'\ufeffState': 'New York', 'Year': '2013', 'Population.12-17': '1440280'}, {'\ufeffState': 'New York', 'Year': '2014', 'Population.12-17': '1427531'}, {'\ufeffState': 'New York', 'Year': '2015', 'Population.12-17': '1416226'}, {'\ufeffState': 'New York', 'Year': '2016', 'Population.12-17': '1403019'}, {'\ufeffState': 'New York', 'Year': '2017', 'Population.12-17': '1375507'}, {'\ufeffState': 'New York', 'Year': '2018', 'Population.12-17': '1348363'}]
        result = search_by_state('nEw YoRk')
        self.assertEqual(result, expected)

class SearchByName(unittest.TestCase):
    def setUp(self):
        """ Arguments: self
        Return Value: None
        Purpose: Makes the data avaliable to the code"""
        load_drugdata()
    def test_invalid_year(self):
        """ Arguments: self
        Return Value: None
        Purpose: ensures that function returns appropriate statement for invalid year input"""
        expected = "No records found for year: 2100"
        result = search_by_year("2100")
        self.assertEqual(result, expected)

    def test_valid_year(self):
        """ Arguments: self
        Return Value: None
        Purpose: Ensures that the function returns appropriate values for year input"""
        expected = [{'\ufeffState': 'Alabama', 'Year': '2018', 'Population.12-17': '371033'}, {'\ufeffState': 'Alaska', 'Year': '2018', 'Population.12-17': '57444'}, {'\ufeffState': 'Arizona', 'Year': '2018', 'Population.12-17': '562546'}, {'\ufeffState': 'Arkansas', 'Year': '2018', 'Population.12-17': '237382'}, {'\ufeffState': 'California', 'Year': '2018', 'Population.12-17': '3017701'}, {'\ufeffState': 'Colorado', 'Year': '2018', 'Population.12-17': '433719'}, {'\ufeffState': 'Connecticut', 'Year': '2018', 'Population.12-17': '268807'}, {'\ufeffState': 'Delaware', 'Year': '2018', 'Population.12-17': '69325'}, {'\ufeffState': 'District of Columbia', 'Year': '2018', 'Population.12-17': '31910'}, {'\ufeffState': 'Florida', 'Year': '2018', 'Population.12-17': '1439529'}, {'\ufeffState': 'Georgia', 'Year': '2018', 'Population.12-17': '868842'}, {'\ufeffState': 'Hawaii', 'Year': '2018', 'Population.12-17': '95153'}, {'\ufeffState': 'Idaho', 'Year': '2018', 'Population.12-17': '155001'}, {'\ufeffState': 'Illinois', 'Year': '2018', 'Population.12-17': '984930'}, {'\ufeffState': 'Indiana', 'Year': '2018', 'Population.12-17': '537380'}, {'\ufeffState': 'Iowa', 'Year': '2018', 'Population.12-17': '245846'}, {'\ufeffState': 'Kansas', 'Year': '2018', 'Population.12-17': '237062'}, {'\ufeffState': 'Kentucky', 'Year': '2018', 'Population.12-17': '339761'}, {'\ufeffState': 'Louisiana', 'Year': '2018', 'Population.12-17': '360378'}, {'\ufeffState': 'Maine', 'Year': '2018', 'Population.12-17': '89221'}, {'\ufeffState': 'Maryland', 'Year': '2018', 'Population.12-17': '450671'}, {'\ufeffState': 'Massachusetts', 'Year': '2018', 'Population.12-17': '477554'}, {'\ufeffState': 'Michigan', 'Year': '2018', 'Population.12-17': '753613'}, {'\ufeffState': 'Minnesota', 'Year': '2018', 'Population.12-17': '438045'}, {'\ufeffState': 'Mississippi', 'Year': '2018', 'Population.12-17': '241623'}, {'\ufeffState': 'Missouri', 'Year': '2018', 'Population.12-17': '465766'}, {'\ufeffState': 'Montana', 'Year': '2018', 'Population.12-17': '76259'}, {'\ufeffState': 'Nebraska', 'Year': '2018', 'Population.12-17': '157259'}, {'\ufeffState': 'Nevada', 'Year': '2018', 'Population.12-17': '231765'}, {'\ufeffState': 'New Hampshire', 'Year': '2018', 'Population.12-17': '94278'}, {'\ufeffState': 'New Jersey', 'Year': '2018', 'Population.12-17': '675646'}, {'\ufeffState': 'New Mexico', 'Year': '2018', 'Population.12-17': '165707'}, {'\ufeffState': 'New York', 'Year': '2018', 'Population.12-17': '1348363'}, {'\ufeffState': 'North Carolina', 'Year': '2018', 'Population.12-17': '793730'}, {'\ufeffState': 'North Dakota', 'Year': '2018', 'Population.12-17': '54491'}, {'\ufeffState': 'Ohio', 'Year': '2018', 'Population.12-17': '889700'}, {'\ufeffState': 'Oklahoma', 'Year': '2018', 'Population.12-17': '318276'}, {'\ufeffState': 'Oregon', 'Year': '2018', 'Population.12-17': '295052'}, {'\ufeffState': 'Pennsylvania', 'Year': '2018', 'Population.12-17': '910130'}, {'\ufeffState': 'Rhode Island', 'Year': '2018', 'Population.12-17': '72481'}, {'\ufeffState': 'South Carolina', 'Year': '2018', 'Population.12-17': '377471'}, {'\ufeffState': 'South Dakota', 'Year': '2018', 'Population.12-17': '69325'}, {'\ufeffState': 'Tennessee', 'Year': '2018', 'Population.12-17': '513011'}, {'\ufeffState': 'Texas', 'Year': '2018', 'Population.12-17': '2485959'}, {'\ufeffState': 'Utah', 'Year': '2018', 'Population.12-17': '312345'}, {'\ufeffState': 'Vermont', 'Year': '2018', 'Population.12-17': '41066'}, {'\ufeffState': 'Virginia', 'Year': '2018', 'Population.12-17': '629725'}, {'\ufeffState': 'Washington', 'Year': '2018', 'Population.12-17': '545968'}, {'\ufeffState': 'West Virginia', 'Year': '2018', 'Population.12-17': '124659'}, {'\ufeffState': 'Wisconsin', 'Year': '2018', 'Population.12-17': '442510'}, {'\ufeffState': 'Wyoming', 'Year': '2018', 'Population.12-17': '44908'}]
        result = search_by_year("2018")
        self.assertEqual(result, expected)

    def test_year_with_extra_spaces(self):
        """ Arguments: self
        Return Value: None
        Purpose: Ensures function still runs appropriately with extra spaces on year"""
        expected = [{'\ufeffState': 'Alabama', 'Year': '2018', 'Population.12-17': '371033'}, {'\ufeffState': 'Alaska', 'Year': '2018', 'Population.12-17': '57444'}, {'\ufeffState': 'Arizona', 'Year': '2018', 'Population.12-17': '562546'}, {'\ufeffState': 'Arkansas', 'Year': '2018', 'Population.12-17': '237382'}, {'\ufeffState': 'California', 'Year': '2018', 'Population.12-17': '3017701'}, {'\ufeffState': 'Colorado', 'Year': '2018', 'Population.12-17': '433719'}, {'\ufeffState': 'Connecticut', 'Year': '2018', 'Population.12-17': '268807'}, {'\ufeffState': 'Delaware', 'Year': '2018', 'Population.12-17': '69325'}, {'\ufeffState': 'District of Columbia', 'Year': '2018', 'Population.12-17': '31910'}, {'\ufeffState': 'Florida', 'Year': '2018', 'Population.12-17': '1439529'}, {'\ufeffState': 'Georgia', 'Year': '2018', 'Population.12-17': '868842'}, {'\ufeffState': 'Hawaii', 'Year': '2018', 'Population.12-17': '95153'}, {'\ufeffState': 'Idaho', 'Year': '2018', 'Population.12-17': '155001'}, {'\ufeffState': 'Illinois', 'Year': '2018', 'Population.12-17': '984930'}, {'\ufeffState': 'Indiana', 'Year': '2018', 'Population.12-17': '537380'}, {'\ufeffState': 'Iowa', 'Year': '2018', 'Population.12-17': '245846'}, {'\ufeffState': 'Kansas', 'Year': '2018', 'Population.12-17': '237062'}, {'\ufeffState': 'Kentucky', 'Year': '2018', 'Population.12-17': '339761'}, {'\ufeffState': 'Louisiana', 'Year': '2018', 'Population.12-17': '360378'}, {'\ufeffState': 'Maine', 'Year': '2018', 'Population.12-17': '89221'}, {'\ufeffState': 'Maryland', 'Year': '2018', 'Population.12-17': '450671'}, {'\ufeffState': 'Massachusetts', 'Year': '2018', 'Population.12-17': '477554'}, {'\ufeffState': 'Michigan', 'Year': '2018', 'Population.12-17': '753613'}, {'\ufeffState': 'Minnesota', 'Year': '2018', 'Population.12-17': '438045'}, {'\ufeffState': 'Mississippi', 'Year': '2018', 'Population.12-17': '241623'}, {'\ufeffState': 'Missouri', 'Year': '2018', 'Population.12-17': '465766'}, {'\ufeffState': 'Montana', 'Year': '2018', 'Population.12-17': '76259'}, {'\ufeffState': 'Nebraska', 'Year': '2018', 'Population.12-17': '157259'}, {'\ufeffState': 'Nevada', 'Year': '2018', 'Population.12-17': '231765'}, {'\ufeffState': 'New Hampshire', 'Year': '2018', 'Population.12-17': '94278'}, {'\ufeffState': 'New Jersey', 'Year': '2018', 'Population.12-17': '675646'}, {'\ufeffState': 'New Mexico', 'Year': '2018', 'Population.12-17': '165707'}, {'\ufeffState': 'New York', 'Year': '2018', 'Population.12-17': '1348363'}, {'\ufeffState': 'North Carolina', 'Year': '2018', 'Population.12-17': '793730'}, {'\ufeffState': 'North Dakota', 'Year': '2018', 'Population.12-17': '54491'}, {'\ufeffState': 'Ohio', 'Year': '2018', 'Population.12-17': '889700'}, {'\ufeffState': 'Oklahoma', 'Year': '2018', 'Population.12-17': '318276'}, {'\ufeffState': 'Oregon', 'Year': '2018', 'Population.12-17': '295052'}, {'\ufeffState': 'Pennsylvania', 'Year': '2018', 'Population.12-17': '910130'}, {'\ufeffState': 'Rhode Island', 'Year': '2018', 'Population.12-17': '72481'}, {'\ufeffState': 'South Carolina', 'Year': '2018', 'Population.12-17': '377471'}, {'\ufeffState': 'South Dakota', 'Year': '2018', 'Population.12-17': '69325'}, {'\ufeffState': 'Tennessee', 'Year': '2018', 'Population.12-17': '513011'}, {'\ufeffState': 'Texas', 'Year': '2018', 'Population.12-17': '2485959'}, {'\ufeffState': 'Utah', 'Year': '2018', 'Population.12-17': '312345'}, {'\ufeffState': 'Vermont', 'Year': '2018', 'Population.12-17': '41066'}, {'\ufeffState': 'Virginia', 'Year': '2018', 'Population.12-17': '629725'}, {'\ufeffState': 'Washington', 'Year': '2018', 'Population.12-17': '545968'}, {'\ufeffState': 'West Virginia', 'Year': '2018', 'Population.12-17': '124659'}, {'\ufeffState': 'Wisconsin', 'Year': '2018', 'Population.12-17': '442510'}, {'\ufeffState': 'Wyoming', 'Year': '2018', 'Population.12-17': '44908'}]
        result= search_by_year("  2018  ")
        self.assertEqual(result, expected)
    
    def test_search_by_year_no_entry(self):
        """ Arguments: self
        Return Value: None
        Purpose: Ensures that the function returns appropriate statement for an empty input"""
        expected = search_by_year()
        result = "Page not found. Go to the homepage and look at the directions for searching through the data."
        self.assertEqual(result, expected)
    
    def test_search_by_year_empty_string(self):
        """ Arguments: self
        Return Value: None
        Purpose: Ensures the funtion doesn't crash for empty string input"""
        expected = search_by_year("")
        result = "Page not found. Go to the homepage and look at the directions for searching through the data."
        self.assertEqual(result, expected)

# Command line test
class TestMain(unittest.TestCase):
    def test_main_year_n(self):
        """ Arguments: self
        Return Value: None
        Purpose: Tests the command line for valid year input"""
        code = subprocess.Popen(['python3','command_line.py', '--year', '2002'],stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf8')
        output, err = code.communicate()
        result = str([{'\ufeffState': 'Alabama', 'Year': '2002', 'Population.12-17': '380805'}, {'\ufeffState': 'Alaska', 'Year': '2002', 'Population.12-17': '69400'}, {'\ufeffState': 'Arizona', 'Year': '2002', 'Population.12-17': '485521'}, {'\ufeffState': 'Arkansas', 'Year': '2002', 'Population.12-17': '232986'}, {'\ufeffState': 'California', 'Year': '2002', 'Population.12-17': '3140739'}, {'\ufeffState': 'Colorado', 'Year': '2002', 'Population.12-17': '385648'}, {'\ufeffState': 'Connecticut', 'Year': '2002', 'Population.12-17': '295157'}, {'\ufeffState': 'Delaware', 'Year': '2002', 'Population.12-17': '66477'}, {'\ufeffState': 'District of Columbia', 'Year': '2002', 'Population.12-17': '33192'}, {'\ufeffState': 'Florida', 'Year': '2002', 'Population.12-17': '1346297'}, {'\ufeffState': 'Georgia', 'Year': '2002', 'Population.12-17': '748467'}, {'\ufeffState': 'Hawaii', 'Year': '2002', 'Population.12-17': '103803'}, {'\ufeffState': 'Idaho', 'Year': '2002', 'Population.12-17': '128028'}, {'\ufeffState': 'Illinois', 'Year': '2002', 'Population.12-17': '1082396'}, {'\ufeffState': 'Indiana', 'Year': '2002', 'Population.12-17': '541577'}, {'\ufeffState': 'Iowa', 'Year': '2002', 'Population.12-17': '246347'}, {'\ufeffState': 'Kansas', 'Year': '2002', 'Population.12-17': '241178'}, {'\ufeffState': 'Kentucky', 'Year': '2002', 'Population.12-17': '327727'}, {'\ufeffState': 'Louisiana', 'Year': '2002', 'Population.12-17': '406965'}, {'\ufeffState': 'Maine', 'Year': '2002', 'Population.12-17': '108861'}, {'\ufeffState': 'Maryland', 'Year': '2002', 'Population.12-17': '476696'}, {'\ufeffState': 'Massachusetts', 'Year': '2002', 'Population.12-17': '508325'}, {'\ufeffState': 'Michigan', 'Year': '2002', 'Population.12-17': '895753'}, {'\ufeffState': 'Minnesota', 'Year': '2002', 'Population.12-17': '446545'}, {'\ufeffState': 'Mississippi', 'Year': '2002', 'Population.12-17': '257508'}, {'\ufeffState': 'Missouri', 'Year': '2002', 'Population.12-17': '491394'}, {'\ufeffState': 'Montana', 'Year': '2002', 'Population.12-17': '81697'}, {'\ufeffState': 'Nebraska', 'Year': '2002', 'Population.12-17': '152465'}, {'\ufeffState': 'Nevada', 'Year': '2002', 'Population.12-17': '184670'}, {'\ufeffState': 'New Hampshire', 'Year': '2002', 'Population.12-17': '113457'}, {'\ufeffState': 'New Jersey', 'Year': '2002', 'Population.12-17': '719658'}, {'\ufeffState': 'New Mexico', 'Year': '2002', 'Population.12-17': '176611'}, {'\ufeffState': 'New York', 'Year': '2002', 'Population.12-17': '1562426'}, {'\ufeffState': 'North Carolina', 'Year': '2002', 'Population.12-17': '685632'}, {'\ufeffState': 'North Dakota', 'Year': '2002', 'Population.12-17': '54387'}, {'\ufeffState': 'Ohio', 'Year': '2002', 'Population.12-17': '987986'}, {'\ufeffState': 'Oklahoma', 'Year': '2002', 'Population.12-17': '302673'}, {'\ufeffState': 'Oregon', 'Year': '2002', 'Population.12-17': '297076'}, {'\ufeffState': 'Pennsylvania', 'Year': '2002', 'Population.12-17': '1028108'}, {'\ufeffState': 'Rhode Island', 'Year': '2002', 'Population.12-17': '85295'}, {'\ufeffState': 'South Carolina', 'Year': '2002', 'Population.12-17': '345629'}, {'\ufeffState': 'South Dakota', 'Year': '2002', 'Population.12-17': '69742'}, {'\ufeffState': 'Tennessee', 'Year': '2002', 'Population.12-17': '473558'}, {'\ufeffState': 'Texas', 'Year': '2002', 'Population.12-17': '2018953'}, {'\ufeffState': 'Utah', 'Year': '2002', 'Population.12-17': '229447'}, {'\ufeffState': 'Vermont', 'Year': '2002', 'Population.12-17': '53924'}, {'\ufeffState': 'Virginia', 'Year': '2002', 'Population.12-17': '607438'}, {'\ufeffState': 'Washington', 'Year': '2002', 'Population.12-17': '528622'}, {'\ufeffState': 'West Virginia', 'Year': '2002', 'Population.12-17': '139163'}, {'\ufeffState': 'Wisconsin', 'Year': '2002', 'Population.12-17': '482686'}, {'\ufeffState': 'Wyoming', 'Year': '2002', 'Population.12-17': '45377'}])
        code.terminate()

    def test_main_state_n(self):
        """ Arguments: self
        Return Value: None
        Purpose: Tests the command line for valid state input"""
        code = subprocess.Popen(['python3', 'command_line.py', '--state', 'alabama'],stdin=subprocess.PIPE, 
        stdout=subprocess.PIPE, encoding='utf8') 
        output, err = code.communicate()
        result = str([{'\ufeffState': 'Alabama', 'Year': '2002', 'Population.12-17': '380805'}, {'\ufeffState': 'Alabama', 'Year': '2003', 'Population.12-17': '381563'}, {'\ufeffState': 'Alabama', 'Year': '2004', 'Population.12-17': '380150'}, {'\ufeffState': 'Alabama', 'Year': '2005', 'Population.12-17': '384026'}, {'\ufeffState': 'Alabama', 'Year': '2006', 'Population.12-17': '386639'}, {'\ufeffState': 'Alabama', 'Year': '2007', 'Population.12-17': '383012'}, {'\ufeffState': 'Alabama', 'Year': '2008', 'Population.12-17': '379377'}, {'\ufeffState': 'Alabama', 'Year': '2009', 'Population.12-17': '375942'}, {'\ufeffState': 'Alabama', 'Year': '2010', 'Population.12-17': '386718'}, {'\ufeffState': 'Alabama', 'Year': '2011', 'Population.12-17': '385060'}, {'\ufeffState': 'Alabama', 'Year': '2012', 'Population.12-17': '383469'}, {'\ufeffState': 'Alabama', 'Year': '2013', 'Population.12-17': '382134'}, {'\ufeffState': 'Alabama', 'Year': '2014', 'Population.12-17': '380801'}, {'\ufeffState': 'Alabama', 'Year': '2015', 'Population.12-17': '378330'}, {'\ufeffState': 'Alabama', 'Year': '2016', 'Population.12-17': '375632'}, {'\ufeffState': 'Alabama', 'Year': '2017', 'Population.12-17': '373065'}, {'\ufeffState': 'Alabama', 'Year': '2018', 'Population.12-17': '371033'}])
    
    def test_main_state_invalid(self):
        """ Arguments: self
        Return Value: None
        Purpose: Tests the command line for invalid state input"""
        code = subprocess.Popen(['python3', 'command_line.py', '--state', 'China'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        encoding='utf8')
        output, err = code.communicate()
        self.assertEqual(output.strip(), 'No records found for state China')
    