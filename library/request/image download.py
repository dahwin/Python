import requests
r = requests.get("https://lh3.googleusercontent.com/TxunDRctVjMvJ_IoggvxNapGfPEkQ4mhwmT6T_XYEfoM_Qkqm8PoD-vOyDVjvVrzFemwDc3ttw6uZfpNyddvUozJBtyoXJpF=w780-rj-l80-nu-e365")
j = requests.get('https://www.pinterest.com/pin/609745237065106553/','rb')
t = open('dahyun00.mp4', 'wb')
for u  in j :
    t.write(u)