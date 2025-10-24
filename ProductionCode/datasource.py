import sys
import psycopg2
import ProductionCode.psql_config as config

#if substance doesnt exist return a message
#make sure its ok if user puts in strings different cases

class DataSource:

    def __init__(self):
        '''Arguments: None
        Return: 
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
        '''Argument: Year
        Return: records, which is a list of data related to searched-year
        Purpose: Select wanted data from connected database'''
        if (Year>2018 or Year<2002):
            return "We only have data from 2002 to 2018. Please input one of these years :)"
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
        '''Argument: Year
        Return: records, which is a list of data related to searched-year
        Purpose: Select wanted data from connected database'''
        try:
            #Open a cursor to perform database operations
            cursor = self.connection.cursor()
            query = "SELECT * FROM %s WHERE State = %s ;"
            #Execute a query
            #Retrieve query results
            cursor.execute(query, (Substance, State,))

            records = cursor.fetchall()
            return records
        except Exception as e: 
            print ("something went wrong when executing the query:",e)
            return None
        