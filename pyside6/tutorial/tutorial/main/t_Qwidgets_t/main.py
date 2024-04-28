from PySide6.QtWidgets import QApplication,QWidget
import sys
from dwidgets import DWidgets
app = QApplication(sys.argv)
window = DWidgets()

window.show()
app.exec()
