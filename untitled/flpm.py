import requests

url = 'http://11.140.160.71:1380/login'

headers = {
    'Host':'11.140.160.71:1380',
    'Origin': 'http://11.140.160.71:1380',
    'Referer': 'http://11.140.160.71:1380/login',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.94 Safari/537.36'
}

data = {
    'username': 'dengyaowen.zh',
    'password': 'kevin200711'
}

resp = requests.post(url, data=data, headers=headers)
wiki = requests.get('http://11.140.160.71:1380/wiki/Index')
print(wiki.text.encode('utf-8'))
