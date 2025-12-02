# CS257-Team Bigstackz Drug Usage in US
Rachel, Eileen, Ayobami, Emmanuel

## features in Drug Usage data in US 
- command lines:
    <python3 command_line.py --substance "type substance" --year "chosen year">
    <python3 command_line.py --substance "type substance" --state "chosen state">
    - Those command line carry our searching data that relates to wanted variables.
### Search_by_year
- search_by_year() is called by the command line
    <python3 command_line.py --substance "type substance" --year "chosen year">
- argument from "chosen year" would be taken as input into this function
- return a list of sublists consisting ['state name: state', 'year number: year', 'age Range: age', 'data: numbers' ]
### Search_by_state
- search_by_state() is called by the command line
    <python3 command_line.py --substance "type substance" --state "chosen state">
- argument from "chosen state" would be taken as input into this function
- return a list of sublists consisting ['state name: state', 'year number: year', 'age]

### Error case for command lines
- Command line would return usage statement and an empty list [].

### Test 
- if wants to run the test files, (test_cl.py, test_datasource.py and test_flask_app.py) to test flask_app and command_lines, run
    <python3 -m unittest discover Tests/>

### Scanability
- You can easily look at the page and just click one of the tabs to go to the search by year or state pages
- There is less space between the text and headings

### Satisficing
- Clickable buttons on the search pages to easily choose a substance type
- You can easily click one of the buttons at the top of the homepage to go to the search pages

### Muddling through
- The different pages allow users to easily click through data (data display comes up on different pages and there are different pages for how to search through the data)

### Front-End Design Improvements
- It was hard for users to go back to the homepage or the searching pages after getting the data results. We made a change to the data_results.html. Our change was adding a nav bar at the top of the page so when users see the results they can quickly navigate to another page.
- Users could easily make a mistake a crash the website if they submitted a search without putting a year/state or selecting a drug type. We changed the search_year.html and search_state.html to check that both search requirements are filled out before the user could click the search button. This ensures that users cannot accidentally crash the website.
- We used to have a lot of commented out code that we weren't using still in our code. This is especially true for our datasource.py file. At about line 51 (between the search by state and year functions) we had a lot of commented out functions that did not work properly. We deleted all of these comments and only left the working code and their docstrings.
-  We used to have a html page for each of the substances in our dataset. These files are now deleted but they were named "substance name".py. Most of the lines in the files were the same with minor changes. We refractored the code by making one file called data_results.html which is universal for all the substances so it can be used to display data from any substance have have the right column labels.






Template for long-term team projects for CS257 Software Design
# Drug-Database-Website
