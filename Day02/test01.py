# 爬取一章小说
import requests#导入requests库，用于获取网页内容
from bs4 import BeautifulSoup  # 从bs4库中导入BeautifulSoup

url = "http://www.ibiqu.org/0_844/636719.html"  # 笔趣阁的斗破苍穹网址，这里只爬取一章
# response = requests.get(url)
# headers 里面的参数内容是从百度里面找的，不然会被反爬虫
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.68"
    # ,
    # "cookie": "HMACCOUNT=8A281AB7DA3B5C6B; HMACCOUNT_BFESS=8A281AB7DA3B5C6B; HMTK=1; BDUSS_BFESS=Vh2c1ZHdjlWUlBWTTYtdlhiaXRGaVJVQ0RaNDlwSS1XVGozSXk5SDhsSHRyNU5rSVFBQUFBJCQAAAAAAAAAAAEAAADe71fXYmVuSHVhbmdiZW4xODUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAO0ibGTtImxkS; BAIDUID_BFESS=98C710950966798F01125E87813FD247:FG=1; ZFY=nIW4thkPzzC4MdJiK3ktFbjKRl9EplO8PeGw9EU2tH0:C; ab_sr=1.0.1_ZDE1MDhkNGY2OGVmZTU0YzE2ZmMwYjEwZGZhYmFjM2MwZDMwYzA5M2FkYThkNjY5YTZlZTZmMmJmZDMxNzVkMmJlOTQ2NzE2MjMyZjA5NjI2ZTkwZTk5NTFjNGVlZWFkZGQ5NzZlZDk2NmE2NjcwYTQwZTY4YWQ2OTk5ZjA5Yjc3Y2Q0MTI5Y2JiNjVlZjIxOTE0ODAzMmI3YzY3YzJlYw=="}
}
response1 = requests.get(url, headers=headers)

# print(response1.text)

# 将文本数据转换成BeautifulSoup对象
# bs=BeautifulSoup(response1.content,"html5lib")#html5lib是解析器,需要pip install html5lib
bs = BeautifulSoup(response1.content, "html.parser")  # 同上

bs_find = bs.find('div', attrs={'id': 'content'})
# print(bs_find)
# print("\n")


book_list = bs_find.findAll('p')  # 查找所有的p标签
# print(book_list)#列表
# 遍历数据
# 写入数据
with open('斗破苍穹.txt', 'a', encoding='utf-8') as f:
    for txt in book_list:
        f.write(txt.text)
        f.write("\n")
print("写入完成")
