from PySide6.QtWidgets import QWidget, QPushButton,QVBoxLayout,QMessageBox
class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("dahyun window")

        button = QPushButton("click")
        button.clicked.connect(self.button_clicked)
        button.pressed.connect(self.button_pressed)
        button.released.connect(self.button_released)
        # Set a fixed size for the button
        button.setFixedSize(100, 30)

        layout = QVBoxLayout(self)
        layout.addWidget(button)


    def button_clicked(self):
        print("clicked")

    def button_pressed(self):
        print("pressed")

    def button_released(self):
        print("released")
    