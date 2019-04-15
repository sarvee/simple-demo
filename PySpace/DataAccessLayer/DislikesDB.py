'''
Created on Mar 10, 2017

@author: rishi.kumar02
'''
from Utility import DB_connectivity
from Classes.Registration import Register
from Classes.Password import Password

''' this method restricts the user to dislike his own status and this updates the no. of dislikes in the database'''


def dislikes(status_id,username):
    try:
        con=DB_connectivity.create_connection()
        cur=DB_connectivity.create_cursor(con)
        cur1=DB_connectivity.create_cursor(con)
        cur.execute("select user_name,dislikes from status where status_id=:sid",{"sid":status_id})
        for row in cur:
            name=row[0]
            if(username==name):
                print("You cann't dislike  your own status!")
                pass
            else:
                dislikes=row[1]+1
                cur1.execute("update status set dislikes=:no_of_dislikes where status_id=:sid",{"sid":status_id,"no_of_dislikes":dislikes})
                print("Status Disliked!")
    finally:
        cur.close()
        cur1.close()
        con.commit()
        con.close()