import random
import openai
import sys
import sqlite3
from PySide6.QtCore import Qt
from PySide6.QtGui import QPalette, QColor, QIcon,QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QTextEdit, QLineEdit, QPushButton, QWidget, QSizePolicy, QHBoxLayout


# SQLite3 Database Initialization
conn = sqlite3.connect("chat_history.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS chat_history (user_message TEXT, ai_response TEXT)")
conn.commit()

# Set a modern dark theme
def set_dark_theme(app):
    app.setStyle("Fusion")

    dark_palette = QPalette()
    dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.WindowText, Qt.white)
    dark_palette.setColor(QPalette.Disabled, QPalette.WindowText, QColor(127, 127, 127))
    dark_palette.setColor(QPalette.Base, QColor(42, 42, 42))
    dark_palette.setColor(QPalette.AlternateBase, QColor(66, 66, 66))
    dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
    dark_palette.setColor(QPalette.ToolTipText, Qt.white)
    dark_palette.setColor(QPalette.Text, Qt.white)
    dark_palette.setColor(QPalette.Disabled, QPalette.Text, QColor(127, 127, 127))
    dark_palette.setColor(QPalette.Dark, QColor(35, 35, 35))
    dark_palette.setColor(QPalette.Shadow, QColor(20, 20, 20))
    dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ButtonText, Qt.white)
    dark_palette.setColor(QPalette.Disabled, QPalette.ButtonText, QColor(127, 127, 127))
    dark_palette.setColor(QPalette.BrightText, Qt.red)
    dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
    dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    dark_palette.setColor(QPalette.Disabled, QPalette.Highlight, QColor(80, 80, 80))
    dark_palette.setColor(QPalette.HighlightedText, Qt.white)
    dark_palette.setColor(QPalette.Disabled, QPalette.HighlightedText, QColor(127, 127, 127))
    app.setPalette(dark_palette)

# Create a new instance of QApplication
app = QApplication(sys.argv)
set_dark_theme(app)  # Move set_dark_theme here

import random
import openai

def chat(prompt):    # List of API keys
    api_keys = [
        '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',
        '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',
        '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',
    ]

    # Randomly select an API key
    selected_api_key = random.choice(api_keys)

    openai.api_key = selected_api_key  # Set the selected API key

    messages = [
        {"role": "system", "content": 'you are a helpful assistant'},
        {"role": "user", "content": prompt}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.7,
        max_tokens=200  # You can adjust this based on the desired length of the summary
    )

    response_text = response.choices[0].message["content"]

    data = {
        prompt: response_text
    }
    return response_text

class ChatApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Chat display area
        self.chat_display = QTextEdit(self)
        self.chat_display.setReadOnly(True)
        layout.addWidget(self.chat_display)

        # Add a spacer item to push the input box and send button higher
        spacer_item = QWidget()
        spacer_item.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        layout.addWidget(spacer_item)

        # Horizontal layout for input box and send button
        # Horizontal layout for input box and send button
        input_layout = QHBoxLayout()

        # Send button with icon
        send_button = QPushButton(self)
        send_button.setIcon(QIcon("send.svg"))
        send_button.clicked.connect(self.process_user_input)
        send_button.setMaximumWidth(360)
        send_button.setMaximumHeight(150)
        input_layout.addWidget(send_button)

        # User input area
        self.input_box = QLineEdit(self)
        self.input_box.setPlaceholderText("Type your message...")
        self.input_box.setMaximumWidth(360)
        self.input_box.setMaximumHeight(80)
        input_layout.addWidget(self.input_box)

        # Set alignment for input_layout to center
        input_layout.setAlignment(Qt.AlignCenter)

        # Add the input layout to the main layout
        layout.addLayout(input_layout)

        # Footer label
        footer_label = QLabel(self)
        footer_label.setText("Blue Footer")
        footer_label.setStyleSheet("background-color: #2196F3; color: white; padding: 5px;")
        
        # Set alignment for the footer label to center
        footer_label.setAlignment(Qt.AlignCenter)

        layout.addWidget(footer_label)

        self.setGeometry(100, 100, 400, 450)  # Increased height for the footer
        self.setWindowTitle('Chat GPT')
        self.show()


    def process_user_input(self):
        user_input = self.input_box.text()

        if user_input:
            self.save_to_database(user_input, "")
            ai_response = chat(user_input)
            self.display_message(user_input, "User")
            self.display_message(ai_response, "AI")
            self.save_to_database("", ai_response)
            self.input_box.clear()
        else:
            self.display_message("Say something...", "System")

    def save_to_database(self, user_message, ai_response):
        cursor.execute("INSERT INTO chat_history VALUES (?, ?)", (user_message, ai_response))
        conn.commit()

    def display_message(self, message, sender):
        formatted_message = f"<b>{sender}:</b> {message}<br>"

        # Load user and AI logos
        user_logo = QPixmap("user.png")
        ai_logo = QPixmap("ai.png")

        # Create QLabel widgets to display the logos
        user_logo_label = QLabel(self)
        user_logo_label.setPixmap(user_logo)
        ai_logo_label = QLabel(self)
        ai_logo_label.setPixmap(ai_logo)

        # Add logos to the chat display
        if sender == "User":
            self.chat_display.append('<img src="user.png" alt="User Logo" height="40" width="40">')
        elif sender == "AI":
            self.chat_display.append('<img src="ai.png" alt="AI Logo" height="40" width="40">')

        # Add the message to the chat display
        self.chat_display.append(formatted_message)

if __name__ == '__main__':
    window = ChatApp()
    sys.exit(app.exec_()) 
    