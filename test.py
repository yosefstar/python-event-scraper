import requests

url = 'https://www.python.org/'

response = requests.get(url)

if response.status_code == 200:
    print('Success')
else:
    print('Failed')
