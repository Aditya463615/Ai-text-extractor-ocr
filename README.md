# Create your own OCR with the power of Ai
`DocumentPro` is a powerful data extraction tool that **utilizes AI and GPT** for accurate data extraction from various documents. It’s particularly useful for **extracting data from financial, logistics, and ID documents**. Users can create custom parsers for any document, table, or form, enabling a wide variety of use cases.

In addition, DocumentPro is a cloud-native document processing tool that uses AI technology to extract invoices from images and PDFs and export them to CSV. It allows for the effortless extraction of invoice information such as party details, payment terms, and item information, using image and PDF files.



# Building with python 
### Creating Parser 
```python
# this is demo parser for Aadhar details extractor
import requests
import json

url = "https://api.documentpro.ai/v1/templates"

payload = json.dumps({
  "template_title": "AadharFront",
  "template_type": "identity card",
  "template_schema": {
    "fields": [
      {
        "name": "name",
        "type": "text",
        "description": "beside the image, in the middle row of id"
      },
      {
        "name": "date of birth",
        "type": "date",
        "description": "beside the image, in the middle row of id"
      },
      {
        "name": "aadhar",
        "type": "number",
        "description": "a 12 digit number on the bottom"
      }
    ]
  }
})

headers = {
  'x-api-key': '<api key>',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

# If the request was successful, status_code will be 200
if response.status_code == 200:
    print(json.loads(response.content)['template_id'])
else:
    print('Failed to create parser')
```
### Using Parser
```python
import requests
import json
import sys

parser_id = "<parser id>"
apikey = '<api key>'

url = f"https://api.documentpro.ai/files/upload/{parser_id}"
payload = {}
files=[
    ('file',('file.jpeg', open('<file path>','rb'),'application/jpg'))
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
## Create Aadhar extractor parser 
- `Aadhar extractor file` had been given in the resporatiory package as well as explained [above](### Creating Parser ) too.
- Remember to replace the variables [`<file path>`](### Creating Parser), [`<api key`](### Creating Parser ) and [`<parser id>`](### Using Parser) in your file.
## Get your API key
- visit [DocumentPro.ai](https://www.documentpro.ai/) website
- sign in or sign up your account
- create a parser
- open setting tab to get **parser id**
- open account setting to generate **API key**
- free account offers only 30 credits
