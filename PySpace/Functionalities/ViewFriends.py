from Utility.UI import Menus
from DataAccessLayer import ViewFriendsDB
from Utility import DataStructures
from Classes.Registration import Register
import HomePage
from Exceptions import ChoiceException

'''this method helps to view the friends of the user !'''

def view_friends(username):
    Menus.banner("View Friends")
    list1=ViewFriendsDB.view_friend_db(username)
    count=0
    for i in list1:
        count=count+1
        print(str(count),'.',i.get_name().upper(),' ',i.get_surname().upper(),' (',i.get_user_name(),'), ',i.get_city())
    
    flag=True
    while(flag==True):
        try:    
            choice=input("(Press x to return to Home):")
            if(choice.lower()=='x'):
                HomePage.home(username)
                flag=False
            else:
                raise ChoiceException.InvalidChoiceException
        except ChoiceException.InvalidChoiceException as e:
            print(e)