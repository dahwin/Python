'''dahyun+darwin = dahwin'''
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import sys
import csv
class Mywindow(QMainWindow):
    def __init__(self):
        super(Mywindow,self).__init__()
def click():
    print('dawin')


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200,200,1080,1000)
    win.setWindowTitle('dahwin')
    lable = QtWidgets.QLabel(win)
    lable.setText('Dahyun is my soul')
    lable.move(500,0)
    b1 = QtWidgets.QPushButton(win)
    b1.setText('Click')
    b1.clicked.connect(click)
    b1.move(500,60)
    win.show()
    sys.exit(app.exec_())
window()


