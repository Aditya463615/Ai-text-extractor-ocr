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
