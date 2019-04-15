from Utility.UI import Menus
from Validations import Validatesignup
from Validations import EditProfileValidation
from Exceptions import EditProfileException,SignUpException
from DataAccessLayer import SetDB
import HomePage

''' from here you can edit profile of the user by entering the right password'''

def edit_profile(username):
    Menus.banner("Edit Profile")
    flag=True
    while(flag==True):
        password=input("Enter your Password:")
        try:
            if(EditProfileValidation.edit_profile_validation(username, password)==True):
                flag=False
                key=False
                while(key==False):
                    try:
                        name=input("Name:")
                        if(Validatesignup.validate_name(name)):
                            key=True
                    except SignUpException.InvalidNameException as e:
                        print(e)
                        
                while(key==True):
                    try:
                        surname=input("Surname:")
                        if(Validatesignup.validate_surname(surname)):
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
                        mobile_number=input("Enter Mobile Number")
                        if (Validatesignup.validate_mobile_number(mobile_number)):
                            key=False
                    except SignUpException.InvalidMobileNumberException as e:
                        print(e)
                        
                while(key==False):
                    try:
                        security_key=input("Enter Security Word:")
                        if (Validatesignup.validate_security_key(security_key)):
                            key=True
                    except SignUpException.InvalidSecurityKeyException as e:
                        print(e)
                        
                SetDB.update_db(username, gender.upper(), city, name, surname, relationship_status,mobile_number,security_key)
                print("Profile Successfully Updated")
                                
                
        except EditProfileException.InvalidpasswordException as e:
            print(e)
    HomePage.home(username)
        
        
    