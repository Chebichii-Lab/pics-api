import requests

response = requests.get('http://127.0.0.1:8000/users')
print(response.json())

response = requests.get('http://127.0.0.1:8000/albums')
print(response.json())

response = requests.get('http://127.0.0.1:8000/photos')
print(response.json())