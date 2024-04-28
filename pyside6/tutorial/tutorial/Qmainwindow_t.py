# from PySide6.QtWidgets import QApplication,QMainWindow,QPushButton
# import sys
# app = QApplication(sys.argv)
# window = QMainWindow()

# window.setWindowTitle("QueenDahyun")
# buttton = QPushButton()
# buttton.setText("Dubu")

# window.setCentralWidget(buttton)
# window.show()
# app.exec()


from typing import Optional
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication,QMainWindow,QPushButton, QWidget
import sys

class ButtonHolder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QueenDahyun")
        buttton = QPushButton("Dubu")
        self.setCentralWidget(buttton)

        
app = QApplication(sys.argv)
window = ButtonHolder()
window.show()
app.exec()