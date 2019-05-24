import npqchat


def createnewgroup(userid):
    print(userid)
    sendmessage="createnewgroup<::>"
    sendmessage+=userid
    groupname=input("input your new group's name:")
    sendmessage+="<::>"
    sendmessage+=groupname
    
    s=npqchat.sendmessages(sendmessage)
    
    
    m=s.recv(1024)
    
    if(m.decode('utf-8')=="success"):
        print("success")
    else:
        print("false")
    #print(m.decode('utf-8'))
    s.close()

def addgroupfirst(userid):
    groupid=input("input groupid that you want to add")
    sendmessage="addgroupfirst<::>"
    sendmessage+=userid
    sendmessage+="<::>"
    sendmessage+=groupid
    
    s=npqchat.sendmessages(sendmessage)
    
    m=s.recv(1024)
    
    if(m.decode('utf-8')=="success"):
        print("success")
    elif(m.decode('utf-8')=="havebeenin"):
        print("havebeenin")
    else:
        print("not found")
    #print(m.decode('utf-8'))
    s.close()
    return groupid,m.decode('utf-8')

def addgroup(userid,elsemessage,addgroupid):
    message="addgroup<::>"
    message+=userid
    message+="<::>"
    message+=addgroupid
    #message+="<::>"
    message+="<::>"
    message+=elsemessage
    s=npqchat.sendmessages(message)
    m=s.recv(1024)
    print(m.decode('utf-8'))
    s.close()