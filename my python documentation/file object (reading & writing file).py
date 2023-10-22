# # read file
# with open('media\\file.txt') as f :
#     print(f.read())
#
#
# # write file
#
# text = 'looooooooovvvvvvvvvvvvvveeeeeeeeee you dahyun'
#
# with open('media\\file_copy.txt','w') as fi :
#     fi.write(text)
#
# # copy text file
#
# with open('media\\file_copy.txt','r') as rt:
#     with open('media\\file_copy_copy.txt','w') as wt:
#         for copy in rt:
#             wt.write(copy)

# copy file
with open('G:\\ratul\\video\\Video\\twice\\feel.mp4','rb') as rf:
    with open('G:\\ratul\\video\\Video\\twice\\dahyun.mp4','wb') as wf:
        for copy in rf:
            wf.write(copy)

