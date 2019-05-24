from PyQt5 import QtCore, QtGui, QtWidgets
import sys

if __name__ == "__main__": import sys
app = QtWidgets.QApplication(sys.argv)
widget = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(widget)
widget.show()
sys.exit(app.exec_())
