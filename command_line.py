'''
The eventual location for the command line interface (CLI) for the project.
This will be the entry point for the project when run from the command line.
'''
import argparse 
import sys
from ProductionCode.drugshelperfuncs import *

# import the python file with the written functions
# import drug_state_year_search.py 

def main ():
    parser= argparse.ArgumentParser(usage = 'python3 command_line.py --year/state "year"/"state" ')
    parser.add_argument('--year')
    parser.add_argument('--state')
    args= parser.parse_args()

    if (sys.argv[0]=="--year"):
        #function of our team project that nees us to write up from scratch
        #the function could really name as anything, I named it like this here
        # get_drugdata_year(): grabs rows of related data based on the year enters"
        if (args.size()==1 or args.size()>2):
            print(usage)
        else:
            search_by_year(sys.argv[1])

    if (sys.argv[0]=="--state"):
        if (args.size()==1 or args.size()>2):
            print(usage)
        else:
            search_by_state(args[1])
            return search_by_state(sys.argv[1])

    # if (sys.argv[0]!="--state" or sys.arg[0]!="--year"):
    #     print(usage)
    # else:
    #     print(usage)

    



if __name__ == '__main__':
    main()