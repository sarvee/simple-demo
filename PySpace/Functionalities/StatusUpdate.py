from Utility.UI import Menus
from Exceptions import StatusUpdateExceptions, StatusUpdationException
from DataAccessLayer import SetStatus
from Functionalities import HomePage
import Validations.StatusValidation

'''this function is used to update the status from the user profile'''

def Status_update(username):
    flag=True
    while(flag==True):
        Menus.banner("Status Update")
        flag1=True
        while(flag1==True):
            try:
                status=input("Enter the status:")
                if(Validations.StatusValidation.validate_status(status)):
                    flag1=False
            except StatusUpdationException.InvalidStatusException as e:
                print(e)
        end=False
        
        while(end==False):
            try:
                confirm=input("Confirm (y/n):")
                if(confirm=='Y' or confirm=='y'):
                    end=True
                    SetStatus.setStatus(username,status)
                    print("Status Updated Successfully!")
                    flag=False
                    HomePage.home(username)
                    break
                elif(confirm=='N' or confirm=='n'):
                    flag=False
                    HomePage.home(username)
                    break
                else:
                    raise StatusUpdateExceptions.ConfirmationException
            except StatusUpdateExceptions.ConfirmationException as e:
                print(e)
    