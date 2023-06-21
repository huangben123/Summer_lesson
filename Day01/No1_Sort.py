# 列表排序
# 1.输入一个列表
# 2.遍历列表，找到最小的值，放在第一个位置
# 3.遍历列表，找到第二小的值，放在第二个位置
# ...
# 4.遍历列表，找到第n-1小的值，放在第n-1个位置
# 5.排序完成
# 冒泡排序
def sort(list):
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i];
    return list


list1 = [1, 3, 2, 4, 5, 10, 8, 7, 6];
print("list1:", list1)
print(sort(list1));
print(list1)


#快速排序
def sort1(list):
    if len(list) <= 1:
        return list
    mid, left, right = list[0], 0, len(list) - 1  # 取第一个值为mid
    while left < right:
        while list[right] >= mid and left < right:  # 从右边开始找到第一个小于等于mid的值
            right -= 1
        list[left] = list[right]  # 找到一个小于等于mid的值,将其放在左边
        while list[left] <= mid and left < right:  # 从左边开始找到第一个大于等于mid的值
            left += 1
        list[right] = list[left]  # 找到一个大于等于mid的值，将其放在右边
    list[left] = mid  # left和right相遇，将mid放在这个位置
    sorted_left = sort1(list[0:left])  # 继续递归排序左边
    sorted_right = sort1(list[left + 1:])  # 继续递归排序右边
    return sorted_left + [mid] + sorted_right # 将左边、mid、右边拼接起来


listt = [1, 3, 2, 4, 5, 10, 8, 7, 6]
print(sort1(listt))

# # 字典排序
# print("------------------字典排序---------------------------------")
#
#
# def sortDict(dict):
#     list = [];
#     for key in dict:
#         list.append(key);
#     list = sort(list);
#     return list;
#
#
# dict1 = {1: 2, 4: 5, 2: 3, 3: 4}
# print("dict1:", dict1)
# print(sorted(dict1))  # 根据key排序
# print(sorted(dict1.values()))  # 根据值排序
