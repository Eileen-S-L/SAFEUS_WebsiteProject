import sys
import psycopg2
import ProductionCode.psql_config as config

#if substance doesnt exist return a message
#make sure its ok if user puts in strings different cases

class DataSource:

    def __init__(self):
        '''Arguments: None
        Return: None 
        Purpose: Constructor that initiates connection to database'''
        self.connection = self.connect()

    def connect(self):
        '''Arguments: None
        Return: connection 
        Purpose: Initiates connection to database using information in the psql_config.py file.'''
        try:
            connection = psycopg2.connect(database=config.DATABASE, user=config.USER, password=config.PASSWORD, host="localhost")
        except psycopg2.Error as e:
            print("Connection error: ", e)
            sys.exit(1)
        return connection
    
    def get_data_by_year(self, Substance, Year):
        '''Argument: Year & substance
        Return: records, which is a list of data related to searched-year
        Purpose: Select wanted data from connected database'''
        if (int(Year)>2018 or int(Year)<2002):
            return "We only have data from 2002 to 2018. Please input one of these years :)"
        # if (Substance != 'cocaine' or Substance != 'marijuana' or Substance != 'alcohol' or Substance != 'tobacco'):
        #     return "We don't have data for a substance with that label (pick between alcohol, marijuana, cocaine, and tobacco)"
        try:
            #Open a cursor to perform database operations
            cursor = self.connection.cursor()
            query = "SELECT * FROM " + Substance + " WHERE Year = %s ;"
            #Execute a query
            #Retrieve query results
            cursor.execute(query, (Year,))

            records = cursor.fetchall()
            return records
        except Exception as e: 
            print ("something went wrong when executing the query:",e)
            return None
    
    def get_data_by_state(self, Substance, State):
        '''Argument: State & substance
        Return: records, which is a list of data related to searched-year
        Purpose: Select wanted data from connected database'''
        # if (Substance != 'cocaine' or Substance != 'marijuana' or Substance != 'alcohol' or Substance != 'tobacco'):
        #     return "We don't have data for a substance with that label (pick between alcohol, marijuana, cocaine, and tobacco)"
        try:
            #Open a cursor to perform database operations
            cursor = self.connection.cursor()
            query = "SELECT * FROM " + Substance + " WHERE State = %s ;"
            #Execute a query
            #Retrieve query results
            cursor.execute(query, (State.title(),))

            records = cursor.fetchall()
            if records == []
                return f"{Substance} does not exist in the USA"
            return records
        except Exception as e: 
            print ("something went wrong when executing the query:",e)
            return None
        

# def get_data_by_substance(self, Substance):
#         '''Argument: substance
#         Return: records, which is a list of data related to searched-substance 
#         Purpose: Select all data from the connected database'''
#         try:
#             #Open a cursor to perform database operations
#             cursor = self.connection.cursor()
#             query = "SELECT * FROM " + Substance + " WHERE State = %s ;"
#             #Execute a query
#             #Retrieve query results
#             cursor.execute(query, (State.title(),))

#             records = cursor.fetchall()
#             if records == []:
#                 return "That state does not exist in the USA"
#             return records
#         except Exception as e: 
#             print ("something went wrong when executing the query:",e)
#             return None
        