from Utility.UI import Menus
from Validations import ValidateForgetPassword
from Exceptions import ForgetPasswordException
from DataAccessLayer import GetPassword
from time import sleep
import WelcomeFunction

def forget_password():
    Menus.banner("Forget Password")
    end=False
    while(end==False):
        try:
            username=input("Enter Your Username")
            mobile_number=input("Enter Your Mobile Number")
            security_key=input("Enter the Security Word You Entered While Sign Up")
            if(ValidateForgetPassword.forget_password_verification(username, mobile_number, security_key.lower())==True):
                print("Congratulations Details Verified")
                password=GetPassword.get_password(username)
                print("Your Password is: ",password)
                sleep(5)
                break
        except ForgetPasswordException.InvalidForgetPasswordDetailsException1 as e:
            print(e)
        except ForgetPasswordException.InvalidForgetPasswordDetailsException2 as e:
            print(e)
        except ForgetPasswordException.InvalidForgetPasswordDetailsException3 as e:
            print(e)
            
    WelcomeFunction.welcome()
        