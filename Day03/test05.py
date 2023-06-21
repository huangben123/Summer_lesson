# 控制谷歌浏览器自动打开京东，搜索手机，获取第一个商品的价格和配置
import time

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
web.get("https://www.jd.com/")#打开京东网页
web.maximize_window()#控制浏览器最大化
# 再页面上定位元素
web.find_element_by_xpath('//*[@id="key"]').send_keys('手机')  # 控制搜索框输入手机
web.find_element_by_xpath(  # 控制搜索按钮点击
    '//*[@id="search"]/div/div[2]/button').click()  # xpath中填入：检查->选中搜索按钮->在源码标签中右键->copy->copy xpath
# --------------新版浏览器-如下配置---------------
# from selenium.webdriver.common.by import By
# web.find_element(By.XPATH,'//*[@id="key"]').send_keys('手机')
time.sleep(3)  # 等待页面加载，否则读取不到数据
i_text = web.find_element_by_xpath('//*[@id="J_goodsList"]/ul/li[1]/div/div[3]/strong/i').text  # 获取价格
em_text = web.find_element_by_xpath('//*[@id="J_goodsList"]/ul/li[1]/div/div[4]/a/em').text  # 获取手机配置
p_text = web.find_element_by_xpath('//*[@id="J_goodsList"]/ul/li[1]/div/div[7]/span/a').text  # 获取手机品牌方
print(i_text)
print(em_text)
print(p_text)
