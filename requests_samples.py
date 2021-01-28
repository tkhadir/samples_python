import requests
import ssl


urlList = [
    'http://www.myurl.fr',
]

def call(urlList):
    for u in urlList:
        url = u
        r = requests.get(url, verify=ssl.CERT_NONE)
        print(url + ' : ' + str(r.status_code))

count=0
while count < 100:
    call(urlList)
    count+=1
    
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
content = {'name': 'james-bond'}
r = requests.post(urlList[0], data=json.dumps(content), verify=ssl.CERT_NONE, headers=headers)
print(str(r.status_code))
