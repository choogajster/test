import pprint
from urllib.parse import urlencode
import requests

URL = 'https://oauth.vk.com/authorize'
ID_APP = '6184907'
REDIRECT_URI = ''

auth_data = {
    'client_id': ID_APP,
    'display': 'popup',
    'response_type': 'token',
    'scope': 'status,friends',
    'v': '5.68'
}

token_url = '?'.join((URL, urlencode(auth_data)))
print(token_url)

access_token = 'cc8aa3138445ca6e459cd794b6c95f7bf78f0e661203073fd3cef5b27f3ab940b676fd8482d744915ef25'

params = {
    'access_token': access_token,
    'v': '5.68'
}
response = requests.get('https://api.vk.com/method.status.get', params)
print(response)
