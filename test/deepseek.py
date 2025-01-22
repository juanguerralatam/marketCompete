import requests

# Ollama API URL
OLLAMA_API_URL = "http://localhost:11434/api/chat"

# JSON payload
payload = {
    "model": "deepseek-r1",
    "messages": [
        {
            "role": "user",
            "content": "in 5 words why is the sky blue?, give me the answer in JSON format "
        }
    ],
    "stream": False
}

# Send the request to the Ollama API
response = requests.post(OLLAMA_API_URL, json=payload)

# Check if the request was successful
if response.status_code == 200:
    print("Response from Ollama:")
    print(response.json())  # Print the JSON response
else:
    print(f"Error: {response.status_code}")
    print(response.text)
