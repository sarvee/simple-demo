from Utility.UI import Menus
from DataAccessLayer import Username_Sign_up
from DataAccessLayer import SetDB
import re
from Exceptions import SignUpException 
'''validate signup credentials'''
def validate_signup_username(username):
    
    if(re.search(r"[a-z A-Z]", username)==None):
        raise SignUpException.InvalidUsernameOnlyDigitsSpecialCharacterException
    else:
        list_of_username=Username_Sign_up.get_username()
        flag=False
        for i in list_of_username:
            if(i.get_user_name()==username):
                flag=True
        if(flag==True):
            raise SignUpException.InvalidUsernameException
        else:
            return True
    
def validate_signup_password(password):
    if(re.search(r"[0-9]", password)==None):
        raise SignUpException.InvalidPasswordDigitException
    elif(re.search(r"[@|#|$|%|&|*]", password)==None):
        raise SignUpException.InvalidPasswordSpeacialCharException
    elif(len(password)<8):
        raise SignUpException.InvalidPasswordLengthException
    else:
        return True
                
    
def validate_signup_gender(gender):
    if(gender.upper()=='M' or gender.upper()=='F'):
        return True
    else:
        raise SignUpException.InvalidGenderException

def validate_name(name):
    if(re.search(r"[@|#|$|%|&|*|_|!]", name)==None and re.search(r"[0-9]", name)==None and re.search(r"[a-z A-Z]", name)!=None):
        return True
    else:
        raise SignUpException.InvalidNameException
    
def validate_surname(surname):
    if(re.search(r"[@|#|$|%|&|*|_|!]", surname)==None and re.search(r"[0-9]", surname)==None and re.search(r"[a-z A-Z]", surname)!=None):
        return True
    else:
        raise SignUpException.InvalidSurnameException
    
def validate_city(city):
    if(re.search(r"[@|#|$|%|&|*|_|!]", city)==None and re.search(r"[0-9]", city)==None and re.search(r"[a-z A-Z]", city)!=None):
        return True
    else:
        raise SignUpException.InvalidCityException
    
def validate_relationship_status(relationship_status):
    if(re.search(r"[@|#|$|%|&|*|_|!]", relationship_status)==None and re.search(r"[0-9]", relationship_status)==None and re.search(r"[a-z A-Z]", relationship_status)!=None):
        return True
    else:
        raise SignUpException.InvalidRelationshipStatusException
    
def validate_mobile_number(mobile_number):
    if(re.search(r"[@|#|$|%|&|*|_]", mobile_number)==None and re.search(r"[a-z A-Z]", mobile_number)==None and len(mobile_number)==10):
        return True
    else:
        raise SignUpException.InvalidMobileNumberException
 
def validate_security_key(security_key):
    if(re.search(r"[a-z A-Z]", security_key)!=None):
        return True
    else:
        raise SignUpException.InvalidSecurityKeyException
 
