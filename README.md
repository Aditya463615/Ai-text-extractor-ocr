
# Create your own OCR with the power of Ai
DocumentPro is a powerful data extraction tool that utilizes AI and GPT for accurate data extraction from various documents. It’s particularly useful for extracting data from financial, logistics, and ID documents. Users can create custom parsers for any document, table, or form, enabling a wide variety of use cases.

In addition, DocumentPro is a cloud-native document processing tool that uses AI technology to extract invoices from images and PDFs and export them to CSV. It allows for the effortless extraction of invoice information such as party details, payment terms, and item information, using image and PDF files.



# Building with python 
```python
import requests
import json
import sys

parser_id = "<your parser id>"
apikey = 'your api key'

url = f"https://api.documentpro.ai/files/upload/{parser_id}"
payload = {}
files=[
    ('file',('file.jpeg', open(input('File: '),'rb'),'application/jpg'))
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
```


![Logo](https://www.documentpro.ai/_next/image/?url=%2F_next%2Fstatic%2Fmedia%2Flogo.10fd3587.png&w=256&q=75)


## Get your API key
- visit [DocumentPro.ai](https://www.documentpro.ai/) website
- sign in or sign up your account
- create a parser
- open setting tab to get **parser id**
- open account setting to generate **API key**
- free account offers only 30 credits
