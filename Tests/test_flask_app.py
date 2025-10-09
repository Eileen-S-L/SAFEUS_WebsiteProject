from flask_app import *
import unittest

class TestSOMEPAGE(unittest.TestCase):
    def test_route(self):
        self.app = app.test_client()
        response = self.app.get('/', follow_redirects=True)
        """ Arguments: function and expected output
        Return Value: None
        Purpose: For making sure that the proper output is shown on the homepage"""
        self.assertEqual(b"Welcome to the homepage! <br> <br> How to view the data: <br> Go to route '/' and put in a row/column to see data. Column 0 shows state names, column 1 shows year, and column 3 shows population size for ages 12-17 <br> Type in route '/year/*a year*' to view the data according to year", response.data)

class TestYearDisplay(unittest.TestCase):
    def test_routeStandard(self):
        output = b"[{'\ufeffState': 'Alabama', 'Year': '2002', 'Population.12-17': '380805'}, {'\ufeffState': 'Alaska', 'Year': '2002', 'Population.12-17': '69400'}, {'\ufeffState': 'Arizona', 'Year': '2002', 'Population.12-17': '485521'}, {'\ufeffState': 'Arkansas', 'Year': '2002', 'Population.12-17': '232986'}, {'\ufeffState': 'California', 'Year': '2002', 'Population.12-17': '3140739'}, {'\ufeffState': 'Colorado', 'Year': '2002', 'Population.12-17': '385648'}, {'\ufeffState': 'Connecticut', 'Year': '2002', 'Population.12-17': '295157'}, {'\ufeffState': 'Delaware', 'Year': '2002', 'Population.12-17': '66477'}, {'\ufeffState': 'District of Columbia', 'Year': '2002', 'Population.12-17': '33192'}, {'\ufeffState': 'Florida', 'Year': '2002', 'Population.12-17': '1346297'}, {'\ufeffState': 'Georgia', 'Year': '2002', 'Population.12-17': '748467'}, {'\ufeffState': 'Hawaii', 'Year': '2002', 'Population.12-17': '103803'}, {'\ufeffState': 'Idaho', 'Year': '2002', 'Population.12-17': '128028'}, {'\ufeffState': 'Illinois', 'Year': '2002', 'Population.12-17': '1082396'}, {'\ufeffState': 'Indiana', 'Year': '2002', 'Population.12-17': '541577'}, {'\ufeffState': 'Iowa', 'Year': '2002', 'Population.12-17': '246347'}, {'\ufeffState': 'Kansas', 'Year': '2002', 'Population.12-17': '241178'}, {'\ufeffState': 'Kentucky', 'Year': '2002', 'Population.12-17': '327727'}, {'\ufeffState': 'Louisiana', 'Year': '2002', 'Population.12-17': '406965'}, {'\ufeffState': 'Maine', 'Year': '2002', 'Population.12-17': '108861'}, {'\ufeffState': 'Maryland', 'Year': '2002', 'Population.12-17': '476696'}, {'\ufeffState': 'Massachusetts', 'Year': '2002', 'Population.12-17': '508325'}, {'\ufeffState': 'Michigan', 'Year': '2002', 'Population.12-17': '895753'}, {'\ufeffState': 'Minnesota', 'Year': '2002', 'Population.12-17': '446545'}, {'\ufeffState': 'Mississippi', 'Year': '2002', 'Population.12-17': '257508'}, {'\ufeffState': 'Missouri', 'Year': '2002', 'Population.12-17': '491394'}, {'\ufeffState': 'Montana', 'Year': '2002', 'Population.12-17': '81697'}, {'\ufeffState': 'Nebraska', 'Year': '2002', 'Population.12-17': '152465'}, {'\ufeffState': 'Nevada', 'Year': '2002', 'Population.12-17': '184670'}, {'\ufeffState': 'New Hampshire', 'Year': '2002', 'Population.12-17': '113457'}, {'\ufeffState': 'New Jersey', 'Year': '2002', 'Population.12-17': '719658'}, {'\ufeffState': 'New Mexico', 'Year': '2002', 'Population.12-17': '176611'}, {'\ufeffState': 'New York', 'Year': '2002', 'Population.12-17': '1562426'}, {'\ufeffState': 'North Carolina', 'Year': '2002', 'Population.12-17': '685632'}, {'\ufeffState': 'North Dakota', 'Year': '2002', 'Population.12-17': '54387'}, {'\ufeffState': 'Ohio', 'Year': '2002', 'Population.12-17': '987986'}, {'\ufeffState': 'Oklahoma', 'Year': '2002', 'Population.12-17': '302673'}, {'\ufeffState': 'Oregon', 'Year': '2002', 'Population.12-17': '297076'}, {'\ufeffState': 'Pennsylvania', 'Year': '2002', 'Population.12-17': '1028108'}, {'\ufeffState': 'Rhode Island', 'Year': '2002', 'Population.12-17': '85295'}, {'\ufeffState': 'South Carolina', 'Year': '2002', 'Population.12-17': '345629'}, {'\ufeffState': 'South Dakota', 'Year': '2002', 'Population.12-17': '69742'}, {'\ufeffState': 'Tennessee', 'Year': '2002', 'Population.12-17': '473558'}, {'\ufeffState': 'Texas', 'Year': '2002', 'Population.12-17': '2018953'}, {'\ufeffState': 'Utah', 'Year': '2002', 'Population.12-17': '229447'}, {'\ufeffState': 'Vermont', 'Year': '2002', 'Population.12-17': '53924'}, {'\ufeffState': 'Virginia', 'Year': '2002', 'Population.12-17': '607438'}, {'\ufeffState': 'Washington', 'Year': '2002', 'Population.12-17': '528622'}, {'\ufeffState': 'West Virginia', 'Year': '2002', 'Population.12-17': '139163'}, {'\ufeffState': 'Wisconsin', 'Year': '2002', 'Population.12-17': '482686'}, {'\ufeffState': 'Wyoming', 'Year': '2002', 'Population.12-17': '45377'}]"
        self.app = app.test_client()
        response = self.app.get('/year/2002', follow_redirects=True)
        """ Arguments: function and expected output
        Return Value: None
        Purpose: Ensuring that the standard case for the year display route passes"""
        self.assertIn(output, response.data)
    
    def test_routeEdge(self):
        self.app = app.test_client()
        response = self.app.get('/year/1990', follow_redirects=True)
        """ Arguments: function and expected output
        Return Value: None
        Purpose: Makes sure that the edge case for the year display route passes"""
        self.assertIn(b'No records found for year: 1990', response.data)

