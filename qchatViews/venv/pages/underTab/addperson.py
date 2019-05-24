#-*- coding:utf-8 -*-
import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.Qt import center

import sys
sys.path.append('D:/pycharmpackages/qchatViews/venv')
from pages.underTab.addTheOne import addTheOne
from pages.underTab.addTheGroup import addTheGroup
from Utils.addPerson.addfriends import addfriends,addfriendsfirst

class addPerson(QWidget):

    def __init__(self,id):
        super().__init__()
        self.initUI()
        self.id=id

    def initUI(self):
        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        self.height = self.screenRect.height()
        self.width = self.screenRect.width()
        self.setGeometry((self.width/2)-200, (self.height/2)-125, 400, 250)
        self.setFixedSize(400,250)
        self.setWindowIcon(QIcon('images/icon_qq.png'))
        self.setWindowTitle('加好友')
        self.setStyleSheet("background:#CCFFFF;")
        self.UI()
        self.show()
    
    def UI(self):
        self.tab = QtWidgets.QTabWidget (self)
        self.tab1=QWidget()
        self.tab2=QWidget()
        self.tab1UI()
        self.tab2UI()
        self.tab.addTab (self.tab1, "加好友")
        self.tab.addTab (self.tab2, "加群")
        self.tab.setCurrentIndex (0)
        self.tab.resize(self.width,440)
        self.tab.move(0,0)
        self.tab.setStyleSheet("QTabBar::tab{width:100px;border-style:none;color:blue;height:30px;}QTabBar::tab:selected{border-bottom:1px solid blue;}")       
    def tab1UI(self):
        self.tab1.resize(self.width,self.height-30)
        self.tab1.move(0,0)
        #搜索框
        self.searchFriend=QLineEdit(self.tab1)
        self.searchFriend.resize(200,20)
        self.searchFriend.move(20,0)
        self.searchFriend.setPlaceholderText("输入Qchat号搜索好友")
        op = QtWidgets.QGraphicsOpacityEffect()  
        op.setOpacity(0.5)  
        self.searchFriend.setGraphicsEffect(op)  
        self.searchFriend.setAutoFillBackground(True)
        self.searchFriend.setStyleSheet("background:url(images/icon_search.png) no-repeat #FFFFFF;border-radius:5px;border-style:none;")
        self.searchFriend.setTextMargins(20,0,0,0)
        self.findFriendButton=QPushButton(self.tab1)
        self.findFriendButton.resize(50,20)
        self.findFriendButton.move(250,0)
        self.findFriendButton.setText("查找")
        self.findFriendButton.setStyleSheet("border-style:none;border:1px solid #0099FF;background:#0099FF;border-radius:5px;color:white;")
        self.findFriendButton.clicked.connect(self.findPerson)
    def tab2UI(self):
        self.tab2.resize(self.width,self.height-30)
        self.tab2.move(0,130)
        self.searchGroup=QLineEdit(self.tab2)
        self.searchGroup.resize(200,20)
        self.searchGroup.move(20,0)
        self.searchGroup.setPlaceholderText("输入群号搜索群")
        op = QtWidgets.QGraphicsOpacityEffect()  
        op.setOpacity(0.5)  
        self.searchGroup.setGraphicsEffect(op)  
        self.searchGroup.setAutoFillBackground(True)
        self.searchGroup.setStyleSheet("background:url(images/icon_search.png) no-repeat #FFFFFF;border-radius:5px;border-style:none;")
        self.searchGroup.setTextMargins(20,0,0,0)
        self.findGroupButton=QPushButton(self.tab2)
        self.findGroupButton.resize(50,20)
        self.findGroupButton.move(250,0)
        self.findGroupButton.setText("查找")
        self.findGroupButton.setStyleSheet("border-style:none;border:1px solid #0099FF;background:#0099FF;border-radius:5px;color:white;")
        self.findGroupButton.clicked.connect(self.findGroup)
    def findPerson(self):
        a=self.searchFriend.text()
        self.addfriendid,nickName,returnmessage=addfriendsfirst(self.id,a)
        #addfriends.addfriend(a,"")
        #执行个函数并返回个结果 util.find()
        if(nickName!=""):
            self.persons=[nickName]
            self.j1=0
            self.lens=0
            self.list=[]
            self.findFriendResult=[]
            if(len(self.persons)!=0):
                self.findFriendResult=self.persons
                self.niCheng1=[]
                self.size1=len(self.findFriendResult)
                while(self.lens<self.size1):
                    self.list.append(QPushButton(self.tab1))
                    self.niCheng1.append(self.findFriendResult[self.lens])
                    self.lens=self.lens+1
                for i in self.list:
                    i.resize(self.width,60)
                    i.move(0,(60*self.j1)+20)
                    self.circle1=QLabel(i)
                    self.circle1.resize(40,40)
                    self.circle1.move(20,10)
                    self.circle1.setStyleSheet("border:1px solid #888888;border-radius:15px;border-image:url(../images/picture.jpg)")
                    self.name1=QLabel(i)
                    self.name1.setText(self.niCheng1[self.j1])
                    self.name1.resize(100,30)
                    self.name1.move(80,5)
                    self.name1.setStyleSheet("font-weight:bold;font-size:15px;background:#CCFFFF;")
                    i.setStyleSheet("QPushButton{border-style:none;}QPushButton::hover{background:#EEEEEE}")
                    self.addButton1=QPushButton(i)
                    self.addButton1.resize(65,25)
                    self.addButton1.move(300,12)
                    self.addButton1.setText("发出申请")
                    self.addButton1.setStyleSheet("border-style:none;border:1px solid #0099FF;background:#0099FF;border-radius:5px;color:white;")
                    self.addButton1.clicked.connect(self.addThePeople)
                    i.show()
                    self.addButton1.show()
                    self.name1.show()
                    self.circle1.show()
                    self.j1=self.j1+1
        else:
            self.res1=QLabel(self.tab1)
            self.res1.resize(200,30)
            self.res1.move(120,50)
            self.res1.setText("没有找到该用户~~")
            self.res1.setStyleSheet("font-weight:bold;font-size:15px;")  
            self.res1.show()
    def findGroup(self):
        #执行个函数并返回个结果 util.find()
        self.groups=["sdf","dsf"]
        self.j2=0
        self.lens2=0
        self.list2=[]
        self.findGroupResult=[]
        if(len(self.groups)!=0):
            self.findGroupResult=self.groups
            self.qunName=[]
            self.size2=len(self.findGroupResult)
            while(self.lens2<self.size2):
                self.list2.append(QPushButton(self.tab2))
                self.qunName.append(self.findGroupResult[self.lens2])
                self.lens2=self.lens2+1
            for i in self.list2:
                i.resize(self.width,60)
                i.move(0,(60*self.j2)+20)
                self.circle2=QLabel(i)
                self.circle2.resize(40,40)
                self.circle2.move(20,10)
                self.circle2.setStyleSheet("border:1px solid #888888;border-radius:15px;border-image:url(../images/picture.jpg)")
                self.name2=QLabel(i)
                self.name2.setText(self.qunName[self.j2])
                self.name2.resize(100,30)
                self.name2.move(80,5)
                self.name2.setStyleSheet("font-weight:bold;font-size:15px;background:#CCFFFF;")
                i.setStyleSheet("QPushButton{border-style:none;}QPushButton::hover{background:#EEEEEE}")
                self.addButton2=QPushButton(i)
                self.addButton2.resize(65,25)
                self.addButton2.move(300,12)
                self.addButton2.setText("发出申请")
                self.addButton2.setStyleSheet("border-style:none;border:1px solid #0099FF;background:#0099FF;border-radius:5px;color:white;")
                self.addButton2.clicked.connect(self.addTheGroups)
                i.show()
                self.addButton2.show()
                self.name2.show()
                self.circle2.show()
                self.j2=self.j2+1
        else:
            self.res2=QLabel(self.tab2)
            self.res2.resize(200,30)
            self.res2.move(120,50)
            self.res2.setText("没有找到该群~~")
            self.res2.setStyleSheet("font-weight:bold;font-size:15px;")  
            self.res2.show()  
    def addThePeople(self):
        self.next=addTheOne(self.id,self.addfriendid)  
    def addTheGroups(self):
        self.next=addTheGroup()
if __name__=="__main__":
    app=QApplication(sys.argv)
    myshow=addPerson()
    myshow.show()
    sys.exit(app.exec_())