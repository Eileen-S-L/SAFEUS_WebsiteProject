import sys
import psycopg2
import ProductionCode.psql_config as config

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
    
    def get_data_by_year(self, drugType, Year):
        '''Argument: Year
        Return: records, which is a list of data related to searched-year
        Purpose: Select wanted data from connected database'''
        try:
            #Open a cursor to perform database operations
            cursor = self.connection.cursor()
            query = "SELECT * FROM %s WHERE Year = %s ;"
            #Execute a query
            #Retrieve query results
            cursor.execute(query, (drugType, Year,))

            records = cursor.fetchall()
            return records
        except Exception as e: 
            print ("something went wrong when executing the query:",e)
            return None
    
    def get_data_by_state(self, drugType, State):
        '''Argument: Year
        Return: records, which is a list of data related to searched-year
        Purpose: Select wanted data from connected database'''
        try:
            #Open a cursor to perform database operations
            cursor = self.connection.cursor()
            query = "SELECT * FROM %s WHERE State = %s ;"
            #Execute a query
            #Retrieve query results
            cursor.execute(query, (drugType, State,))

            records = cursor.fetchall()
            return records
        except Exception as e: 
            print ("something went wrong when executing the query:",e)
            return None
        