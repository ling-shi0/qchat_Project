# -*- coding: utf-8 -*-
import enroll
import login

flag=0
while True:
    flag=input("1:login\n2:enroll\n")
    print(flag)
    if(flag=="1"):
        login.login()
    elif(flag=="2"):
        enroll.enroll()
    else:
        print("welcome next use")