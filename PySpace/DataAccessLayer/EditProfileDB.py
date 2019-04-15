from Utility import DB_connectivity
from Classes.Registration import Register

''' this method is used to check the password of the user by checking into the database'''
def edit_profile_db(username,password):
    
    try:
        con=DB_connectivity.create_connection()
        cur=DB_connectivity.create_cursor(con)
        cur.execute("select * from owner where user_name=:usernm",{"usernm":username})
        for row in cur:
            if(row[1]==password):
                
                return True
            else:
                return False
    finally:
        cur.close()
        con.commit()
        con.close()