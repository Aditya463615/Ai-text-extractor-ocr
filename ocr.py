import requests
import json
import sys

parser_id = "<parser_id>"
apikey = '<api key>'

url = f"https://api.documentpro.ai/files/upload/{parser_id}"
payload = {}
files=[
    ('file',('aadhar.jpeg', open(input('File: '),'rb'),'application/jpg'))
]
headers = {
    'x-api-key': apikey
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)
request_id = json.loads(response.content)['request_id']

url = f"https://api.documentpro.ai/files?request_id={request_id}"

payload = {}
headers = {
    'x-api-key': apikey
}

response = json.loads(requests.request("GET", url, headers=headers, data=payload).text)
while response['response_body']["result_json_data"] == None:
    
    url = f"https://api.documentpro.ai/files?request_id={request_id}"

    payload = {}
    headers = {
        'x-api-key': apikey
    }

    response = json.loads(requests.request("GET", url, headers=headers, data=payload).text)

print(response['response_body']["result_json_data"])
with open('response.ocr','a') as file:
    file.write(str(response['response_body']["result_json_data"]))

input('time to exit')
