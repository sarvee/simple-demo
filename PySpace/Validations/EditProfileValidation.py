from DataAccessLayer import EditProfileDB
from Exceptions import EditProfileException
'''validate password'''
def edit_profile_validation(username,password):
    boolean1=EditProfileDB.edit_profile_db(username, password)
    if(boolean1==True):
        return True
    else:
        raise EditProfileException.InvalidpasswordException