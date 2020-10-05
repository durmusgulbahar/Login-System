# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 19:04:16 2020

@author: Durmus
"""
from User import User
from Users import Users as us


class SignUp:
    
    def sign():
        from HomePage import HomePage
        un = input("Enter the Username : ")
        pw = input("Enter the Password : ")
        
        user1 = User(un,pw)
        
        us.addUser(user1)
        
        HomePage.exitt()