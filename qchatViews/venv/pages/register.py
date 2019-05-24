#-*- coding:utf-8 -*-
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from idlelib import autocomplete_w
import sys
sys.path.append('D:/pycharmpackages/qchatViews/venv')
import login2
import Utils.logAndReg.enroll
class register(QWidget):
    def __init__(self):       
        super(register,self).__init__()
        self.initUi()

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
        self.pic=QPixmap('../images/picture.jpg')
        self.touXiang=QLabel(self)
        self.touXiang.setPixmap(self.pic)
        self.touXiang.setScaledContents(True)
        self.touXiang.resize(50,50)
        self.touXiang.setStyleSheet('border:2px solid #AAAAAA;')
        self.touXiang.move(175,75)
        
        #表单输入区域
        #用户名
        self.lb1 = QLabel(self)
        self.lb1.resize(50, 20)
        self.lb1.setText("用户名：")
        self.lb1.setScaledContents(True)
        self.lb1.move(100,130)
        self.text1=QLineEdit(self)
        self.text1.resize(120,20)
        self.text1.setStyleSheet("border-style:none;border-radius:5px;font-family: 'Comic Sans MS';text-indent:5px;")
        self.text1.move(155,130)
        
        
        #密码
        self.label2 = QLabel(self)
        self.label2.resize(50,20)
        self.label2.setText("  密码：")
        self.label2.setScaledContents(True)
        self.label2.move(100,155)
        self.text2=QLineEdit(self)
        self.text2.resize(120,20)
        self.text2.setStyleSheet("border-style:none;border-radius:5px;font-family: 'Comic Sans MS';text-indent:5px;")
        self.text2.move(155,155)
        
        #记住密码等按钮
        

        #登录按钮
        self.Button=QPushButton(self)
        self.Button.resize(200,30)
        self.Button.setText("注  册")
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
        ret=Utils.logAndReg.enroll.enroll(a,b)
        if(ret=="false"):
            self.text1.setStyleSheet('border:2px solid red')
            self.text2.setStyleSheet('border:2px solid red')
            self.Button.setText(" 注 册  失 败")
        else:
            self.Button.setText(" 注 册 成 功")
            self.timer.start(2000) 
    def closeMain(self):
        self.close()
        print("结束了哦~开始跳转页面喽")
        self.next= login2.InputDialog()
        self.timer.stop()
          


if __name__=="__main__":
    import sys
    app=QApplication(sys.argv)
    myshow=register()
    myshow.show()
    sys.exit(app.exec_())