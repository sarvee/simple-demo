from Utility.UI import Menus
from DataAccessLayer import ApproveRequestDB
from Classes import Registration
import HomePage
from Exceptions import RequestException, ChoiceException

''' this method is used to view friend request sent to the user and he can accept it or rejects it'''

def approve_request(username):
    Menus.banner("Approve Request")
    list1=ApproveRequestDB.approve_request_DB(username)
    count=0
    for i in list1:
        count=count+1
        print(str(count),'.',i.get_name(),' ',i.get_surname(),' (',i.get_user_name(),'), ',i.get_city(),' ',i.get_date())
    l=len(list1)   
    
    flag=True
    
    while(flag==True):
        try:
            request=input("Select Request (Press x to return to Home):")
            if(request.lower()=='x'):
                HomePage.home(username)
                flag=False
            elif(request.isdigit()):  
                if(int(request)>=1 and int(request)<=l):
                    flag=False
                    end=False
                    while(end==False):
                        try:
                            choice=Menus.display_menu1('Accept,Reject')
                            r=int(request)-1
                            if((int(choice)>=1 and int(choice)<=2)):
                                if(int(choice)==1):
                                    friend1=list1[r].get_user_name()
                                    ApproveRequestDB.approve_friend_accept(username, friend1)
                                    print("Friend Request Approved")
                                    approve_request(username)
                                    end=True
                                    #ViewFunctions.view_product()
                                if(int(choice)==2):
                                    friend1=list1[r].get_user_name()
                                    ApproveRequestDB.approve_friend_reject(username, friend1)
                                    print("Friend Request Rejected")
                                    approve_request(username)
                                    end=True
                            else:
                                raise ChoiceException.InvalidAutoChoiceException("Please enter a valid option ( 1,2)")
                        except ChoiceException.InvalidAutoChoiceException as e:
                            print(e)
                else:
                    raise RequestException.InvalidRequestException
                
            else:
                raise RequestException.InvalidRequestException
        except RequestException.InvalidRequestException as e:
            print(e)
