# 爬取单张图片
import requests  # 导入requests库

url = "https://scpic.chinaz.net/files/pic/pic9/202112/hpic4875.jpg"  # 图片地址
response = requests.get(url)  # 获取图片
with open("img/test1.jpg", "wb") as f:  # wb:写入二进制文件
    f.write(response.content)  # 写入图片
print("图片下载完成")
