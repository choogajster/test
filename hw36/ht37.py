from urllib.parse import urlencode
import requests
import time
import itertools

APP_ID = 'b72cf26991b74ddb9884c45bc346f750'
AUTHORIZE_URL = 'https://oauth.yandex.ru/authorize'
# Пароль: 14a7483095d64630894ecdeb66a658cb



auth_data = {
    'client_id': 'ID_APP',
    'display': 'popup',
    'response_type': 'token',
    'scope': 'status,friends',
    'v': '5.68'
}

print('?'.join((AUTHORIZE_URL, url)))