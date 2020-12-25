# urllib.request和urllib.error模块

### urllib.request
import wget
from urllib import request

html = request.urlopen('http://58.222.239.245/images/1.mp4')
print(html.read(10))

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}
print(html.readline())

print(html.read())

url = 'http://58.222.239.245/images/1.mp4'
html = request.urlopen(url)
data = html.read()
with open(r"C:\Users\168\Desktop\1.mp4", 'wb') as fobj:
    fobj.write(data)
