from flask_app import *
import unittest

class TestHomePage(unittest.TestCase):
    def test_homepage_route(self):
        """ Arguments: function and expected output
        Return Value: None
        Purpose: For making sure that the proper output is shown on the homepage"""
        self.app = app.test_client()
        response = self.app.get('/', follow_redirects=True)
        self.assertIn('<li><a href="/about">About the Data</a></li>\n', response.get_data(as_text=True))

    def test_about_route(self):
        self.app = app.test_client()
        response = self.app.get('/about',follow_redirects=True)
        self.assertIn("<p>The primary dataset used in this project comes from the", response.get_data(as_text=True))

    def test_search_by_state_route(self):
        self.app = app.test_client()
        response = self.app.get("/state", follow_redirects=True)
        self.assertIn("Search by State and Substance",response.data.decode())

    def test_search_by_year_route(self):
        self.app = app.test_client()
        response = self.app.get("/year", follow_redirects = True)
        self.assertIn("Enter a Year (2002-2018)",response.data.decode())

class TestInSearchByState(unittest.TestCase):
    
    def test_valid_state_and_substance(self):
        self.app = app.test_client()
        response = self.app.get('/state/Alabama/substance/Tobacco',follow_redirects = True)
        #partial_output = "('Alabama', 2002, 380805, 499453, 2812905, 52, 196, 728, 136.906, 392.404, 258.844, 63, 226, 930, 166.578, 451.976, 330.659)"
        html = response.get_data(as_text=True)
        self.assertIn("<table>", html)
        self.assertIn("<td>Alabama</td>", html)
        self.assertIn("<td>2002</td>", html)
        self.assertIn("<td>2003</td>", html)
    
    def test_invalid_state_valid_substance(self):
        self.app = app.test_client()
        response = self.app.get('/state/China/substance/Tobacco', follow_redirects = True)
        output = " We do not have data for Tobacco in China"
        self.assertIn(output, str(response.get_data(as_text=True)))
    
class TestInSearchByYear(unittest.TestCase):

    def test_valid_year_and_substance(self):
        self.app = app.test_client()
        response = self.app.get('/year/2002/substance/Tobacco', follow_redirects = True)
        html = response.get_data(as_text=True)
        self.assertIn("<h2>2002 Tobacco Data</h2>", html)
        self.assertIn("<td>Alabama</td>", html)
        self.assertIn("<td>Arkansas</td>", html)
        self.assertIn("<td>District of Columbia</td>", html)

    def test_out_of_range_year_and_valid_substance(self):
        self.app = app.test_client()
        response = self.app.get('/year/2020/substance/Tobacco', follow_redirects = True)
        self.assertIn(' We do not have data for Tobacco in 2020',response.get_data(as_text=True))

class TestExceptionalCases(unittest.TestCase):
    def test_invalid_substance_in_year_search(self):
        self.app = app.test_client()
        response = self.app.get('/year/2005/substance/Weed', follow_redirects = True)
        self.assertIn('We do not have data for Weed in Alabamaa', response.get_data(as_text=True))


