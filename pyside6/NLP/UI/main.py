from PySide6.QtWidgets import QApplication, QDialog
from dahyun import Ui_Dialog
from PySide6.QtCore import Qt

class MyDialog(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

class CustomDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.Window | Qt.WindowTitleHint | Qt.WindowMinimizeButtonHint | Qt.WindowMaximizeButtonHint)

    def closeEvent(self, event):
        # Handle the window close event here
        # You can add custom actions or simply call the parent closeEvent
        event.accept()

if __name__ == "__main__":
    app = QApplication([])
    window = CustomDialog()
    window.show()
    app.exec()
