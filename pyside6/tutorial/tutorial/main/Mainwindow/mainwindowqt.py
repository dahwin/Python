"dahyun+darwin=dahwin"
from PySide6.QtWidgets import QApplication,QMainWindow,QToolBar,QPushButton,QStatusBar
from PySide6.QtCore import QSize
from PySide6.QtGui import QAction,QIcon
import os
class MainWindow(QMainWindow):
    def __init__(self,app):
        super().__init__()
        self.app = app
        self.setWindowTitle("Dwindows")


        menu_bar = self.menuBar()
        file_menue = menu_bar.addMenu("&File")
        quit_action = file_menue.addAction("Quit")
        quit_action.triggered.connect(self.quit_app)

        edit_menu = menu_bar.addMenu("Edit")
        edit_menu.addAction("Copy")
        edit_menu.addAction("Cut")
        edit_menu.addAction("Paste")
        edit_menu.addAction("Undo")
        edit_menu.addAction("Redo")

        window_menu = menu_bar.addMenu("Window")
        setting_menu = menu_bar.addMenu("Setting")
        help_menu = menu_bar.addMenu("Help")

        toolbar = QToolBar("MY dahyun's toolbar")
        toolbar.setIconSize(QSize(16,16))
        self.addToolBar(toolbar)

        toolbar.addAction(quit_action)

        action1 = QAction("Some action", self)
        action1.setStatusTip("status message for some action")
        action1.triggered.connect(self.toolbar_button_click)
        toolbar.addAction(action1)

        # Use absolute path to the image file
        script_directory = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(script_directory, "queendahyun.png")
        action2 = QAction(QIcon(rf"{image_path}"),"some other action",self)
        action2.setStatusTip("status message for some other action")
        action2.triggered.connect(self.toolbar_button_click)
        action2.setCheckable(True)
        toolbar.addAction(action2)
        toolbar.addSeparator()
        toolbar.addWidget(QPushButton("Click Here"))

        self.setStatusBar(QStatusBar(self))

        button1 = QPushButton("Button1")
        button1.clicked.connect(self.button_clicked)
        self.setCentralWidget(button1)

        self.setMinimumSize(800,450)
    def quit_app(self):
        self.app.quit()

    def toolbar_button_click(self):
        # print("action triggered")
        self.statusBar().showMessage("My Dahyun's Message",3000)
    def button_clicked():
        print("CLicked on the button")
