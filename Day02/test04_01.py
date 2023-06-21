#测试爬取小说
import requests
from bs4 import BeautifulSoup  # 从bs4库中导入BeautifulSoup

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.68"
    ,
    "cookie": "HMACCOUNT=8A281AB7DA3B5C6B; HMACCOUNT_BFESS=8A281AB7DA3B5C6B; HMTK=1; BDUSS_BFESS=Vh2c1ZHdjlWUlBWTTYtdlhiaXRGaVJVQ0RaNDlwSS1XVGozSXk5SDhsSHRyNU5rSVFBQUFBJCQAAAAAAAAAAAEAAADe71fXYmVuSHVhbmdiZW4xODUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAO0ibGTtImxkS; BAIDUID_BFESS=98C710950966798F01125E87813FD247:FG=1; ZFY=nIW4thkPzzC4MdJiK3ktFbjKRl9EplO8PeGw9EU2tH0:C; ab_sr=1.0.1_ZDE1MDhkNGY2OGVmZTU0YzE2ZmMwYjEwZGZhYmFjM2MwZDMwYzA5M2FkYThkNjY5YTZlZTZmMmJmZDMxNzVkMmJlOTQ2NzE2MjMyZjA5NjI2ZTkwZTk5NTFjNGVlZWFkZGQ5NzZlZDk2NmE2NjcwYTQwZTY4YWQ2OTk5ZjA5Yjc3Y2Q0MTI5Y2JiNjVlZjIxOTE0ODAzMmI3YzY3YzJlYw=="}  # 伪装成浏览器
url = "https://www.quge9.cc/book/6427/1.html"  # 小说网址
resopnse = requests.get(url, headers=headers)
print(resopnse.text)
bs = BeautifulSoup(resopnse.content, "html.parser")
bs_find = bs.find('div', attrs={'id': 'chaptercontent'})
print(bs_find)
for i in bs_find:
    print(i.text)
