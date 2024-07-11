# from PySide6.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QFrame
# from PySide6.QtCore import Qt

# class Window(QWidget):
#     def __init__(self):
#         super().__init__()

#         # Create a central label
#         self.label = QLabel("This is a label inside a frame")
#         self.label.setStyleSheet("""
#             QLabel {
#                 background: qlineargradient(
#                     x1: 0, y1: 0, x2: 1, y2: 0,
#                     stop: 0 blue, stop: 1 purple
#                 );
#                 color: white; /* Optional: set text color to white for better readability */
#                 padding: 10px; /* Optional: add some padding */
#             }
#         """)


#         # Create a frame with a vertical layout
#         self.frame = QFrame()
#         self.frame.setFrameShape(QFrame.StyledPanel)  # Set the frame shape
#         self.frame.setFrameShadow(QFrame.Raised)   # Set the frame shadow
#         self.frame.setLineWidth(3)              # Set the frame line width
#         self.frame.setMidLineWidth(2)            # Set the frame middle line width
#         # self.frame.setStyleSheet("""
#         #     QFrame {
#         #         background: qlineargradient(
#         #             x1: 0, y1: 0, x2: 1, y2: 0,
#         #             stop: 0 blue, stop: 1 purple
#         #         );
#         #     }
#         # """)  # Set the gradient background color of the frame
#         self.frame.setStyleSheet("background-color: None;")  # Set the background color of the frame


#         # Create a vertical layout for the frame
#         layout = QVBoxLayout()
#         layout.addWidget(self.label, alignment=Qt.AlignCenter)
#         self.frame.setLayout(layout)

#         # Create a main layout for the window
#         main_layout = QVBoxLayout()
#         main_layout.addWidget(self.frame, alignment=Qt.AlignCenter)

#         # Set the layout of the window
#         self.setLayout(main_layout)

#         # Set the window title
#         self.setWindowTitle("QFrame Example")

# if __name__ == "__main__":
#     app = QApplication()
#     window = Window()
#     window.show()
#     app.exec()


















from PySide6.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QFrame
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QPainter, QLinearGradient, QColor

class AnimatedLabel(QLabel):
    def __init__(self, text):
        super().__init__(text)
        self.offset = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateGradient)
        self.timer.start(50)  # Adjust the interval for speed of animation
        self.setStyleSheet("background-color: #333333; color: white; padding: 10px;")  # Dark background and padding

    def updateGradient(self):
        self.offset += 0.01  # Increment the offset for animation
        if self.offset > 1:
            self.offset = 0
        self.update()  # Trigger a repaint

    def paintEvent(self, event):
        painter = QPainter(self)
        gradient = QLinearGradient(0, 0, self.width(), 0)
        gradient.setColorAt(0, QColor("blue"))
        gradient.setColorAt(1, QColor("purple"))
        gradient.setColorAt((self.offset + 0.5) % 1, QColor("blue"))
        gradient.setColorAt((self.offset + 1.0) % 1, QColor("purple"))
        painter.fillRect(self.rect(), gradient)
        super().paintEvent(event)

class Window(QWidget):
    def __init__(self):
        super().__init__()

        # Create a central label with gradient background
        self.label = AnimatedLabel("This is a label inside a frame")

        # Create a frame with a vertical layout
        self.frame = QFrame()
        self.frame.setFrameShape(QFrame.StyledPanel)  # Set the frame shape
        self.frame.setFrameShadow(QFrame.Raised)      # Set the frame shadow
        self.frame.setLineWidth(3)                    # Set the frame line width
        self.frame.setMidLineWidth(2)                 # Set the frame middle line width
        self.frame.setStyleSheet("background-color: lightgrey;")  # Set the background color of the frame

        # Create a vertical layout for the frame
        layout = QVBoxLayout()
        layout.addWidget(self.label, alignment=Qt.AlignCenter)
        self.frame.setLayout(layout)

        # Create a main layout for the window
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.frame, alignment=Qt.AlignCenter)

        # Set the layout of the window
        self.setLayout(main_layout)

        # Set the window title
        self.setWindowTitle("QLabel Gradient Animation Example")

if __name__ == "__main__":
    app = QApplication()
    window = Window()
    window.show()
    app.exec()
