from Utility import DB_connectivity
from Classes.Registration import Register
from Utility import DataStructures

''' this method is used to get the username of the user'''
def get_username():
    try:
        con=DB_connectivity.create_connection()
        cur=DB_connectivity.create_cursor(con)
        list_of_username=[]
        cur.execute("select user_name from owner")
        for username in cur:
          
            owner=Register()
            owner.set_user_name(username[0])
            list_of_username.append(owner)
       
        
        return list_of_username
        
    finally:
        cur.close()
        con.close()
