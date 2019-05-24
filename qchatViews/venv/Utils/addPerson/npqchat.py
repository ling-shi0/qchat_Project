import socket
import sys
sys.path.append('D:/pycharmpackages/qchatViews/venv')
from Utils.addPerson import staticnumber
def sendmessages(sendinformation):
    #='nsajdn'
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #print("2")
    host = staticnumber.host
    #host="118.24.68.245"
    print(host)
    port=9999
    print((host,port))
    s.connect((host,port))
    print(s)
    s.send(sendinformation.encode('utf-8'))
    print(sendinformation)
    return s

def main():
    sendmessages()


if __name__ == '__main__':
    main()