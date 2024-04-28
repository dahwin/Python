from typing import Optional
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QSlider, QVBoxLayout, QWidget
import sys

class SliderHolder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QueenDahyun")

        # Create a central widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Create a vertical layout for the central widget
        layout = QVBoxLayout(central_widget)

        # Create the slider
        slider = QSlider(Qt.Horizontal)
        slider.setMinimum(1)
        slider.setMaximum(100)
        slider.setValue(25)

        # Connect the slider's valueChanged signal to the change_slider slot
        slider.valueChanged.connect(self.change_slider)

        # Add the slider to the layout
        layout.addWidget(slider)

    def change_slider(self, data):
        print("dubu slider", data)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SliderHolder()
    window.show()
    sys.exit(app.exec())
