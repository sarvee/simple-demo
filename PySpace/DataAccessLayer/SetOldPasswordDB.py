from Utility import DB_connectivity
from Classes.Registration import Register
from Classes.Password import Password

''' this method is used to update the new password and the previous last 3 used passwords''' 

def set_old_password(username,password,password1):
    try:
        l1=[username,password,password1]
        con=DB_connectivity.create_connection()
        cur=DB_connectivity.create_cursor(con)
        list1=[]
        p=Password(username)
        cur.execute("update owner set password=:1 where user_name=:2",{':1':password1,':2':username})
        cur.execute("select * from loginval where user_name=:usrnm",{"usrnm":username})
        for row in cur:
            
            p.set_oldpass_1(row[1])
            p.set_oldpass_2(row[2])
            p.set_oldpass_3(row[3])
        p.set_oldpass_3(p.get_oldpass_2())
        p.set_oldpass_2(p.get_oldpass_1())
        p.set_oldpass_1(password)
        list1=[]
        list1.append(p.get_oldpass_1())
        list1.append(p.get_oldpass_2())
        list1.append(p.get_oldpass_3())
        
        
        cur.execute("update loginval set old_pass1=:1,old_pass2=:2,old_pass3=:3 where user_name=:4",{':1':list1[0],':2':list1[1],':3':list1[2],':4':username})
        
        
    finally:
        cur.close()
        con.commit()

#set_old_password("rishi.kumar", 'rishikumar@1', 'rishikumar#4')