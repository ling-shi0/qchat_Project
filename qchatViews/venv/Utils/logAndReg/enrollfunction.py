import getid
import socket
import pymysql
import staticnumber
def enrollmessage(msg,clientsocket):
    db = pymysql.connect("localhost","root",staticnumber.mysqlpassword,"qchat" )
    cursor = db.cursor()
    idnum=getid.getid()
    sql = "insert into pwd values('%s','%s','%s')" %(idnum,msg[1],msg[2])
    print(sql)
    reply=str(idnum)+ "\r\n"
    clientsocket.send(reply.encode('utf-8'))
    clientsocket.close()
    try:
        cursor.execute(sql)
        db.commit()
    except:
        #print(len(results))
        print ("Error: unable to fetch data")
    db.close()


def main():
    enrollmessage()


if __name__ == '__main__':
    main()