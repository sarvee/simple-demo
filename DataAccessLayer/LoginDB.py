from Utility import DB_connectivity
from Classes.Registration import Register

'''this checks whether the login password and username are correct or not'''

def db_login(username,password):
    
    try:
        con=DB_connectivity.create_connection()
        cur=DB_connectivity.create_cursor(con)
        cur.execute("select * from owner where user_name=:usernm",{"usernm":username})
        for row in cur:
            if(row[0]==username and row[1]==password):
                return True
            else:
                return False
    finally:
        cur.close()
        con.commit()
        con.close()