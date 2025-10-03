import pandas as pd
#helper function for reading columns by the state name
def searchstatename(state):
    df = pd.read_csv("drugs-1.csv",
                    dtype = {"State": str})

#helper function for reading colums by the year
def searchbyyear():