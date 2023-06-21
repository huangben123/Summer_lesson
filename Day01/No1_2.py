# 分支循环

# if 2 < 1:
#     pass  # 占位符
# if 2 > 1:
#     print("2>1")
# elif 2 == 1:
#     print("2=1")
# else:
#     print("2<1")
# num = int(input("请输入一个数字"))
# if num > 18:
#     print("成年人")
# else:
#     print("未成年人")
# num = random.randint(1, 10)
# num1 = int(input("请输入一个数字0-10"))
# if num == num1:
#     print("猜对了")
# elif num > num1:
#     print("猜小了")
# else:
#     print("猜大了")
# print("随机数是", num)
# 循环----------------------------------------
# for i in range(1, 10, 2):  # 1-9步长为2
#     print(i, end=" ")  # end=" "表示不换行
# while True:
#     print("helloworld")
#     break  # 跳出循环
# --------------------------------------------
# num1 = random.randint(1, 101);
# while True:
#     for i in range(0, 3):
#         num2 = int(input("请输入一个数字1-100\n"))
#         if num1 == num2:
#             print("猜对了")
#             break;
#         elif num1 > num2:
#             print("猜小了,你还有", 2 - i, "次机会")
#         else:
#             print("猜大了,你还有", 2 - i, "次机会")
#     break
#
# dict = {1: 2, 2: 3, 3: 4, 4: 5}
# for i, j in enumerate(dict):
#     print(i, j);

# 函数-------------------------------------------
def add(a, b):
    return a + b;


def add1(a=1, b=2):
    return a + b;


def printHello():
    print("hello");


def max(a, b):
    return a if a > b else b  # 三元运算符


def sort(alist):
    for i in range(0, len(alist)):
        for j in range(i + 1, len(alist)):
            if alist[i] > alist[j]:
                alist[i], alist[j] = alist[j], alist[i]
    return alist


# 匿名函数
function = lambda x, y: x + y

a = 10
b = 5
print(add(a, b))
print("max is:", max(a, b))
printHello()
list1 = [1, 3, 2, 4, 5, 10, 8, 7, 6]
print(sort(list1))
print(add1(10, 10))
print("匿名方法", function(10, 10))
print("---------------------------------------------------")
# 全局变量
num = 10


def test():
    global num  # 声明全局变量才能修改这个变量,否则只能访问，但是全局变量不会改变
    num = 20
    print("test", num)


print("外面的全局变量没有变：", num)

test()
print("---------------------------------------------------")
# 内嵌函数
# map(方法名，计算体)
list1 = [1, 2, 3, 4, 5, 6]


def count(x):
    return x + 1


print(list(map(count, list1)))
print(list(map(lambda x: x + 1, list1)))  # 匿名函数
print("---------------------------------------------------")
# zip
print("--------------zip---------------")
list2 = [6, 7, 8, 9, 10]
print(list(zip(list1, list2)))
print(tuple(zip(list1, list2)))
print(dict(zip(list1, list2)))

print("---------------------------------------------------")


# filter(方法名，计算体)--------------
print("-------------------------filter-----------------------")
def filter1(x):
    return x > 3


print(list(filter(filter1, list1)))
print(list(filter(lambda x: x % 2 == 0, list1)))

# sorted(方法名，计算体)----------------
print("-------------------------sorted-----------------------")
list3 = [1, 5, 3, 9, 6, 0, 2]
print(sorted(list3))
print(sorted(list3, reverse=True))  # 倒序

print("---------------------------------------------------")
# 求最小值
print(min(list1))
# 求和
print(sum(list1))
# 求长度
print(len(list1))
# 求绝对值
print(abs(-10))
# 求幂
print(pow(2, 3))
# 求商和余数
print(divmod(10, 3))
# 求round
print(round(10.5))
# 求round
print(round(10.4))
# 求round
print(round(10.6))
