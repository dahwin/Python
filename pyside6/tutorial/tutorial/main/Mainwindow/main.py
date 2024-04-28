from PySide6.QtWidgets import QApplication,QWidget
import sys
from mainwindowqt import MainWindow
app = QApplication(sys.argv)
window =MainWindow(app)

window.show()
app.exec()
