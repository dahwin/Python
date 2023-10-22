import requests
url = 'https://scrolller.com/dahyun-maroon-red-dress-3kgkp6me51'
req = requests.get(url)
filename = req.url[url.rfind("/")+1:]
with open(filename, 'wb')as f:
    for chunk in req.iter_content(chunk_size=8192):
        if chunk:
            f.write(chunk)