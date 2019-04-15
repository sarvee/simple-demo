from Utility.DataStructures import Stack
from DataAccessLayer import ViewDB, viewprofileDB,CommentDB
from DataAccessLayer import LikesDB
from DataAccessLayer import DislikesDB
from Utility.UI import Menus
from Classes import Feed
from Exceptions import ChoiceException
import HomePage

''' this method show the feeds and the comments of the user and his/her friends'''

def show_feeds(username):
    count=0
    stack_of_status=ViewDB.get_status(username)
    Menus.banner("Show Feeds")
    status_stack_index=stack_of_status.get_top()
    status_stack_elements=stack_of_status.get_elements()
    while(status_stack_index>=0):
        status=status_stack_elements[status_stack_index]
        feed_id=stack_of_status.get_top()-(status_stack_index)+1
        name=status.get_username()
        user_obj=viewprofileDB.view_profile(name)
        print(feed_id,". ",user_obj.get_name(),"(",status.get_username(),"):",status.get_status())
        print("Likes",status.get_likes(),", Dislikes:",status.get_dislikes())
        comment_stack=status.get_comment()
        comment_stack_index=comment_stack.get_top()
        comment_stack_elements=comment_stack.get_elements()
        while comment_stack_index>=0:
            comment=comment_stack_elements[comment_stack_index]
            comment_user_obj=viewprofileDB.view_profile(comment.get_comment_username())
            print("   >",comment_user_obj.get_name(),"(",comment.get_comment_username(),"):",comment.get_comment_text())
            comment_stack_index-=1
        count+=1
        
        status_stack_index-=1
        if count>20:
            break
        print("-------------------------------------------")
    flag1=True
    while(flag1==True):
        try:
            feed_choice=input("select Feed(select X to return to home)")
            if feed_choice.upper()=='X':
                flag1=False
                HomePage.home(username)
                break
            elif(feed_choice.isdigit() and int(feed_choice)<=stack_of_status.get_top()+1):
                flag1=False
                feed=status_stack_elements[stack_of_status.get_top()+1-int(feed_choice)]
                sid=feed.get_statusid()
                print("1. Like")
                print("2. Dislike")
                print("3. Comment")
                end=False
                while(end==False):
                    try:
                        choice=input("choice:")
                        if(choice.isdigit()):
                            
                            if int(choice)==1:
                                LikesDB.likes(sid, username)
                                show_feeds(username)
                                end=True
                            elif int(choice)==2:
                                DislikesDB.dislikes(sid, username)
                                show_feeds(username)
                                end=True
                            elif int(choice)==3:
                                CommentDB.comment(sid, username)
                                show_feeds(username)
                                end=True
                            else:
                                raise ChoiceException.InvalidChoiceException
                        else:
                            raise ChoiceException.InvalidChoiceException
                    except ChoiceException.InvalidChoiceException as e:
                        print(e)

            else:
                raise ChoiceException.InvalidChoiceException
            
        except ChoiceException.InvalidChoiceException as e:
            print(e)
        
    
        