'''
The eventual location for the command line interface (CLI) for the project.
This will be the entry point for the project when run from the command line.
'''
import argparse 

def main ():
    parser= argparse.ArgumentParser(usage = 'python3 command_line.py --year/state "year"/"state" ')
    parser.add_argument('--y', '--year')
    parser.add_argument('--s', '--state')
    args= parser.parse_args()

    if (args[0]=="--year")or(args[0]=="--y"):
        #function of our team project that nees us to write up from scratch
        #the function could really name as anything, I named it like this here
        # get_drugdata_year(): grabs rows of related data based on the year enters"
        if (args.size()==1):
            print(usage)
        else:
            get_drugdata_year(args[1])

    if (args[0]=="--state")or(args[0]=="--s"):
        if (args.size()==1):
            print(usage)
        else:
            get_drugdata_state(args[1])

    if (args[0]!="--s") and (args[0]!="--state")and(args[0]!="--y")and(args[0]!="--state"):
        print(usage)
    



if __name__ == '__main__':
    main()