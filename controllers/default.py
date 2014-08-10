'''
Created on Aug 9, 2014

@author: Dean4Devil
'''

import os

from jinja2 import Template
from jinja2.environment import Environment
from jinja2.loaders import FileSystemLoader

class Default():
    '''s
    The default controller.
    This acts like the "index.html" page of an usual page
    '''

    def __init__(self):
        '''
        In here you should setup anything that is necessary for all of the models for the controller.
        '''
        
    def run(self, requested_model, request_dict):
        ''' Runs the specified model '''
        if requested_model == "default":
            from models.default import Model
            model = Model()
            template_var = model.default()
            # Get the view necessary
            env = Environment()
            env.loader = FileSystemLoader('/var/www/oetfdev/views/')
            template = env.get_template('default.tmpl')
            return str(template.render(template_var))
        else:
            return "Dafuq mate"
