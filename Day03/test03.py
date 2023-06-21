# Json数据解析get请求
# 爬取网址：https://101.qq.com/#/hero
import requests
import csv
import os

path_name = 'LOL';
if not os.path.exists(path_name):
    os.mkdir(path_name)
url = "https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js?ts=2811332"
response = requests.get(url).json()
# print(response)
print(len(response['hero']))  # hero键下面值（列表）的长度
for i in response['hero']:
    # print(i['name'], i['alias'], i['title'], i['heroId'])
    name = i['name']
    alias = i['alias']
    title = i['title']
    heroId = i['heroId']
    with open(f'{path_name}/hero.csv', 'a', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([name, alias, title, heroId])
