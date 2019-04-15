from DataAccessLayer import LoginDB
from Exceptions import LoginException
'''checks the username and password to login are correct or not'''
def login_validation(username,password):
    
    boolean1=LoginDB.db_login(username, password)
    if(boolean1==True):
        return True
    else:
        raise LoginException.LoginUsernamePasswordException
    
    