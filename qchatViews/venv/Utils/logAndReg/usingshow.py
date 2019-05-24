import socket

def usingshow():
    myname = socket.getfqdn(socket.gethostname(  ))
    #获取本机ip
    myaddr = socket.gethostbyname(myname)
    print(myaddr)

def main():
    usingshow()


if __name__ == '__main__':
    main()