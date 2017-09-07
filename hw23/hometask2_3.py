import json
import chardet

# Вроде бы все закончил, спасибо!


def read_from_file(filename):
    with open(filename,'rb') as f:
        data = f.read()
        encoding = chardet.detect(data)
        news = data.decode(encoding['encoding'])
    return json.loads(news)


def get_all_words(my_dict):
    temp_list = []
    result = []
    for i in range(len(my_dict['rss']['channel']['items'])):
        temp_list.append(my_dict['rss']['channel']['items'][i]['description'])
        tmp_result = temp_list[i].split(" ")
        result = result + tmp_result
    return result


def separate_long_words(word_list):
    result = []
    for i in range(len(word_list)):
        if len(word_list[i]) > 6:
            result.append(word_list[i])
    return result


def count_most_frequent(word_list):
    temp = set(word_list)
    fin = {}
    for i in temp:
        fin[i] = word_list.count(i)
    result = (sorted(fin, key=fin.get, reverse=True)[:10])

    return result


def general_result(files=[]):
    for i in range(len(files)):
        file = read_from_file(files[i])
        words = get_all_words(file)
        long_words = separate_long_words(words)
        result = count_most_frequent(long_words)
        header = file['rss']['channel']['description'].split()
        country = header[0]
        print('{} {}:\n{}\n'.format("Топ 10 слов региона",country,result))


general_result(['newscy.json', 'newsit.json', 'newsfr.json', 'newsafr.json'])

