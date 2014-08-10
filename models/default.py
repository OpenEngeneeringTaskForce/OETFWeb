'''
Created on Aug 9, 2014

@author: Dean4Devil
'''

import os

class Model():
    '''
    Default Model
    '''

    def __init__(self):
        '''
        Construct all model specific data (SQL Connection i.e.)
        '''
        
    def default(self):
        ''' Default action. Just returns a static Hello page. '''
        return { 'we_are': str(os.path.abspath(os.path.curdir)) }