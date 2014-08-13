'''
Created on Aug 9, 2014

@author: Dean4Devil
'''

import os
import time
import math
import hashlib

import urllib.parse
from http.cookies import SimpleCookie

from pycore.url_util import strip_request_uri
from pycore.mysql_helper import MySQLHelper

class Response():
    'Response object.'

    def __init__(self, status, body, session, **raw_head):
        'Response contructor'
        self.session = session
        self.status = status
        self.body = body
        self.raw_headers = {}
        self.headers = []
        self.headers.append(('Content-Type', 'text/html; charset=utf-8'))
        self.headers.append(('X-Powerer-By', 'PyPeaches'))
        self.headers.append(('Pragma', 'no-cache'))
        self.cookie = session.cookie
        self.set_cookie(self.cookie)
     
    def set_cookie(self, cookie):
        'Adds a cookie to a response'
        cookieheaders = ('Set-Cookie', cookie.output(sep="; "))
        self.headers.append(cookieheaders)
    
    def send(self, response_function):
        ''' Executes the Response '''
        
        headers = self.headers
        for k,v in (self.raw_headers.items()):
            headers.append((k, str(v)))
        
        headers.append(('Content-length', str(sum(len(line) for line in self.body)))) 
        
        response_function(self.status, headers)
        
        return [ str(self.body).encode('utf-8') ]


class Session():
    '''
    Session object. Stores information about the session of the currently browsing user.
    '''
    
    def __init__(self, request):
        'Session constructor'
        self.username = None
        self.user_id = 0
        self.cookie = self.get_cookie(request.environ)
    
    def get_cookie(self, environ):
        if 'HTTP_COOKIE' in environ:
            cookie = SimpleCookie(environ['HTTP_COOKIE'])
            if 'oetf' in cookie:    # That's our cookie
                return cookie
            
        cookie = SimpleCookie()
        cookie['oetf'] = ""
        cookie['oetf']['expires'] = time.strftime("%a, %d %b %Y %H %M %S GMT", time.localtime(math.floor(time.time()) + 63072000 )) # Create a cookie that will expire in two years.

class Request():
    ''' 
    Request object. Created from an wsgi environ and contains all the necessary information for controller & model 
    - mvc_dict { controller, model }
    - method
    '''
    
    def __init__(self, environ):
        self.environ = environ
        self.post_vars = None
        self.method = environ['REQUEST_METHOD']
        self.controller = ""
        self.model = ""
        self.cookie = None
        
    def parse_post_vars(self):
        if self.post_vars == None:
            self.post_vars = urllib.parse.parse_qs(self.environ['wsgi.input'].readline().decode('utf-8'),True)
    
    def parse_request_uri(self):
        request_dict = strip_request_uri(self.environ['REQUEST_URI'])
        request_list = request_dict.get("r", ["default/default"])[0].split("/")
        if len(request_list) == 1:
            request_list.append("default")
        self.controller = request_list[0]
        self.model = request_list[1]
