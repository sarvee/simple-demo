from Utility import DB_connectivity
from Classes.Registration import Register
from Classes.Password import Password

'''this method fetches the last 3 old passwords of the user'''

def change_password_db(username):
    try:
        con=DB_connectivity.create_connection()
        cur=DB_connectivity.create_cursor(con)
        cur.execute("select * from loginval where user_name=:usrnm",{"usrnm":username})
        p=Password(username)
        for row in cur:
            
            p.set_oldpass_1(row[1])
            p.set_oldpass_2(row[2])
            p.set_oldpass_3(row[3])
        
        return p
        
    finally:
        cur.close()
        con.commit()
        con.close()
        
