import requests
url = "https://raw.githubusercontent.com/Almagesth/tsiattista-dataset/main/tsiattista.json"
response = requests.get(url)
data = response.json()
print(data[0]["title"])