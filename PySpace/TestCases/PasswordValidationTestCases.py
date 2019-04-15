from Validations import PasswordValidation
from Exceptions import PasswordException
import pytest


'''Positive Test Cases'''''
    
boolean1=PasswordValidation.password_validation("rishi.kumar", "rishikumar#12", "rishikumar%1", "rishikumar%1")
if(boolean1==True):
    print(True)

boolean1=PasswordValidation.password_validation("rishi.kumar", "rishikumar#12", "rishikumar%134", "rishikumar%134")
if(boolean1==True):
    print(True)
    



'''Negetive Test Case'''
    
    
try:    
    boolean1=PasswordValidation.password_validation("rishi.kumar", "rishikumar#12", "rishikumar12!", "rishikumar12!")
    if(boolean1==True):
        print(True)
except PasswordException.PasswordException as e:
    print(e)

