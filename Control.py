# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 09:33:46 2020

@author: Durmus
"""

import Exceptions
from PIL import Image
import webbrowser
import time


class Control:
    
    
    
    
    def controlUsername(user0):
        """control length of username"""
        
        if len(user0.username)==8:
           return True;
               
               
        else:
            raise Exceptions.UsernameError("Username must be 8 characters.")
        
    
    def controlPassword(user0):
        """control length of  password and digits"""
        try:
            if len(user0.password)==4 and type(int(user0.password)) is int:
                return True
        except:
            raise Exceptions.PasswordError("Password must be 4 digits numbers.")
            
    def controlLogin(user0):
        from Users import Users
        Users.loadUsers()
        if user0.username in Users.userList.keys():
            if user0.password==Users.userList.get(user0.username):
                print("You have entered the room.\n****************\nPARASIDE IS COMING...")
                for i in range(3):
                    print(str(i+1)+'...')
                    time.sleep(1.5)
                
                webbrowser.open('https://bilder.t-online.de/b/82/03/84/64/id_82038464/tid_da/unter-dem-tuerkischen-praesidenten-recep-tayyip-erdogan-wurden-insgesamt-55-deutsche-festgenommen-zwoelf-davon-aus-politischen-gruenden-.jpg')
            else:
                raise Exceptions.LoginError("Username or password is wrong")
        else:
            raise Exceptions.CantFindUserError("Account not found")