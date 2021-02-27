import requests
import json

header = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36'
}
response = requests.get(url='http://open.iciba.com/dsapi/',params={'date':'2021-02-07'},headers=header)  # date参数为空代表今天,此处设置的为2021年2月7日
response_next = requests.get(url='http://open.iciba.com/dsapi/',params={'date':'2021-02-07','type':'next'},headers=header)  # type参数为next表示今天的下一天
response_last = requests.get(url='http://open.iciba.com/dsapi/',params={'date':'2021-02-07','type':'last'},headers=header)  # type参数为last表示今天的上一天
print(response.json())  # 以json的格式接收返回的数据，因为file的默认格式为json
print(response_next.json())
print(response_last.json())

