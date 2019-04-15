'''
Created on Mar 10, 2017

@author: rishi.kumar02
'''
from Utility import DB_connectivity
from Classes.Registration import Register
from Classes.Password import Password

''' this method restricts the user to like his own status and this updates the no. of likes in the database'''
def likes(status_id,username):
    try:
        con=DB_connectivity.create_connection()
        cur=DB_connectivity.create_cursor(con)
        cur1=DB_connectivity.create_cursor(con)
        cur.execute("select user_name,likes from status where status_id=:sid",{"sid":status_id})
        for row in cur:
            name=row[0]
            if(username==name):
                print("You cann't like  your own status!")
                pass
            else:
                likes=row[1]+1
                cur1.execute("update status set likes=:no_of_likes where status_id=:sid",{"sid":status_id,"no_of_likes":likes})
                print("Status Liked!")
    finally:
        cur.close()
        cur1.close()
        con.commit()
        con.close()