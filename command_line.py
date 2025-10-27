'''
The eventual location for the command line interface (CLI) for the project.
This will be the entry point for the project when run from the command line.
'''
import argparse 
import sys
# from ProductionCode.CSVdrugshelperfuncs import *
from ProductionCode.datasource import *

# import the python file with the written functions
# import drug_state_year_search.py 

data = DataSource()
def main ():
        parser = argparse.ArgumentParser(usage = 'To filter the dataset by year use: python3 command_line.py --year \"chosen year\" \nTo filter the dataset by state name use: python3 command_line.py --state \"chosen state\" \nTo filter the dataset by substance name(this is required for both state search and year search) use: python3 command_line.py -- substance \"chosen subtance type\"')
        parser.add_argument('--year')
        parser.add_argument('--state')
        parser.add_argument('--substance')
        args, unknown = parser.parse_known_args()

        usage = 'To filter the dataset by year use: python3 command_line.py --year \"chosen year\" \nTo filter the dataset by state name use: python3 command_line.py --state \"chosen state\" \nTo filter the dataset by substance name(this is required for both state search and year search) use: python3 command_line.py -- substance \"chosen substance type\"'

        if (len(sys.argv) > 6):
                #why do we need and comparison in the following codes
                print(usage)
        
        elif unknown:
                print(usage)

        elif (args.substance ==None):
                print(usage)

        # elif (args.year != None and args.state == None):
        elif (args.year != None and args.substance !=None):
                print(str(data.get_data_by_year(args.substance, args.year)))
                pass

        # elif (args.state != None and args.year == None):
        elif (args.state != None and args.substance != None):
                print(str(data.get_data_by_state(args.substance, args.state)))
                pass
        #elif (args.substance != None):
                #print()

        else:
                print(usage)


if __name__ == '__main__':
        main()