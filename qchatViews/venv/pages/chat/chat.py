#-*- coding:utf-8 -*-
import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.Qt import center

class chats(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        self.height = self.screenRect.height()
        self.width = self.screenRect.width()
        self.setGeometry((self.width/2)-400, (self.height/2)-250, 800, 500)
        self.setFixedSize(800, 500)
        self.setWindowIcon(QIcon('images/icon_qq.png'))
        self.setWindowTitle('昵称')
        self.setStyleSheet("background:#CCFFFF;")
        #self.UI()
        self.show()
    
    #def UI(self):
        #self.Text=QTextBlock(self)
        
    
       
    
if __name__=="__main__":
    app=QApplication(sys.argv)
    myshow=chats()
    myshow.show()
    sys.exit(app.exec_())