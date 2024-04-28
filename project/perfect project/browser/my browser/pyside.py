'dahyun+darwin = dahwin'
import sys
from PySide6.QtCore import QUrl
from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar, QLineEdit, QVBoxLayout, QPushButton, QDialog
from PySide6.QtWebEngineWidgets import QWebEngineView

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Web engine view
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://queendahyun.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # Navbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        # Back button
        back_button = QPushButton('Back')  # Use QPushButton instead of QAction
        back_button.clicked.connect(self.browser.back)
        navbar.addWidget(back_button)

        # Forward button
        forward_button = QPushButton('Forward')  # Use QPushButton instead of QAction
        forward_button.clicked.connect(self.browser.forward)
        navbar.addWidget(forward_button)

        # Reload button
        reload_button = QPushButton('Reload')  # Use QPushButton instead of QAction
        reload_button.clicked.connect(self.browser.reload)
        navbar.addWidget(reload_button)

        # Home button
        home_button = QPushButton('Home')  # Use QPushButton instead of QAction
        home_button.clicked.connect(self.navigate_home)
        navbar.addWidget(home_button)

        # URL bar
        self.url_bar = QLineEdit()
        navbar.addWidget(self.url_bar)
        self.url_bar.returnPressed.connect(self.navigate_to_url)

        # History button
        history_button = QPushButton('History')  # Use QPushButton instead of QAction
        history_button.clicked.connect(self.show_history)
        navbar.addWidget(history_button)

        # Create a list to store the history
        self.history = []

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

        history_dialog.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    QApplication.setApplicationName("Dahwin : chrome killer")
    window = MainWindow()
    app.exec_()
