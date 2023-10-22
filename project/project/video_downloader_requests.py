import requests
url = 'https://www.pinterest.com/pin/609745237065695603/'
response = requests.get(url)

# Save the video to a file
with open("pinterest.mp4", "wb") as f:
    f.write(response.content)
