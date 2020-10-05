# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 09:44:01 2020

@author: Durmus

"""

#Sign up 
class UsernameError(Exception):
    """Username must be 8 characters."""
    


class PasswordError(Exception):
    """Password must be 4 digits numbers."""
    

    
class AccountFound(Exception):
    """This account already exist"""
    
#Login
class CantFindUserError(Exception):
    """Account not found."""
    


class LoginError(Exception):
    """Username or password is wrong."""