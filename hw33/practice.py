import requests


def read_from_file(filename):
    with open(filename, 'r') as f:
        text = f.read()
    return text


def write_to_file(filename, text):
    with open(filename, 'w', encoding='UTF-8') as f:
        f.write(text)


def translate_it(text, source_lang, result_lang):
    """
    YANDEX translation plugin

    docs: https://tech.yandex.ru/translate/doc/dg/reference/translate-docpage/

    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]

    :param text: <str> name of the file with text for translation.
    :param source_lang: <str> language of original file.
    :param result_lang: <str> language of translation.
    :return: <str> translated text.
    """
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    key = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'

    params = {
        'key': key,
        'lang': '{}-{}'.format(source_lang,result_lang),
        'text': read_from_file(text),
    }
    response = requests.get(url, params=params).json()

    write_to_file('result.txt', ' '.join(response.get('text', [])))
    return ' '.join(response.get('text', []))


a = translate_it('FR.txt', 'fr', 'ru')
print(a)




