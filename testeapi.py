import requests

url = "https://whatsapp2.contrateumdev.com.br/getAllGroups"

payload = "{\n    \"session\": \"1234\"\n}"
headers = {
  'sessionkey': '1234'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)