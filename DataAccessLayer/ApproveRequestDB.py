from Utility import DB_connectivity
from Classes.Registration import Register
from Classes.Password import Password

'''this method fetches the details of the friend who have sent request to the user''' 

def approve_request_DB(username):
    try:
        con=DB_connectivity.create_connection()
        cur=DB_connectivity.create_cursor(con)
        
        list1=[]
        cur.execute("select sender_user_name,to_char(request_date,'dd/mm/yy') from friend_request where reciever_user_name=:usrnm order by request_time desc",{":usrnm":username})
        for row in cur:
            cur2=DB_connectivity.create_cursor(con)
            cur2.execute("select first_name,sur_name,city,user_name from owner where user_name=:kp",{':kp':row[0]})
            for row1 in cur2:
                user1=Register()
                user1.set_name(row1[0])
                user1.set_surname(row1[1])
                user1.set_user_name(row1[3])
                user1.set_city(row1[2])
                user1.set_date(row[1])
                list1.append(user1)
            cur2.close()
        return list1
    finally:
        cur.close()
        con.commit()
        con.close()
'''this method insert the friend and user into the friend_list table after approving the request and deletes the friend request'''

def approve_friend_accept(username,friend1):
    try:
        con=DB_connectivity.create_connection()
        cur=DB_connectivity.create_cursor(con)
        cur.execute("insert into friend_list(user_name,friend_user_name) values(:1,:2)",{":1":username,":2":friend1})
        cur.execute("insert into friend_list(user_name,friend_user_name) values(:1,:2)",{":1":friend1,":2":username})
        cur.execute("delete from friend_request where sender_user_name=:1 and reciever_user_name=:2",{":1":friend1,":2":username})
    finally:
        cur.close()
        con.commit()
        con.close()
''' this method deletes the data from the database of the rejected friend request'''
           
def approve_friend_reject(username,friend1):
    try:
        con=DB_connectivity.create_connection()
        cur=DB_connectivity.create_cursor(con)
        cur.execute("delete from friend_request where sender_user_name=:1 and reciever_user_name=:2",{":1":friend1,":2":username})
    finally:
        cur.close()
        con.commit()
        con.close()