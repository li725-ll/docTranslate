import requests,os
import json,time


def load_sentence():
    header = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36'
    }
    dirs = os.listdir("json")
    if dirs:
        if time.strftime("%Y-%m-%d", time.localtime()) + ".json" in dirs:
            pass
        else:
            for i in dirs:
                os.remove("json/"+i)
    else:
        response = requests.get(url='http://open.iciba.com/dsapi/',params={'date':time.strftime("%Y-%m-%d", time.localtime())},headers=header)  # date参数为空代表今天
        with open("json/"+time.strftime("%Y-%m-%d", time.localtime())+".json", "w", encoding="utf-8") as file:
            file.write(json.dumps(response.json()))


def load_vocabulary(shuru):
    header = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36'
    }
    response1 = requests.get(url="http://dict-co.iciba.com/api/dictionary.php?w="+ shuru +"&type=json&key=金山词霸密钥", headers=header)
    dirs = os.listdir("music/vocabulary")
    if len(dirs) >= 50:
        for i in dirs:
            os.remove("music/vocabulary/" + i)
        try:
            response2 = requests.get(response1.json()['symbols'][0]['ph_en_mp3'], headers=header)
            print(response2)
            with open("music/vocabulary/" + shuru + ".mp3", "wb") as file:
                file.write(response2.content)
            return ",".join(response1.json()['symbols'][0]['parts'][0]['means']) + '。'
        except:
            return "出错了哦"
    else:
        if shuru+".mp3" in dirs:
            return ",".join(response1.json()['symbols'][0]['parts'][0]['means'])+'。'
        else:
            try:
                urls = [response1.json()['symbols'][0]['ph_en_mp3'],response1.json()['symbols'][0]['ph_am_mp3'],response1.json()['symbols'][0]['ph_tts_mp3']]
                
                for url in urls:
                    if url:
                        URL = url
                        break
                
                response2 = requests.get(url=URL, headers=header)
                print(response2)
                with open("music/vocabulary/"+shuru+".mp3","wb") as file:
                    file.write(response2.content)
                return ",".join(response1.json()['symbols'][0]['parts'][0]['means'])+'。'
            except Exception:
                return "出错了哦"
