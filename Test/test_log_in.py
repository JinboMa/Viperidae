import json
import urllib.request
import urllib.parse

data = {
    'telphone': '13091719005',
    'password': '123456'
}

data = urllib.parse.urlencode(data).encode()

request = urllib.request.Request('http://127.0.0.1:8088/login', data, method='POST')

response = urllib.request.urlopen(request).read().decode()

print(json.loads(response))