#         Return Value: None
#         Purpose: Ensuring that the standard case for the year display route passes"""
#         output = b"[('Alabama', 2004, 380150, 506120, 2871062, 6, 31, 43, 15.926, 60.775, 15.039), ('Alaska', 2004, 68162, 73462, 373429, 1, 5, 6, 19.52, 74.081, 17.152), ('Arizona', 2004, 510698, 643907, 3549522, 12, 48, 66, 22.733, 75.131, 18.628), ('Arkansas', 2004, 232095, 310177, 1729803, 4, 20, 23, 16.42, 62.876, 13.2), ('California', 2004, 3290671, 3974135, 21850567, 52, 251, 322, 15.881, 63.122, 14.729), ('Colorado', 2004, 392822, 506705, 2865042, 7, 44, 54, 18.606, 86.75, 18.944), ('Connecticut', 2004, 299013, 344048, 2265842, 6, 29, 39, 19.419, 84.328, 17.225), ('Delaware', 2004, 67454, 92253, 534950, 1, 7, 9, 14.018, 74.483, 17.428), ('District of Columbia', 2004, 34350, 65197, 364207, 0, 4, 12, 5.225, 57.81, 32.289), ('Florida', 2004, 1404055, 1719548, 11530104, 25, 139, 223, 17.705, 80.754, 19.298), ('Georgia', 2004, 775954, 990545, 5412379, 10, 41, 80, 12.709, 41.489, 14.775), ('Hawaii', 2004, 100585, 123191, 796942, 2, 7, 11, 15.016, 54.883, 14.328), ('Idaho', 2004, 127552, 172734, 841609, 2, 11, 10, 17.009, 62.898, 11.644), ('Illinois', 2004, 1099965, 1406715, 7910382, 14, 82, 145, 13.158, 58.0, 18.333), ('Indiana', 2004, 549720, 709599, 3856681, 8, 53, 58, 14.933, 74.629, 15.156), ('Iowa', 2004, 240059, 353384, 1883725, 4, 19, 23, 17.037, 53.543, 12.116), ('Kansas', 2004, 233656, 327533, 1673455, 4, 22, 30, 16.512, 68.225, 17.907), ('Kentucky', 2004, 336219, 453022, 2645240, 5, 31, 47, 16.298, 68.975, 17.944), ('Louisiana', 2004, 398611, 545993, 2712415, 5, 26, 43, 11.935, 48.435, 15.694), ('Maine', 2004, 108414, 137266, 884793, 2, 12, 14, 18.945, 90.703, 15.336), ('Maryland', 2004, 492847, 571917, 3512136, 6, 33, 65, 12.091, 57.804, 18.399), ('Massachusetts', 2004, 511301, 676924, 4186567, 10, 68, 81, 19.059, 100.473, 19.238), ('Michigan', 2004, 907902, 1111809, 6354775, 14, 77, 107, 15.461, 69.657, 16.898), ('Minnesota', 2004, 437674, 597384, 3220581, 8, 44, 46, 17.543, 73.176, 14.235), ('Mississippi', 2004, 255659, 348523, 1747645, 3, 16, 28, 13.421, 46.58, 15.989), ('Missouri', 2004, 486907, 653900, 3636194, 8, 53, 56, 17.015, 81.682, 15.329), ('Montana', 2004, 77617, 108976, 599979, 1, 9, 8, 16.474, 80.355, 13.83), ('Nebraska', 2004, 148189, 210903, 1077324, 2, 15, 14, 16.237, 72.2, 13.128), ('Nevada', 2004, 201110, 239773, 1493077, 3, 16, 18, 16.092, 64.839, 12.163), ('New Hampshire', 2004, 115243, 136890, 849273, 2, 12, 11, 18.494, 89.49, 13.085), ('New Jersey', 2004, 745809, 832522, 5605723, 12, 52, 82, 16.351, 62.084, 14.547), ('New Mexico', 2004, 173285, 224690, 1167618, 4, 16, 17, 21.447, 70.452, 14.77), ('New York', 2004, 1584677, 2050011, 12371557, 24, 151, 223, 15.406, 73.502, 18.057), ('North Carolina', 2004, 715542, 897851, 5379787, 9, 51, 82, 13.053, 56.321, 15.179), ('North Dakota', 2004, 50426, 82738, 398634, 1, 4, 4, 16.961, 46.801, 11.223), ('Ohio', 2004, 980119, 1257858, 7263612, 12, 70, 108, 12.325, 55.743, 14.838), ('Oklahoma', 2004, 292067, 418925, 2171414, 5, 26, 26, 16.702, 61.191, 11.959), ('Oregon', 2004, 297935, 396541, 2331124, 5, 26, 32, 16.562, 64.831, 13.844), ('Pennsylvania', 2004, 1035623, 1322980, 8059411, 16, 101, 139, 15.182, 76.417, 17.259), ('Rhode Island', 2004, 88122, 125374, 691117, 2, 12, 14, 18.496, 96.766, 19.939), ('South Carolina', 2004, 358954, 464027, 2642693, 6, 29, 46, 16.216, 63.466, 17.328), ('South Dakota', 2004, 66529, 94332, 472172, 1, 5, 5, 16.232, 50.186, 11.284), ('Tennessee', 2004, 477163, 642419, 3799709, 7, 40, 63, 15.138, 62.665, 16.699), ('Texas', 2004, 2052845, 2628020, 13267576, 49, 175, 206, 24.081, 66.691, 15.501), ('Utah', 2004, 226903, 358089, 1304188, 4, 19, 22, 18.802, 53.818, 16.535), ('Vermont', 2004, 52660, 70932, 411991, 1, 7, 7, 20.145, 103.594, 16.892), ('Virginia', 2004, 622210, 774068, 4680347, 9, 55, 83, 13.947, 70.787, 17.703), ('Washington', 2004, 527538, 692546, 3955836, 8, 59, 56, 15.67, 84.586, 14.124), ('West Virginia', 2004, 136919, 192780, 1215454, 3, 20, 21, 21.568, 102.62, 17.011), ('Wisconsin', 2004, 472397, 638835, 3502106, 9, 44, 52, 19.085, 69.063, 14.733), ('Wyoming', 2004, 42257, 61866, 321211, 1, 4, 4, 18.018, 67.608, 12.655)]"
#         self.app = app.test_client()
#         response = self.app.get('/substance/cocaine/year/2004', follow_redirects=True)
#         self.assertIn(output, response.data)
    
