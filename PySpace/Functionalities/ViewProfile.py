from Utility.UI import Menus
from DataAccessLayer import viewprofileDB
import EditProfile,ViewFriends

'''this function is used to view profile of the username and has options like - Edit Profile and View Friends of the user !'''

def view_profile(username):
    Menus.banner("View Profile")
    
    user1=viewprofileDB.view_profile(username)
    p=user1.get_gender()
    if(p=='M'):
        g='Male'
    else:
        g='Female'
    print("Username:",user1.get_user_name())
    print("Name:",user1.get_name().upper())
    print("Surname:",user1.get_surname().upper())
    print("Gender:",g)
    print("City:",user1.get_city().upper())
    print("Relationship Status:",user1.get_relationship_status().upper())
    
    choice=Menus.display_menu("Other options", 'Edit Profile,View Friends')
    if(choice.isdigit() and (int(choice)>=1 and int(choice)<=2)):
        if(int(choice)==1):
            EditProfile.edit_profile(username)
            
        if(int(choice)==2):
            ViewFriends.view_friends(username)
 
    else:
        print("Please enter a valid option ( 1,2)")
    
    