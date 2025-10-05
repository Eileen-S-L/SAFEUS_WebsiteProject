'''
The eventual location for the command line interface (CLI) for the project.
This will be the entry point for the project when run from the command line.
'''
import argparse 
from ProductionCode.drugshelperfuncs import search_by_state
from ProductionCode.drugshelperfuncs import search_by_year


# import the python file with the written functions
# import drug_state_year_search.py 

def main ():
    parser= argparse.ArgumentParser(usage = 'python3 command_line.py --year/state "year"/"state" ')
    parser.add_argument('--year')
    parser.add_argument('--state')
    args= parser.parse_args()

    if (args[0]=="--year"):
        #function of our team project that nees us to write up from scratch
        #the function could really name as anything, I named it like this here
        # get_drugdata_year(): grabs rows of related data based on the year enters"
        if (args.size()==1):
            print(usage)
        if (args.size()>2):
            print(usage)
        else:
            search_by_year(args[1])

    if (args[0]=="--state"):
        if (args.size()==1):
            print(usage)
        if (args.size()>2):
            print(usage)
        else:
            search_by_state(args[1])

    if (args[0]!="--s") and (args[0]!="--state")and(args[0]!="--y")and(args[0]!="--state"):
        print(usage)
    



if __name__ == '__main__':
    main()