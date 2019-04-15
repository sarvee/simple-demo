from Validations import EditProfileValidation
from Exceptions import EditProfileException
import pytest


'''Positive Test Cases'''''
    
boolean1=EditProfileValidation.edit_profile_validation("rishi.kumar","rishikumar#12")
if(boolean1==True):
    print(True)


'''Negetive Test Case'''
    
    
try:    
    boolean1=EditProfileValidation.edit_profile_validation("rishi.kumar","rishikumar")
    if(boolean1==True):
        print(True)
except EditProfileException.InvalidpasswordException as e:
    print(e)
