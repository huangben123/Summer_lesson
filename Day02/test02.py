import requests
from bs4 import BeautifulSoup  # 从bs4库中导入BeautifulSoup

url = "https://www.bbiquge.net/book/133312/56524593.html"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.68",

}
response = requests.get(url, headers=headers)
# print(response.text)
bs = BeautifulSoup(response.content, "html.parser")  # 同上
title = bs.find('title')
print(title.text)
content = bs.find('div', attrs={'id': 'content'})
# print(content.text)
for txt in content:
    print(txt.text)

with open('斗破苍穹第一章.txt', 'a', encoding='utf-8') as f:
    for txt1 in content:
        f.write(txt1.text)
