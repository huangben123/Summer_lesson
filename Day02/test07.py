# 分页爬取图片
import requests  # 导入requests库
import os  # 导入os库
from bs4 import BeautifulSoup  # 从bs4库中导入BeautifulSoup

name_path = 'img2'
if not os.path.exists(name_path):  # 判断文件夹是否存在
    os.mkdir(name_path)  # 创建文件夹

Sum = 0  # 用于记录下载的图片数量


# 获取图片地址
def getUrl(num):
    if num == '1':  # 第一页特殊处理
        url = "https://sc.chinaz.com/tupian/gudianmeinvtupian.html"
    else:
        url = f"https://sc.chinaz.com/tupian/gudianmeinvtupian_{num}.html"  # 图片地址
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
    global Sum
    Sum += 1


if __name__ == '__main__':
    num = input_num = input("请输入要爬取的总页数：[1-7]\n")
    if (int(num) > 7):
        print("输入有误，最大为7")
        exit()
    else:
        for i in range(1, int(num) + 1):
            getUrl(num)
            print(f"第{i}页爬取完成")
        print(f"共下载{Sum}张图片")
