# 文件操作：
# 读写：w 写入，r 读取，a 追加
# 打开一个文件：
# open(文件名，打开方式，编码方式)
f = open('test.txt', 'w', encoding='utf-8')
# 写入内容：
f.write("hello world")
f.write("这个你好")
# 关闭文件：
f.close()
# 读取文件：
f = open('test.txt', 'r', encoding='utf-8')
print(f.read())
f.close()
# 追加内容：
f = open('test.txt', 'a', encoding='utf-8')
f.write("追加内容")
f.close()
# with open('test.txt', 'w', encoding='utf-8') as f:自动关闭文件 f是别名
with open('/Day02/txt\\txt1.txt', 'r', encoding='utf-8') as f:
    print((f.read()))
