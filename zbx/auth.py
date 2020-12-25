import requests
import json

url="http://192.168.0.146/api_jsonrpc.php"
headers={"Content-Type":"application/json-rpc"}

#data={"jsonrpc":"2.0","method":"apiinfo.version","id":1,"auth":'null',"params":{}}
data={
    "jsonrpc":"2.0",
    "method":"user.login",
    "params":{
         "user":"Admin",
         "password":"zabbix"
          },
    "id":1,
}

r = requests.post(url,data = json.dumps(data),headers=headers)
print(r.json())