from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget,  QLabel, QHBoxLayout, QVBoxLayout, QPushButton

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dahwin vision")

        image_label = QLabel()

        image_label.setPixmap(QPixmap(r"c:\Users\ALL USER\Desktop\e\images\fonts\4mp_FILL0_wght400_GRAD0_opsz48.png"))

        layout = QVBoxLayout()
        layout.addWidget(image_label)

        self.setLayout(layout)