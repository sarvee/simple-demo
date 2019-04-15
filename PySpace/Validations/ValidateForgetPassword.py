from DataAccessLayer import Username_Sign_up, ForgetPasswordDB
from Exceptions import ForgetPasswordException



def forget_password_verification(username,mobile_number,security_key):
    
    list_of_credentials=ForgetPasswordDB.get_password_verification_details()
    flag1=False
    flag2=False
    flag3=False
    for user in list_of_credentials:
        if(user.get_user_name()==username):
            flag1=True
            if(user.get_mobile_number()==mobile_number):
                flag2=True
                if(user.get_security_question()==security_key):
                    flag3=True
                    return True
    if(flag1==False):
        raise ForgetPasswordException.InvalidForgetPasswordDetailsException1
    elif(flag2==False):
        raise ForgetPasswordException.InvalidForgetPasswordDetailsException2
    elif(flag3==False):
        raise ForgetPasswordException.InvalidForgetPasswordDetailsException3
    
    
                
    
    