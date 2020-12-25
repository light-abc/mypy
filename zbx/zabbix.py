import requests
import json

url="http://10.0.18.245/api_jsonrpc.php"
headers={"Content-Type":"application/json-rpc"}
datac={
     "jsonrpc": "2.0",
     "method": "item.update",
     "params": {
        "itemid": "51696",
        "key_": "sar.cpu[27]"
    },
     "auth": "a7ed4f4b0d01e4813eb4d8bc27c4ba2f",
     "id": 1
}

datam={
     "jsonrpc": "2.0",
     "method": "item.update",
     "params": {
        "itemid": "51847",
        "key_": "sar.mem[27]"
    },
     "auth": "a7ed4f4b0d01e4813eb4d8bc27c4ba2f",
     "id": 1
}

rc = requests.post(url,data = json.dumps(datac),headers=headers)
rm = requests.post(url,data = json.dumps(datam),headers=headers)
print(rc.json())
print(rm.json())