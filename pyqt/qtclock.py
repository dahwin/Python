import sys
from PyQt5.QtCore import QTimer, QDateTime, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget

class ClockWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Create labels for time and date
        self.time_label = QLabel(self)
        self.date_label = QLabel(self)

        # Set the font size and alignment for the labels
        font_size = 40
        self.time_label.setFont(QFont('Arial', font_size))
        self.time_label.setAlignment(Qt.AlignCenter)
        self.date_label.setFont(QFont('Arial', font_size // 2))
        self.date_label.setAlignment(Qt.AlignCenter)

        # Create a layout and add the labels to it
        layout = QVBoxLayout()
        layout.addWidget(self.time_label)
        layout.addWidget(self.date_label)

        # Set the layout for the widget
        self.setLayout(layout)
        # Set the background color to black
        self.setStyleSheet("background-color: black;")

        # Set the font color to white
        self.time_label.setStyleSheet("color: white;")
        self.date_label.setStyleSheet("color: white;")

        # Set up the timer to update the clock every second
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_clock)
        self.timer.start(1000)

        # Update the clock immediately
        self.update_clock()

    def update_clock(self):
        # Get the current time and date
        time_string = QDateTime.currentDateTime().toString('hh:mm:ss AP')
        date_string = QDateTime.currentDateTime().toString('dddd, MMMM d, yyyy')

        # Update the labels with the new time and date
        self.time_label.setText(time_string)
        self.date_label.setText(date_string)

if __name__ == '__main__':
    # Set up the application and the clock widget
    app = QApplication(sys.argv)
    clock = ClockWidget()

    # Set the window properties
    clock.setWindowTitle('Clock')
    clock.setGeometry(100, 100, 400, 200)

    # Show the window and run the application
    clock.show()
    sys.exit(app.exec_())
