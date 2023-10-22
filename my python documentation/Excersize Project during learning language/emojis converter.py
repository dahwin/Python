def emojis_converter(o):
    split = o.split(' ')
    emojis = {
        'sad': '😞',
        'happy': '😀',
        'board': '😑',
        'smile': '😊'
    }
    output = ''
    for c in split:
        output += emojis.get(c, c) + " "
        return output
o = input(':')

print(emojis_converter(o))