class TestStateDisplay(unittest.TestCase):
    def test_routeStandard(self):
        output = b"[{'\ufeffState': 'Texas', 'Year': '2002', 'Population.12-17': '2018953'}, {'\ufeffState': 'Texas', 'Year': '2003', 'Population.12-17': '2038642'}, {'\ufeffState': 'Texas', 'Year': '2004', 'Population.12-17': '2052845'}, {'\ufeffState': 'Texas', 'Year': '2005', 'Population.12-17': '2083455'}, {'\ufeffState': 'Texas', 'Year': '2006', 'Population.12-17': '2105817'}, {'\ufeffState': 'Texas', 'Year': '2007', 'Population.12-17': '2107904'}, {'\ufeffState': 'Texas', 'Year': '2008', 'Population.12-17': '2113980'}, {'\ufeffState': 'Texas', 'Year': '2009', 'Population.12-17': '2125058'}, {'\ufeffState': 'Texas', 'Year': '2010', 'Population.12-17': '2243713'}, {'\ufeffState': 'Texas', 'Year': '2011', 'Population.12-17': '2265694'}, {'\ufeffState': 'Texas', 'Year': '2012', 'Population.12-17': '2295567'}, {'\ufeffState': 'Texas', 'Year': '2013', 'Population.12-17': '2327085'}, {'\ufeffState': 'Texas', 'Year': '2014', 'Population.12-17': '2361420'}, {'\ufeffState': 'Texas', 'Year': '2015', 'Population.12-17': '2395358'}, {'\ufeffState': 'Texas', 'Year': '2016', 'Population.12-17': '2431437'}, {'\ufeffState': 'Texas', 'Year': '2017', 'Population.12-17': '2463690'}, {'\ufeffState': 'Texas', 'Year': '2018', 'Population.12-17': '2485959'}]"
        self.app = app.test_client()
        response = self.app.get('/state/texas', follow_redirects=True)
        """ Arguments: function and expected output
        Return Value: None
        Purpose: Ensuring that the standard case for the state display route passes"""
        self.assertIn(output, response.data)
    
    def test_routeEdge(self):
        self.app = app.test_client()
        response = self.app.get('/state/china', follow_redirects=True)
        """ Arguments: function and expected output
        Return Value: None
        Purpose: Makes sure that the edge case for the state display route passes"""
        self.assertIn(b'No records found for state china', response.data)

class TestErrorHandler(unittest.TestCase):
    def test_404error(self):
        self.app = app.test_client()
        response = self.app.get('404', follow_redirects=True)
        """ Arguments: 404
        Return Value: String explaining the error
        Purpose: Make sure that the user realizes that there is an error"""
        self.assertIn(b"Page not found. Go to the homepage and look at the directions for searching through the data.", response.data)