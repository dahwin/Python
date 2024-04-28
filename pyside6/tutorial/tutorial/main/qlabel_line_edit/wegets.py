# from PySide6 import QtWidgets
# x = dir(QtWidgets)
# print('\n'.join(x))

from PySide6.QtWidgets import QWidget, QLineEdit,QHBoxLayout,QVBoxLayout,QLabel,QPushButton

class Widgets(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Dubu")
        label = QLabel("Fullname:")
        self.line_edit = QLineEdit()
        # self.line_edit.textChanged.connect(self.text_change)
        # self.line_edit.cursorPositionChanged.connect(self.cursor_position_changed)
        # self.line_edit.editingFinished.connect(self.editing_finished)
        # self.line_edit.returnPressed.connect(self.return_pressed)
        # self.line_edit.selectionChanged.connect(self.selection_changed)

        self.line_edit.textEdited.connect(self.text_edited)


        button = QPushButton("Grab Data")
        button.clicked.connect(self.button_clicked)
        self.text_holder_label = QLabel("I am dahwin")
        h_layout = QHBoxLayout()
        h_layout.addWidget(label)
        h_layout.addWidget(self.line_edit)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(button)
        v_layout.addWidget(self.text_holder_label)

        self.setLayout(v_layout)
    
    def button_clicked(self):
        print("Full name: ", self.line_edit.text())
        self.text_holder_label.setText(self.line_edit.text())
    def text_edited(self,new_text) : 
        print("Text edited. New text : ",new_text)

    def text_change(self):
        print("Full name: ", self.line_edit.text())
        self.text_holder_label.setText(self.line_edit.text())
    
    def cursor_position_changed(self,old,new):
        print("cursor old position : ",old," -new position : ",new)
    def editing_finished(self) : 
        print("Editing finished")
    def return_pressed(self):
        print("Return pressed")

    def selection_changed(self):
        print("Selection Changed : ",self.line_edit.selectedText())

    def text_edited(self,new_text) : 
        print("Text edited. New text : ",new_text)