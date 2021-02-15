import requests
import hashlib


def fanyi(shuru):
    header = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    appid, salt, key = "百度翻译appid", "随机码", "百度翻译密钥"  # 去百度翻译官网申请注册免费的
    q = shuru
    sign = appid+q+salt+key
    md5 = hashlib.md5()
    md5.update(sign.encode('utf-8'))
    data = {
        "q": q,
        "from": "auto",
        "to": "zh",
        "appid": appid,
        "salt": salt,
        "sign": md5.hexdigest()
    }
    try:
        response = requests.post('https://fanyi-api.baidu.com/api/trans/vip/translate',headers=header, data=data )
        text = response.json()
        # print(text)
        shuchu = text['trans_result'][0]['dst']
        shuchu = fenge(shuchu)
    except KeyError:
        return " 翻译出错！请重试！！"
    
    return shuchu


def fenge(shuchu):  # 加入换行符
    lenstring = len(shuchu)
    liststring = list(shuchu)
    for i in range(0, lenstring, 40):
        liststring.insert(i, '\n')
    return ''.join(liststring)