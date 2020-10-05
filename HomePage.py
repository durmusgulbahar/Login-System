# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 09:32:44 2020

@author: Durmus
"""

from SignUp import SignUp
from Login import Login
import sys


class HomePage:
    
    def home():
        
        print("Welcome:\n(1) for Login\n(2) for Sign up")
        
        num = input()
            
        if str(num) == '1':
            Login.login()
        elif str(num) == '2':
            SignUp.sign()
    

    def exitt():
        print("0 for HomePage")
        x = input()
        if str(x)=='0':
            HomePage.home()
        else:
            
            sys.exit()

