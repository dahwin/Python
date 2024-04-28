from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QSpacerItem, QSizePolicy

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        button1 = QPushButton('Button 1')
        button2 = QPushButton('Button 2')

        # Create a horizontal spacer
        spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        layout.addWidget(button1)
        layout.addItem(spacer)
        layout.addWidget(button2)

        self.setLayout(layout)

app = QApplication([])
window = MyWidget()
window.show()
app.exec()
