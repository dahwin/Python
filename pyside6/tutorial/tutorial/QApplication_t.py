from PySide6.QtWidgets import QApplication,QWidget
import sys
app = QApplication(sys.argv)
window = QWidget()
# Set the background color to dark black
window.setStyleSheet("background-color: rgb(0, 0, 0)")
window.show()
app.exec()


