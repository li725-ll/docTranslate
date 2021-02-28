import requests
import json,time


def load_sentence():
    header = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36'
    }
    response = requests.get(url='http://open.iciba.com/dsapi/',params={'date':time.strftime("%Y-%m-%d", time.localtime())},headers=header)  # date参数为空代表今天
    with open("json/"+time.strftime("%Y-%m-%d", time.localtime())+".json", "w", encoding="utf-8") as file:
        file.write(json.dumps(response.json()))

