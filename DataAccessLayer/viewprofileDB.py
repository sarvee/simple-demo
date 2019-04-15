from Utility import DB_connectivity
from Classes.Registration import Register

'''this method for viewing user's profile, the data is fetched from the database'''

def view_profile(username):
    try:
        con=DB_connectivity.create_connection()
        cur=DB_connectivity.create_cursor(con)
        cur.execute("select * from owner where user_name=:usernm",{"usernm":username})
        for row in cur:
            user1=Register()
            user1.set_user_name(row[0])
            user1.set_name(row[2])
            user1.set_surname(row[3])
            user1.set_gender(row[4])
            user1.set_city(row[5])
            user1.set_relationship_status(row[6])
            
        return user1
    finally:
        cur.close()
        con.commit()
        con.close()