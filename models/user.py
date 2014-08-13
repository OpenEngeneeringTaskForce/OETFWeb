'''
Created on Aug 11, 2014

@author: Dean4Devil
'''

import random

from pycore.mysql_helper import MySQLHelper 

class Model():
    '''
    User Model. Provides Authentication & Permissions. Relies on SQLHelper & Session Data.
    '''
    uname_missing = ["Username Motherfucker, do you have one?!",
                     "If you are trying to hack this page, YOU ARE DOING IT WRONG!",
                     "Dude.... Try again",
                     "Oh no, not YOU again....",
                     "Stahp! You are hurting meeeee! :<",
                     "Well, luckily I'm not a zombie. Cause I can't see a brain anywhere.",
                     "Did ... Did you forget how to login??"]
    passwd_missing = ["Thats not a password you twat. Thats an empty input field!", 
                      "Can you read??",
                      "Oh no, not YOU again....",
                      "Stahp! You are hurting meeeee! :<",
                      "If you are trying to hack this page, YOU ARE DOING IT WRONG!",
                      "Did ... Did you forget how to login??",
                      "We don't serve your kind here. Get a brain first."]
    uname_or_passwd_wrong = [ "Even MySQL thinks you are stupid!", 
                             "Wrong Username or Password you moron!", 
                             "If you are trying to hack this page, YOU ARE DOING IT WRONG!", 
                             "Try again Idiot!", 
                             "Thats not your password! Is that even your account??",
                             "Oh no, not YOU again....",
                             "Stahp! You are hurting meeeee! :<",
                             "You're gonna be my new meat bicycle!!"]


    def __init__(self, request):
        '''
        Constructor
        '''
        self.request = request
        self.sql_helper = MySQLHelper()
        
    def login(self, session):
        ' Logs the user in '
        try:
            request = self.request
            # Get user credentials'
            request.parse_post_vars()
            username = request.post_vars.get("username")
            password = request.post_vars.get("password")
            tabledata = self.sql_helper.query_data("SELECT id, password FROM users WHERE username = '" + username[0] + "'")
            if tabledata == []:
                return {"failed": True, "f_reason": self.uname_or_passwd_wrong[random.randrange(0, len(self.uname_or_passwd_wrong))]}
            tabledata = tabledata[0]
            user_id = tabledata[0]
            table_passwd = tabledata[1].decode('utf-8')
            
            if username == [""]:
                return {"failed": True, "f_reason": self.uname_missing[random.randrange(0, len(self.uname_missing))]}
            if password == [""]:
                return {"failed": True, "f_reason": self.passwd_missing[random.randrange(0, len(self.passwd_missing))]}
            
            if password == [ table_passwd ]:
                # Login successful
                session.log_in(user_id)
                return {"failed": False}
                
            return {"failed": True, "f_reason": self.uname_or_passwd_wrong[random.randrange(0, len(self.uname_or_passwd_wrong))]}
        except Exception as e:
            raise Exception("The problem is login: " + str(e))
