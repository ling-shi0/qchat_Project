#-*- coding:utf-8 -*-
import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.Qt import center
from PyQt5.QtCore import QTimer

import sys
sys.path.append('D:/pycharmpackages/qchatViews/venv')
from Utils.addPerson.addfriends import addfriends
class addTheOne(QWidget):

    def __init__(self,id,friendid):
        super().__init__()
        self.initUI()
        self.id=id
        self.addfriendid=friendid
    def initUI(self):
        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        self.height = self.screenRect.height()
        self.width = self.screenRect.width()
        self.setGeometry((self.width/2)-200, (self.height/2)-100, 400, 200)
        self.setFixedSize(400, 200)
        self.setWindowIcon(QIcon('images/icon_qq.png'))
        self.setWindowTitle('添加好友')
        self.setStyleSheet("background:#CCFFFF;")
        self.UI()
        self.show()
    
    def UI(self):
        self.Text=QTextEdit(self)
        self.Text.resize(350,100)
        self.Text.move(25,20)
        self.Text.setPlaceholderText("请输入申请信息")
        self.Text.setStyleSheet("border-radius:5px;border:1px solid #000000;")
        self.button=QPushButton(self)
        self.button.setText("发送请求")
        self.button.resize(60,30)
        self.button.move(230,150)
        self.button.setStyleSheet("border-style:none;border:1px solid #0099FF;background:#0099FF;border-radius:5px;color:white;")
        self.cancel=QPushButton(self)
        self.cancel.setText("取消")
        self.cancel.resize(60,30)
        self.cancel.move(300,150)
        self.cancel.setStyleSheet("border-style:none;border:1px solid #0099FF;background:#0099FF;border-radius:5px;color:white;")
        self.button.clicked.connect(self.send)
        self.cancel.clicked.connect(self.cancelButton)
        #延迟器关闭
        self.timer = QTimer(self) #初始化一个定时器
        self.timer.timeout.connect(self.cancelButton) #计时结束调用operate()方法
    def send(self):   
        tex=self.Text.toPlainText()
        print(tex)
        addfriends(self.id,tex,self.addfriendid)
        self.Text.hide()
        self.label=QLabel(self)
        self.label.setText("申请成功，请等待确认..")
        self.label.resize(200,30)
        self.label.move(125,50)
        self.label.setStyleSheet("font-weight:bold;")
        self.label.show()
        self.timer.start(2000)
    def cancelButton(self):
        self.close()
if __name__=="__main__":
    app=QApplication(sys.argv)
    myshow=addTheOne()
    myshow.show()
    sys.exit(app.exec_())