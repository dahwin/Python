# class Dahwin():
#     dubu:str='dubu'
#     dahwin:str='dahwin'
#     dahyun:str='dahyun'
#     darwin:str='darwin'

import os

# Specify the folder path you want to check
folder_path = r"C:\Users\ALL USER\Desktop\Python"

# Specify the size threshold in bytes (100 MB)
size_threshold = 100 * 1024 * 1024  # 100 MB in bytes

# Iterate over the files in the folder
for root, dirs, files in os.walk(folder_path):
    for file in files:
        file_path = os.path.join(root, file)
        file_size = os.path.getsize(file_path)

        if file_size > size_threshold:
            print(f"File: {file_path} is larger than 100 MB ({file_size / (1024*1024):.2f} MB)")


    