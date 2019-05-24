#-*- coding:utf-8 -*-
import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.Qt import center

class setting(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        self.height = self.screenRect.height()
        self.width = self.screenRect.width()
        self.setGeometry((self.width/2)-200, (self.height/2)-125, 400, 250)
        self.setFixedSize(400,250)
        self.setWindowIcon(QIcon('images/icon_qq.png'))
        self.setWindowTitle('设置')
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
        self.search=QLineEdit(self.tab1)
        self.search.resize(200,20)
        self.search.move(20,0)
        self.search.setPlaceholderText("输入Qchat号搜索好友")
        op = QtWidgets.QGraphicsOpacityEffect()  
        op.setOpacity(0.5)  
        self.search.setGraphicsEffect(op)  
        self.search.setAutoFillBackground(True)
        self.search.setStyleSheet("background:url(images/icon_search.png) no-repeat #FFFFFF;border-radius:5px;border-style:none;")
        self.search.setTextMargins(20,0,0,0)
        self.findButton=QPushButton(self.tab1)
        self.findButton.resize(50,20)
        self.findButton.move(250,0)
        self.findButton.setText("查找")
        self.findButton.setStyleSheet("border-style:none;border:1px solid #0099FF;background:#0099FF;border-radius:5px;color:white;")
        #结果列表
        j=0
        len=0
        self.tab1.list=[]
        self.tab1.niCheng=[]
        while(len<10):
            self.tab1.list.append(QPushButton(self.tab1))
            self.tab1.niCheng.append("昵称")
            len=len+1
        for i in self.tab1.list:
            i.resize(self.width,60)
            i.move(0,(60*j)+20)
            circle=QLabel(i)
            circle.resize(40,40)
            circle.move(20,10)
            circle.setStyleSheet("border:1px solid #888888;border-radius:15px;border-image:url(../images/picture.jpg)")
            name=QLabel(i)
            name.setText(self.tab1.niCheng[j])
            name.resize(100,30)
            name.move(80,5)
            name.setStyleSheet("font-weight:bold;font-size:15px;background:#CCFFFF;")
            i.setStyleSheet("QPushButton{border-style:none;}QPushButton::hover{background:#EEEEEE}")
            addButton=QPushButton(i)
            addButton.resize(65,25)
            addButton.move(300,12)
            addButton.setText("发出申请")
            addButton.setStyleSheet("border-style:none;border:1px solid #0099FF;background:#0099FF;border-radius:5px;color:white;")
            j=j+1
    def tab2UI(self):
        self.tab2.resize(self.width,self.height-30)
        self.tab2.move(0,130)
        self.search=QLineEdit(self.tab2)
        self.search.resize(200,20)
        self.search.move(20,0)
        self.search.setPlaceholderText("输入群号搜索群")
        op = QtWidgets.QGraphicsOpacityEffect()  
        op.setOpacity(0.5)  
        self.search.setGraphicsEffect(op)  
        self.search.setAutoFillBackground(True)
        self.search.setStyleSheet("background:url(images/icon_search.png) no-repeat #FFFFFF;border-radius:5px;border-style:none;")
        self.search.setTextMargins(20,0,0,0)
        self.findButton=QPushButton(self.tab2)
        self.findButton.resize(50,20)
        self.findButton.move(250,0)
        self.findButton.setText("查找")
        self.findButton.setStyleSheet("border-style:none;border:1px solid #0099FF;background:#0099FF;border-radius:5px;color:white;")
if __name__=="__main__":
    app=QApplication(sys.argv)
    myshow=setting()
    myshow.show()
    sys.exit(app.exec_())