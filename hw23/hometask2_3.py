import json
import pprint
import chardet



def read_from_file(filename):


    with open(filename,'rb') as f:
        data = f.read()
        encoding = chardet.detect(data)
        news = data.decode(encoding['encoding'])
        jnews = json.loads(news)
    return jnews

def get_all_words(dict):
    temp_list = []
    result = []
    for i in range(len(dict['rss']['channel']['items'])):
        temp_list.append(dict['rss']['channel']['items'][i]['description'])
        tmp_result = temp_list[i].split(" ")
        result = result + tmp_result
    return result



FILE_DATA = read_from_file('newsit.json')
# ALL_WORDS = (get_all_words(FILE_DATA))

get_all_words(FILE_DATA)