from Utility import DB_connectivity
from Classes.Registration import Register

'''this method is used to set the information of signup in the database'''

def set_db(username,password,gender,city,name,surname,relationship_status,mobile_number,security_key):
    try:
        l1=[username,password,name,surname,gender,city,relationship_status,mobile_number,security_key.lower()]
        con=DB_connectivity.create_connection()
        cur=DB_connectivity.create_cursor(con)
        cur.execute("insert into owner values(:1,:2,:3,:4,:5,:6,:7,:8,:9)",l1)
        cur.execute("insert into loginval values(:1,null,null,null)",{':1':username})
        
    finally:
        cur.close()
        con.commit()
        con.close()
        
''' this method is used in editing the profile of the user by updating the value in the database'''
        
def update_db(username,gender,city,name,surname,relationship_status,mobile_number,security_key):
    try:
        l1=[username,name,surname,gender,city,relationship_status,mobile_number,security_key]
        con=DB_connectivity.create_connection()
        cur=DB_connectivity.create_cursor(con)
        cur.execute("UPDATE owner SET first_name=:2,sur_name=:3,gender=:4,city=:5,relationship_status=:6,mobile_number=:7,security_question=:8 WHERE user_name=:1",{':1':l1[0],':2':l1[1],':3':l1[2],':4':l1[3],':5':l1[4],':6':l1[5],':7':l1[6],':8':l1[7]})
    finally:
        cur.close()
        con.commit()
        con.close()
              
