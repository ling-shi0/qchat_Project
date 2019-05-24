import getid
import socket
import pymysql
import staticnumber

def deallogin(msg,clientsocket):
    userid=msg[1]
    userpwd=msg[2]
    reply=""
    sql = "select * from pwd where userid='%s' and userpwd='%s';" %(userid,userpwd)
    
    print(sql)
    db = pymysql.connect("localhost","root",staticnumber.mysqlpassword,"qchat" )
    cursor = db.cursor()
    try:
        
        cursor.execute(sql)
        results=cursor.fetchone()
        if(results==None):
            reply="false"
        else:
            reply="success"
        db.commit()
    except:
        print ("Error: unable to fetch data")
    db.close()
    clientsocket.send(reply.encode('utf-8'))
    #print(clientsocket.getpeername()[0] )
    clientsocket.close()




def main():
    deallogin()


if __name__ == '__main__':
    main()