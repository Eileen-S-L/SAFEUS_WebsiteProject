# CS257-Team Bigstackz Drug Usage in US (2025FALL)
This is a collaboration poject: 
Rachel, Eileen, Ayobami, Emmanuel


## Purpose
- The platform facilate investigation of substance misuse trends through demographic and regional filtering. By organizing the data to show how drug misuse reflects its influence regionally.
- This project served as a comprehensive full-stack exercise, allowing our team to master the integration of back-end data architecture with a responsive front-end interface while building a mission-driven tool for public health awareness.

## Dataset
This dataset contains detailed information on substance usage, overdose fatalities, and the most affected demographic groups.  
https://www.cdc.gov/overdose-prevention/data-research/facts-stats/dose-sys-accessible.html https://1drv.ms/x/c/1780d1644addf8f2/EUwK5nKEM_dOvIkdHshL80MBrENPYVZElS8rthGOUpodbA?e=ZWy7eI

## Potential User Interaction
- Age-Based Filtering: The system allows users to customize their view by specific age groups to compare substance use trends, though the current data structure groups all individuals over 25, which limits granularity for older demographics.

- Location and Substance Search: By utilizing string-based searches for specific regions or drug types, users can access highly relatable and specialized perspectives; however, this functionality is sensitive to input accuracy and requires users to be familiar with specific dataset terminology to avoid invalid results.

- Temporal Data Access: The inclusion of year-based numerical lookups supports data-driven reporting and historical analysis, but because the dataset is static and contains certain year gaps, it may not fully reflect real-time changes or long-term longitudinal trends.


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
- The different pages allow users to easily click through data (data display comes up on different pages and there are different pages for how to search through the data.



Template for long-term team projects for CS257 Software Design
