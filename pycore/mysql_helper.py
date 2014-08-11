'''
Created on Aug 11, 2014

@author: Dean4Devil
'''

import mysql.connector


config = {  # Will later be get from a file config/mysql.conf
            'user': 'oetf',
            'password': 'xCMEdTde6n9bqLQ',
            'host': '127.0.0.1',
            'database': 'oetf',
          }

class MySQLHelper():
    '''
    MySQL Helper class. Every controller or module that needs SQL storage should import this class and use its functions.
    '''
    
    def __init__(self):
        ''' Constructor. Establish connection and await querys. '''
        self.connection = mysql.connector.connect(**config)
        
    def query_data(self, select_string, from_string, where_string):
        ''' Starts a query to the MySQL Server and returns the result '''
        cursor = self.connection.cursor()
        
        query = ("SELECT " + select_string + " FROM " + from_string + " WHERE " + where_string)
        
        cursor.execute(query)
        
        result = []
        
            
