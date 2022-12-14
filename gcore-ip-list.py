import json
import requests
url = 'https://api.gcorelabs.com/cdn/public-ip-list'
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    arr = data['addresses']
       
    with open('ip.txt', 'w') as f:
        for value in arr:
            f.write(value + '\n')
else:
    print('网络请求失败')

