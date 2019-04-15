from Utility import DB_connectivity
from Classes.Registration import Register
from Utility import DataStructures

''' this method is used to fetch the username,mobile number and security question  of the user from the database to retrieve password'''
def get_password_verification_details():
    try:
        con=DB_connectivity.create_connection()
        cur=DB_connectivity.create_cursor(con)
        list_of_credentials=[]
        cur.execute("select user_name,mobile_number,security_question from owner")
        for user in cur:
          
            owner=Register()
            owner.set_user_name(user[0])
            owner.set_mobile_number(user[1])
            owner.set_security_question(user[2])
            list_of_credentials.append(owner)
       
        return list_of_credentials
        
    finally:
        cur.close()
        con.close()
