import re
from requests import get, utils

RE_HELLISH_SPELL = re.compile(
    r'((?:[0-9]{1,3}\.){3}[0-9]{1,3})[\s-]+(\[([^\[\]]+)\])\s"([G|H]E..?)\s([/\w\d]+)\s[\w/\.]+"\s(\d\d\d)\s(\d{1,3})')

# Способ 1, через файл, экономно и долго
with open('nginx_logs.txt', 'w', encoding='utf-8') as f:
    response = get('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    f.write(content)
with open('nginx_logs.txt', encoding='utf-8') as f:
    for line in f:
        print(RE_HELLISH_SPELL.findall(line))


# Способ 2, все в ОЗУ
response = get('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs')
encodings = utils.get_encoding_from_headers(response.headers)
content = response.content.decode(encoding=encodings)
print(RE_HELLISH_SPELL.findall(content))
