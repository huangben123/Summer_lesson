# wD8o9sOR basePlayerContainer N3wGggaQ danMuPlayerStyle midControlHigh modalPlayer xgplayer xgplayer-pc replay xgplayer-playing xgplayer-inactive
import requests
import os
from bs4 import BeautifulSoup
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.68"
    ,
    "cookie": "HMACCOUNT=8A281AB7DA3B5C6B; HMACCOUNT_BFESS=8A281AB7DA3B5C6B; HMTK=1; BDUSS_BFESS=Vh2c1ZHdjlWUlBWTTYtdlhiaXRGaVJVQ0RaNDlwSS1XVGozSXk5SDhsSHRyNU5rSVFBQUFBJCQAAAAAAAAAAAEAAADe71fXYmVuSHVhbmdiZW4xODUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAO0ibGTtImxkS; BAIDUID_BFESS=98C710950966798F01125E87813FD247:FG=1; ZFY=nIW4thkPzzC4MdJiK3ktFbjKRl9EplO8PeGw9EU2tH0:C; ab_sr=1.0.1_ZDE1MDhkNGY2OGVmZTU0YzE2ZmMwYjEwZGZhYmFjM2MwZDMwYzA5M2FkYThkNjY5YTZlZTZmMmJmZDMxNzVkMmJlOTQ2NzE2MjMyZjA5NjI2ZTkwZTk5NTFjNGVlZWFkZGQ5NzZlZDk2NmE2NjcwYTQwZTY4YWQ2OTk5ZjA5Yjc3Y2Q0MTI5Y2JiNjVlZjIxOTE0ODAzMmI3YzY3YzJlYw=="}  # 伪装成浏览器

url = 'https://www.douyin.com/user/MS4wLjABAAAAKvs9R7M8tcakgst9WPELG47Pvs9w6ruO5ua2EENemSw?vid=7242686292738247992'
response = requests.get(url,headers=headers)
print(response)
soup = BeautifulSoup(response.content, 'html.parser')
print(soup)
