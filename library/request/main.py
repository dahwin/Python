import requests

payload = {'page':2, 'count':25}
p = requests.get('https://www.jype.com', params=payload)

print(p.url)