import  os
path1 = 'C:\\Users\\Shofiullah\\Desktop\python\\my python documentation\\json.py'
path2 = 'C:\\Users\\Shofiullah\\Desktop\python\\my python documentation\\media'
if os.path.exists(path1):
    print('exist')
    if os.path.isfile(path1):
        print('this is a file')
    if os.path.isdir(path2):
        print('exist folder')

else:
    print('no')