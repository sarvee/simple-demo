from Utility import DB_connectivity
from Classes.Registration import Register
from Classes.Feed import Status

''' this method is used to insert the entered  status into the database'''

def setStatus(username,status):
    try:
        con=DB_connectivity.create_connection()
        cur=DB_connectivity.create_cursor(con)
        cur.execute("select count(*) from status")
        for row in cur:
            value=row[0]
        s=Status(username,status)
        s.set_statusid(value+1)
        id=s.get_statusid()
        s.get_status()
        
        l1=[id,status,username]
        cur.execute("insert into status(status_id,status_update,user_name) values(:1,:2,:3)",{":1":id,":2":status,":3":username})
    finally:
        cur.close()
        con.commit()
        con.close()
    