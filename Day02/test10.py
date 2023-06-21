# 下载视频
import requests
import os

path_name = 'DOUYIN'
if not os.path.exists(path_name):
    os.mkdir(path_name)
i = 7
# url是你要下载的视频地址
url = 'https://v3-web.douyinvod.com/96991852e33a54349f083c2e7153f545/648aab39/video/tos/cn/tos-cn-ve-15c001-alinc2/oE1aJeB9CnkYGBAcIgO9AcpQQbkH67ADe2oRog/?a=6383&ch=5&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br=578&bt=578&cs=2&ds=4&ft=GN7rKGVVywp5RF780mo~xj7ScoAp-qe_6vrKtpL162o0g3&mime_type=video_mp4&qs=15&rc=MzozZTlmNTczNzg7aGk1ZkBpamw1cTc6ZjQ7ajMzNGkzM0A0LzIyYWA2NmExYC0uXzAxYSMzZGhycjRvYmFgLS1kLS9zcw%3D%3D&l=20230615130819F11C5E522A597E0C58AE&btag=e00028000'

url1 = "https://v26-web.douyinvod.com/e99cd87a9462333fc423d10b9c645861/648aad98/video/tos/cn/tos-cn-ve-15c001-alinc2/oYBTAhIQOfmGLAjQIyhzGmNtEMJygW9iADGA5e/?a=6383&ch=26&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br=2235&bt=2235&cs=0&ds=3&ft=GN7rKGVVywp5RF780mo~xj7ScoAp1Ce_6vrKtpL162o0g3&mime_type=video_mp4&qs=0&rc=ZztnMzk4OTlpZ2lpaDo5OkBpajtxcjk6ZjM5bDMzNGkzM0AzNS4xYzZhXzMxM2IyYGAxYSNqZmsycjQwai9gLS1kLTBzcw%3D%3D&l=202306151319461BCB50E799227F0E58FF&btag=e00010000"
# ctrl+f:xg-video-container
url2 ="https://v26-web.douyinvod.com/f74d81a2bd726d2b058b1b07e55bfc04/648ef097/video/tos/cn/tos-cn-ve-15c001-alinc2/oUeDureJFAZCBwTaDZ9fM76Ca3XbIZHOBWqAQn/?a=6383&ch=42&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br=498&bt=498&cs=2&ds=3&ft=GN7rKGVVywp5RF780mo~xj7ScoAp0-c.6vrKX~U5Yto0g3&mime_type=video_mp4&qs=15&rc=aWQ2PGg3Z2doaGY2NjZkZkBpanJocWY6Zm55bDMzNGkzM0AxMDMxLmJfNWExYC9gXi5gYSNeL2hpcjRvLjJgLS1kLWFzcw%3D%3D&l=202306181854505DDF137B9C627DE38D32&btag=e00008000"
def download(url):
    response = requests.get(url).content
    with open(f'{path_name}/{i}.mp4', "wb") as f:
        f.write(response)
        print("下载完成")
    print(f"i={i}")


if __name__ == '__main__':
    i += 1
    download(url2)
