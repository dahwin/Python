'''Dahyun+Darwin = Dahwin'''
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Web engine view
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # Navbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        # Back button
        back_button = QAction('Back', self)
        back_button.triggered.connect(self.browser.back)
        navbar.addAction(back_button)

        # Forward button
        forward_button = QAction('Forward', self)
        forward_button.triggered.connect(self.browser.forward)
        navbar.addAction(forward_button)

        # Reload button
        reload_button = QAction('Reload', self)
        reload_button.triggered.connect(self.browser.reload)
        navbar.addAction(reload_button)

        # Home button
        home_button = QAction('Home', self)
        home_button.triggered.connect(self.navigate_home)
        navbar.addAction(home_button)

        # URL bar
        self.url_bar = QLineEdit()
        navbar.addWidget(self.url_bar)
        self.url_bar.returnPressed.connect(self.navigate_to_url)

        # History button
        history_button = QAction('History', self)
        history_button.triggered.connect(self.show_history)
        navbar.addAction(history_button)

        # Create a list to store the history
        self.history = []

        # Connect the urlChanged signal to the update_url method
        self.browser.urlChanged.connect(self.update_url)

    def update_url(self, q):
        self.url_bar.setText(q.toString())

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))
        self.history.append(url)

    def navigate_home(self):
        self.browser.setUrl(QUrl("https://youtube.com"))
        self.history.append("https://youtube.com")

    def show_history(self):
        history_dialog = QDialog(self)
        history_dialog.setWindowTitle("History")
        layout = QVBoxLayout()
        history_dialog.setLayout(layout)

        for url in self.history:
            button = QPushButton(url)
            button.clicked.connect(lambda state, x=url: self.browser.setUrl(QUrl(x)))
            layout.addWidget(button)

        history_dialog.exec()




app = QApplication(sys.argv)
QApplication.setApplicationName("Dahwin : chrome killer")
window = MainWindow()
app.exec()