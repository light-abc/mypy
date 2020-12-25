import requests
import json

url="http://192.168.0.146/api_jsonrpc.php"
headers={"Content-Type":"application/json-rpc"}
n=""

for i in range(10083,10086):
    n=i + 1
    a=int(n)
    print(a)
    data = {
     "jsonrpc" : "2.0",
     "method" : "host.update",
     "params" : {
       "hostid" : a,
        "templates" : [
            {
                "templateid": "10001"
            },
            {
                "templateid": "10316"
            }
        ]
     },
     "auth" : "faebfb518597ed169ecac69e9b03f73f",
     "id" : a
    }

    r = requests.post(url,data = json.dumps(data),headers=headers)
    print(r.json())