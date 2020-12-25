import requests
import json

url="http://10.0.18.249/api_jsonrpc.php"
headers={"Content-Type":"application/json-rpc"}

data = {
     "jsonrpc" : "2.0",
     "method" : "template.update",
     "params" : {
        "templateid" : "10086",
         "tags" : [
            {
                "tag" : "DB2",
                 "value" : "{HOST.NAME}"
            }
        ]
    },
     "auth" : "670c9edfa3981adf4dfd62ac7b482f69",
     "id" : 1
}

r = requests.post(url,data = json.dumps(data),headers=headers)
print(r.json())