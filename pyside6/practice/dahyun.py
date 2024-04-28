from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QMainWindow, QMenuBar, QPlainTextEdit, QPushButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1098, 895)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(330, 130, 411, 561))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.plainTextEdit = QPlainTextEdit(self.verticalLayoutWidget_2)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

 

        self.verticalLayout_2.addWidget(self.plainTextEdit)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_28 = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_28.setObjectName(u"pushButton_28")

        self.horizontalLayout_2.addWidget(self.pushButton_28)

        self.pushButton_27 = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_27.setObjectName(u"pushButton_27")

        self.horizontalLayout_2.addWidget(self.pushButton_27)

        self.pushButton_25 = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_25.setObjectName(u"pushButton_25")

        self.horizontalLayout_2.addWidget(self.pushButton_25)

        self.pushButton_26 = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_26.setObjectName(u"pushButton_26")

        self.horizontalLayout_2.addWidget(self.pushButton_26)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_13 = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_13.setObjectName(u"pushButton_13")

        self.gridLayout.addWidget(self.pushButton_13, 5, 1, 1, 1)

        self.pushButton_15 = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_15.setObjectName(u"pushButton_15")

        self.gridLayout.addWidget(self.pushButton_15, 0, 2, 1, 1)

        self.pushButton_18 = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_18.setObjectName(u"pushButton_18")

        self.gridLayout.addWidget(self.pushButton_18, 6, 2, 1, 1)

        self.pushButton_14 = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_14.setObjectName(u"pushButton_14")

        self.gridLayout.addWidget(self.pushButton_14, 6, 1, 1, 1)

        self.pushButton_2 = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 0, 0, 1, 1)

        self.pushButton_11 = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.gridLayout.addWidget(self.pushButton_11, 3, 1, 1, 1)

        self.pushButton = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 4, 2, 1, 1)

        self.pushButton_12 = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_12.setObjectName(u"pushButton_12")

        self.gridLayout.addWidget(self.pushButton_12, 4, 1, 1, 1)

        self.pushButton_16 = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_16.setObjectName(u"pushButton_16")

        self.gridLayout.addWidget(self.pushButton_16, 1, 2, 1, 1)

        self.pushButton_3 = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout.addWidget(self.pushButton_3, 3, 2, 1, 1)

        self.pushButton_17 = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_17.setObjectName(u"pushButton_17")

        self.gridLayout.addWidget(self.pushButton_17, 5, 2, 1, 1)

        self.pushButton_24 = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_24.setObjectName(u"pushButton_24")

        self.gridLayout.addWidget(self.pushButton_24, 6, 3, 1, 1)

        self.pushButton_20 = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_20.setObjectName(u"pushButton_20")

        self.gridLayout.addWidget(self.pushButton_20, 1, 3, 1, 1)

        self.pushButton_19 = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_19.setObjectName(u"pushButton_19")

        self.gridLayout.addWidget(self.pushButton_19, 0, 3, 1, 1)

        self.pushButton_22 = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_22.setObjectName(u"pushButton_22")

        self.gridLayout.addWidget(self.pushButton_22, 4, 3, 1, 1)

        self.pushButton_23 = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_23.setObjectName(u"pushButton_23")

        self.gridLayout.addWidget(self.pushButton_23, 5, 3, 1, 1)

        self.pushButton_21 = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_21.setObjectName(u"pushButton_21")

        self.gridLayout.addWidget(self.pushButton_21, 3, 3, 1, 1)

        self.pushButton_10 = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.gridLayout.addWidget(self.pushButton_10, 1, 1, 1, 1)

        self.pushButton_4 = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout.addWidget(self.pushButton_4, 6, 0, 1, 1)

        self.pushButton_5 = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout.addWidget(self.pushButton_5, 1, 0, 1, 1)

        self.pushButton_8 = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.gridLayout.addWidget(self.pushButton_8, 4, 0, 1, 1)

        self.pushButton_6 = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.gridLayout.addWidget(self.pushButton_6, 5, 0, 1, 1)

        self.pushButton_7 = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.gridLayout.addWidget(self.pushButton_7, 3, 0, 1, 1)

        self.pushButton_9 = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.gridLayout.addWidget(self.pushButton_9, 0, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1098, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"QD Calulator", None))
        self.plainTextEdit.setPlainText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_28.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_27.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_25.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_26.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_24.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_22.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_23.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))


    # retranslateUi



class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create an instance of the Ui_MainWindow class
        self.ui = Ui_MainWindow()

        # Call the setupUi method to set up the UI
        self.ui.setupUi(self)

        # Additional initialization code can go here

if __name__ == "__main__":
    app = QApplication([])
    main_window = MyMainWindow()
    main_window.show()
    app.exec()