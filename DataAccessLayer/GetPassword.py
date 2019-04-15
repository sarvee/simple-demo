from Utility import DB_connectivity
from Classes.Registration import Register
from Utility import DataStructures

'''method is used to get password of the user'''

def get_password(username):
    try:
        con=DB_connectivity.create_connection()
        cur=DB_connectivity.create_cursor(con)
        cur.execute("select password from owner where user_name=:1",{":1":username})
        for row in cur:
            return row[0]
        return
        
    finally:
        cur.close()
        con.close()