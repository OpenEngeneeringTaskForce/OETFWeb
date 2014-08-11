'''
Created on Aug 11, 2014

@author: Dean4Devil
'''

from jinja2 import Template
from jinja2.environment import Environment
from jinja2.loaders import FileSystemLoader

from pycore.http_util import Response
from pycore.mysql_helper import MySQLHelper

class User():
    '''
    User controller, providing login/logout & User data
    '''

    def __init__(self):
        ''' We have to get some things started. MySQL i.e. '''
        sql_helper = MySQLHelper()
        
    def run(self, requested_model, request_dict):
        ''' Runs the specified model, catches the output and returns a populated view '''
        from models.user import Model
        if requested_model == "login":
            model = Model()
            env = Environment()
            env.loader = FileSystemLoader('views/')
            template = env.get_template('login.tmpl')
            return Response("200 OK", str(template.render({"login": True})))
