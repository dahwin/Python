from PySide6.QtWidgets import QWidget,QPushButton,QHBoxLayout,QVBoxLayout

class DWidgets(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(" D Wedgets")
        button1 = QPushButton("button1")
        button1.clicked.connect(self.button_click_1)
        button2 = QPushButton("button2")
        button2.clicked.connect(self.button_click_2)
        button_layout = QHBoxLayout(self)
        button_layout.addWidget(button1)
        button_layout.addWidget(button2)

    def button_click_1(self):
        print("button clicked 1")
    def button_click_2(self):
        print("button clicked 2")
