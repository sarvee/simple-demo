from DataAccessLayer import ChangePasswordDB
from Exceptions import PasswordException

'''validate the new password entered is equal to the the last three old used password and the current password'''

def password_validation(username,password,password1,password2):
    p=ChangePasswordDB.change_password_db(username)
    flag=True
    if(p.get_oldpass_1()!=password1 and p.get_oldpass_2()!=password1 and p.get_oldpass_3()!=password1 and password1!=password):
        return True

    else:
        raise PasswordException.PasswordException
        
