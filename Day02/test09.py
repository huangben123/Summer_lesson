# 爬取视频
import requests
import os

path_name = 'mp4'
if not os.path.exists(path_name):
    os.mkdir(path_name)
url = "https://www.douyin.com/aweme/v1/play/?video_id=v0200fg10000cgnka9rc77u7u4li98eg&line=0&file_id=9aba0ce3d54744fd88dee179f33e137c&sign=d40bb348733e92b555f43125682446b3&is_play_url=1&source=PackSourceEnum_FEED&aid=6383&device_platform=web&channel=channel_pc_web&app_name=aweme&webid=7240656436697744957&user_agent=Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F112.0.0.0%20Safari%2F537.36&fp=verify_ligtmvbu_2zYlmjsX_EcsJ_4SbU_Apys_NHEyndP1NQP2&did=0&referer=https%3A%2F%2Fcn.bing.com%2F&target=7219064593212034362&downgrade_264=1"
response = requests.get(url).content
with open(f'{path_name}/1.mp4', "wb") as f:
    f.write(response)
    print("下载完成")
