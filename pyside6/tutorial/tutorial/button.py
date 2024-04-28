from typing import Optional
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication,QMainWindow,QPushButton, QWidget
import sys

class ButtonHolder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QueenDahyun")
        buttton = QPushButton("Dubu")
        buttton.setCheckable(True)
        buttton.clicked.connect(self.click_button)
        self.setCentralWidget(buttton)
    def click_button(self,data):
        print("dubu clicked",data)

        
app = QApplication(sys.argv)
window = ButtonHolder()
window.show()
app.exec()