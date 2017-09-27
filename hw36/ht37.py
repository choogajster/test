from pprint import pprint
from urllib.parse import urlencode

import requests

APP_ID = 'b8944ac1d2ba40c18eca3e00135c7f00'
AUTHORIZE_URL = 'https://oauth.yandex.ru/authorize'
# Пароль: 14a7483095d64630894ecdeb66a658cb



auth_data = {
    'response_type': 'token',
    'client_id': APP_ID
}

# print('?'.join((AUTHORIZE_URL, urlencode(auth_data))))
TOKEN = 'AQAEA7qhdYkUAASPy05fDnGUZ0KqrFv41vGwf2A'

params = {
    'preset': 'sources_summary',
    'id': APP_ID,
    'oauth_token': TOKEN
}

management_url = 'https://api-metrika.yandex.ru/management/v1/counters'
stat_url = 'https://api-metrika.yandex.ru/stat/v1/data'
headers = {
    'Content-type': 'application/json',
    'Authorization': 'OAuth {}'.format(TOKEN)
}


def get_counters():
    response = requests.get(management_url, headers=headers)
    print(response.status_code)
    return response.json()['counters']


def get_counter_visits(counter_id):
    params = {
        'id': counter_id,
        'metrics': 'ym:s:visits'
    }
    response = requests.get(stat_url, params, headers=headers)
    return response.json()['data']

counters = get_counters()

for counter in counters:
    pprint(get_counter_visits(counter['id']))


class YandexMetrika:
    management_url = 'https://api-metrika.yandex.ru/management/v1/counters'
    stat_url = 'https://api-metrika.yandex.ru/stat/v1/data'

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-type': 'application/json',
            'Authorization': 'OAuth {}'.format(TOKEN)
        }

    def get_counters(self):
        headers = self.get_headers()
        response = requests.get(self.management_url, headers=headers)
        return response.json()['counters']

    def get_counter_visits(self, counter_id):
        params = {
            'id': counter_id,
            'metrics': 'ym:s:visits'
        }
        response = requests.get(stat_url, params, headers=headers)
        return response.json()

    def get_counter_pageviews(self, counter_id):
        params = {
            'id': counter_id,
            'metrics': 'ym:s:pageviews'
        }
        response = requests.get(stat_url, params, headers=headers)
        return response.json()

    def get_counter_users(self, counter_id):
        params = {
            'id': counter_id,
            'metrics': 'ym:s:users'
        }
        response = requests.get(stat_url, params, headers=headers)
        return response.json()

metr = YandexMetrika(TOKEN)
pprint(metr.get_counter_visits('46092072'))
pprint(metr.get_counter_pageviews('46092072'))
pprint(metr.get_counter_users('46092072'))
