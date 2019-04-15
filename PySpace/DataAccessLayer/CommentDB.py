from Utility import DB_connectivity
from Classes.Registration import Register
from Classes.Password import Password

'''this method add comments into the database'''
def comment(sid,username):
    try:
        con=DB_connectivity.create_connection()
        cur=DB_connectivity.create_cursor(con)
        comment_text=input("Comment:")
        cur.execute("insert into comments(status_id,coment,user_name) values(:sid,:comment1,:username)",{"sid":sid,"comment1":comment_text,"username":username})
    finally:
        cur.close()
        con.commit()
        con.close()