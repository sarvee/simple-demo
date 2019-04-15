from Validations import LoginValidation
from Exceptions import LoginException
import pytest


'''Positive Test Cases'''''
    
boolean1=LoginValidation.login_validation("rishi.kumar","rishikumar#12")
if(boolean1==True):
    print(True)


'''Negetive Test Case'''
    
    
try:    
    boolean2=LoginValidation.login_validation("rishi.kumar","rishikumar$")
    if(boolean2==True):
        print(True)
except LoginException.LoginUsernamePasswordException as e:
    print(e)

try:    
    boolean2=LoginValidation.login_validation("rishikumar$1","rishi.kumar")
    if(boolean2==True):
        print(True)
except LoginException.LoginUsernamePasswordException as e:
    print(e)