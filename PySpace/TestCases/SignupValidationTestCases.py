from Validations import Validatesignup
from Exceptions import SignUpException
import pytest




'''Positive Test Cases'''''




    
boolean1=Validatesignup.validate_signup_username("rishi.kumar123")
if(boolean1==True):
    print(True)
    
boolean1=Validatesignup.validate_signup_password("rishikumar#12")
if(boolean1==True):
    print(True)

boolean1=Validatesignup.validate_signup_gender("m")
if(boolean1==True):
    print(True)

boolean1=Validatesignup.validate_name("rishi")
if(boolean1==True):
    print(True)

boolean1=Validatesignup.validate_surname("Kumar")
if(boolean1==True):
    print(True)
    
boolean1=Validatesignup.validate_city("delhi")
if(boolean1==True):
    print(True)

boolean1=Validatesignup.validate_relationship_status("single")
if(boolean1==True):
    print(True)
    
    
    
    
    
'''Negetive Test Case'''
    
    
    
    
try:    
    boolean1=Validatesignup.validate_signup_username("rishi.kumar@1")
    if(boolean1==True):
        print(True)
except SignUpException.InvalidUsernameException as e:
    print(e)

try:    
    boolean1=Validatesignup.validate_signup_username("4324632321$#@")
    if(boolean1==True):
        print(True)
except SignUpException.InvalidUsernameOnlyDigitsSpecialCharacterException as e:
    print(e)
    
    
    
try:    
    boolean1=Validatesignup.validate_signup_password("rishikumar")
    if(boolean1==True):
        print(True)
except SignUpException.InvalidPasswordDigitException as e:
    print(e)
    
try:    
    boolean1=Validatesignup.validate_signup_password("rishikumar1")
    if(boolean1==True):
        print(True)
except SignUpException.InvalidPasswordSpeacialCharException as e:
    print(e)
    
try:    
    boolean1=Validatesignup.validate_signup_password("ris@1")
    if(boolean1==True):
        print(True)
except SignUpException.InvalidPasswordLengthException as e:
    print(e)
    
try:    
    boolean1=Validatesignup.validate_signup_gender("male")
    if(boolean1==True):
        print(True)
except SignUpException.InvalidGenderException as e:
    print(e)
    
try:    
    boolean1=Validatesignup.validate_name("rishi1")
    if(boolean1==True):
        print(True)
except SignUpException.InvalidNameException as e:
    print(e)
    
try:    
    boolean1=Validatesignup.validate_surname("kumar1")
    if(boolean1==True):
        print(True)
except SignUpException.InvalidSurnameException as e:
    print(e)
    
try:    
    boolean1=Validatesignup.validate_city("delhi112")
    if(boolean1==True):
        print(True)
except SignUpException.InvalidCityException as e:
    print(e)

try:    
    boolean1=Validatesignup.validate_relationship_status("single112")
    if(boolean1==True):
        print(True)
except SignUpException.InvalidRelationshipStatusException as e:
    print(e)
