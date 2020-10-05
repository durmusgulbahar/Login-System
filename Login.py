# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 19:09:30 2020

@author: Durmus
"""
from User import User
from Control import Control as ct



class Login:
    
    
    def login():
        from HomePage import HomePage
        un = input("Enter the Username : ")
        pw = input("Enter the Password : ")
        
        user = User(un,pw)
        
        ct.controlLogin(user)
        
        HomePage.exitt()
            

