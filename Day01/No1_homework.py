# list1=['Java12','Python34','C56','C++78','Go35','C#29']
# 将列表中的数字组成一个新的列表，数字的下标不变
# 如list2=['12','34','56','78','35',29]
# 自己写一个排序将这个新列表降序排列的函数传递的参数是列表，里面的字符串类型的数值改为int类型。


# 第一题--------------------------------------------------------
list1 = ['Java12', 'Python34', 'C56', 'C++78', 'Go35', 'C#29']
list2 = []



def filter1(x):  # 过滤掉非数字
    if x.isdigit():
        return x


for i in list1:
    list2.append(''.join(filter(filter1, i)))
print(list2)


# 第二题--------------------------------------------------------
list3 = ['12', '34', '56', '78', '35', '29']
toDigit = lambda x: int(x)  # 匿名函数将字符串转换为数字
list3 = list(map(toDigit, list3))  # 利用map函数将list3中的每个元素都转换为数字
print("排序之前：", list3)


# --------------------用冒泡排序和快速排序对list3进行降序排列--------------------
def sort(list):  # 冒泡排序
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            if list[i] < list[j]:
                list[i], list[j] = list[j], list[i];
    return list


print("冒泡排序：", sort(list3))


# 快速排序
def sort1(list):
    if len(list) <= 1:
        return list
    mid, left, right = list[0], 0, len(list) - 1  # 取第一个值为mid
    while left < right:
        while list[right] <= mid and left < right:  # 从右边开始找到第一个大于等于mid的值
            right -= 1
        list[left] = list[right]  # 找到一个大于等于mid的值,将其放在左边
        while list[left] >= mid and left < right:  # 从左边开始找到第一个小于等于mid的值
            left += 1
        list[right] = list[left]  # 找到一个小于等于mid的值，将其放在右边
    list[left] = mid  # left和right相遇，将mid放在这个位置
    sorted_left = sort1(list[0:left])  # 继续递归排序左边
    sorted_right = sort1(list[left + 1:])  # 继续递归排序右边
    return sorted_left + [mid] + sorted_right  # 将左边、mid、右边拼接起来


print("快速排序：", sort1(list3))
