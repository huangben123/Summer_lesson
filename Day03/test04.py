# post请求
# 爬取网址："https://music.163.com/#/song?id=190072"
import requests

url = "https://music.163.com/weapi/comment/resource/comments/get?csrf_token="
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'cookie': 'bid=IvtJHpetnDo; ll="108258"; __utmc=30149280; __utmt=1; __utma=30149280.573424069.1681452459.1686793301.1686793317.4; __utmz=30149280.1686793317.4.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmb=30149280.1.10.1686793317; ap_v=0,6.0; __gads=ID=9bdc14de8e1a2959-2240c51394de002a:T=1681452459:RT=1686793345:S=ALNI_MZD1_aD7LqfrUOMeMqYvydFFGhHJw; __gpi=UID=00000bf4641d88a5:T=1681452459:RT=1686793345:S=ALNI_MYKd2nmI437u9xtmQy4ACXQW7xktg'}

data = {
    'params': 'MLpbh0fdwblWBo7n1Fb8RLfLap340b1ME9hnvKEMIVe/R9d4jTVx9RwdEqUxE61jyfSjrvTUjuoUSKkoWte4cCeNAL5vxFd64RTtVezMac/0s/N7Z1q8VvF+Zek+Wjp4tQnboquSYgyeq4DkY2uD2lCjbU+DAm/NjtB/RkJJm+CR1VjbUUCjuhp5dr8+yivFrX8KtJ88JY97w7rWzh6xzOOxRzEO9+JB7zQprfE9mgvx6M7vE0hgjvvrMxiFpY03yl0jgScLjhxDshDanJfDqg==',
    'encSecKey': 'b99f460b6372169c738de67e58dbca4bdec07852fd71093eb26f267e57004e9d1e389a09a8556dbe0908465ad41feeb9fe5f1ffbdcaf156153005dff838a123be7facd90f433184e50739f8bdcf1f388361e30d470f7c308ec4c3ec9d71b36f03f2a57d2a513c76026d9f87099e2c7091900745e48ae428f4cececea4d3c6934'}
post = requests.post(url, headers=headers, data=data);  # data是post请求的参数，不加data会报错
response = print(post.json())
for i in response:
    print(i)
