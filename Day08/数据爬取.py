# 爬取豆瓣网址电影的短评并写入到csv文件中
import requests
import os
from bs4 import BeautifulSoup
import csv
import time


nums = 0  # 用于记录评论数


def getTable(num):
    # 获取短评
    url = f"https://movie.douban.com/subject/1292052/comments?start={num}&limit=20&status=P&sort=new_score"
    # url = f"https://movie.douban.com/subject/35711450/comments?start={num}&limit=20&status=P&sort=new_score"  # 主页
    url1 = "https://movie.douban.com/subject/35711450/comments?start=0&limit=20&status=P&sort=new_score"  # 主页
    url2 = "https://movie.douban.com/subject/35711450/comments?start=20&limit=20&status=P&sort=new_score"  # 每一页start的值增加20
    headers = {
        'user-agent':
            "'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'"
        ,
        'cookie':
            'bid=IvtJHpetnDo; __yadk_uid=DFV1ZTyivH9ZbPq3MFJQUVWZcBNYM566; ll="108258"; __utmz=30149280.1686793317.4.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmz=223695111.1686793321.3.2.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _pk_id.100001.4cf6=5737f89bf3526cf1.1681452459.; _vwo_uuid_v2=D0141D5CCE68AEB41C766B408768FB3A4|3b438585d5e7d6f65d2af226ce626fe1; __gads=ID=9bdc14de8e1a2959-2240c51394de002a:T=1681452459:RT=1686793345:S=ALNI_MZD1_aD7LqfrUOMeMqYvydFFGhHJw; __gpi=UID=00000bf4641d88a5:T=1681452459:RT=1686793345:S=ALNI_MYKd2nmI437u9xtmQy4ACXQW7xktg; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1687173941%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.4cf6=1; __utma=30149280.573424069.1681452459.1686798082.1687173942.6; __utmb=30149280.0.10.1687173942; __utmc=30149280; __utma=223695111.255182283.1681452459.1686798082.1687173942.5; __utmb=223695111.0.10.1687173942; __utmc=223695111; ap_v=0,6.0; ucf_uid=553f38e2-4761-4e22-ae3e-c9629f76ee0d; _pbjs_userid_consent_data=3524755945110770; cto_bundle=mu-kkF9UM2glMkZrbjhuN3JPamMlMkJOMDdsb0w0ckVCektyVGRwczUzeTJPVUN3QW5CbFdkVG5VY2NST255OUtFcmZqODNDTEVlWlhkUGxyd21ITTE1YkR6ZU5EQVdQWG9ZN05ZemlCbWU0dlNYZXhSSDZVU1FGeTg4UlJRZG9FZENTWnR4QXBnMmdrcG80WE94ZEluQkdMSTIwQXpBJTNEJTNE; cto_bidid=ryCfeV9Fc2U5b1gyVlFUSFB4ZkRZZTVoRTlaY3dNVUpQQ2k1aGZ4Q0xMUUlSZFZKejhEUUVCU1lXdWxoUzFZSEdoJTJCcG0xaWJQbWQ1cVlicG9QTWRURkVRUmlSM0glMkIlMkJyWmZBWUNKUCUyRmFWdHJDemlRJTNE'
    }
    response = requests.get(url, headers=headers)
    # print(response.text)
    bs = BeautifulSoup(response.content, "html.parser")  # 解析网页
    # print(bs)

    bs_find = bs.find('div', attrs={'class': 'review-list'})  # 找到整个评论区的div
    # print(bs_find)
    bs_find2 = bs_find.find_all('div', attrs={'class': 'main '})  # 找到所有评论区的div
    # print(bs_find2)
    movie_name = bs.find('div', attrs={'id': 'content'}).find('h1').text  # 找到电影名字
    print(f"电影名字：{movie_name}\n")
    for i in bs_find2:
        global nums
        nums += 1  # 记录评论数
        name = i.find('span', attrs={'class': 'comment-info'}).find('a').text  # 找到评论者的名字
        score = i.find('span', attrs={'class': 'rating'})  # 找到评论者的评分
        if score is None:
            score = "未评分"
        else:
            score = score.get('title')
        time = i.find('span', attrs={'class': 'comment-time'})
        time = time.get('title')  # 找到评论时间
        comment = i.find('p').text.replace('\n', '')  # 找到评论内容
        # print(f"评论者：{name}\n评分：{score}\n评论时间：{time}\n评论内容：{comment}\n")
        # --------------------------------写入csv文件-------------------------------
        with open(f'Comments/{movie_name}.csv', 'a', newline='', encoding='utf-8-sig') as f:  # utf-8-sig解决乱码问题
            writer = csv.writer(f)
            writer.writerow([name, score, time, comment])
            print(f"评论者：{name}\n评分：{score}\n评论时间：{time}\n评论内容：{comment}\n")
        print(f"{name}的评论写入成功")
        print(f"爬取{nums}条评论\n")


if __name__ == '__main__':
    start = int(input("输入开始的页数："))
    total = int(input("输入结束的页数："))
    for i in range(start, total):
        try:
            getTable(i * 20)  # 爬取10页
        except:
            print("爬取失败")
            continue
        time.sleep(1)  # 爬取一次休息一秒
    print("爬取完成")
