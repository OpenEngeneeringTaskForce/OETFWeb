#/bin/python3
# -*- coding: utf-8

'''
Created on Aug 9, 2014

@author: Dean4Devil
'''

import os
import sys

path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, path)

from jinja2 import Template
from jinja2.environment import Environment
from jinja2.loaders import FileSystemLoader

from pycore.url_util import strip_request_uri
from pycore.http_util import Response

def application(environ, responder):
    ''' The WSGI entry function '''
    
    response = dynamify(strip_request_uri(environ['REQUEST_URI']))
    return response.send(responder)
    
def dynamify(request_dict):
    ''' Takes a controller, executes a model and populates a view with the result '''
    request_list = request_dict.get("r", ["default/default"])[0].split("/")
    if len(request_list) == 1:
        request_list.append("default")
    try:
        if request_list[0] == "default":
            from controllers.default import Default
            controller = Default()
            return controller.run(request_list[1], request_dict)
        elif request_list[0] == "user":
            from controllers.user import User
            controller = User()
            return controller.run(request_list[1], request_dict)
        else:
            env = Environment()
            env.loader = FileSystemLoader(['views/'])
            template = env.get_template('404.tmpl')
            return Response("404 PAGE NOT FOUND", template.render(request_dict))
    
    except Exception as e:
        env = Environment()
        env.loader = FileSystemLoader(['views/'])
        template = env.get_template('error.tmpl')
        return Response("500 SERVER ERROR", template.render({"error_num": "500", "exception_content": str(e)}))
