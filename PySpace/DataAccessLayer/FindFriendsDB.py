from Utility import DB_connectivity, DataStructures
from Classes.Registration import Register

'''used to get the username of the user by fetching from the database'''
def get_username():
    try:
        con=DB_connectivity.create_connection()
        cur=DB_connectivity.create_cursor(con)
        list_of_username=[]
        cur.execute("select user_name from owner")
        for username in cur:
            users=Register()
            users.set_user_name(username[0])
            list_of_username.append(users)
        return list_of_username
    
    finally:
        cur.close()
        con.commit()
        con.close()

''' this method is used to view the profile of the user by fetching from the database'''
        
def view_profile(username):
    try:
        con=DB_connectivity.create_connection()
        cur=DB_connectivity.create_cursor(con)
        profile=Register()
        cur.execute("select first_name,sur_name,gender,city,relationship_status from owner where user_name=:1",{":1":username})
        for name, surname, gender, city, relationship_status in cur:
            profile.set_user_name(username)
            profile.set_name(name)
            profile.set_surname(surname)
            profile.set_gender(gender)
            profile.set_city(city)
            profile.set_relationship_status(relationship_status)
        
        return profile
    
    finally:
        cur.close()
        con.commit()
        con.close()

''' this method is used to get the first name of the user by fetching from the database'''
        
def get_name(username):
    try:
        con=DB_connectivity.create_connection()
        cur=DB_connectivity.create_cursor(con)
        cur.execute("select first_name from owner where user_name=:1 ",{":1":username})
        for name in cur:
            users=Register()
            users.set_name(name[0])
        return users
    
    finally:
        cur.close()
        con.commit()
        con.close()  
'''this method is used to search the friends of the user by fetching from the database'''
        
def search_friends(username1):
    
    try:
        con=DB_connectivity.create_connection()
        cur=DB_connectivity.create_cursor(con)
        list_of_friends=[]
        cur.execute("select city from owner where user_name=:1",{":1":username1})
        for row in cur:
            user_city=row[0].lower()
        cur.execute("select first_name,sur_name,user_name,city from owner where city<>:1 and user_name<>:2",{"1":user_city,":2":username1})
        for name,surname,username,city in cur:
            find_fri=Register()
            find_fri.set_city(city)
            find_fri.set_name(name)
            find_fri.set_surname(surname)
            find_fri.set_user_name(username)
            list_of_friends.append(find_fri)
        
        cur.execute("select first_name,sur_name,user_name,city from owner where city=:1 and user_name<>:2",{"1":user_city,":2":username1})
        for name,surname,username,city in cur:
            find_fri=Register()
            find_fri.set_city(city)
            find_fri.set_name(name)
            find_fri.set_surname(surname)
            find_fri.set_user_name(username)
            list_of_friends.append(find_fri)
        return list_of_friends
    
    finally:
        cur.close()
        con.commit()
        con.close() 
        
'''this method is used to view the friend list by fetching from the database'''        
def view_friendlist(username):
    try:
        con=DB_connectivity.create_connection()
        cur=DB_connectivity.create_cursor(con)
        cur.execute("SELECT COUNT(*) FROM friend_list")
        for count in cur:
            value=count[0]
        friend_stack=DataStructures.Stack(value)
        cur.execute("SELECT friend_user_name FROM friend_list WHERE user_name=:1 ORDER BY accept_time",{":1":username})
        for friend in cur:
            friend_details=view_profile(friend[0])
            friend_stack.push(friend_details)
        return friend_stack
    finally:
        cur.close()
        con.commit()
        con.close() 
    
'''this method send the friend request to other user of pyspace and adding this to the database'''
        
def giving_request(username,friendname):
    
    try:
        con=DB_connectivity.create_connection()
        cur=DB_connectivity.create_cursor(con)
        cur.execute("INSERT INTO friend_request (reciever_user_name,sender_user_name) VALUES (:1,:2)",{":1":friendname,":2":username})
        
    finally:
        cur.close()
        con.commit()
        con.close()