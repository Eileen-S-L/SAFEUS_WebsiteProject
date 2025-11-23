from flask_app import *
import unittest

class TestHomePage(unittest.TestCase):
    def test_homepage_route(self):
        """ Arguments: function and expected output
        Return Value: None
        Purpose: For making sure that the proper output is shown on the homepage"""
        self.app = app.test_client()
        response = self.app.get('/', follow_redirects=True)
        self.assertIn('Reading through CSVs and Excel could be tiring', response.get_data(as_text=True))

    def test_about_route(self):
        """Arguments: self
        Return Value: About page content
        Purpose: Ensures that the about page displays the correct information about the data"""
        self.app = app.test_client()
        response = self.app.get('/about',follow_redirects=True)
        self.assertIn("<p>The primary dataset used in this project comes from the", response.get_data(as_text=True))

    def test_start_explore_page(self):
        """Arguments: self
        Return Value: Start explore page content
        Purpose: Ensure that the start explore button on the start page works properly"""
        self.app = app.test_client(self)
        response = self.app.get('/start_explore', follow_redirects=True)
        html = response.get_data(as_text=True)
        self.assertIn("<h1>Search Starts Here!</h1>", html)
        
    def test_search_by_state_route(self):
        """Arguments: self
        Return Value: redirect to search by state page
        Purpose: To ensure that the state search page displays correctly"""
        self.app = app.test_client()
        response = self.app.get("/state", follow_redirects=True)
        self.assertIn("Search by State and Substance",response.data.decode())

    def test_search_by_year_route(self):
        """Arguments: self
        Return Value: redirect to search by year page
        Purpose: To ensure that the year search page displays correctly"""
        self.app = app.test_client()
        response = self.app.get("/year", follow_redirects = True)
        self.assertIn("Enter a Year (2002-2018)",response.data.decode())

class TestInSearchByState(unittest.TestCase):
    
    def test_valid_state_and_substance(self):
        """Arguments: self
        Return Value: table for the data by substance and state
        Purpose: To ensure that the data by state and substance displays correctly"""
        self.app = app.test_client()
        response = self.app.get('/state/Alabama/substance/Tobacco',follow_redirects = True)
        html = response.get_data(as_text=True)
        self.assertIn("<table>", html)
        self.assertIn("<td>Alabama</td>", html)
        self.assertIn("<td>2002</td>", html)
        self.assertIn("<td>2003</td>", html)
    
    def test_invalid_state_valid_substance(self):
        """Arrguments: self
        Return Value: appropriate error message for invalid state
        Purpose: To ensure that an invalid state returns the correct error message"""
        self.app = app.test_client()
        response = self.app.get('/state/China/substance/Tobacco', follow_redirects = True)
        output = " We do not have data for Tobacco in China"
        self.assertIn(output, str(response.get_data(as_text=True)))
    
class TestInSearchByYear(unittest.TestCase):

    def test_valid_year_and_substance(self):
        """Arguments: self
        Return Value: table for the data by year and substance
        Purpose: To ensure that the data by year and substance displays correctly"""
        self.app = app.test_client()
        response = self.app.get('/year/2002/substance/Tobacco', follow_redirects = True)
        html = response.get_data(as_text=True)
        self.assertIn("<h2>2002 Tobacco Data</h2>", html)
        self.assertIn("<td>Alabama</td>", html)
        self.assertIn("<td>Arkansas</td>", html)
        self.assertIn("<td>District of Columbia</td>", html)

    def test_out_of_range_year_and_valid_substance(self):
        """Arguments: self
        Return Value: appropriate error message for out of range year
        Purpose: To ensure that an out of range year returns the correct error message"""
        self.app = app.test_client()
        response = self.app.get('/year/2020/substance/Tobacco', follow_redirects = True)
        self.assertIn(' We do not have data for Tobacco in 2020',response.get_data(as_text=True))

class TestExceptionalCases(unittest.TestCase):
    def test_invalid_substance_in_year_search(self):
        """Arguments: invalid substance/function and expected output
        Return Value: String explaining the error
        Purpose: Make sure that the user realizes that the substance is invalid"""
        self.app = app.test_client()
        response = self.app.get('/state/Alabamaa/substance/Weed', follow_redirects = True)
        self.assertIn('We do not have data for Weed in Alabamaa', response.get_data(as_text=True))

    def test_404error(self):
        """ Arguments: 404/function and expected output
        Return Value: String explaining the error
        Purpose: Make sure that the user realizes that there is an error"""
        self.app = app.test_client()
        response = self.app.get('/nonexistentpage', follow_redirects=True)
        self.assertIn(b"Page not found. This is the link to get back to the", response.data)
    
    def test_500error(self):
        """ Arguments: 500/function and expected output
        Return Value: String explaining the error
        Purpose: Ensures that the coder recognizes that there is an error"""
        self.app = app.test_client()
        response = self.app.get('/wrong/randomword', follow_redirects=True)
        self.assertIn(b"Sorry, there's something wrong with the code! Also ensure that you choose a", response.data)
