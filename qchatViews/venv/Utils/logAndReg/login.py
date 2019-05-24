import socket
def login(username,userpwd):
    
    sendinformation="login"+"<::>"+username+"<::>"+userpwd
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     
    #host = socket.gethostname()
    host="118.24.68.245"
    port = 9999
    s.connect((host, port))
    
    s.send(sendinformation.encode('utf-8'))
    #print(sendinformation)
    m=s.recv(1024)
    s.close()
    if(m.decode('utf-8')=="success"):
        return "success"
    else:
        return "False"
    #print(m.decode('utf-8'))
    
    
def main():
    login()


if __name__ == '__main__':
    main()