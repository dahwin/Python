from time import sleep
a="kim dahyun"
b="abcdefghijklmnopqrstuvwxyz "
v=""
for i in a:
    for j in b:
        if i==j:
            v+=j
            continue
        print(v+j)
        sleep(0.02)

