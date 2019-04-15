from Utility.UI.Menus import banner
import HomePage
from DataAccessLayer.FindFriendsDB import *
from Utility.DataStructures import Stack
import re
from Validations import FindFriendValidation
from DataAccessLayer import FindFriendsDB
import Exceptions

''' this method is used to find the PYSPACCE Users by search options'''

def find_friends(username,password):
    banner("Find Friends")
    search=input("Search: ")
    search=search.lower()
    list_of_friends=search_friends(username)
    find_list=[]
    friend_stack=Stack(len(list_of_friends))
    for x in list_of_friends:
        if re.search(search,x.get_name().lower()) or re.search(search,x.get_user_name().lower()) or re.search(search,x.get_surname().lower()):
            friend_stack.push(x)
    count=0
    while friend_stack.is_empty()!=True:
        data=friend_stack.pop()
        find_list.append(data)
        count+=1
        print(str(count)+".",data.get_name(),data.get_surname(),"("+data.get_user_name()+"),",data.get_city())
    key_for_choice=False
    while key_for_choice==False:
        try:
            choice=input("Select Profile (Press x to return to Home): ")
            if (choice.lower()=="x" or choice.isdigit()):
                if(int(choice)>0 and int(choice)<=count):
                    key_for_choice=True
            else:
                raise Exceptions.ChoiceException.InvalidAutoChoiceException("Wrong Choice")
        except Exceptions.ChoiceException.InvalidAutoChoiceException as e:
            print(e)
                
    if choice.lower()=="x":
        HomePage.home(username)
    else:
        friend=find_list[int(choice)-1]
        find_friends_of_friends(friend.get_user_name(),username,password)
        
'''this methods is used to view the friend  searched on PYSPACE and user can send friend request from here '''

def find_friends_of_friends(friendname,username,password):
    
    profile=view_profile(friendname)
    fullname=profile.get_name()+" "+profile.get_surname()
    banner(fullname)
    print("Username:",profile.get_user_name())
    print("Name:",profile.get_name())
    print("Surname:",profile.get_surname())
    if profile.get_gender().lower()=="m":
        print("Gender:  Male")
    else:
        print("Gender:  Female")
    print("City:",profile.get_city())
    print("Relationship Status:",profile.get_relationship_status())
    
    if (FindFriendValidation.validate_is_two_friends(username, friendname)):
        print("(Already in your friend list)")
        print("1. View Friend List")
        key_for_choice=False
        while key_for_choice==False:
            try:
                choice=input("Choice(Press x to return to Home): ")
                if choice.lower()=="x" or choice=="1":
                    key_for_choice=True
                else:
                    raise Exceptions.ChoiceException.InvalidAutoChoiceException("Wrong Choice")
                    
            except Exceptions.ChoiceException.InvalidAutoChoiceException as e:
                print(e)
            
        if choice.lower()=="x":
            HomePage.home(username)
        else:
            find_friendlist_of_friend(friendname, username, password)
    else:
        print("1. Add Friend")
        print("2. View Friend List")
        key_for_choice=False
        while key_for_choice==False:
            try:
                choice=input("Choice(Press x to return to Home): ")
                if choice.lower()=="x" or choice=="1" or choice=="2":
                    key_for_choice=True
                else:
                    raise Exceptions.ChoiceException.InvalidAutoChoiceException("Wrong Choice")
                    
            except Exceptions.ChoiceException.InvalidAutoChoiceException as e:
                print(e)
            
        if choice.lower()=="x":
            HomePage.home(username)
        elif choice=="1":
            try:
                if (username!=friendname):
                    FindFriendsDB.giving_request(username, friendname)
                    print("Request sent Successfully")
                    HomePage.home(username)
                else:
                    raise Exceptions.RequestException.InvalidSendingRequestException
                    
            except Exceptions.RequestException.InvalidSendingRequestException as e:
                print(e)
            HomePage.home(username)
            
        else:
            find_friendlist_of_friend(friendname, username, password)

'''this method shows the friend of the searched person and from here you can select and view profile of that friend'''

def find_friendlist_of_friend(friendname,username,password):
    
    profile=view_profile(friendname)
    banner(profile.get_name()+"'s Friend List")
    friend_stack=view_friendlist(friendname)
    count=0
    friend_list=[]
    while friend_stack.is_empty() != True:
        data=friend_stack.pop()
        count+=1
        friend_list.append(data)
        print(str(count)+".",data.get_name(),data.get_surname(),"("+data.get_user_name()+"),",data.get_city())
    
    key_for_choice=False
    while key_for_choice==False:
        try:
            choice=input("Select Profile (Press x to return to Home): ")
            if choice=="x" or (int(choice)>0 and int(choice)<=count):
                key_for_choice=True
            else:
                raise Exceptions.ChoiceException.InvalidAutoChoiceException("Wrong Choice")
                
        except Exceptions.ChoiceException.InvalidAutoChoiceException as e:
            print(e)
                
    
    if choice=="x":
        HomePage.home(username)
    else:
        friend_choose=friend_list[(int(choice))-1]
        find_friends_of_friends(friend_choose.get_user_name(), username, password)