# 爬虫下载一本小说
import time
import requests
import os
from bs4 import BeautifulSoup  # 从bs4库中导入BeautifulSoup
import random  # 导入随机数模块,用于随机生成休眠时间,防止被封IP（这个方法很慢）,还可以用代理IP

# headers随便找一个浏览器的请求头就行
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.68"
    ,
    "cookie": "HMACCOUNT=8A281AB7DA3B5C6B; HMACCOUNT_BFESS=8A281AB7DA3B5C6B; HMTK=1; BDUSS_BFESS=Vh2c1ZHdjlWUlBWTTYtdlhiaXRGaVJVQ0RaNDlwSS1XVGozSXk5SDhsSHRyNU5rSVFBQUFBJCQAAAAAAAAAAAEAAADe71fXYmVuSHVhbmdiZW4xODUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAO0ibGTtImxkS; BAIDUID_BFESS=98C710950966798F01125E87813FD247:FG=1; ZFY=nIW4thkPzzC4MdJiK3ktFbjKRl9EplO8PeGw9EU2tH0:C; ab_sr=1.0.1_ZDE1MDhkNGY2OGVmZTU0YzE2ZmMwYjEwZGZhYmFjM2MwZDMwYzA5M2FkYThkNjY5YTZlZTZmMmJmZDMxNzVkMmJlOTQ2NzE2MjMyZjA5NjI2ZTkwZTk5NTFjNGVlZWFkZGQ5NzZlZDk2NmE2NjcwYTQwZTY4YWQ2OTk5ZjA5Yjc3Y2Q0MTI5Y2JiNjVlZjIxOTE0ODAzMmI3YzY3YzJlYw=="}  # 伪装成浏览器
fileName = "我在精神病院学斩神"
if not os.path.exists(fileName):  # 判断文件夹是否存在
    os.mkdir(fileName)  # 创建文件夹


def book_file(bookName, bookUrl):
    url = f'https://www.quge9.cc/{bookUrl}'  # 小说章节网址
    bookName = bookName
    # 开始下载
    resopnse = requests.get(url, headers=headers)  #
    bs = BeautifulSoup(resopnse.content, "html.parser")  # 转换成bs对象
    bs_find = bs.find('div', attrs={'id': 'chaptercontent'})  # 查找div的id为chaptercontent的标签的内容
    with open(f'{fileName}/{bookName}.txt', 'a', encoding='utf-8') as f:
        f.write(bookName + '\n')  # 写入章节名
        for txt in bs_find:  # 循环写入章节内容
            f.write(txt.text)
    print(f'{bookName}\t下载完成')


def url_list():  # 获取小说章节列表:章节名+章节网址
    url = "https://www.quge9.cc/book/6427/"  # 小说网址
    resopnse = requests.get(url, headers=headers)

    bs = BeautifulSoup(resopnse.content, "html.parser")
    bs_find = bs.find('div', attrs={'class': 'listmain'})
    find_all = bs_find.find_all('a')
    for i in find_all:
        book_Name = i.text
        book_Url = i.get('href')
        # time.sleep(random.randint(1, 3))  # 随机休眠1-3秒,防止ip被封
        try:
            book_file(book_Name, book_Url)  # 调用函数
        except:
            print('下载失败')
            continue


if __name__ == '__main__':
    url_list()  # 调用函数
    print('下载完成')
