# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

import requests
import json

# Ollama API endpoint for generating responses
OLLAMA_API_URL = "http://localhost:11434/api/chat"

# JSON payload
payload = {
  "model": "deepseek-r1",
  "messages": [
    {
      "role": "user",
      "content": "why is the sky blue?"
    }
  ],
  "stream": False
}

# Convert the payload to a JSON string
json_payload = json.dumps(payload)

# Headers for the POST request
headers = {
    'Content-Type': 'application/json'
}

try:
    # Send the request to Ollama API
    response = requests.post(OLLAMA_API_URL, data=json_payload, headers=headers)
    
    # Check if the request was successful
    response.raise_for_status()
    
    # Print the response text
    print("Status Code:", response.status_code)
    print("Response Body:", response.text)
    
except requests.exceptions.HTTPError as errh:
    print ("Http Error:",errh)
except requests.exceptions.ConnectionError as errc:
    print ("Error Connecting:",errc)
except requests.exceptions.Timeout as errt:
    print ("Timeout Error:",errt)
except requests.exceptions.RequestException as err:
    print ("OOps: Something Else",err)