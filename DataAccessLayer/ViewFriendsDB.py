from Utility import DB_connectivity,DataStructures
from Classes.Registration import Register
from Classes.Password import Password

'''this method is to view friends of the user fetches details from the table'''

def view_friend_db(username):
    try:
        con=DB_connectivity.create_connection()
        cur=DB_connectivity.create_cursor(con)
        
        list1=[]
        cur.execute("select friend_user_name from friend_list where user_name=:usrnm order by accept_time",{":usrnm":username})
        for row in cur:
            cur2=DB_connectivity.create_cursor(con)
            cur2.execute("select first_name,sur_name,city,user_name from owner where user_name=:friend_username",{':friend_username':row[0]})
            for row1 in cur2:
                user1=Register()
                user1.set_name(row1[0])
                user1.set_surname(row1[1])
                user1.set_user_name(row1[3])
                user1.set_city(row1[2])
                list1.append(user1)
            cur2.close()
        return list1
    finally:
        cur.close()
        con.commit()
        con.close()
        
''' this method checks if the 2 users are friends of each other or not '''

def check_friends(username,friendname):
    try:
        con=DB_connectivity.create_connection()
        cur=DB_connectivity.create_cursor(con)
        cur.execute("select count(*) from friend_list where user_name=:1 and friend_user_name=:2",{":1":username,":2":friendname})
        for row in cur:
            return(row[0])
    finally:
        cur.close()
        con.commit()
        con.close()

        
        
        
        
        
        
