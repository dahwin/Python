import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QSlider, QLabel
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Custom Slider')
        self.setGeometry(100, 100, 500, 100)

        # Create a QSlider
        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setGeometry(50, 40, 400, 20)

        # Set slider range
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)

        # Create a QLabel to display the slider value
        self.label = QLabel(self)
        self.label.setGeometry(50, 70, 400, 20)
        self.label.setAlignment(Qt.AlignCenter)

        # Apply custom styles
        self.slider.setStyleSheet("""
            QSlider::groove:horizontal {
                border: 1px solid #bbb;
                background: white;
                height: 10px;
                border-radius: 4px;
            }

            QSlider::sub-page:horizontal {
                background: #0C7BDC;
                border: 1px solid #777;
                height: 10px;
                border-radius: 4px;
            }

            QSlider::add-page:horizontal {
                background: #d7d7d7;
                border: 1px solid #777;
                height: 10px;
                border-radius: 4px;
            }

            QSlider::handle:horizontal {
                background: #3A3A3A;
                border: 1px solid #5c5c5c;
                width: 18px;
                height: 18px;
                margin-top: -5px;
                margin-bottom: -5px;
                border-radius: 9px;
            }

            QSlider::handle:horizontal:hover {
                background: #1E1E1E;
                border: 1px solid #3A3A3A;
            }

            QSlider::handle:horizontal:pressed {
                background: #1E1E1E;
                border: 1px solid #3A3A3A;
            }
        """)

        # Connect the valueChanged signal to a custom slot
        self.slider.valueChanged.connect(self.update_label)

        # Print the current slider value
        current_value = self.slider.value()
        print(f'The current slider value is: {current_value}')

        # Set the slider to a specific value and update the label
        self.slider.setValue(50)
        self.update_label(50)

    def update_label(self, value):
        self.label.setText(f'Slider value: {value}')
        print(f'Slider value changed to: {value}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
