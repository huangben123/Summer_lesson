print("欢迎来到python的世界")
# 列表-------------------------------------
a = [1, 3, 4, 5, 2];
a.insert(0, 10);  # 在0位置插入10
a.index(1);  # 返回1的位置
a.append(11);  # 在末尾插入11
a.append("yumazi");


print("排列前", a)
print("index", a.index(1));
a.pop();  # 删除末尾元素
a.remove(1);  # 删除第一个1,根据值删除
a.pop(0);  # 删除第一个元素
# a.sort();
# 元组 保障数据安全-------------------------------------
b = (1);  # 不可变
b = (1,);  # 在元组中只有一个元素时，需要在元素后面添加逗号
b = (1, 2, 3);  # 不可变
print("元组", b)
print("b的类型是", type(b))
print("b解包之后是", *b)  # 解包
print("转换类型之后的b的类型是", type(list(b)))  # 要修改里面的值的时候，转换为列表
print("b解包之后是", *b)  # 解包
# 字典-------------------------------------
c = {1: "helloworld", 2: "yumazi", 3: "hb"};
c.update({2: "yumazi"});
c.pop(2);
print("排列后", a)
print(b)
s = set();
s.add(1);
s.pop();
s.add(2)
print("s集合", s)
print("c字典", c)
c[1]="你好"#将key为1的值改为你好
print("修改之后c字典", c)
print("c.get(1)是",c[1])#如果没有这个key，会报错
#print(c.get(1))#get方法，如果没有这个key，返回None
print("c.get(2)是",c.get(2))#get方法，如果没有这个key，返回None
print("c.get(2,3)是",c.get(2,"没有这个值"))#get方法，如果没有这个key，返回没有这个值
print("c.get(1,3)是",c.get(1,"没有这个值"))#get方法，如果没有这个key，返回没有这个值

del c[1]#删除key为1的值
print("删除之后c字典", c)
#清空字典
c.clear()
print("清空之后c字典", c)
c={};#清空字典
print("清空之后c字典", c)
cc={1: "helloworld", 2: "yumazi", 3: "hb"};
#set集合  去重功能-------------------------------------
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1];
set(list1);
print("set去重之后", set(list1))
#修改集合要进行强制转换为list
print("去重后的set集合转化为list之后", list(set(list1)));
print("将字典的key转化为列表",list(cc))#将字典的key转换为列表

#字符串----------------------------------------
a=1;
b=a;
print(a,b)
b=2;
print(a,b)

str="helloworld"
print(str[0:5])#切片
print(str[0:5:2])#切片
print(str[-5:-1])#切片  worl：-1是最后一个元素，-2是倒数第二个元素
print(str[-5:])#切片
print(str[2:-1])#切片 从第二个元素开始到倒数第二个元素
str="111|222|333|444|555";
print(str.replace("|","-"))#替换
print(str.split("|"))#切片
print(str.split("|")[0])#切片

#字符串拼接：
str1="helloworld"
str2="yumazi"
print(str1+str2);
print(str.split("|"))#切片
print(str1.join(str.split("|")));#将列表中的元素用str1拼接起来
name=input("请输入");#输入的是字符串
str11=f"hello {name}";#f表示格式化字符串
print(str11);
num=1;
# print(str(num))#将数字转换为字符串

age=int(input("请输入你的年龄："))#将字符串转换为数字
sex=input("请输入你的性别：")
print("年龄为",age)
print("年龄类型为",type(age))
print("性别的类型为",type(sex))
#换行
print("hello\nworld")
