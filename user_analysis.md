# Drug_data_search features - CIDER analysis
- features:
  1. search data by year or by state through command line.
  2. Users can search using simple search links like /year/<year> or /state/<state>.
  3. Error messages appear when users enter wrong search or invalid inputs.

## Potential Users
- Students and researchers exploring drug use data across U.S. states and years.
- Students who want to use the data for school projects or data collection.
- Anyone interested in drug data in the U.S.

## Potential benefits
- could provide an easy access to dataset information for users who could properly carry out the searching process.
- Makes it easier to find drug data without opening large CSV files.
- Helps users see connections between age, state, and drug use trends.
- Could help establish correlation between substance intake, geographical locations and age groups in the U.S.

## Potential Harms
- Some user might be excluded due to various reasons.(check CIDER analysis).
- The smaller Minidrugdataset is only for testing, so if used alone, it could give incomplete results.

## Critique
General:
Assumption 1. The user must be literated, and an english-speaker in order to use command line.
Assumption 2. The user must be visually functional to see the screen and read result.
Assumption 3. The user needs basic computer and internet access.
Assumption 4. The user need basic level of training about computer science.
Assumption 5. The dataset is served for user who only cares about younger population's drug usage. Assuming that user might inclined to search their own age range, this dataset may serve only young users well. 
Database:
Assumption 1. Assume user had understanding about Past-Month rule in substance questionnair 
Assumption 2. Assume user understand age-range classification 
Front-End:
Assumption 1. The user must be an english speaker.
Assumption 2. The user must have intact vision(including color perception).


## Imagine
Critique 3:
- If someone doesn’t have a computer or internet access, they can’t use our websites. 
- Even if they do, they might not know how to type the search links for example, /year/2010 or /state/Texas.
- Users might felt perplex because they're unclear about the Past month element of data
- Or user might not instantly realize that numbers like 12-17 or 18-25 is for age range.
Front-end:
- Maybe user would want to switch webpage language, which is a feature not provided by us.
- The user may found our webpage unclear to read if they aren't sensitive to blue/green.
## Design 
*ignore technical feasibility*
1. Add an auto-translate/explanation feature for users who don’t speak English.
2. Add an audio option that reads results aloud for people with vision problems.
3. Offer an optional short tutorial or guide before users start searching.
Database:
5. Allow the app to update or switch datasets based on user requests. 
6. Give verbal explanation of data columns or titles - maybe made it mandatory?
Front-End:
7. Provide language switch feature.
8. Provide different color palette - including some high contrast ones.

## Expand
- the dataset is limited, users might make biased assumptions or overgeneralize the results about specific age groups or substances without sufficient evidence/ or information
- the data only asks for state and year it does not provide graphs for better visualisation
- It could be improved by adding visual graphs or connecting to live data updates.
- A hover-over explanation could be provided (like those ones look similar to wikipedia?)
Front-End:
- Maybe we can create a webpage that allows user to choose their own color palette. That would make it flexible for multiple circumstances. 
## Repeat
- we repeat this CIDER process twice, all ideas are recorded in previous sections. 
