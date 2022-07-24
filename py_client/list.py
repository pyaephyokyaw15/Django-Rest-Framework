import requests
from getpass import getpass

auth_endpoint = "http://127.0.0.1:8000/api/auth/"
username = input("What is your username?")
password = getpass('What is your password?')

# We can also use our crated token.
# fixed_token = 'dded61a06a72c0f6137934765fe9a407c18d5f7e'
# endpoint = "http://127.0.0.1:8000/api/products/list/create/"
# headers = {
#         "Authorization": f"Bearer {fixed_token}",
#     }
# get_response = requests.get(endpoint, headers=headers)
# print(get_response.json())


auth_response = requests.post(auth_endpoint, json={'username': username, 'password': password})
print(auth_response.json())

if auth_response.status_code == 200:
    token = auth_response.json()['token']
    print(token)
    headers = {
        # "Authorization": f"Token {token}",
        "Authorization": f"Bearer {token}",
    }
    endpoint = "http://127.0.0.1:8000/api/products/list/create/"

    get_response = requests.get(endpoint, headers=headers)
    print(get_response.json())
    data = get_response.json()
    next_url = data['next']
    print(next_url)
    # you can run while loop until next_url is None