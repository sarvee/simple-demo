from Utility.UI import Menus
from Validations import LoginValidation
import random
from Exceptions import LoginException
import HomePage

'''From here we can login into the PYSPACE'''

def login():
    
    Menus.banner("Login")
    key=False
    count=0
    while(count<3):
        try:
            count=count+1
            username=input("Enter Username:")
            password=input("Enter Password:")
            if(LoginValidation.login_validation(username,password)==True):
                HomePage.home(username)
                key=True
                break
        except LoginException.LoginUsernamePasswordException as e:
            print(e)
            
    while(key==False):
        try:
            randomnum= 'qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM'
            i=''
            for j in range(0,6):
                x=randomnum[random.randrange(1,62)]
                i+=x
            print("Captcha:",i)
            captcha=input("Captcha:")
            username=input("Enter Username:")
            password=input("Enter Password:")
            if(i==captcha):
                if(LoginValidation.login_validation(username,password)==True):
                    key=True
                    HomePage.home(username)
                    break
            else:
                raise LoginException.LoginCaptchaException
        except LoginException.LoginCaptchaException as e:
            print(e)
            
        except LoginException.LoginUsernamePasswordException as e:
            print(e)
