import socket

import sys
sys.path.append('D:/pycharmpackages/qchatViews/venv')
from Utils.addPerson import npqchat,staticnumber

def addfriends(userid,elsemessage,addfriendid):
    #addfriendid=input("input your add friend's id")
    message="addfriends<::>"
    message+=userid
    message+="<::>"
    message+=addfriendid
    #message+="<::>"
    message+="<::>"
    message+=elsemessage
    s=npqchat.sendmessages(message)
    m=s.recv(1024)
    print(m.decode('utf-8'))
    s.close()

def addfriendsfirst(userid,addfriendid):
    #addfriendid=input("input your add friend's id")
    message="addfriendsfirst<::>"
    message+=userid
    message+="<::>"
    message+=addfriendid
    print(message)
    
    s=npqchat.sendmessages(message)
    
    m=s.recv(1024)
    print(m.decode('utf-8'))
    
    s.close()
    m=m.decode('utf-8').split("<::>")
    return addfriendid,m[1],m[0]

def main():
    addfriends()


if __name__ == '__main__':
    main()