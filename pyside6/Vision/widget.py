from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QTextEdit, QPushButton, QHBoxLayout
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import Qt, QThread, Signal
from PIL import Image
import os
import requests

class ImageGeneratorThread(QThread):
    finished = Signal(str)

    def __init__(self, prompt):
        super().__init__()
        self.prompt = prompt

    def run(self):
        # Move the generate_image logic to this method
        url = 'https://f8b7-34-173-211-93.ngrok-free.app/prompt'
        data = {'dahwin': f'{self.prompt}'}
        response = requests.post(url, json=data)
        print("Raw Response Content:", response.content)

        # Emit the finished signal with the generated image file path
        self.finished.emit(get_last_created_file(os.getcwd()))


def generate_image(prompt):
    # Define the URL of your FastAPI application
    url = 'https://f8b7-34-173-211-93.ngrok-free.app/prompt'

    data = {'dahwin': f'{prompt}'}  # Include the 'name' field in the JSON data

    # Send a POST request
    response = requests.post(url, json=data)


    # Print the raw response content for debugging
    print("Raw Response Content:", response.content)
def get_last_created_file(directory="."):
    # Get a list of all files in the directory
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

    # Check if there are any files in the directory
    if not files:
        return None

    # Get the full path for each file
    file_paths = [os.path.join(directory, f) for f in files]

    # Get the file with the latest creation time
    last_created_file = max(file_paths, key=os.path.getctime)

    # Get the absolute path
    last_created_file_absolute = os.path.abspath(last_created_file)

    return last_created_file_absolute

# Example usage:
current_directory = "."  # You can change this to the desired directory


class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dahwin vision")
        self.setStyleSheet("background-color: rgb(0, 0, 0)")

        self.image_label = QLabel()
        self.text_edit = QTextEdit()
        self.text_edit.setPlaceholderText("Type your imagination!")
        self.text_edit.setMaximumSize(600, 60)
        generated_image_file = get_last_created_file(os.getcwd())
        print(generated_image_file)

        # Open the image file using Pillow
        original_image = Image.open(generated_image_file)

        # Define the new size you want (e.g., width and height)
        new_width = 250  # You can change this to your desired width
        new_height = int(original_image.height * (new_width / original_image.width))

        # Resize the image with the new size and maintaining aspect ratio
        resized_image = original_image.resize((new_width, new_height), Image.ANTIALIAS)

        # Convert the Pillow Image to a QImage
        q_image = QImage(resized_image.tobytes(), resized_image.width, resized_image.height, resized_image.width * 3, QImage.Format_RGB888)

        # Create a QPixmap from the QImage
        scaled_pixmap = QPixmap.fromImage(q_image)

        # Apply CSS to the QTextEdit
        self.text_edit.setStyleSheet(
            "QTextEdit {"
            "   background-color: #f0f0f0;"   # Set background color
            "   border: 1px solid #800080;"    # Set purple border
            "   border-radius: 5px;"           # Set border radius
            "   padding: 5px;"                 # Set padding
            "}"
        )

        # Set the pixmap to the QLabel
        self.image_label.setPixmap(scaled_pixmap)
        self.image_label.setMaximumSize(400, 400)

        sendbutton = QPushButton("Send")
        sendbutton.setMaximumSize(60, 25)
        # Connect the button click to the new slot
        sendbutton.clicked.connect(self.start_image_generation)

        sendlayout = QHBoxLayout()
        sendlayout.addWidget(self.text_edit)
        sendlayout.addWidget(sendbutton)

        layout = QVBoxLayout()
        layout.addWidget(self.image_label)  
        layout.addLayout(sendlayout)  

        # # Set alignment for sendlayout to be aligned at the top of the layout
        layout.setAlignment(sendlayout, Qt.AlignTop)

        la = QLabel("THis is Dahyun Vision")
        la_layout = QHBoxLayout()
        la_layout.addLayout(layout)
        la_layout.addWidget(la)
        la_layout.setAlignment(la, Qt.AlignRight)


        self.setLayout(la_layout)

    def start_image_generation(self):
        # Get the prompt from the QTextEdit
        prompt = self.text_edit.toPlainText()

        # Create and start the ImageGeneratorThread
        self.image_generator_thread = ImageGeneratorThread(prompt)
        self.image_generator_thread.finished.connect(self.update_generated_image)
        self.image_generator_thread.start()

    def update_generated_image(self, generated_image_file):
        # Load the newly created image
        print(generated_image_file)
        original_image = Image.open(generated_image_file)
        new_width = 250
        new_height = int(original_image.height * (new_width / original_image.width))

        resized_image = original_image.resize((new_width, new_height), Image.ANTIALIAS)
        q_image = QImage(resized_image.tobytes(), resized_image.width, resized_image.height, resized_image.width * 3, QImage.Format_RGB888)
        scaled_pixmap = QPixmap.fromImage(q_image)

        # Set the new pixmap to the QLabel
        self.image_label.setPixmap(scaled_pixmap)








    # def gen_img(self):
    #     prompt = self.text_edit.toPlainText()
    #     generate_image(prompt)

    #     # Load the newly created image
    #     generated_image_file = get_last_created_file(os.getcwd())
    #     print(generated_image_file)
    #     # Open the image file using Pillow
    #     original_image = Image.open(generated_image_file)
    #     # Define the new size you want (e.g., width and height)
    #     new_width = 250  # You can change this to your desired width
    #     new_height = int(original_image.height * (new_width / original_image.width))

    #     # Resize the image with the new size and maintaining aspect ratio
    #     resized_image = original_image.resize((new_width, new_height), Image.ANTIALIAS)

    #     # Convert the Pillow Image to a QImage
    #     q_image = QImage(resized_image.tobytes(), resized_image.width, resized_image.height, resized_image.width * 3, QImage.Format_RGB888)

    #     # Create a QPixmap from the QImage
    #     scaled_pixmap = QPixmap.fromImage(q_image)

    #     # Set the new pixmap to the QLabel
    #     self.image_label.setPixmap(scaled_pixmap)
