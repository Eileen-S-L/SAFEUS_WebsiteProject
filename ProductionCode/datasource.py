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
            return []
        try:
            #Open a cursor to perform database operations
            cursor = self.connection.cursor()
            query = "SELECT * FROM " + Substance + " WHERE Year = %s ;"
            #Retrieve query results
            cursor.execute(query, (Year,))

            records = cursor.fetchall()
            print(records)
            return records
        except Exception as e: 
            print ("something went wrong when executing the query:",e)
            return None
    
    def get_basics_by_year(self, Substance, Year):
        '''Argument: Year & substance
        Return: records, which is a list of data related to searched-year
        Purpose: Select wanted data from connected database'''
        if (int(Year)>2018 or int(Year)<2002):
            return "We only have data from 2002 to 2018. Please input one of these years :)"
        try:
            #Open a cursor to perform database operations
            cursor = self.connection.cursor()
            query = "SELECT State, Year, Population_12To17, Population_18To25, Population_26AndMore FROM " + Substance + " WHERE Year = %s ;"
            #Retrieve query results
            cursor.execute(query, (Year,))
            records_basics = cursor.fetchall()
            print(records_basics)
            return records_basics
        except Exception as e: 
            print ("something went wrong when executing the query:",e)
            return None


    def get_pastyear_by_year(self, Substance, Year):
        '''Argument: Year & substance
        Return: records, which is a list of data related to searched-year
        Purpose: Select wanted data from connected database'''
        if (int(Year)>2018 or int(Year)<2002):
            return "We only have data from 2002 to 2018. Please input one of these years :)"
        try:
            #Open a cursor to perform database operations
            cursor = self.connection.cursor()
            query = "SELECT Past_year_12To17,Past_year_18To25,Past_year_26AndMore, Rate_year_12To17,Rate_year_18To25, Rate_year_26 FROM " + Substance + " WHERE Year = %s ;"
            #Retrieve query results
            cursor.execute(query, (Year,))

            records_pastyear = cursor.fetchall()
            print("Pastyear")
            return records_pastyear
        except Exception as e: 
            print ("something went wrong when executing the query:",e)
            return None

    def get_pastmonth_by_year(self, Substance, Year):
            '''Argument: Year & substance
            Return: records, which is a list of data related to searched-year
            Purpose: Select wanted data from connected database'''
            if (int(Year)>2018 or int(Year)<2002):
                return "We only have data from 2002 to 2018. Please input one of these years :)"
            try:
                #Open a cursor to perform database operations
                cursor = self.connection.cursor()
                query = "SELECT Past_month_12To17,Past_month_18To25,Past_month_26AndMore,Rate_month_12To17, Rate_month_18To25, Rate_month_26AndMore FROM " + Substance + " WHERE Year = %s ;"
                #Retrieve query results
                cursor.execute(query, (Year,))

                records_pastmonth = cursor.fetchall()
                print("Past Month")
                return records_pastmonth
            except Exception as e: 
                print ("something went wrong when executing the query:",e)
                return []

    def get_newuser_by_year(self, Substance, Year):
        '''Argument: Year & substance
            Return: records, which is a list of data related to searched-year
            Purpose: Select wanted data from connected database'''
        if (int(Year)>2018 or int(Year)<2002):
                return "We only have data from 2002 to 2018. Please input one of these years :)"
        try:
            #Open a cursor to perform database operations
            cursor = self.connection.cursor()
            query = "SELECT New_users_12To17, New_users_18To25, New_users_26AndMore, Rate_newusers_12To17, Rate_newusers_18To25, Rate_newusers_26AndMore FROM " + Substance + " WHERE Year = %s ;"
            #Retrieve query results
            cursor.execute(query, (Year,))

            records_newusers = cursor.fetchall()
            print("New User")
            return records_newusers
        except Exception as e: 
            print ("something went wrong when executing the query:",e)
            return None


    def get_data_by_state(self, Substance, State):
        '''Argument: State & substance
        Return: records, which is a list of data related to searched-year
        Purpose: Select wanted data from connected database'''
        try:
            allowed_substances = {'Cocaine','Marijuana','Alcohol','Tobacco'}
            if Substance not in allowed_substances:
                print("Invalid table:", Substance)
                return []
            #Open a cursor to perform database operations
            cursor = self.connection.cursor()
            query = "SELECT * FROM " + Substance + " WHERE State = %s ;"
            #Retrieve query results
            cursor.execute(query, (State.title(),))

            records = cursor.fetchall()
            # if records == []:
            #     return f"{State} does not exist in the USA or doesn't have any data correspondence"
            return records
        except Exception as e:
                print ("something went wrong when executing the query:",e)
                return []
        