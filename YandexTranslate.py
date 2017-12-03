import requests

host = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
key = 'trnsl.1.1.20171202T133038Z.284a1f7f3c4c7f0f.3bc14c3826e10105dbf20850e33e1c84136d66e7'


results = requests.get(host, params={'key': key, 'lang': 'en-sv', 'text': 'Hello there my good friend'})
print(results.text[results.text.index('[')+2:results.text.index(']')-1])
