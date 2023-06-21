# 爬取古诗词网址的古诗：https://www.gushiwen.cn/
import requests
import os
from bs4 import BeautifulSoup
import csv
import time

totals = 0  # 用于记录爬取古诗的数量

path_name = "古诗"
if not os.path.exists(path_name):  # 判断文件夹是否存在
    os.mkdir(path_name)  # 创建文件夹


def getPoems(num):
    # url1 = "https://www.gushiwen.cn/default_1.aspx"  # 第一页
    # url2 = "https://www.gushiwen.cn/default_2.aspx"  # 第二页
    url = f"https://www.gushiwen.cn/default_{num}.aspx"  # 第num页
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
        'cookie': 'bid=IvtJHpetnDo; ll="108258"; __utmc=30149280; __utmt=1; __utma=30149280.573424069.1681452459.1686793301.1686793317.4; __utmz=30149280.1686793317.4.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmb=30149280.1.10.1686793317; ap_v=0,6.0; __gads=ID=9bdc14de8e1a2959-2240c51394de002a:T=1681452459:RT=1686793345:S=ALNI_MZD1_aD7LqfrUOMeMqYvydFFGhHJw; __gpi=UID=00000bf4641d88a5:T=1681452459:RT=1686793345:S=ALNI_MYKd2nmI437u9xtmQy4ACXQW7xktg'}
    response = requests.get(url, headers=headers)
    # print(response.text)
    bs = BeautifulSoup(response.content, "html.parser")  # 解析网页
    # print(bs)
    bs_find = bs.find('div', attrs={'class': 'main3'})  # 找到古诗的div
    # print(bs_find)
    bs_find_poem = bs_find.find('div', attrs={'class': 'left'})  # 找到古诗的div
    # print(bs_find_poem)
    bs_find_poems = bs_find_poem.find_all('div', attrs={'class': 'sons'})  # 找到所有古诗的div
    # print(bs_find_poem2)
    for i in bs_find_poems:
        with open(f'{path_name}/poem.csv', 'a', newline='', encoding='utf-8') as f:
            try:
                title = i.find('b').text  # 找到标题
                name = i.find('p', attrs={'class': 'source'}).text.replace('\n', '')  # 找到作者
                poem = i.find('div', attrs={'class': 'contson'}).text.replace('\n', '')  # 找到古诗
                # print(f"标题：{title}\n作者：{name}\n古诗：{poem}\n")
                writer = csv.writer(f)
                writer.writerow([title, name, poem])
                print(f"{title}已爬取")
                global totals
                totals += 1
            except:
                # print("爬取失败")#有些古诗不符合规范，会报错，所以用try...except...来捕获异常
                continue

if __name__ == '__main__':
    pages = int(input("输入你要爬取的页数1-n："))
    if pages <= 0:
        print("输入错误")
        exit(0)
    for i in range(1, pages + 1):
        getPoems(i)  # 爬取10页
        print(f"已爬取---------------------------{i}页")
    time.sleep(1)  # 爬取一次休息一秒
    print(f"爬取完成，共爬取{totals}首古诗")
