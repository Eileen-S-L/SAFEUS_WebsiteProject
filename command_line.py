'''
The eventual location for the command line interface (CLI) for the project.
This will be the entry point for the project when run from the command line.
'''
import argparse 
from ProductionCode.drugshelperfuncs import *

# import the python file with the written functions
# import drug_state_year_search.py 

def main ():
    parser= argparse.ArgumentParser(usage = 'python3 command_line.py --year/state "year"/"state" ')
    parser.add_argument('--year')
    parser.add_argument('--state')
    args= parser.parse_args()
    usage = 'python3 command_line.py --year/state "year"/"state" '

    if (args.year != None and args.state == None):
            print(search_by_year(args.year))

    if (args.state != None and args.year == None):
            print(search_by_state(args.state))

    else:
        print(usage)


if __name__ == '__main__':
    main()