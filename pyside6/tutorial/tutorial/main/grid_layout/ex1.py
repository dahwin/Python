from PySide6.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QLineEdit, QSizePolicy
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget,  QSizePolicy, QGridLayout
class Window(QWidget):
    def __init__(self):
        super().__init__()

        # Create widgets
        self.label_1 = QLabel("First Label:")
        self.label_2 = QLabel("Second Label:")
        self.line_edit_1 = QLineEdit()
        self.line_edit_2 = QLineEdit()
        self.button = QPushButton("Click Me")

        # Create a grid layout
        grid_layout = QGridLayout()

        # Add widgets to the grid layout
        grid_layout.addWidget(self.label_1, 0, 0)
        grid_layout.addWidget(self.line_edit_1, 0, 1)
        grid_layout.addWidget(self.label_2, 1, 0)
        grid_layout.addWidget(self.line_edit_2, 1, 1)
        grid_layout.addWidget(self.button, 2, 0,1,2)

        # Set the layout of the window
        self.setLayout(grid_layout)

        # Set the window title
        self.setWindowTitle("QGridLayout Example")

        # Set the size policy of the line edits to expand horizontally
        self.line_edit_1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.line_edit_2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        # Connect the button to a slot
        self.button.clicked.connect(self.on_button_clicked)

    def on_button_clicked(self):
        # Get the text from the line edits
        text_1 = self.line_edit_1.text()
        text_2 = self.line_edit_2.text()

        # Display the text in a message box
        # (Replace with your desired functionality)
        print(f"Text 1: {text_1}\nText 2: {text_2}")

if __name__ == "__main__":
    app = QApplication()
    window = Window()
    window.show()
    app.exec()