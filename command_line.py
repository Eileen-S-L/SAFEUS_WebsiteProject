'''
The eventual location for the command line interface (CLI) for the project.
This will be the entry point for the project when run from the command line.
'''
import argparse 
import sys
from ProductionCode.CSVdrugshelperfuncs import *

# import the python file with the written functions
# import drug_state_year_search.py 

def main ():
        parser = argparse.ArgumentParser(usage = 'To filter the dataset by year use: python3 command_line.py --year \"chosen year\" \nTo filter the dataset by state name use: python3 command_line.py --state \"chosen state\" \nTo filter the dataset by state name use: python3 command_line.py -- drug type \"chosen drug type\"')
        parser.add_argument('--year')
        parser.add_argument('--state')
        parser.add_argument('--substance')
        args, unknown = parser.parse_known_args()

        usage = 'To filter the dataset by year use: python3 command_line.py --year \"chosen year\" \nTo filter the dataset by state name use: python3 command_line.py --state \"chosen state\" \nTo filter the dataset by state name use: python3 command_line.py -- drug type \"chosen drug type\"'

        if (len(sys.argv) > 4):
                #why do we need and comparison in the following codes
                print(usage)
        
        elif unknown:
                print(usage)
        

        # elif (args.year != None and args.state == None):
        elif (args.year != None):
                print(search_by_year(args.year))


        # elif (args.state != None and args.year == None):
        elif (args.state != None):
                print(search_by_state(args.state))
                pass

        else:
                print(usage)


if __name__ == '__main__':
        main()