# 爬取批量图片
import requests  # 导入requests库
import os  # 导入os库
from bs4 import BeautifulSoup  # 从bs4库中导入BeautifulSoup

name_path = 'img2'
if not os.path.exists(name_path):  # 判断文件夹是否存在
    os.mkdir(name_path)  # 创建文件夹

# 获取图片地址
def getUrl():
    url = "https://sc.chinaz.com/tupian/gudianmeinvtupian.html"  # 图片地址
    response = requests.get(url)
    img_txt = BeautifulSoup(response.content, "html.parser")  # 解析网页
    find = img_txt.find("div", attrs={'class': 'tupian-list com-img-txt-list'})  # 查找图片
    find_all = find.find_all("div", attrs={'class': 'item'})  # 查找所有图片
    for i in find_all:
        url = 'https:' + i.find('img').get('data-original')  # 获取图片地址
        name = i.find('a').text  # 获取图片名字
        # print(name, url)
        try:
            getImg(url, name)  # 调用getImg方法
        except:  # 相当于java中的catch
            print("下载失败");
            continue  # 如果下载失败，跳过

# 下载图片
def getImg(ImageUrl, ImageName):
    response = requests.get(ImageUrl).content  # 获取图片
    with open(f'{name_path}/{ImageName}.jpg', 'wb') as f:  # 保存图片,wb表示写入二进制文件
        f.write(response)
    print(ImageName, "下载完成")


if __name__ == '__main__':
    getUrl()
