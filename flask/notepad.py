'''Dahyun+Darwin = Dahwin'''

import os
class NOtepad:
    def __init__(self):
        self.filename=None

    def new_file(self):
        self.filename = None
        self.text = ''

    def open_file(self,file_path):
        self.filename = file_path
        with open(self.filename,'r') as f:
            self.text = f.read()
        # return self.text

    def save_file(self,file_path):
        if file_path:
            self.filename = file_path
            if not self.filename:
                raise  ValueError('Please specify a file path.')
            with open(self.filename,'w') as f:
                f.write(self.text)
    def append_text(self,new_text):
        self.text +=new_text

    def delete_text(self):
        self.text = ''
    def get_text(self):
        return self.text
notepad = NOtepad()
notepad.new_file()
notepad.append_text('DahyunDarwin')
notepad.save_file('example.txt')

load_text = notepad.get_text()
# print(load_text)

