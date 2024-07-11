from PySide6.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QFrame, QHBoxLayout, QPushButton
from PySide6.QtCore import Qt

class Window(QWidget):
    def __init__(self):
        super().__init__()

        # Create a central label
        self.label = QLabel("This is a label inside a frame")

        # Create a frame with a vertical layout
        self.frame = QFrame()
        self.frame.setFrameShape(QFrame.StyledPanel)  # Set the frame shape
        self.frame.setFrameShadow(QFrame.Raised)   # Set the frame shadow
        self.frame.setLineWidth(3)              # Set the frame line width
        self.frame.setMidLineWidth(2)            # Set the frame middle line width
        self.frame.setStyleSheet("background-color: lightblue;") # Set the background color of the frame

        # Create a vertical layout for the frame
        layout = QVBoxLayout()
        layout.addWidget(self.label, alignment=Qt.AlignCenter)

        # Create a button inside the frame
        self.button = QPushButton("Click Me")
        layout.addWidget(self.button, alignment=Qt.AlignCenter)

        # Connect the button's clicked signal to a slot
        self.button.clicked.connect(self.on_button_clicked)

        self.frame.setLayout(layout)

        # Create a main layout for the window
        main_layout = QHBoxLayout()
        main_layout.addWidget(self.frame, alignment=Qt.AlignCenter)

        # Set the layout of the window
        self.setLayout(main_layout)

        # Set the window title
        self.setWindowTitle("QFrame Example")

    def on_button_clicked(self):
        # Get the text from the label
        text = self.label.text()

        # Change the label's text when the button is clicked
        self.label.setText(f"You clicked the button!  {text}")

if __name__ == "__main__":
    app = QApplication()
    window = Window()
    window.show()
    app.exec()