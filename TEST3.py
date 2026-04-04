# import random
# a = int(input("请输入0~100之间的一个数字: "))
# b = random.randint(0, 100)
# while True:
#     if a == b:
#         print("yes")
#         break
#     elif a > b:
#         print("too big")
#         a = int(input("请输入0~100之间的一个数字: "))
#     else:
#         print("too small")
#         a = int(input("请输入0~100之间的一个数字: "))

"""九九乘法表"""
# for i in range(1,10):
#     for k in range(1,i+1):
#         print(f"{k}*{i}={i*k}",end='\t')
#     print()
 
"""
列表

arr = [元素1，元素2，元素3，...]
arr=[1,1.0,'str]
有序，可重复，元素可以修改

正序，0~n-1
反序，-n~ -1
有两个索引，正序索引和反序索引
"""
arr=[1,2,3,4,5,6,7,8,'string']
# del arr[len(arr)-1]
# for i in arr:
#     print(i,end='  ')
# print(arr[0:9:2])    
""""
list切片的用法和range函数的用法一样，都是前闭后开区间，步长默认为1
[begin:end:step]
但是用':' 分隔开
s[0,-1]也是对的,py始终是前壁厚开区间，-1是最后一个元素的索引，-1之前的元素都被包含在切片中
"""
print(arr[-1:-5:-1])