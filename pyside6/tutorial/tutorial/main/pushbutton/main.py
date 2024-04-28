from PySide6.QtWidgets import QApplication
import sys
from wegets import Widget

app = QApplication(sys.argv)
widget = Widget()
widget.show()

app.exec()