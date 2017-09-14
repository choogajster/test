
from urllib.parse import urlencode
import requests
import time
import itertools

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
# print(token_url)

access_token = 'cc8aa3138445ca6e459cd794b6c95f7bf78f0e661203073fd3cef5b27f3ab940b676fd8482d744915ef25'

params = {
    'access_token': access_token,
    'v': '5.68',
    'user_id': ''
}


def get_friends():
    response = requests.get('https://api.vk.com/method/friends.get', params)
    friends = response.json()['response']['items']
    print(friends)
    return friends


def get_friends_of_friends(fr_list):
    friends_of_friends = []
    for friend in fr_list:
        params['user_id'] = friend
        response = requests.get('https://api.vk.com/method/friends.get', params)
        result = response.json()['response']['items']
        # print(friend, result)
        friends_of_friend = {'Id':friend, 'List': result}
        friends_of_friends.append(friends_of_friend)
        time.sleep(1)
        print(friends_of_friends)


def get_mutual_friends(source, target):
    params['source_uid'] = source
    params['target_uid'] = target
    response = requests.get('https://api.vk.com/method/friends.getMutual', params)
    friends = response.json()['response']
    print('Source: {}; Target:{}'.format(source, target))
    print('Quantity: {}; List of ids:{}\n'.format(len(friends), friends))
    return friends


def get_all_mutual_friends(friend_list):
    for x,y in itertools.combinations(friend_list, 2):
        get_mutual_friends(x, y)
        time.sleep(0.4)

# get_friends()
# get_mutual_friends('2173154', '2197844')
get_all_mutual_friends(get_friends())

