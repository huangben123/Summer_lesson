# 获取京东手机页面的所有信息
import time
import csv
import os
# pip install selenium==3.141.0
# 谷歌浏览器
# https://npm.taobao.org/mirrors/chromedriver/
# https://registry.npmmirror.com/binary.html?path=chromedriver/#这里下载chrome的驱动，下载对应的版本，将压缩包里面的exe复制到：C:\Program Files\Google\Chrome\Application里面,还要复制到python的目录下
# 挂载驱动
from selenium import webdriver

# 防止浏览器自动关闭
# option=webdriver.ChromeOptions()#创建一个配置对象
# option.add_experimental_option('detach',True)#让浏览器不要自动关闭
# web=webdriver.Chrome(options=option)#挂载驱动
# 挂载驱动
web = webdriver.Chrome()
# 发送请求
web.get("https://www.jd.com/")  # 打开京东网页
web.maximize_window()  # 控制浏览器最大化
# 再页面上定位元素
web.find_element_by_xpath('//*[@id="key"]').send_keys('手机')  # 控制搜索框输入手机
web.find_element_by_xpath(  # 控制搜索按钮点击
    '//*[@id="search"]/div/div[2]/button').click()  # xpath中填入：检查->选中搜索按钮->在源码标签中右键->copy->copy xpath
# --------------新版浏览器-如下配置---------------
# from selenium.webdriver.common.by import By
# web.find_element(By.XPATH,'//*[@id="key"]').send_keys('手机')
time.sleep(3)  # 等待3秒


def getLen():
    web.execute_script('window.scrollTo(0,document.body.scrollHeight)')  # 执行js脚本，滚动到页面底部，
    time.sleep(3)  # 等待3秒
    lens = len(web.find_elements_by_xpath('//*[@id="J_goodsList"]/ul/li'))
    print(lens)
    for i in range(1, lens + 1):
        getUtil(i)
    global num
    num += 1


def getUtil(a):  # a表示第几个商品
    # print(a)
    text1 = web.find_element_by_xpath(f'//*[@id="J_goodsList"]/ul/li[{a}]/div/div[3]/strong/i').text  # 获取价格
    text2 = web.find_element_by_xpath(f'//*[@id="J_goodsList"]/ul/li[{a}]/div/div[4]/a/em').text  # 获取手机配置
    uid = web.find_element_by_xpath(f'//*[@id="J_goodsList"]/ul/li[{a}]/div/div[8]').get_attribute('id')  # 获取id属性的值
    try:
        text3 = web.find_element_by_xpath(f'//*[@id="{uid}"]/ i[1]').text  # 判断是不是自营店
    except:
        text3 = "零售"
    with open(f'{path_name}/jd.csv', 'a', newline='', encoding='utf-8') as f:
        csv_write = csv.writer(f)
        csv_write.writerow([text1, text2, text3])
    print(f'第{num}页第{a}个商品信息写入成功！')
    # // *[ @ id = "J_pro_100052892476"]


path_name = '../Day03/jd'
if not os.path.exists(path_name):
    os.mkdir(path_name)


# //*[@id="J_bottomPage"]/span[1]/a[9]  # 翻页按钮
def sk():
    web.find_element_by_xpath('//*[@id="J_bottomPage"]/span[1]/a[9]').click()  # 点击进入下一页
    time.sleep(3)  # 等待3秒

num=0#记录翻页次数
if __name__ == '__main__':
    while True:
        getLen()
        if num == 10:#翻页10次
            break
        else:
            sk()
    getLen()
