'''
Created on Aug 9, 2014

@author: Dean4Devil
'''

class Response():
    '''
    Response object.
    '''

    def __init__(self, status, body, **raw_head):
        ''' Response contructor '''
        self.status = status
        self.body = body
        self.raw_headers = {}
        self.headers = []
        self.headers.append(('Content-Type', 'text/html; charset=utf-8'))
        self.headers.append(('X-Powerer-By', 'PyPeaches'))
        self.headers.append(('Pragma', 'no-cache'))
        
    def send(self, response_function):
        ''' Executes the Response '''
        
        headers = self.headers
        for k,v in (self.raw_headers.items()):
            headers.append((k, str(v)))
        
        response_function(self.status, headers)
        
        return [ str(self.body).encode('utf-8') ]

class Session():
    ''' Defines a session. Every client gets one. Used for storage of auth etc. '''
    
