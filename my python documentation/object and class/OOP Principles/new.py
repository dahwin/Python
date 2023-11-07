import urllib3
from langchain import tools
x = dir(urllib3)
print('\n'.join(x))
print(len(x))
# import urllib3

# http = urllib3.PoolManager()
# response = http.request('GET', 'http://httpbin.org/robots.txt')

# print(response.status)
# print(response.data)


