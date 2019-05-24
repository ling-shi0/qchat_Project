#-*- coding:utf-8 -*-
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from idlelib import autocomplete_w
from _ctypes import resize
from pages.box import Example 
import Utils.logAndReg.login
class InputDialog(QWidget):
    def __init__(self):       
        super(InputDialog,self).__init__()
        self.initUi()
        self.show()

    def initUi(self):
        #主窗口大小和位置及标题栏设置
        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        self.height = self.screenRect.height()
        self.width = self.screenRect.width()
        self.setGeometry((self.width/2)-200, (self.height/2)-125, 400, 250)
        self.setFixedSize(400,250)
        self.setWindowTitle('Qchat')
        self.setWindowIcon(QIcon('../images/icon_qq.png'))
        self.setStyleSheet("border-style:none;border-radius:5px;")
        
        #界面第一部分头像栏
        #底色
        self.label1=QLabel(self)
        self.label1.setStyleSheet("background: #3299cc")
        self.label1.resize(400,100)
        self.label1.move(0,0)
        #欢迎语句
        self.welcome=QLabel(self)
        self.welcome.setText(" w e l c o m e ")
        self.welcome.setScaledContents(True)
        self.welcome.setStyleSheet('font-size:30px;font-family: "Comic Sans MS";color: #32cd32;text-shadow: 0 0 20px #fdec84, 10px -10px 30px #ffae35,20px -20px 40px #ec760c, -20px -60px 50px #cd4607,0px -80px 60px #973717, 10px -40px 70px #451b0e;margin-left:25px;')
        self.welcome.resize(250,50)
        self.welcome.move(75,25)
        #头像框
        self.touXiang=QLabel(self)
        self.touXiang.resize(50,50)
        self.touXiang.setStyleSheet('border:1px solid #000000;border-image:url("../images/picture.jpg"); border-radius:25px;')
        self.touXiang.move(175,75)
        
        #表单输入区域
        #用户名
        self.pix = QPixmap('../images/icon_qq.png')
        self.pix2 = QPixmap('../images/password.png')
        self.lb1 = QLabel(self)
        self.lb1.setPixmap(self.pix)
        self.lb1.resize(20, 20)
        self.lb1.setScaledContents(True)
        self.lb1.move(120,130)
        self.text1=QLineEdit(self)
        self.text1.resize(120,20)
        self.text1.setStyleSheet("border-style:none;border-radius:5px;font-family: 'Comic Sans MS';")
        self.text1.move(155,130)
        self.text1.textChanged.connect(self.textClick)
        
        #密码
        self.label2 = QLabel(self)
        self.label2.setPixmap(self.pix2)
        self.label2.resize(20,20)
        self.label2.setScaledContents(True)
        self.label2.move(120,155)
        self.text2=QLineEdit(self)
        self.text2.resize(120,20)
        self.text2.setStyleSheet("border-style:none;border-radius:5px;font-family: 'Comic Sans MS';")
        self.text2.move(155,155)
        self.text2.textChanged.connect(self.textClick)
        
        #记住密码等按钮
        self.cb = QCheckBox(self)
        self.cb.resize(20,18)
        self.cb.move(105, 180)
        self.cb.setStyleSheet("border-radius:5px;")
        self.tip=QLabel(self)
        self.tip.setText("记住密码")
        self.tip.setStyleSheet("font-family: 'Comic Sans MS';color:#999999;")
        self.tip.resize(50,25)
        self.tip.move(125,175)
        self.forget=QLabel(self)
        self.forget.setText("忘记密码")
        self.forget.resize(50,25)
        self.forget.move(225,175)
        self.forget.setStyleSheet("color:#999999;")

        #登录按钮
        self.Button=QPushButton(self)
        self.Button.resize(200,30)
        self.Button.setText("登   录")
        self.Button.setStyleSheet("background: #3299cc;border-style:none;border-radius:5px;")
        self.Button.move(100,205)
        self.Button.clicked.connect(self.loginZhangHu)


        #延迟器关闭
        self.timer = QTimer(self) #初始化一个定时器
        self.timer.timeout.connect(self.closeMain) #计时结束调用operate()方法
        
        
        

    #登录验证函数
    def loginZhangHu(self):
        a=self.text1.text()
        b=self.text2.text()
        ret=Utils.logAndReg.login.login(a,b)
        if(ret=="success"):
            self.text1.setStyleSheet('border:2px solid green')
            self.text2.setStyleSheet('border:2px solid green')
            self.Button.setText("登 录 成 功")
            self.timer.start(1000)
        else:
            self.text1.setStyleSheet('border:2px solid red')
            self.text2.setStyleSheet('border:2px solid red')
            self.Button.setText("登 录  失 败")
    def closeMain(self):
        self.close()
        print("结束了哦~跳转开始跳转页面喽")
        self.next=Example()       
        self.timer.stop()
    def textClick(self):
        self.Button.setText("登   录")

if __name__=="__main__":
    import sys
    app=QApplication(sys.argv)
    myshow=InputDialog()
    myshow.show()
    sys.exit(app.exec_())
