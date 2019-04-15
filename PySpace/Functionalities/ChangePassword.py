from Utility.UI import Menus
from Validations import PasswordValidation
from Validations import Validatesignup
from Validations import EditProfileValidation
from Exceptions import SignUpException,EditProfileException,PasswordException
from DataAccessLayer import SetOldPasswordDB
import WelcomeFunction

'''this method is used to change the password of the user and before doing so check whether it is not matching the last three used passwords'''

def change_password(username):
    Menus.banner("Change Password ")
    flag=True
    while(flag==True):
        password=input("Enter your Password:")
        try:
            if(EditProfileValidation.edit_profile_validation(username, password)==True):
                flag=False
                print("Verified!")
                key=True
                while(key==True):
                    try:
                        password1=input("Enter your new password:")
                        password2=input("Confirm your new password:")
                        boolean2=Validatesignup.validate_signup_password(password1)
                        if(boolean2==True):
                            try:
                                if(password1==password2):
                                    boolean5=PasswordValidation.password_validation(username,password,password1,password2)
                                    if(boolean5==True):
                                        SetOldPasswordDB.set_old_password(username,password,password1)
                                        print("Password Updated")
                                        key=False
                                else:
                                    print("password doesn't match")
                            except PasswordException.PasswordException as e:
                                print(e)
                    except SignUpException.InvalidPasswordDigitException as e:
                        print(e)
                    except SignUpException.InvalidPasswordLengthException as e:
                        print(e)
                    except SignUpException.InvalidPasswordSpeacialCharException as e:
                        print(e)
                        
        except EditProfileException.InvalidpasswordException as e:
            print(e)
    WelcomeFunction.welcome()          
    