import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
sys.path.append('D:/pycharmpackages/qchatViews/venv/pages')
from underTab.addperson import addPerson 
from underTab.setting import setting
from chat.chat import chats
class Example(QWidget):

    def __init__(self,id):
        super().__init__()
        self.initUI()
        self.id=id

    def initUI(self):
        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        self.height = self.screenRect.height()
        self.width = self.screenRect.width()
        self.setGeometry(0, 0, 300, (self.height-200))
        self.setFixedSize(300,(self.height-200))
        self.setWindowIcon(QIcon('images/icon_qq.png'))
        self.setWindowTitle('Qchat')
        self.setStyleSheet("background:#CCFFFF;")
        self.UI()
        self.show()
    
    def UI(self):
        #上部头像框等部分
        #头像框
        self.touxiang=QLabel(self)
        self.touxiang.resize(60,60)
        self.touxiang.move(10,10)
        self.touxiang.setStyleSheet("border-image:url(images/picture.jpg);border:1px solid #888888;border-radius:30px;")
        #状态栏
        self.state=QLabel(self)
        self.state.resize(12,12)
        self.state.move(55,55)
        self.state.setStyleSheet("border:1px solid white;background:green;border-radius:6px;")
        #昵称
        self.name=QLabel(self)
        self.name.setText("昵称")
        self.name.resize(100,25)
        self.name.move(80,15)
        self.name.setStyleSheet("font-weight:bold;font-size:20px;font-family: '微软雅黑';")
        #签名
        self.qianMing=QLabel(self)
        self.qianMing.setText("设计签名吧~")
        self.qianMing.resize(100,15)
        self.qianMing.move(80,45)
        #搜索框
        self.search=QLineEdit(self)
        self.search.resize(self.width,20)
        self.search.move(0,80)
        self.search.setPlaceholderText(" 搜索框")
        op = QtWidgets.QGraphicsOpacityEffect()  
        op.setOpacity(0.5)  
        self.search.setGraphicsEffect(op)  
        self.search.setAutoFillBackground(True)
        self.search.setStyleSheet("background:url(images/icon_search.png) no-repeat #FFFFFF;border-radius:5px;border-style:none;")
        self.search.setTextMargins(20,0,0,0)
        #第二部分下半部分聊天功能部分
        self.tab = QtWidgets.QTabWidget (self)
        self.tab1=QWidget()
        self.tab2=QWidget()
        self.tab3=QWidget()
        self.tab1UI()
        self.tab2UI()
        self.tab3UI()
        self.tab.addTab (self.tab1, "好友列表")
        self.tab.addTab (self.tab2, "群聊")
        self.tab.addTab (self.tab3, "消息")
        self.tab.setCurrentIndex (0)
        self.tab.resize(self.width,440)
        self.tab.move(0,100)
        self.tab.setStyleSheet("QTabBar::tab{width:100px;border-style:none;color:blue;height:30px;}QTabBar::tab:selected{border-bottom:1px solid blue;}")       
        #一些菜单底部栏
        self.underTab=QLabel(self)
        self.underTab.resize(self.width,35)
        self.underTab.move(0,535)
        self.underTab.setStyleSheet("background:#DDFFFF;border-top:1px solid #AAAAAA;")
        addPersonLabel=QPushButton(self.underTab)
        addPersonLabel.resize(16,16)
        addPersonLabel.move(10,10)
        addPersonLabel.setObjectName("add")
        addPersonLabel.setStyleSheet("#add{border-top:none;border-image:url(images/icon_addperson.png);height:35px;}#add:hover{background:#EEEEEE;color:blue;}")
        QToolTip.setFont(QFont("SansSerif", 10))
        addPersonLabel.setToolTip("加好友")
        addPersonLabel.clicked.connect(self.addPerson)
        settingButton=QPushButton(self.underTab)
        settingButton.resize(16,16)
        settingButton.move(32,10)
        settingButton.setObjectName("setting")
        settingButton.setStyleSheet("#setting{border-top:none;border-image:url(images/icon_setting.png);height:35px;}#setting:hover{background:#EEEEEE;color:blue;}")
        settingButton.setToolTip("设置")
        settingButton.clicked.connect(self.settingFunction)
    def tab1UI(self):
        j=0
        len=0
        #好友列表界面
        self.tab1.resize(self.width,self.height-30)
        self.tab1.move(0,130)
        self.tab1.setMinimumSize(250, 2000)
        self.tab1.list=[]
        self.tab1.niCheng=[]
        self.tab1.times=[]
        while(len<10):
            self.tab1.list.append(QPushButton(self.tab1))
            self.tab1.niCheng.append("昵称")
            self.tab1.times.append("8:00")
            len=len+1
        for i in self.tab1.list:
            i.resize(self.width,60)
            i.move(0,60*j)
            circle=QLabel(i)
            circle.resize(40,40)
            circle.move(20,10)
            circle.setStyleSheet("border:1px solid #888888;border-radius:15px;border-image:url(images/picture.jpg)")
            name=QLabel(i)
            name.setText(self.tab1.niCheng[j])
            name.resize(100,30)
            name.move(80,5)
            name.setStyleSheet("font-weight:bold;font-size:15px;background:#CCFFFF;")
            time=QLabel(i)
            time.setText(self.tab1.times[j])
            time.resize(40,20)
            time.move(250,15)
            time.setStyleSheet("color:#BBBBBB;")
            i.setStyleSheet("QPushButton{border-style:none;}QPushButton::hover{background:#EEEEEE}")
            i.clicked.connect(self.haveAChat)
            j=j+1
    def tab2UI(self):
        j=0
        len=0
        #群聊列表界面
        self.tab2.resize(self.width,self.height-30)
        self.tab2.move(0,130)
        self.tab2.setMinimumSize(250, 2000)
        self.tab2.list=[]
        self.tab2.niCheng=[]
        self.tab2.times=[]
        while(len<10):
            self.tab2.list.append(QPushButton(self.tab2))
            self.tab2.niCheng.append("群昵称")
            self.tab2.times.append("8:00")
            len=len+1
        for i in self.tab2.list:
            i.resize(self.width,60)
            i.move(0,60*j)
            circle=QLabel(i)
            circle.resize(40,40)
            circle.move(20,10)
            circle.setStyleSheet("border:1px solid #888888;border-radius:15px;border-image:url(images/picture.jpg)")
            name=QLabel(i)
            name.setText(self.tab2.niCheng[j])
            name.resize(100,30)
            name.move(80,5)
            name.setStyleSheet("font-weight:bold;font-size:15px;background:#CCFFFF;")
            time=QLabel(i)
            time.setText(self.tab2.times[j])
            time.resize(40,20)
            time.move(250,15)
            time.setStyleSheet("color:#BBBBBB;")
            i.setStyleSheet("QPushButton{border-style:none;}QPushButton::hover{background:#EEEEEE}")
            j=j+1
    def tab3UI(self):
        j=0
        len=0
        #消息列表界面
        self.tab3.resize(self.width,self.height-30)
        self.tab3.move(0,130)
        self.tab3.setMinimumSize(250, 2000)
        self.tab3.list=[]
        self.tab3.niCheng=[]
        self.tab3.times=[]
        while(len<5):
            self.tab3.list.append(QPushButton(self.tab3))
            self.tab3.niCheng.append("群昵称")
            self.tab3.times.append("8:00")
            len=len+1
        for i in self.tab3.list:
            i.resize(self.width,60)
            i.move(0,60*j)
            circle=QLabel(i)
            circle.resize(40,40)
            circle.move(20,10)
            circle.setStyleSheet("border:1px solid #888888;border-radius:15px;border-image:url(images/picture.jpg)")
            name=QLabel(i)
            name.setText(self.tab3.niCheng[j])
            name.resize(100,30)
            name.move(80,5)
            name.setStyleSheet("font-weight:bold;font-size:15px;background:#CCFFFF;")
            time=QLabel(i)
            time.setText(self.tab3.times[j])
            time.resize(40,20)
            time.move(250,15)
            time.setStyleSheet("color:#BBBBBB;")
            i.setStyleSheet("QPushButton{border-style:none;}QPushButton::hover{background:#EEEEEE}")
            j=j+1
    def addPerson(self):
        self.next=addPerson(self.id)
    def settingFunction(self):
        self.next=setting()
    def haveAChat(self):
        self.next=chats()
if __name__=="__main__":
    app=QApplication(sys.argv)
    myshow=Example()
    myshow.show()
    sys.exit(app.exec_())