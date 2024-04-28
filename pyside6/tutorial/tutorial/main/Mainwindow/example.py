from PySide6.QtWidgets import QMainWindow, QPushButton, QHBoxLayout, QApplication, QWidget, QSizePolicy,QVBoxLayout
import sys
from PySide6.QtGui import QPalette, QColor
class DWidgets(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("D Widgets")

        # Create buttons
        button1 = QPushButton("Button 1")
        button1.clicked.connect(self.button_click_1)
        button2 = QPushButton("Button 2")
        button2.clicked.connect(self.button_click_2)

        # Set size hint for buttons
        button1.setFixedSize(70, 30)
        button2.setFixedSize(70, 30)

        # Create a central widget to hold the buttons
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Create a horizontal layout
        button_layout = QHBoxLayout(central_widget)

        # Add buttons to the layout
        button_layout.addWidget(button1)
        button_layout.addWidget(button2)
        # Set a minimum size for the main window
        self.setMinimumSize(800, 450)

        # Set the background color of the main window to black
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(255,255,255))
        self.setPalette(palette)

    def button_click_1(self):
        print("Button clicked 1")

    def button_click_2(self):
        print("Button clicked 2")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DWidgets()
    window.show()
    sys.exit(app.exec())
