'''
Created on Mar 9, 2017

@author: rishi.kumar02
'''
class LoginUsernamePasswordException(Exception):
    def __init__(self):
        super().__init__("Invalid Username-Password combination")
        
class LoginCaptchaException(Exception):
    def __init__(self):
        super().__init__("Invalid Captcha!")
        