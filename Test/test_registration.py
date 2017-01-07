import json
import urllib.request
import urllib.parse

data = {
    'telphone': '15858284229',
    'password': 'xnxn`fw`1993',
    'nickname': '这个'
}

data = urllib.parse.urlencode(data).encode()

request = urllib.request.Request('http://127.0.0.1:8088/registration', data, method='POST')

response = urllib.request.urlopen(request).read().decode()

print(json.loads(response))
