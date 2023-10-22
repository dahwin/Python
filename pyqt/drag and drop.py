'''dahyun+darwin = dahwin'''
import sys
import cv2
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt5.QtCore import Qt, QMimeData, QFileInfo
from PyQt5.QtGui import QDrag, QPixmap, QImage


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setAcceptDrops(True)
        self.label = QLabel("Drop image here", self)
        self.label.move(50, 50)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        for url in event.mimeData().urls():
            file_path = url.toLocalFile()
            file_info = QFileInfo(file_path)
            if file_info.suffix().lower() in ["png", "jpg", "jpeg"]:
                image = cv2.imread(file_path)
                if image is None:
                    print("Error: Could not open image.")
                    return
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                height, width, channel = image.shape
                bytes_per_line = 3 * width
                qimage = QImage(image.data, width, height, bytes_per_line, QImage.Format_RGB888)
                pixmap = QPixmap.fromImage(qimage)
                self.label.setPixmap(pixmap)
                self.label.setAlignment(Qt.AlignCenter)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())


