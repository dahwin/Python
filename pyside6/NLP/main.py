from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,QThread, Signal,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform,QTextCursor)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QListView, QMainWindow,
    QMenuBar, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QTextEdit, QVBoxLayout, QWidget)
 
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1342, 805)
        icon = QIcon()
        icon.addFile(u":/icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        # Replace the existing style sheet rules for side_widget, side_widget QPushButton, and chat_list
        MainWindow.setStyleSheet(u"QPushButton {\n"
            "    text-align: left;\n"
            "}\n"
            "#side_widget, #side_widget * {\n"
            "    background-color: #000000;\n"
            "}\n"
            "#side_widget QPushButton, #side_widget QPushButton * {\n"
            "    text-align: left;\n"
            "    color: #fff;\n"
            "    border: none;\n"
            "    padding: 10px 10px;\n"
            "    border-radius: 5px;\n"
            "    background: none;\n"
            "}\n"
            "#chat_list, #chat_list * {\n"
            "    background-color: #000000;\n"
            "    color: #fff;\n"
            "}\n"
            "#side_widget QPushButton:hover, #chat_list::item:hover, #user_frame:hover, #menu_frame QFrame:hover {\n"
            "    background-color: #2a2b32;\n"
            "}\n"
            "#chat_list::item:selected {\n"
            "    background-color: #343541;\n"
            "}\n"
            "#chat_list {\n"
            "    border: none;\n"
            "}\n"
            "#chat_list::item {\n"
            "    color: #fff;\n"
            "    padding: 10px;\n"
            "    border-radius: 5px;\n"
            "    margin-top: 5px;\n"
            "}\n"
            "#chat_list_scrollArea {\n"
            "    border: none;\n"
            "}\n"
            "#menu_fr"
            "ame {\n"
            "    border-top: 0.5px solid #4d4d4f;\n"
            "}\n"
            " QScrollBar:vertical {\n"
            "     border: none;\n"
            "     background: #202123;\n"
            "     width: 8px;\n"
            "     margin: 0;\n"
            "    border-radius: 4px;\n"
            " }\n"
            " QScrollBar::handle:vertical {\n"
            "     background: #565869;\n"
            "     min-height: 20px;\n"
            "     border-radius: 4px;\n"
            " }\n"
            " QScrollBar::add-line:vertical {\n"
            "     border: none;\n"
            "     background: #202123;\n"
            "     subcontrol-position: bottom;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "     background: none;\n"
            " }\n"
            "QScrollBar::handle:hover {\n"
            "    background-color: #acacbe;\n"
            "}\n"
            "#comboBox  {\n"
            "    border: none;\n"
            "    background: transparent;\n"
            "    color: #fff;\n"
            "}\n"
            "#comboBox:editable {\n"
            "    background: transparent;\n"
            "}\n"
        )

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_3 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.side_widget = QWidget(self.centralwidget)
        self.side_widget.setObjectName(u"side_widget")
        self.side_widget.setMinimumSize(QSize(241, 0))
        self.side_widget.setMaximumSize(QSize(250, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.side_widget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.side_widget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.new_chat_btn = QPushButton(self.frame)
        self.new_chat_btn.setObjectName(u"new_chat_btn")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.new_chat_btn.setFont(font)
        self.new_chat_btn.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u"qd.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.new_chat_btn.setIcon(icon1)
        self.new_chat_btn.setIconSize(QSize(18, 18))

        self.verticalLayout_2.addWidget(self.new_chat_btn)


        self.verticalLayout_3.addWidget(self.frame)

        self.frame_3 = QFrame(self.side_widget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 100))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, 0, -1, 0)
        self.chat_list = QListView(self.frame_3)
        self.chat_list.setObjectName(u"chat_list")
        font1 = QFont()
        font1.setPointSize(11)
        self.chat_list.setFont(font1)
        self.chat_list.setFocusPolicy(Qt.NoFocus)
        self.chat_list.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.gridLayout.addWidget(self.chat_list, 0, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.frame_3)

        self.menu_frame = QFrame(self.side_widget)
        self.menu_frame.setObjectName(u"menu_frame")
        self.menu_frame.setFrameShape(QFrame.StyledPanel)
        self.menu_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.menu_frame)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(9, 5, 9, 5)
        self.frame_7 = QFrame(self.menu_frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(9, 0, 9, 0)

        self.verticalLayout.addWidget(self.frame_7)

        self.pushButton_9 = QPushButton(self.menu_frame)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setFont(font1)
        self.pushButton_9.setStyleSheet(u"background: none;")

        self.verticalLayout.addWidget(self.pushButton_9)

        self.user_frame = QFrame(self.menu_frame)
        self.user_frame.setObjectName(u"user_frame")
        self.user_frame.setFrameShape(QFrame.StyledPanel)
        self.user_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.user_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(9, 0, 9, 0)

        self.verticalLayout.addWidget(self.user_frame)

        self.frame_10 = QFrame(self.menu_frame)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.comboBox = QComboBox(self.frame_10)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFont(font1)
        self.comboBox.setFocusPolicy(Qt.NoFocus)
        self.comboBox.setStyleSheet(u"#comboBox QListView {\n"
"	padding-top:5px;\n"
"	font-size: 11px;\n"
"	background-color: #2a2b32;\n"
"	outline: 0px;  /*\u53bb\u865a\u7ebf*/\n"
"	border-radius: 0px;\n"
"}\n"
"\n"
"#comboBox QListView::item{\n"
"	padding-left:5px;\n"
"	background: transparent;\n"
"	padding:5px;\n"
"	color: #fff;\n"
"}\n"
"#comboBox QListView::item:hover{\n"
"   background-color:#1e90ff;\n"
"}\n"
"\n"
"#comboBox QListView::item:selected{\n"
"   background-color:#1e90ff;\n"
"}")

        self.horizontalLayout.addWidget(self.comboBox)


        self.verticalLayout.addWidget(self.frame_10)

        self.frame_6 = QFrame(self.menu_frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(9, 0, 9, 0)




        self.pushButton_8 = QPushButton(self.frame_6)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setFont(font1)
        self.pushButton_8.setStyleSheet(u"background: none;")

        self.horizontalLayout_7.addWidget(self.pushButton_8)


        self.verticalLayout.addWidget(self.frame_6)

        self.frame_5 = QFrame(self.menu_frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, 0)
   

        self.pushButton_5 = QPushButton(self.frame_5)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setFont(font1)
        self.pushButton_5.setStyleSheet(u"background: none;")

        self.horizontalLayout_6.addWidget(self.pushButton_5)


        self.verticalLayout.addWidget(self.frame_5)

        self.frame_4 = QFrame(self.menu_frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(9, 0, 9, 0)
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(17, 17))
        self.label.setPixmap(QPixmap(u":/icons/icons/logout.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.label)

        self.pushButton_6 = QPushButton(self.frame_4)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setFont(font1)
        self.pushButton_6.setStyleSheet(u"background: none;")

        self.horizontalLayout_5.addWidget(self.pushButton_6)


        self.verticalLayout.addWidget(self.frame_4)


        self.verticalLayout_3.addWidget(self.menu_frame)


        self.horizontalLayout_3.addWidget(self.side_widget)

        self.main_widget = QWidget(self.centralwidget)
        self.main_widget.setObjectName(u"main_widget")
        self.main_widget.setStyleSheet(u"background: #fff;")
        self.gridLayout_3 = QGridLayout(self.main_widget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(0)
        self.gridLayout_3.setVerticalSpacing(6)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 20)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.input_frame = QFrame(self.main_widget)
        self.input_frame.setObjectName(u"input_frame")
        self.input_frame.setMinimumSize(QSize(650, 0))
        self.input_frame.setMaximumSize(QSize(16777215, 200))
        self.input_frame.setStyleSheet(u"#input_frame\n"
"{\n"
"	border: 1px solid #e5e5e5;\n"
"	background: #fff;\n"
"	border-radius: 5px;\n"
"}")
        self.gridLayout_2 = QGridLayout(self.input_frame)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(10, 10, 5, 10)

        self.send_btn = QPushButton(self.input_frame)
        self.send_btn.setObjectName(u"send_btn")
        self.send_btn.setMinimumSize(QSize(45, 45))
        self.send_btn.setMaximumSize(QSize(45, 45))
        self.send_btn.setStyleSheet(u"#send_btn {\n"
            "border: none;\n"
            "padding: 5px;\n"
            "border-radius: 5px;\n"
            "}\n"
            "\n"
            "#send_btn:hover {\n"
            "	background: #ececf1;\n"
            "}")
        icon2 = QIcon()
        icon2.addFile(u"send.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.send_btn.setIcon(icon2)
        self.send_btn.setIconSize(QSize(35, 35))

        self.gridLayout_2.addWidget(self.send_btn, 1, 2, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.gridLayout_2.addItem(self.verticalSpacer_3, 0, 2, 1, 1)

        self.input_textEdit = QTextEdit(self.input_frame)
        self.input_textEdit.setObjectName(u"input_textEdit")
        font2 = QFont()
        font2.setPointSize(10)
        self.input_textEdit.setFont(font2)
        self.input_textEdit.setStyleSheet(u"border: none;")

        # Update the layout to add comboBox_2 to the right of input_textEdit
        self.gridLayout_2.addWidget(self.input_textEdit, 0, 0, 2, 1)

        self.comboBox_2 = QComboBox(self.input_frame)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        # Update the layout to add comboBox_2 to the right of input_textEdit
        self.gridLayout_2.addWidget(self.input_textEdit, 0, 0, 2, 1)

        # Modify the input_frame styling to align contents to the top-right
        self.gridLayout_2.setAlignment(Qt.AlignTop | Qt.AlignRight)

        # Add comboBox_2 directly to the main layout
        self.gridLayout_3.addWidget(self.comboBox_2, 1, 2, 1, 1)
        self.gridLayout_3.addWidget(self.input_frame, 1, 1, 1, 1)

        self.scrollArea = QScrollArea(self.main_widget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"border: none;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 1092, 558))
        self.gridLayout_4 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setVerticalSpacing(50)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer, 0, 0, 1, 1)
    
        # Add these lines to create and set the object name for the QTextBrowser
        self.text_browser = QTextBrowser(self.scrollAreaWidgetContents_2)
        self.text_browser.setObjectName(u"text_browser")
        self.gridLayout_4.addWidget(self.text_browser, 0, 0, 1, 1)


        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_3.addWidget(self.scrollArea, 0, 0, 1, 3)


        self.horizontalLayout_3.addWidget(self.main_widget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1342, 21))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ChatGPT", None))
        self.new_chat_btn.setText(QCoreApplication.translate("MainWindow", u"New Conversation", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Sponsor us", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"QueenDahyun", None))


        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Dark mode", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", "Future Plan", None))
        self.label.setText("")
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Log out", None))
        self.send_btn.setText("")
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"chatgml3_6b", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Solar_10", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"Mixtral_8x_7b", None))
    def toggle_dark_mode(self):
        if self.main_widget.styleSheet() == "":
            # Enable dark mode
            self.main_widget.setStyleSheet("background: #212121; color: white;")
        else:
            # Disable dark mode (remove stylesheet)
            self.main_widget.setStyleSheet("")

    # retranslateUi

from PySide6.QtWidgets import QApplication, QMainWindow

from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLineEdit, QTextBrowser, QPushButton
import random
import openai
from PySide6.QtCore import QThread, Signal
import openai
import random

class ChatThread(QThread):
    message_received = Signal(str)

    def __init__(self, user_input):
        super().__init__()
        self.user_input = user_input

    def run(self):
        try:
            api_response = self.chat(self.user_input)
            self.message_received.emit(api_response)
        except Exception as e:
            print(f"Error in ChatThread: {e}")

    def chat(self, prompt):
        api_keys = [

            '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',
        ]

        selected_api_key = random.choice(api_keys)
        print(selected_api_key)
        openai.api_key = selected_api_key

        messages = [
            {"role": "system", "content": 'you are a helpful assistant'},
            {"role": "user", "content": prompt}
        ]

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.7,
            max_tokens=200
        )

        response_text = response.choices[0].message["content"]
        return response_text
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QTextBrowser, QPushButton, QTextEdit
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
import random
import openai
from PySide6.QtCore import QEvent

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        

        # Connect the send button click event to a custom method
        self.ui.send_btn.clicked.connect(self.send_user_message)

        # Create an instance of ChatThread
        self.chat_thread = ChatThread("")

        # Connect the message_received signal to the display_ai_response method
        self.chat_thread.message_received.connect(self.display_ai_response)

        # Connect the Enter key press event to the send_user_message method
        self.ui.input_textEdit.setAcceptRichText(False)
        self.ui.input_textEdit.installEventFilter(self)
        # Connect the toggle_dark_mode method to the Dark mode button click event
        self.ui.pushButton_8.clicked.connect(self.ui.toggle_dark_mode)

    def eventFilter(self, obj, event):
        if obj is self.ui.input_textEdit and event.type() == QEvent.KeyPress and event.key() == Qt.Key_Return:
            self.send_user_message()
            return True
        return super().eventFilter(obj, event)


    def send_user_message(self):
        # Get user input from the text edit
        user_input = self.ui.input_textEdit.toPlainText()

        # Display the user message immediately
        self.display_user_message(user_input)

        # Update the ChatThread's user_input
        self.chat_thread.user_input = user_input

        # Start the ChatThread
        if not self.chat_thread.isRunning():
            self.chat_thread.start()

    def display_user_message(self, user_input):
        # Access the QTextBrowser widget directly from the UI
        text_browser = self.ui.text_browser

        if text_browser:
            # Insert the user's message with logo into the QTextBrowser
            user_message = f"<img src='user.png' width='40' height='40' style='border-radius: 20px;'> <b>user:</b><br><span style='font-size: 14pt;'>{user_input}</span><br><br>"
            text_browser.append(user_message)

    def display_ai_response(self, ai_response):
        # Access the QTextBrowser widget directly from the UI
        text_browser = self.ui.text_browser

        if text_browser:
            # Insert the AI response with logo into the QTextBrowser
            ai_message = f"<img src='queendahyun.png' width='40' height='40' style='border-radius: 20px;'> <b>QueenDahyun:</b><br><span style='font-size: 14pt;'>{ai_response}</span><br><br>"
            text_browser.append(ai_message)

            # Apply style to the entire QTextBrowser
            text_browser.setStyleSheet("font-size: 14pt;")

if __name__ == "__main__":
    app = QApplication([])
    window = MyMainWindow()
    window.show()
    app.exec()

