from Utility.UI import Menus
import StatusUpdate,ViewProfile,ChangePassword,ApproveRequest,ShowFeed,FindFriends
from DataAccessLayer import GetPassword
import WelcomeFunction

'''this is the home method where a user can choose many other functions of PYSPACE '''

def home(username):
    
    choice=Menus.display_menu('Home', 'Status Update,View Profile,Show Feeds,Approve Request,Change Password,Find Friends,Logout')
    if(choice.isdigit() and (int(choice)>=1 and int(choice)<=7)):
        if(int(choice)==1):
            StatusUpdate.Status_update(username)
            #Login_function.login()
            #ViewFunctions.view_product()
        if(int(choice)==2):
            #Sign_Up.signup()
            ViewProfile.view_profile(username)
#     
        if(int(choice)==3):
            ShowFeed.show_feeds(username)
            
        if(int(choice)==4):
            ApproveRequest.approve_request(username)
            
        if(int(choice)==5):
            ChangePassword.change_password(username)
            
#     
        if(int(choice)==6):
            password=GetPassword.get_password(username)
            FindFriends.find_friends(username, password)
            
        if(int(choice)==7):
            WelcomeFunction.welcome()
            
    else:
        print("Please enter a valid option ( 1,2,3,4,5,6,7)")