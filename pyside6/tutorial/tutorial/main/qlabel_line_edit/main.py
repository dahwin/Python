from PySide6.QtWidgets import QApplication
import sys
from wegets import Widgets
app = QApplication(sys.argv)

widget = Widgets()
widget.show()

app.exec()