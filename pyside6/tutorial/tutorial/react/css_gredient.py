import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt6.QtCore import Qt, QTimer, QPropertyAnimation, pyqtProperty
from PyQt6.QtGui import QLinearGradient, QBrush, QPalette, QColor, QPainter, QPen

class GradientLabel(QLabel):
    def __init__(self, text='', parent=None):
        super().__init__(text, parent)
        self.gradient_position = 0
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

    @pyqtProperty(float)
    def gradientPosition(self):
        return self.gradient_position

    @gradientPosition.setter
    def gradientPosition(self, pos):
        self.gradient_position = pos
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        gradient = QLinearGradient(0, 0, self.width(), 0)
        gradient.setColorAt(0, QColor('#51d3da'))
        gradient.setColorAt(0.5, QColor('#c165dd'))
        gradient.setColorAt(1, QColor('#ff44b7'))
        gradient.setStart(self.gradient_position * self.width(), 0)
        gradient.setFinalStop(self.width(), 0)

        painter.setPen(QPen(QBrush(gradient), 1))
        painter.drawText(self.rect(), self.alignment(), self.text())

class StyledWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Styled PyQt6 App')

        # Vertical layout
        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Header with gradient animation
        self.header = GradientLabel('Welcome to PyQt6')
        self.header.setObjectName('header')
        self.header.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Button container
        button_container = QHBoxLayout()
        button_container.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Buttons
        btn1 = QPushButton('Button 1')
        btn1.setObjectName('btn-primary')
        btn2 = QPushButton('Button 2')
        btn2.setObjectName('btn-secondary')

        button_container.addWidget(btn1)
        button_container.addWidget(btn2)

        # Adding widgets to the main layout
        main_layout.addWidget(self.header)
        main_layout.addLayout(button_container)

        self.setLayout(main_layout)

        # Applying styles
        self.setStyleSheet("""
            #header {
                font-size: 24px;
                padding: 20px;
                border-radius: 10px;
                background: transparent;
            }
            #btn-primary {
                background-color: #61dafb;
                color: black;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
            }
            #btn-primary:hover {
                background-color: #21a1f1;
            }
            #btn-secondary {
                background-color: #ff44b7;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
            }
            #btn-secondary:hover {
                background-color: #e0338f;
            }
        """)

        # Start gradient animation
        self.start_gradient_animation()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        gradient = QLinearGradient(0, 0, self.width(), self.height())
        gradient.setColorAt(0, QColor('#0A0E24'))  # Blue color
        gradient.setColorAt(1, QColor('#2F0618'))  # Purple color

        painter.fillRect(self.rect(), gradient)

    def start_gradient_animation(self):
        self.animation = QPropertyAnimation(self.header, b'gradientPosition')
        self.animation.setDuration(3000)
        self.animation.setStartValue(0.0)
        self.animation.setEndValue(1.0)
        self.animation.setLoopCount(-1)
        self.animation.start()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = StyledWindow()
    window.show()
    sys.exit(app.exec())








# import sys
# from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton
# from PyQt6.QtCore import Qt, QTimer, QPropertyAnimation, pyqtProperty, QSequentialAnimationGroup, QParallelAnimationGroup
# from PyQt6.QtGui import QLinearGradient, QBrush, QPalette, QColor, QPainter

# class GradientLabel(QLabel):
#     def __init__(self, text='', parent=None):
#         super().__init__(text, parent)
#         self.gradient_position = 0

#     @pyqtProperty(float)
#     def gradientPosition(self):
#         return self.gradient_position

#     @gradientPosition.setter
#     def gradientPosition(self, pos):
#         self.gradient_position = pos
#         self.update_gradient()

#     def update_gradient(self):
#         gradient = QLinearGradient(0, 0, self.width(), 0)
#         gradient.setColorAt(0, QColor('#51d3da'))
#         gradient.setColorAt(0.5, QColor('#c165dd'))
#         gradient.setColorAt(1, QColor('#ff44b7'))
#         gradient.setStart(self.gradient_position * self.width(), 0)
#         gradient.setFinalStop(self.width(), 0)

#         brush = QBrush(gradient)
#         palette = self.palette()
#         palette.setBrush(QPalette.ColorRole.WindowText, brush)
#         self.setPalette(palette)

#     def resizeEvent(self, event):
#         super().resizeEvent(event)
#         self.update_gradient()

#     def paintEvent(self, event):
#         painter = QPainter(self)
#         painter.setPen(Qt.PenStyle.NoPen)
#         gradient = QLinearGradient(0, 0, self.width(), 0)
#         gradient.setColorAt(0, QColor('#51d3da'))
#         gradient.setColorAt(0.5, QColor('#c165dd'))
#         gradient.setColorAt(1, QColor('#ff44b7'))
#         gradient.setStart(self.gradient_position * self.width(), 0)
#         gradient.setFinalStop(self.width(), 0)

#         painter.setBrush(QBrush(gradient))
#         painter.drawRect(self.rect())

#         painter.setPen(Qt.PenStyle.SolidLine)
#         painter.setBrush(Qt.BrushStyle.NoBrush)
#         painter.setClipRect(self.rect())
#         super().paintEvent(event)

# class StyledWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         self.setWindowTitle('Styled PyQt6 App')

#         # Vertical layout
#         main_layout = QVBoxLayout()
#         main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

#         # Header with gradient animation
#         self.header = GradientLabel('Welcome to PyQt6')
#         self.header.setObjectName('header')
#         self.header.setAlignment(Qt.AlignmentFlag.AlignCenter)

#         # Button container
#         button_container = QHBoxLayout()
#         button_container.setAlignment(Qt.AlignmentFlag.AlignCenter)

#         # Buttons
#         btn1 = QPushButton('Button 1')
#         btn1.setObjectName('btn-primary')
#         btn2 = QPushButton('Button 2')
#         btn2.setObjectName('btn-secondary')

#         button_container.addWidget(btn1)
#         button_container.addWidget(btn2)

#         # Adding widgets to the main layout
#         main_layout.addWidget(self.header)
#         main_layout.addLayout(button_container)

#         self.setLayout(main_layout)

#         # Applying styles
#         self.setStyleSheet("""
#             #header {
#                 font-size: 24px;
#                 color: transparent;  /* Text color should be transparent for gradient effect */
#                 padding: 20px;
#                 border-radius: 10px;
#             }
#             #btn-primary {
#                 background-color: #61dafb;
#                 color: black;
#                 padding: 10px 20px;
#                 border: none;
#                 border-radius: 5px;
#             }
#             #btn-primary:hover {
#                 background-color: #21a1f1;
#             }
#             #btn-secondary {
#                 background-color: #ff44b7;
#                 color: white;
#                 padding: 10px 20px;
#                 border: none;
#                 border-radius: 5px;
#             }
#             #btn-secondary:hover {
#                 background-color: #e0338f;
#             }
#             QWidget {
#                 background-color: #20232a;
#             }
#         """)

#         # Start gradient animation
#         self.start_gradient_animation()

#     def start_gradient_animation(self):
#         self.animation = QPropertyAnimation(self.header, b'gradientPosition')
#         self.animation.setDuration(3000)
#         self.animation.setStartValue(0.0)
#         self.animation.setEndValue(1.0)
#         self.animation.setLoopCount(-1)
#         self.animation.start()

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = StyledWindow()
#     window.show()
#     sys.exit(app.exec())
