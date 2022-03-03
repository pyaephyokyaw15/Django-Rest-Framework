import requests

endpoint = "https://httpbin.org/"

get_response = requests.get(endpoint)
print(get_response.text)
