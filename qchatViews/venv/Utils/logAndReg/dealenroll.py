# -*- coding: utf-8 -*-
import socket
import getid
import pymysql
import enrollfunction
import staticnumber
import deallogin

# 创建 socket 对象
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 9999
serversocket.bind((host, port))

# 设置最大连接数，超过后排队
serversocket.listen(5)

while True:
    # 建立客户端连接
    clientsocket,addr = serversocket.accept()   
    msg = clientsocket.recv(1024)
    
    print(msg.decode('utf-8'))
    
    db = pymysql.connect("localhost","root",staticnumber.mysqlpassword,"qchat" )
    cursor = db.cursor()
    msg=msg.decode('utf-8')
    #print(msg)
    msg=msg.split("<::>")
    if(msg[0]=="enroll"):
        enrollfunction.enrollmessage(msg,clientsocket)
    elif(msg[0]=="login"):
        deallogin.deallogin(msg,clientsocket)
        
        