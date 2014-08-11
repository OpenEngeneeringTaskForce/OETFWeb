'''
Created on Aug 9, 2014

@author: Dean4Devil
'''

from jinja2 import Template
from jinja2.environment import Environment
from jinja2.loaders import FileSystemLoader

from pycore.http_util import Response

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
        env = Environment()
        env.loader = FileSystemLoader(['views/'])
        if requested_model == "default":
            from models.default import Model
            model = Model()
            template_var = model.default()
            # Get the view necessary
            template = env.get_template('default.tmpl')
            return Response("200 OK", str(template.render(template_var)))
        
        elif requested_model == "about":
            # Get the view necessary
            template = env.get_template('about.tmpl')
            return Response("200 OK", str(template.render({"about": True})))
        
        template = env.get_template('404.tmpl')
        return Response("404 PAGE NOT FOUND", template.render(request_dict))
