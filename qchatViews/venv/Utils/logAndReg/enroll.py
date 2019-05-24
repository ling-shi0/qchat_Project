# -*- coding: utf-8 -*-
import socket

def enroll(nickname,pwd):
    sendinformation="enroll"+"<::>"+nickname+"<::>"+pwd
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     
    #host = socket.gethostname()
    host="118.24.68.245"
    port = 9999
    s.connect((host, port))
    
    s.send(sendinformation.encode('utf-8'))
    m=s.recv(1024)
    #print("注册成功，您的id为：",end="")
    #print(m.decode('utf-8'))
    if(m=="false"):
        return "fail"
    else:
        return m.decode('utf-8')
    s.close()

def main():
    enroll()


if __name__ == '__main__':
    main()