import json
import requests
url = 'https://api.gcorelabs.com/cdn/public-ip-list'
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    arr = data['addresses']
    arrv6 = data['addresses_v6']  
    with open('GcoreCDN-ip.txt', 'w') as f:
        for value in arr:
            f.write(value + '\n')
    with open('GcoreCDN-ipv6.txt', 'w') as f:
        for value in arrv6:
            f.write(value + '\n')
    print("Succeed")
else:
    print('网络请求失败')

