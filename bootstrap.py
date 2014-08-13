#/bin/python3
# -*- coding: utf-8

'''
Created on Aug 9, 2014

@author: Dean4Devil
'''

import os
import sys
from pprint import pformat

path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, path)

from jinja2 import Template
from jinja2.environment import Environment
from jinja2.loaders import FileSystemLoader

from pycore.url_util import strip_request_uri
from pycore.http_util import Response, Request, Session
import urllib.parse

def application(environ, responder):
    ''' The WSGI entry function '''

    # Create a Request object:
    request = Request(environ)
    request.parse_request_uri()
    
    # Create a Session
    session = Session(request)
    
    return dynamify(request, session).send(responder)
    
def dynamify(request, session):
    ' Takes a controller, executes a model and populates a view with the result. '
    try:
        if request.controller == "default":
            from controllers.default import Default
            controller = Default()
            return controller.run(request, session)
        
        elif request.controller == "user":
            from controllers.user import User
            controller = User()
            return controller.run(request, session)
        
        else:
            env = Environment()
            env.loader = FileSystemLoader(['views/'])
            template = env.get_template('404.tmpl')
            return Response("404 PAGE NOT FOUND", template.render({}), session)
    
    except Exception as e:
        env = Environment()
        env.loader = FileSystemLoader(['views/'])
        template = env.get_template('error.tmpl')
        return Response("500 SERVER ERROR", template.render({"error_num": "500", "exception_content": str(e)}), session)
