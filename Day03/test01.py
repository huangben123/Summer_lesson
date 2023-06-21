import csv  # csv 是逗号分隔值的缩写，是一种常用的文本格式，用于存储表格数据，被广泛应用于软件开发、数据库数据导入导出等场景。

filename = "hello.csv"

# 写入一行数据 writerow
# with open(filename, "a", encoding="utf-8", newline='') as csvfile:  # newline=''是为了防止写入的时候出现空行
#     csv.writer(csvfile).writerow(["4", "4", "4", "4", "4", "4", "4", "4", "4", "4", "4"], )  # 写入一行数据，只能写入列表形式的数据

# 插入多行数据 writerows
with open(filename, "a", encoding="utf-8", newline='') as csvfile:  # newline=''是为了防止写入的时候出现空行
    csv.writer(csvfile).writerows([['111', '222'], ['333', '444']])  # 写入一行数据，只能写入列表形式的数据

with open(filename, "r", encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:  # 读取每一行的数据
        print(row)  # 列表形式打印每一行的数据，字符串形式