#     def test_routeEdge(self):
#         """ Arguments: function and expected output
#         Return Value: None
#         Purpose: Makes sure that the edge case for the year display route passes"""
#         self.app = app.test_client()
#         response = self.app.get('/substance/cocaine/year/2020', follow_redirects=True)
#         self.assertIn(b'We only have data from 2002 to 2018. Please input one of these years :)', response.data)

#     def test_routeSubstanceOnly(self):
#         """ Arguments: function and expected output
#         Return Value: None
#         Purpose: Ensures that the edge case for the year display route passes when only substance is given"""
#         self.app = app.test_client()
#         response = self.app.get('/substance/cocaine/', follow_redirects=True)
#         self.assertIn(b'Page not found. Go to the homepage and look at the directions for searching through the data.', response.data)

# class TestStateDisplay(unittest.TestCase):
#     def test_routeStandard(self):
#         """ Arguments: function and expected output
#         Return Value: None
#         Purpose: Ensuring that the standard case for the state display route passes"""
#         output = b"[('New York', 2002, 1562426, 2036478, 12316861, 22, 141, 248, 14.14, 69.253, 20.154), ('New York', 2003, 1571709, 2047533, 12344264, 22, 156, 225, 13.863, 76.01, 18.262), ('New York', 2004, 1584677, 2050011, 12371557, 24, 151, 223, 15.406, 73.502, 18.057), ('New York', 2005, 1587906, 2106543, 12383739, 24, 155, 273, 14.812, 73.407, 22.082), ('New York', 2006, 1579916, 2179143, 12397704, 21, 154, 274, 13.165, 70.581, 22.069), ('New York', 2007, 1559314, 2218415, 12500501, 20, 143, 261, 12.508, 64.631, 20.877), ('New York', 2008, 1535172, 2262614, 12574826, 17, 165, 254, 10.861, 73.087, 20.194), ('New York', 2009, 1509858, 2236966, 12648267, 15, 144, 211, 9.658, 64.245, 16.693), ('New York', 2010, 1497645, 2236959, 12651349, 12, 112, 184, 8.258, 50.015, 14.524), ('New York', 2011, 1474700, 2242476, 12760358, 11, 126, 211, 7.465, 56.244, 16.505), ('New York', 2012, 1456617, 2243318, 12875810, 9, 124, 212, 6.087, 55.343, 16.485), ('New York', 2013, 1440280, 2239134, 12988411, 10, 120, 250, 7.108, 53.512, 19.278), ('New York', 2014, 1427531, 2228431, 13092078, 10, 140, 274, 7.31, 62.869, 20.957), ('New York', 2015, 1416226, 2197628, 13150285, 6, 127, 265, 4.522, 57.674, 20.146), ('New York', 2016, 1403019, 2156021, 13244748, 6, 125, 283, 4.437, 57.929, 21.336), ('New York', 2017, 1375507, 2093893, 13260774, 5, 144, 290, 3.946, 68.801, 21.833), ('New York', 2018, 1348363, 2031273, 13191928, 4, 131, 282, 3.223, 64.42, 21.374)]"
#         self.app = app.test_client()
#         response = self.app.get('/substance/cocaine/state/new york', follow_redirects=True)
#         self.assertIn(output, response.data)
    
#     def test_routeEdge(self):
#         """ Arguments: function and expected output
#         Return Value: None
#         Purpose: Makes sure that the edge case for the state display route passes"""
#         self.app = app.test_client()
#         response = self.app.get('/substance/cocaine/state/china', follow_redirects=True)
#         self.assertIn(b'That state does not exist in the USA', response.data)

# class TestErrorHandler(unittest.TestCase):
#     def test_404error(self):
#         """ Arguments: 404/function and expected output
#         Return Value: String explaining the error
#         Purpose: Make sure that the user realizes that there is an error"""
#         self.app = app.test_client()
#         response = self.app.get('404', follow_redirects=True)
#         self.assertIn(b"Page not found. Go to the homepage and look at the directions for searching through the data.", response.data)

#     def test_500error(self):
#         """ Arguments: 500/function and expected output
#         Return Value: String explaining the error
#         Purpose: Ensures that the coder recognizes that there is an error"""
#         self.app = app.test_client()
#         response = self.app.get('/wrong/rachel', follow_redirects=True)
#         self.assertIn(b"You made an error! Go back through your code to find it!", response.data)
        