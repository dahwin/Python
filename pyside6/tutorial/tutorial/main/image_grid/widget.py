import os
import csv
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QScrollArea, QCheckBox, QPushButton, QHBoxLayout, QFileDialog

class ImageWidget(QWidget):
    def __init__(self, image_path, checkbox_callback):
        super().__init__()

        self.image_path = os.path.abspath(image_path)

        image_label = QLabel()
        image_label.setPixmap(QPixmap(self.image_path))

        self.checkbox = QCheckBox(os.path.basename(image_path))
        self.checkbox.toggled.connect(lambda state: checkbox_callback(state, self.image_path))

        layout = QVBoxLayout()
        layout.addWidget(image_label)
        layout.addWidget(self.checkbox)

        self.setLayout(layout)

class ImageGallery(QWidget):
    def __init__(self, directory_path):
        super().__init__()

        self.setWindowTitle("Dahwin vision")

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)

        content_widget = QWidget()
        self.scroll_area.setWidget(content_widget)

        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.scroll_area)

        self.selected_images = set()

        self.load_images(directory_path)

        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.save_images_to_csv)

        main_layout.addWidget(self.save_button)

    def checkbox_callback(self, checked, image_path):
        if checked:
            print(f"Image selected: {image_path}")
            self.selected_images.add(image_path)
        else:
            print(f"Image unselected: {image_path}")
            self.selected_images.discard(image_path)

    def load_images(self, directory_path):
        files = os.listdir(directory_path)
        image_files = [file for file in files if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

        content_layout = QVBoxLayout()

        for image_file in image_files:
            absolute_path = os.path.join(directory_path, image_file)
            image_widget = ImageWidget(absolute_path, self.checkbox_callback)
            content_layout.addWidget(image_widget)

        content_widget = QWidget()
        content_widget.setLayout(content_layout)
        self.scroll_area.setWidget(content_widget)

    def save_images_to_csv(self):
        if not self.selected_images:
            print("No images selected.")
            return

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getSaveFileName(self, "Save CSV File", "", "CSV Files (*.csv);;All Files (*)", options=options)

        if file_name:
            with open(file_name, 'w', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow(["Selected Images"])
                for image_path in self.selected_images:
                    csv_writer.writerow([image_path])

            print(f"CSV file saved to: {file_name}")

if __name__ == "__main__":
    app = QApplication([])

    directory_path = r'C:\Users\ALL USER\Desktop\e\images\fonts'

    image_gallery = ImageGallery(directory_path)
    image_gallery.show()

    app.exec()
