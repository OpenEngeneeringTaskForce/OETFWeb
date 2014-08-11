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
        '''
        Default page. For now just returns a static Hello page.
        Later on we will crunch some new information together to display on the page (i.e. Last two commits) 
        '''
        return { 'default': True}