from Utility import DB_connectivity,DataStructures
from Classes.Registration import Register
from Classes.Feed import Status
from DataAccessLayer import ViewFriendsDB
from Classes.Comment import Comment

''' this method is used in show feeds to show status and comments fetched from tthe database'''
def get_status(username):
    list1=ViewFriendsDB.view_friend_db(username)
    list_of_friends=[]
    for i in list1:
        list_of_friends.append(i.get_user_name())
    list_of_friends.append(username)
    try:
        con=DB_connectivity.create_connection()
        cur=DB_connectivity.create_cursor(con)
        cur1=DB_connectivity.create_cursor(con)
        stack_of_status=DataStructures.Stack(100)
        list_of_status=[]
        for user_friend in list_of_friends:  
            cur.execute("select * from status where user_name=:username",{"username":user_friend})
            for row in cur:
                feed=Status(None,None)
                feed.set_statusid(row[0])
                feed.set_status(row[1])
                feed.set_username(row[2])
                feed.set_status_timestamp(row[3])
                feed.set_likes(row[4])
                feed.set_dislikes(row[5])
                sid=feed.get_statusid()
                comment_list=DataStructures.Stack(100)
                
                cur1.execute("select * from comments where status_id=:sid order by comment_time",{"sid":sid})
                for row1 in cur1:
                    comment=Comment()
                    comment.set_statusid(row1[0])
                    comment.set_comment_text(row1[1])
                    comment.set_comment_username(row1[2])
                    comment.set_comment_timestamp(row1[3])
                    comment_list.push(comment)
                
                feed.set_comment(comment_list)
                list_of_status.append(feed)
        list_of_status=sorted(list_of_status,key=lambda i:i.get_status_timestamp())
        for feed_obj in list_of_status:
            stack_of_status.push(feed_obj)
                    
        return stack_of_status
    finally:
        cur.close()
        cur1.close()
        con.commit()
        con.close()
        
# get_status("rishi.kumar")
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                