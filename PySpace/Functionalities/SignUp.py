from Utility.UI import Menus
from DataAccessLayer import Username_Sign_up
from DataAccessLayer import SetDB
import re
from Validations import Validatesignup
from Exceptions import SignUpException

''' this function is used to register into the pyspace'''

def signup():
    
        Menus.banner("Sign Up")
        key=False
        while(key==False):
            try:
                username=input("enter your username:")
                boolean1=Validatesignup.validate_signup_username(username)
                if(boolean1==True):
                    key=True
            except SignUpException.InvalidUsernameException as e:
                print(e)
            except SignUpException.InvalidUsernameOnlyDigitsSpecialCharacterException as e:
                print(e)
           
        print("Password must contain a digit, a special character and should be at least 8 chars long")
        while(key==True):
            try:
                password=input("enter your password:")
                boolean2=Validatesignup.validate_signup_password(password)
                if(boolean2==True):
                    key=False
            except SignUpException.InvalidPasswordDigitException as e:
                print(e)
        
            except SignUpException.InvalidPasswordLengthException as e:
                print(e)
            
            except SignUpException.InvalidPasswordSpeacialCharException as e:
                print(e)
                
        while(key==False):
            try:        
                name=input("Name:")
                if (Validatesignup.validate_name(name)):
                    key=True
            except SignUpException.InvalidNameException as e:
                print(e)
        while(key==True):
            try:
                surname=input("Surname:")
                if (Validatesignup.validate_surname(surname)):
                    key=False
            except SignUpException.InvalidSurnameException as e:
                print(e)
        while(key==False):
            try:
                gender=input("Gender (m/f):")
                boolean3=Validatesignup.validate_signup_gender(gender)
                if(boolean3==True):
                    key=True
            except SignUpException.InvalidGenderException as e:
                print(e)
                
        while(key==True):
            try:
                city=input("City:")
                if (Validatesignup.validate_city(city)):
                    key=False
            except SignUpException.InvalidCityException as e:
                print(e)  
                
        while(key==False):
            try:
                relationship_status=input("Relationship Status:")
                if (Validatesignup.validate_relationship_status(relationship_status)):
                    key=True
            except SignUpException.InvalidRelationshipStatusException as e:
                print(e)  
        while(key==True):
            try:
                mobile_number=input("Enter Your Mobile Number(10 digits):")
                if (Validatesignup.validate_mobile_number(mobile_number)):
                    key=False
            except SignUpException.InvalidMobileNumberException as e:
                print(e)    
        while(key==False):
            try:
                security_key=input("Enter Security Word(Remember this and Do not tell this word to anyone as it will help you to get your forgotten password):")
                if (Validatesignup.validate_security_key(security_key)):
                    key=True
            except SignUpException.InvalidSecurityKeyException as e:
                print(e)
        
        
        SetDB.set_db(username, password, gender.upper(), city.lower(), name, surname, relationship_status,mobile_number,security_key)
        print("Sign Up Successful!!")
    
    
    
    