# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 09:33:39 2020

@author: Durmus
"""


from Control import Control as ct
import Exceptions


class Users:
    
    
   
    userList = {}
    
    def __init__(self):
       pass
    
    
    
    def loadUsers():
        f = open('C:/Users/Durmus/Login System/userinfo')
        u = f.readlines()
        u = [x.strip() for x in u]
        
        for s in u:
           string = s.split(':')
           Users.userList[string[0]] = string[1]
        
        f.close()
        
        
        
        
    def usersList():
        f = open('C:/Users/Durmus/Login System/userinfo')
        print(f.read()) 
        f.close()
        
        
        
    def addUser(obj):
        Users.loadUsers()
        if obj.username in Users.userList :
            raise Exceptions.AccountFound("This account already exist")
        else:
            if ct.controlUsername(obj) is True:
                if ct.controlPassword(obj) is True:
                    
                    with open('C:/Users/Durmus/Login System/userinfo',mode='a') as w:
                        w.write(obj.username+":"+str(obj.password)+"\n")
                        w.close()
                    print("You signed up!")
            
            
        
    def removeUser(obj):
        Users.userList.pop(obj.username)
        