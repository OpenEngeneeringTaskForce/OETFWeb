'''
Created on Aug 11, 2014

@author: Dean4Devil
'''

import mysql.connector
import configparser

from contextlib import closing

configp = configparser.ConfigParser()
configp.read('config/mysql.conf')
config = dict(configp['MySQL'])

class MySQLHelper():
    '''
    MySQL Helper class. Every controller or module that needs SQL storage should import this class and use its functions.
    '''
    
    def __init__(self):
        'Constructor. Establish connection and await querys.'
        self.con = mysql.connector.connect(**config)
        
    def query_data(self, query_statement):
        'Starts a query to the MySQL Server and returns the result'
        result = []
        with closing(self.con.cursor()) as cursor:
            cursor.execute(query_statement)
            for row in cursor:
                result.append(row)
        return result
                
    
    def insert_data(self, structure, data):
        'Inserts data into the specified table'
        with closing(self.con.cursor()) as cursor:
            cursor.execute(structure, data)
            self.con.commit()
